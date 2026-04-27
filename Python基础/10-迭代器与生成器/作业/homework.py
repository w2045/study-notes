"""Python基础 · 第十章 · 迭代器与生成器 — 作业"""

from typing import Iterator, List, Callable, Any

# Q1
def first_n(it: Iterator, n: int) -> List:
    """取迭代器前n项 >>> first_n(iter([1,2,3,4]), 2) == [1,2]"""
    pass

# Q2
def count_up(n: int):
    """生成1..n >>> list(count_up(3)) == [1,2,3]"""
    pass

# Q3
def filter_gen(predicate, it):
    """筛选生成器 >>> list(filter_gen(lambda x: x>0, iter([-1,2,-3,4]))) == [2,4]"""
    pass

# Q4
def even_squares(n: int):
    """偶数平方生成器 >>> list(even_squares(5)) == [0,4,16]"""
    pass

# Q5
def interleave(a, b):
    """轮流产出 >>> list(interleave(iter([1,3]), iter([2,4,5]))) == [1,2,3,4,5]"""
    pass

# Q6
class MyRange:
    """自定义range >>> list(MyRange(2,8,2)) == [2,4,6]"""
    def __init__(self, start, stop, step=1):
        pass

    def __iter__(self):
        pass

# Q7
def fib_gen():
    """斐波那契生成器"""
    pass

# Q8
class Counter:
    """无限计数器 >>> c = Counter(0, 2); [next(c) for _ in range(3)] == [0,2,4]"""
    def __init__(self, start=0, step=1):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

# Q9
def my_enumerate(iterable, start=0):
    """模拟enumerate >>> list(my_enumerate(['a','b'])) == [(0,'a'),(1,'b')]"""
    pass

# Q10
def chunked(it, n):
    """分块 >>> list(chunked(iter([1,2,3,4,5]), 2)) == [[1,2],[3,4],[5]]"""
    pass

# Q11
def pipe(*funcs):
    """管道 >>> f = pipe(lambda it: (x*2 for x in it), lambda it: (x for x in it if x>5))
    >>> list(f(iter([1,2,3,4]))) == [6,8]
    """
    pass

# Q12
def primes():
    """素数生成器"""
    pass

if __name__ == "__main__":
    import doctest; doctest.testmod()
