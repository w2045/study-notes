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

**钻石问题**：当多个父类有共同祖先时，MRO 保证每个类只被访问一次。复杂的多继承在 Python 中合法，但应谨慎使用。

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

**原则**：能用组合时优先用组合。继承引入了紧耦合——子类的修可能破坏父类的假设。

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
