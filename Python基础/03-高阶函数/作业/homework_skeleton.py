"""Python基础 · 第三章 · 高阶函数 — 作业"""

from typing import Callable, List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

# Q1
def apply_func(f: Callable[[T], U], x: T) -> U:
    """将 f 应用到 x >>> apply_func(lambda x: x*2, 5) == 10"""
    pass

# Q2
def make_adder(n: float) -> Callable[[float], float]:
    """返回加法器 >>> make_adder(5)(10) == 15"""
    pass

# Q3
def keep_if(predicate: Callable[[T], bool], lst: List[T]) -> List[T]:
    """保留 predicate 为 True 的元素 >>> keep_if(lambda x: x>0, [-3,5,-2,0,7]) == [5,7]"""
    pass

# Q4
def transform_list(f: Callable[[T], U], lst: List[T]) -> List[U]:
    """对每项应用 f >>> transform_list(abs, [-3,5,-2]) == [3,5,2]"""
    pass

# Q5
def compose(f: Callable[[U], T], g: Callable[[V], U]) -> Callable[[V], T]:
    """复合 f ∘ g >>> compose(lambda x: x+1, lambda x: x*2)(3) == 7"""
    pass

# Q6
def curry2(f):
    """柯里化 >>> curry2(lambda x, y: x + y)(3)(5) == 8"""
    pass

# Q7
def make_power(n: int) -> Callable[[float], float]:
    """返回 x^n >>> make_power(3)(2) == 8"""
    pass

# Q8
def make_repeater(f: Callable[[T], T], n: int) -> Callable[[T], T]:
    """重复应用 f n 次 >>> make_repeater(lambda x: x*2, 3)(1) == 8"""
    pass

# Q9
def accumulate(combiner, base, n, term):
    """通用累积 — combiner(combiner(...combiner(base, term(1)), term(2))..., term(n))
    >>> from operator import add, mul
    >>> accumulate(add, 0, 5, lambda x: x) == 15
    >>> accumulate(mul, 1, 5, lambda x: x) == 120
    """
    pass

# Q10
def make_and(pred1, pred2):
    """合取谓词，短路求值
    >>> is_pos = lambda x: x > 0
    >>> is_even = lambda x: x % 2 == 0
    >>> f = make_and(is_pos, is_even)
    >>> f(4), f(-2), f(3)
    (True, False, False)
    """
    pass

# Q11
def square_list(lst: List[float]) -> List[float]:
    """每项平方，用 transform_list + lambda 一行实现
    >>> square_list([1,2,3,4]) == [1,4,9,16]
    """
    pass

# Q12
def make_alternator(f, g):
    """交替执行 f 和 g
    >>> f = lambda x: x + 1
    >>> g = lambda x: x * 10
    >>> alt = make_alternator(f, g)
    >>> alt(5), alt(5), alt(5)
    (6, 50, 6)
    """
    pass

if __name__ == "__main__":
    import doctest; doctest.testmod()
