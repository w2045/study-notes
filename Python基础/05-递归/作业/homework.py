"""Python基础 · 第五章 · 递归 — 作业"""

from typing import List

# Q1
def factorial(n: int) -> int:
    """递归阶乘，n≥0 >>> factorial(5) == 120"""
    pass

# Q2
def sum_digits(n: int) -> int:
    """递归数字之和 >>> sum_digits(123) == 6"""
    pass

# Q3
def power(x: float, n: int) -> float:
    """递归求幂 x^n，n≥0 >>> power(2, 3) == 8"""
    pass

# Q4
def is_palindrome(s: str) -> bool:
    """递归判断回文，忽略大小写 >>> is_palindrome('Racecar') == True"""
    pass

# Q5
def count_up(n: int) -> None:
    """递归打印1到n，每行一个数 >>> count_up(3) 输出1\\n2\\n3\\n"""
    pass

# Q6
def gcd(a: int, b: int) -> int:
    """递归版欧几里得 >>> gcd(48, 18) == 6"""
    pass

# Q7
def my_len(lst: List) -> int:
    """递归求列表长度，不用len >>> my_len([1,2,3]) == 3"""
    pass

# Q8
def reverse_string(s: str) -> str:
    """递归反转字符串 >>> reverse_string('abc') == 'cba'"""
    pass

# Q9
def recursive_sum(lst: List) -> float:
    """递归求和 >>> recursive_sum([1,2,3,4]) == 10"""
    pass

# Q10
def recursive_max(lst: List) -> float:
    """递归求最大值，不用max >>> recursive_max([3,1,4,1,5]) == 5"""
    pass

# Q11
def count(x, lst: List) -> int:
    """递归统计x出现次数 >>> count(1, [1,2,1,3]) == 2"""
    pass

# Q12
def binary_search(lst: List, target) -> int:
    """递归二分查找，返回索引或-1
    >>> binary_search([1,3,5,7,9], 5) == 2
    >>> binary_search([1,3,5,7,9], 6) == -1
    """
    pass

if __name__ == "__main__":
    import doctest; doctest.testmod()
