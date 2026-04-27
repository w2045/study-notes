# Python基础 · 第十一章 · 对象与类 — 参考答案

<details><summary>Q1 — Rectangle</summary>

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```
</details>

<details><summary>Q2 — Counter</summary>

```python
class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0

    def get(self):
        return self.count
```
</details>

<details><summary>Q3 — Vector</summary>

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```
</details>

<details><summary>Q4 — Student</summary>

```python
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def grade(self):
        avg = self.average()
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        return "F"

    def __str__(self):
        return f"{self.name} ({self.average():.1f})"
```
</details>

<details><summary>Q5 — BankAccount</summary>

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
        return f"{self.owner}: {self.balance}"
```
</details>

<details><summary>Q6 — Fraction</summary>

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

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"
```
</details>

<details><summary>Q7 — Temperature</summary>

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9
```
</details>

<details><summary>Q8 — Complex</summary>

```python
class Complex:
    def __init__(self, real, imag):
        self.real, self.imag = real, imag

    def __add__(self, o):
        return Complex(self.real + o.real, self.imag + o.imag)

    def __sub__(self, o):
        return Complex(self.real - o.real, self.imag - o.imag)

    def __mul__(self, o):
        return Complex(self.real * o.real - self.imag * o.imag,
                       self.real * o.imag + self.imag * o.real)

    def __eq__(self, o):
        return self.real == o.real and self.imag == o.imag

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"
```
</details>

<details><summary>Q9 — Timer</summary>

```python
import time

class Timer:
    def __init__(self):
        self._start = time.time()

    def elapsed(self):
        return time.time() - self._start

    def reset(self):
        self._start = time.time()
```
</details>

<details><summary>Q10 — TodoList</summary>

```python
class TodoList:
    def __init__(self):
        self._items = []

    def add(self, task):
        self._items.append(task)

    def remove(self, task):
        if task in self._items:
            self._items.remove(task)

    def list_all(self):
        return list(self._items)

    def clear(self):
        self._items.clear()

    def __len__(self):
        return len(self._items)
```
</details>

<details><summary>Q11 — Person</summary>

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, 2026 - year)

    def __str__(self):
        return f"{self.name}, {self.age}"
```
</details>

<details><summary>Q12 — Circle</summary>

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius
```
</details>
