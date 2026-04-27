# Python基础 · 第十二章 · 继承 — 参考答案

<details><summary>Q1 — Animal / Dog / Cat</summary>

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"
```
</details>

<details><summary>Q2 — Person / Student</summary>

```python
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
    def __str__(self):
        return f"{self.name} ({self.age})"

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
    def __str__(self):
        return f"{self.name} ({self.age}) - {self.school}"
```
</details>

<details><summary>Q3 — count_animals</summary>

```python
def count_animals(lst):
    return sum(1 for x in lst if isinstance(x, Animal))
```
</details>

<details><summary>Q4 — Shape / Square / Circle</summary>

```python
class Shape:
    def area(self):
        return 0
    def description(self):
        return "I am a shape"

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
```
</details>

<details><summary>Q6 — Vehicle / Car</summary>

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def info(self):
        return self.brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def info(self):
        return f"{self.brand} {self.model}"
```
</details>

<details><summary>Q7 — Employee / Manager / CEO</summary>

```python
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def get_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus
    def get_salary(self):
        return self.base_salary + self.bonus

class CEO(Manager):
    def get_salary(self):
        return self.base_salary + self.bonus * 2
```
</details>

<details><summary>Q8 — all_speak</summary>

```python
def all_speak(animals):
    return [a.speak() for a in animals]
```
</details>

<details><summary>Q9 — Appliance / WashingMachine / Refrigerator</summary>

```python
from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self): pass

    @abstractmethod
    def turn_off(self): pass

class WashingMachine(Appliance):
    def turn_on(self): return "Washing..."
    def turn_off(self): return "Done"

class Refrigerator(Appliance):
    def turn_on(self): return "Cooling..."
    def turn_off(self): return "Off"
```
</details>

<details><summary>Q10 — get_methods</summary>

```python
def get_methods(cls):
    return sorted(
        m for m in dir(cls)
        if not m.startswith('_') and callable(getattr(cls, m))
    )
```
</details>

<details><summary>Q11 — BankError / withdraw</summary>

```python
class BankError(Exception): pass

class InsufficientFunds(BankError): pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds("余额不足")
    return balance - amount
```
</details>

<details><summary>Q12 — Engine / Car (组合)</summary>

```python
class Engine:
    def start(self): return "Engine started"
    def stop(self): return "Engine stopped"

class Car2:
    def __init__(self):
        self.engine = Engine()
    def start(self): return self.engine.start()
    def stop(self): return self.engine.stop()
```
</details>

<details><summary>Q13 — LogMixin / Account</summary>

```python
class LogMixin:
    def log(self, msg):
        print(f"[{self.__class__.__name__}] {msg}")

class Account(LogMixin):
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount
        self.log(f"Deposited {amount}")
        return self._balance

    @property
    def balance(self):
        return self._balance
```
</details>
