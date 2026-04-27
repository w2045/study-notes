"""Python基础 · 第八章 · 数据抽象 — 作业"""

from math import gcd
from typing import List, Callable, Any

# Q1
def make_rational(numer: int, denom: int) -> list:
    """构造有理数 >>> r = make_rational(3, 4); r == [3, 4]"""
    pass

# Q2
def numer(r: list) -> int:
    """分子 >>> numer(make_rational(3, 4)) == 3"""
    pass

def denom(r: list) -> int:
    """分母 >>> denom(make_rational(3, 4)) == 4"""
    pass

# Q3
def make_rational_simplified(numer: int, denom: int) -> list:
    """化简有理数 >>> make_rational_simplified(2, 4) == [1, 2]"""
    pass

# Q4
def mul_rational(r1: list, r2: list) -> list:
    """有理数乘法 >>> mul_rational(make_rational(1,2), make_rational(3,4)) == [3,8]"""
    pass

# Q5
def tree(label, branches=None) -> list:
    """树构造器"""
    pass

def label(t: list):
    """树标签 >>> label(tree(5)) == 5"""
    pass

def branches(t: list) -> list:
    """子树列表 >>> branches(tree(5)) == []"""
    pass

def is_leaf(t: list) -> bool:
    """是叶子？ >>> is_leaf(tree(5)) == True"""
    pass

# Q6
def count_leaves(t: list) -> int:
    """叶子数 >>> t = tree(1, [tree(2), tree(3)]); count_leaves(t) == 2"""
    pass

# Q7
def tree_sum(t: list) -> int:
    """所有标签之和 >>> tree_sum(tree(1, [tree(2), tree(3)])) == 6"""
    pass

# Q8
def tree_map(f: Callable, t: list) -> list:
    """标签映射 >>> tree_map(lambda x: x*2, tree(1, [tree(2)]))"""
    pass

# Q9
def make_rational_closure(numer: int, denom: int):
    """闭包有理数"""
    pass

def numer_closure(r) -> int:
    """闭包分子 >>> numer_closure(make_rational_closure(3, 4)) == 3"""
    pass

def denom_closure(r) -> int:
    """闭包分母 >>> denom_closure(make_rational_closure(3, 4)) == 4"""
    pass

# Q10
def cons(a, b):
    """闭包有序对 >>> car(cons(1, 2)) == 1"""
    pass

def car(p):
    """取第一元素"""
    pass

def cdr(p):
    """取第二元素"""
    pass

# Q11
def add_rational(r1: list, r2: list) -> list:
    """有理数加法 >>> add_rational(make_rational(1,2), make_rational(1,3)) == [5,6]"""
    pass

# Q12
def max_label_path(t: list) -> int:
    """最大标签路径和 >>> max_label_path(tree(3, [tree(1), tree(5)])) == 8"""
    pass

if __name__ == "__main__":
    import doctest; doctest.testmod()
