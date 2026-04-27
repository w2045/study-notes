"""Python基础 · 第十一章 · 对象与类 — 作业"""

import math, time
from typing import List

# Q1
class Rectangle:
    """矩形 >>> Rectangle(3,4).area() == 12"""
    pass

# Q2
class Counter:
    """计数器 >>> c = Counter(); c.inc(); c.inc(); c.get() == 2"""
    pass

# Q3
class Vector:
    """向量 >>> Vector(1,2) + Vector(3,4) == Vector(4,6)"""
    pass

# Q4
class Student:
    """学生 >>> s = Student('Alice', [90,100]); s.average() == 95.0"""
    pass

# Q5
class BankAccount:
    """银行账户 >>> a = BankAccount('Bob', 100); a.deposit(50); a.withdraw(30) == 120"""
    pass

# Q6
class Fraction:
    """分数 >>> Fraction(1,2) + Fraction(1,3) == Fraction(5,6)"""
    pass

# Q7
class Temperature:
    """温度 >>> t = Temperature(0); t.fahrenheit == 32.0"""
    pass

# Q8
class Complex:
    """复数 >>> Complex(1,2) + Complex(3,4) == Complex(4,6)"""
    pass

# Q9
class Timer:
    """计时器 >>> t = Timer(); t.elapsed() >= 0"""
    pass

# Q10
class TodoList:
    """待办列表 >>> t = TodoList(); t.add('a'); len(t) == 1"""
    pass

# Q11
class Person:
    """人 >>> p = Person.from_birth_year('Alice', 2000); 'Alice' in str(p)"""
    pass

# Q12
class Circle:
    """圆 >>> c = Circle(5); round(c.area, 2) == 78.54"""
    pass

if __name__ == "__main__":
    import doctest; doctest.testmod()
