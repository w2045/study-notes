# Python基础 · 第十一章 · 对象与类

← 前置: [10 — 迭代器与生成器](../10-迭代器与生成器/notes.md)
→ 延伸: [12 — 继承](../12-继承/notes.md)

---

## 1. 直觉引入：把数据和操作绑定在一起

前面我们写了很多函数操作数据——`numer(r)`、`label(t)`、`tree_sum(t)`。每次都要记住哪个函数操作哪种数据。能不能把数据和操作绑定在一起，让 `r.numer()` 代替 `numer(r)`？

这就是**面向对象编程**的核心思想：对象 = 数据 + 操作该数据的方法。

---

## 2. 类与实例

```python
class Dog:
    """一个简单的狗类。"""

    # 类属性（所有实例共享）
    species = "Canis familiaris"

    # 初始化方法（构造函数）
    def __init__(self, name, age):
        self.name = name      # 实例属性
        self.age = age

    # 实例方法
    def bark(self):
        return f"{self.name} says woof!"

    def human_age(self):
        return self.age * 7
```

```python
>>> buddy = Dog("Buddy", 3)
>>> buddy.name
'Buddy'
>>> buddy.bark()
'Buddy says woof!'
>>> buddy.human_age()
21
>>> Dog.species
'Canis familiaris'
```

### 关键点

- `class` 是创建对象的模板（蓝图）
- `__init__` 在实例化时自动调用，`self` 指向新创建的对象
- 实例属性通过 `self.xxx` 定义，每个实例各自拥有
- 类属性在 `class` 块内直接定义，所有实例共享
- 方法第一个参数永远是 `self`——调用时 Python 自动传入

---

## 3. self 与环境模型

```python
buddy = Dog("Buddy", 3)
buddy.bark()
```

`buddy.bark()` 等价于 `Dog.bark(buddy)`——Python 自动把 `.` 前面的对象作为第一个参数传入。

环境模型中，每个对象有自己的帧（`__dict__`），方法调用创建新帧，`self` 指向该对象：

```
Global: Dog → class Dog
buddy → Dog instance
  __dict__: {"name": "Buddy", "age": 3}

buddy.bark()
  创建帧: self=buddy → return self.name + " says woof!"
  沿 self 找到 name="Buddy"
```

### 3.1 属性查找：`obj.attr` 到底做了什么？

理解属性查找是理解 Python 面向对象的枢纽——它直接连通到第十二章的 MRO（方法解析顺序）。

当你写 `buddy.name` 时，Python 按以下顺序查找：

```
1. 实例的 __dict__  →  {"name": "Buddy", "age": 3}
2. 类的 __dict__     →  {species, __init__, bark, human_age, ...}
3. 父类的 __dict__   →  沿着 MRO 链向上（第十二章展开）
```

可以手动验证：

```python
>>> buddy = Dog("Buddy", 3)
>>> buddy.__dict__                         # 实例自己的属性
{'name': 'Buddy', 'age': 3}
>>> Dog.__dict__['species']                # 类属性，不在实例中
'Canis familiaris'
>>> buddy.species                          # 但可以通过实例访问——Python 会自动向上查找
'Canis familiaris'
```

**方法也是通过这个机制找到的**：`buddy.bark` 在实例 `__dict__` 中找不到，于是去 `Dog.__dict__` 中找到 `bark` 函数对象。调用时，Python 自动把 `buddy` 作为 `self` 传入——等价于 `Dog.bark(buddy)`。

**类属性共享的陷阱**：如果类属性是可变对象（如列表），所有实例共享同一个对象：

```python
class Team:
    members = []             # 类属性——所有实例共享！

>>> a = Team()
>>> b = Team()
>>> a.members.append("Alice")
>>> b.members                # b 也看到了！
['Alice']
```

这往往是 bug 的源头。可变属性应该放到 `__init__` 中（每实例独立），不可变常量（如 `species = "Canis familiaris"`）用类属性是安全的。

---

## 4. 方法类型

### 4.1 实例方法

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1      # 修改实例状态
        return self.count
