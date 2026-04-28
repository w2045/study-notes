# Python基础 · 第十二章 · 继承

← 前置: [11 — 对象与类](../11-对象与类/notes.md)
→ 延伸: [数据结构与算法](../../../数据结构与算法/01-简介与C++基础/notes.md)

---

## 1. 直觉引入：共享代码，表达关系

上一章我们写了 `Dog` 类。如果要加 `Cat` 类呢？两者有大量重复——都有 `name`、`age`、`speak()` 方法，只是具体叫声不同。

**继承**（inheritance）让一个类从另一个类「继承」属性和方法，只需重写不同的部分：

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "..."

    def description(self):
        return f"{self.name}, {self.age} 岁"

class Dog(Animal):              # Dog 继承 Animal
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):              # Cat 也继承 Animal
    def speak(self):
        return f"{self.name} says meow!"
```

```python
>>> d = Dog("Buddy", 3)
>>> d.speak()
'Buddy says woof!'
>>> d.description()            # ← 继承自 Animal，没有重写
'Buddy, 3 岁'
```

---

## 2. 术语与基本机制

| 术语 | 说明 |
|------|------|
| 父类 / 基类 / 超类 | 被继承的类（Animal） |
| 子类 / 派生类 | 继承的类（Dog, Cat） |
| 重写 (override) | 子类重新定义父类的方法 |
| `super()` | 获取父类的代理对象，用于调用父类方法 |

### 2.1 调用父类方法

```python
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)    # 先调用父类的 __init__
        self.breed = breed             # 再添加子类自己的属性

    def speak(self):
        return f"{self.name} ({self.breed}) says woof!"
```

`super()` 让子类可以「扩展」而非「替换」父类的行为。

继承建立了类之间的「是」关系。有时你需要在运行时确认这个关系——判断一个对象能否被当作某种类型来操作。Python 提供了两个内置函数来检查继承层次。

---

## 3. isinstance 与 issubclass

```python
>>> d = Dog("Buddy", 3)
>>> isinstance(d, Dog)       # True
>>> isinstance(d, Animal)    # True — 子类实例也是父类的实例
>>> isinstance(d, Cat)       # False

>>> issubclass(Dog, Animal)  # True
>>> issubclass(Dog, Cat)     # False
>>> issubclass(Dog, Dog)     # True — 自己也是自己的子类
```

`isinstance(d, Dog)` 和 `isinstance(d, Animal)` 都返回 `True`——这没问题，因为只有一个父类。但如果 `Dog` 同时继承 `Animal` 和 `Friend`，`d.method()` 先在哪个父类中找？Python 需要一套确定的规则来回答这个问题。

---

## 4. 方法解析顺序 (MRO)

当调用 `d.speak()` 时，Python 按固定顺序在类层次结构中查找：
1. 先在 `Dog` 类找
2. 再到 `Animal` 类找
3. 最后到 `object`（所有类的最终基类）

```python
>>> Dog.__mro__
(Dog, Animal, object)
```

MRO 保证了在多继承时查找顺序是确定的（C3 线性化算法）。

MRO 是多继承的底层规则。现在看多继承的实际用法——一个类同时从多个父类获取方法和属性。Python 支持它，但用法需要克制。

---

## 5. 多继承

Python 支持多重继承：

```python
class Flyer:
    def fly(self):
        return "I can fly!"

class Swimmer:
    def swim(self):
        return "I can swim!"

class Duck(Animal, Flyer, Swimmer):
    def speak(self):
        return "Quack!"

>>> d = Duck("Donald", 2)
>>> d.speak(), d.fly(), d.swim()
('Quack!', 'I can fly!', 'I can swim!')
```

**钻石问题**：当多个父类有共同祖先时，Python 通过 MRO 保证每个类的方法只被查找一次，顺序确定不混乱：

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B" + super().method()

class C(A):
    def method(self):
        return "C" + super().method()

class D(B, C):           # D 继承 B 和 C，B 和 C 都继承 A（菱形！）
    def method(self):
        return "D" + super().method()

>>> D.__mro__             # 看查找顺序
(D, B, C, A, object)
>>> D().method()          # D → B → C → A，每类只走一次
'DBCA'
```

`super()` 沿 MRO 链调用下一个类——不是简单的「调用父类」。钻石结构中，MRO 保证了 `A.method` 只被调用一次（在最后），不会被 `B` 和 `C` 各调一次造成重复。这就是 C3 线性化算法的价值。

