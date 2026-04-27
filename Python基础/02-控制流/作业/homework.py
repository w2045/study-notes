"""Python基础 · 第二章 · 控制流 — 作业"""

from typing import List

# Q1
def sign(n: int) -> int:
    """n>0→1, n<0→-1, n==0→0 >>> sign(5)==1; sign(-3)==-1; sign(0)==0"""
    pass

# Q2
def my_abs(n: float) -> float:
    """返回 |n|，禁 abs >>> my_abs(-5.5)==5.5"""
    pass

# Q3
def sum_to(n: int) -> int:
    """while 循环返回 1+2+...+n >>> sum_to(5)==15"""
    pass

# Q4
def fizzbuzz(n: int) -> List[str]:
    """i=1..n, 3x→Fizz, 5x→Buzz, 15x→FizzBuzz >>> fizzbuzz(3)==['1','2','Fizz']"""
    pass

# Q5
def factorial(n: int) -> int:
    """while 循环 n! >>> factorial(5)==120"""
    pass

# Q6
def gcd(a: int, b: int) -> int:
    """while 循环欧几里得 >>> gcd(48,18)==6"""
    pass

# Q7
def is_prime(n: int) -> bool:
    """n 是否素数 >>> is_prime(7)==True; is_prime(4)==False"""
    pass

# Q8
def digit_sum(n: int) -> int:
    """各位数字之和，while 循环 >>> digit_sum(123)==6"""
    pass

# Q9
def max_of_three(a: float, b: float, c: float) -> float:
    """禁 max >>> max_of_three(1,5,3)==5"""
    pass

# Q10
def print_table(n: int) -> None:
    """打印 n×n 乘法表，不 return"""
    pass

# Q11
def collatz_steps(n: int) -> int:
    """偶数→n/2, 奇数→3n+1, 直到 1, 返回步数 >>> collatz_steps(6)==8"""
    pass

# Q12
def fibonacci(k: int) -> int:
    """F(0)=0, F(1)=1, while 循环 >>> fibonacci(6)==8"""
    pass

if __name__ == "__main__":
    import doctest; doctest.testmod()