```

### 4.2 特殊方法（dunder methods）

双下划线方法让对象与 Python 内置操作集成：

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        """给开发者看的字符串表示"""
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        """给用户看的字符串表示"""
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """+ 运算符"""
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """== 运算符"""
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        """abs() / |v|"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __len__(self):
        """len() — 返回维度"""
        return 2

    def __getitem__(self, i):
        """v[i] 索引访问"""
        return self.x if i == 0 else self.y
```

```python
>>> v1 = Vector(3, 4)
>>> v2 = Vector(1, 2)
>>> v1 + v2
Vector(4, 6)
>>> abs(v1)
5.0
>>> v1 == Vector(3, 4)
True
```

### 4.3 `__str__` vs `__repr__` —— 给谁看的？

这两个方法很容易混淆，但目的完全不同：

| | `__str__` | `__repr__` |
|---|---|---|
| 目标读者 | 用户（人） | 开发者（调试） |
| 触发方式 | `print(obj)`, `str(obj)`, f-string `{obj}` | `repr(obj)`, 交互环境直接输入对象, 容器的 `__str__` |
| 目标 | 可读性好 | 无歧义，最好能 `eval` 还原 |
| 没定义时的回退 | 找 `__repr__` | 显示默认 `<ClassName at 0x...>` |

关键差异演示：

```python
>>> from datetime import datetime
>>> now = datetime.now()
>>> print(now)              # 用 __str__ → 给人看
2026-04-28 14:30:00
>>> repr(now)               # 用 __repr__ → 调试用，可 eval 还原
'datetime.datetime(2026, 4, 28, 14, 30, 0, 123456)'

>>> # 容器总是用 __repr__ 显示元素
>>> print([now])            # 列表的 __str__ 调用元素的 __repr__
[datetime.datetime(2026, 4, 28, 14, 30, 0, 123456)]
```

**原则**：至少实现 `__repr__`。如果你只定义一个，定义 `__repr__`——`__str__` 在没定义时会回退到 `__repr__`，反过来则会丢失调试信息。

---

## 5. 属性封装：property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius     # _ 前缀约定「内部使用」

    @property
    def radius(self):
        """getter — 像属性一样访问"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """setter — 赋值时自动调用"""
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value

    @property
    def area(self):
        """计算属性 — 看起来像属性，实际每次计算"""
        return 3.14159 * self._radius ** 2

>>> c = Circle(5)
>>> c.radius        # 不写括号——像属性
5
>>> c.radius = 10   # 自动调用 setter
>>> c.area           # 计算属性
314.159
```

---

## 6. 静态方法与类方法

```python
class Date:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_string(cls, date_str):
        """工厂方法：从字符串创建"""
        y, m, d = map(int, date_str.split("-"))
        return cls(y, m, d)       # cls 是 Date 类本身

    @staticmethod
    def is_valid(year, month, day):
        """不需要访问 self 或 cls"""
        return 1 <= month <= 12 and 1 <= day <= 31
```

- **实例方法**：`self`，操作实例数据
- **类方法**：`cls`，作为替代构造器或工厂
- **静态方法**：不需要实例或类数据，普通函数放类里

---

## 7. 例题

### 例 1：BankAccount 类

<details><summary>存款/取款，禁止负数余额</summary>

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"{self.owner}: {self.balance}元"
```
</details>

### 例 2：Fraction 类（有理数）

<details><summary>约分化简 + 运算符重载</summary>

```python
from math import gcd

class Fraction:
    def __init__(self, num, den=1):
        g = gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"
```
</details>

---

## 本章核心概念速查

| 概念 | 语法 |
|------|------|
| 类定义 | `class Name:` |
| 构造器 | `def __init__(self, ...):` |
| 实例方法 | `def method(self, ...):` |
| 类属性 | 在 class 块内直接赋值 |
| 实例属性 | `self.xxx = value` |
| `__repr__` | 开发者可读表示 |
| `__str__` | 用户可读表示 |
| `__add__` 等 | 运算符重载 |
| `@property` | 计算属性 / getter/setter |
| `@classmethod` | 类方法（工厂） |
| `@staticmethod` | 静态方法 |