复杂的多继承在 Python 中合法，但应谨慎使用。当继承层次变深时，`super()` 的行为可能令人意外——理解 MRO 是调试它的唯一途径。

多继承提供了灵活性，但灵活性过大意味着出错空间大。有时你希望明确限制：这个基类**只定义接口，不允许直接实例化**，子类必须实现特定方法才能使用。抽象基类（ABC）就是为此设计——它强制子类遵守约定。

---

## 6. 抽象基类 (ABC)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """子类必须实现"""
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# c = Shape()       # ❌ TypeError — 不能实例化抽象类
c = Circle(5)       # ✅ Circle 实现了所有抽象方法
```

ABC 是继承的规范用法——定义接口，强制实现。但它仍然是继承。继承不是代码复用的唯一方式，甚至不是最好的方式。另一种思路是**组合**——一个类包含另一个类的实例，通过委托来复用功能。两者的区别可以用两个英文短语概括：

---

## 7. 组合 vs 继承

继承表示 **IS-A**（狗是动物），组合表示 **HAS-A**（汽车有引擎）。

```python
# 继承：Dog IS-A Animal
class Dog(Animal): ...

# 组合：Car HAS-A Engine
class Engine:
    def start(self): ...

class Car:
    def __init__(self):
        self.engine = Engine()    # 组合——Car 拥有 Engine

    def start(self):
        self.engine.start()
```

**原则**：能用组合时优先用组合。继承引入紧耦合——子类修改可能破坏父类假设，而组合通过接口通信，双方独立演化。

**一个具体权衡**：假设你要实现一个 `Stack`。两种方式：

```python
# 继承方式：Stack IS-A list
class Stack(list):
    def push(self, item):
        self.append(item)
    def pop(self):                     # 覆盖了 list.pop！
        return super().pop()

>>> s = Stack()
>>> s.push(1); s.push(2)
>>> s.pop()
2
>>> s.insert(0, 99)                   # 不——list.insert 仍然可用！
>>> s[0]                               # 用索引直接访问，破坏了栈的语义
99
```

继承暴露了父类的**全部接口**，包括不该在栈上使用的 `insert`、`sort`、索引赋值等。用户可以用这些方法破坏栈的 LIFO 约束。

```python
# 组合方式：Stack HAS-A list
class Stack:
    def __init__(self):
        self._items = []               # 列表藏在里面
    def push(self, item):
        self._items.append(item)
    def pop(self):
        return self._items.pop()
    def __len__(self):
        return len(self._items)

>>> s = Stack()
>>> s.push(1)
>>> s.insert(0, 99)                   # AttributeError —— insert 不存在！
```

组合只暴露你**选择暴露**的方法——接口简洁、不变量受保护。代价是如果要支持 `len(s)`、`for x in s` 等 Python 协议，需要手动转发（如上文的 `__len__`）。

**选择指南**：
- 继承：子类**确实是**父类的一种（Dog IS-A Animal），且你希望复用父类的大部分接口
- 组合：子类**拥有**另一个对象作为实现细节（Stack HAS-A list），只暴露精选接口
- 多继承：在 Python 中，Mixin 类（只提供方法的轻量类）是多继承的合理用例——如 `class MyView(APIView, LoggingMixin, AuthMixin)`。避免深层次的「是」关系多继承

---

## 8. 例题

### 例 1：员工管理系统

<details><summary>Employee → Manager 继承层次</summary>

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f"{self.name}: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus

>>> m = Manager("Alice", 80000, 20000)
>>> m.get_pay()
100000
```
</details>

### 例 2：异常层次

<details><summary>自定义异常继承 Exception</summary>

```python
class BankError(Exception): pass
class InsufficientFunds(BankError): pass
class AccountFrozen(BankError): pass

# 可以捕获特定的或所有的
try:
    raise InsufficientFunds("余额不足")
except BankError:          # 捕获所有银行异常
    print("银行错误")
```
</details>

---

## 本章核心概念速查

| 概念 | 说明 |
|------|------|
| `class Child(Parent):` | 继承语法 |
| 重写 override | 子类重新定义父类方法 |
| `super()` | 调用父类方法 |
| `isinstance(obj, cls)` | 检查对象是否是类的实例 |
| `issubclass(cls1, cls2)` | 检查类是否是另一个类的子类 |
| MRO | 方法解析顺序（`__mro__`） |
| ABC + `@abstractmethod` | 抽象基类 |
| 组合 vs 继承 | IS-A vs HAS-A |
