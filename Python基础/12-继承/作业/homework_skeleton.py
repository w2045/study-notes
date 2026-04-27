"""Python基础 · 第十二章 · 继承 — 作业"""

from abc import ABC, abstractmethod
from typing import List

# Q1
class Animal:
    """动物基类 >>> Dog('Rex').speak() == 'woof'"""
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Q2
class Person:
    """人 >>> str(Student('Alice',20,'MIT')) == 'Alice (20) - MIT'"""
    pass

class Student(Person):
    pass

# Q3
def count_animals(lst: List) -> int:
    """统计Animal实例数 >>> count_animals([Dog('a'), Cat('b'), 42]) == 2"""
    pass

# Q4
class Shape:
    """形状基类"""
    pass

class Square(Shape):
    """正方形 >>> Square(3).area() == 9"""
    pass

# Q5 (Circle is part of Q4 above)
class Circle(Shape):
    """圆形"""
    pass

# Q6
class Vehicle:
    """交通工具 >>> Car('Toyota','Camry').info() == 'Toyota Camry'"""
    pass

class Car(Vehicle):
    pass

# Q7
class Employee:
    """员工"""
    pass

class Manager(Employee):
    """经理"""
    pass

class CEO(Manager):
    """CEO"""
    pass

# Q8 — Q7 continued (polymorphism)
def all_speak(animals: List[Animal]) -> List[str]:
    """所有动物的叫声 >>> all_speak([Dog('a'), Cat('b')]) == ['woof', 'meow']"""
    pass

# Q9 (Q8 in description)
class Appliance(ABC):
    """抽象电器"""
    pass

class WashingMachine(Appliance):
    pass

class Refrigerator(Appliance):
    pass

# Q10 (Q9 in description)
def get_methods(cls) -> List[str]:
    """非dunder方法名列表"""
    pass

# Q11 (Q10 in description)
class BankError(Exception):
    pass

class InsufficientFunds(BankError):
    pass

def withdraw(balance: float, amount: float) -> float:
    """取款 >>> withdraw(100, 30) == 70"""
    pass

# Q12 (Q11 in description - Composition)
class Engine:
    """引擎"""
    pass

class Car2:  # Car2 to avoid conflict with Q6 Car
    """汽车组合Engine"""
    pass

# Q13 (Q12 in description - Mixin)
class LogMixin:
    """日志Mixin"""
    pass

class Account(LogMixin):
    """账户"""
    pass

if __name__ == "__main__":
    import doctest; doctest.testmod()
