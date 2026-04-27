"""Python基础 · 第四章 · 环境图与Lambda — 作业"""

from typing import Callable, List

# Q1
square = None   # 改成 lambda
is_even = None  # 改成 lambda
add = None      # 改成 lambda

# Q2
def make_multiplier(n: float) -> Callable[[float], float]:
    """返回乘法器 >>> make_multiplier(3)(7) == 21"""
    pass

# Q3
def sort_by_last_letter(words: List[str]) -> List[str]:
    """按每词最后一字母排序 >>> sort_by_last_letter(['apple','kiwi','banana']) == ['banana','apple','kiwi']"""
    pass

# Q4
def make_averager():
    """返回求均值函数 >>> a = make_averager(); a(10); a(20); a(30) == 20.0"""
    pass

# Q5
def make_bank_account(initial: float):
    """银行账户 >>> acc = make_bank_account(100); acc(50); acc(-30) == 120"""
    pass

# Q6
def curry_power(x: float) -> Callable[[float], float]:
    """柯里化幂 >>> curry_power(2)(3) == 8"""
    pass

# Q7
def apply_to_two(f, a, b):
    """双参数应用 >>> apply_to_two(lambda x,y: x+y, 3, 5) == 8"""
    pass

# Q8
def make_counter(step: int = 1):
    """计数器 >>> c = make_counter(2); c(); c() == 4"""
    pass

# Q9
def filter_map(predicate, mapper, lst):
    """筛选后变换 >>> filter_map(lambda x: x>0, lambda x: x*2, [-3,5,-2,7]) == [10,14]"""
    pass

# Q10
def decode_lambda() -> int:
    """返回 lambda x: (lambda y: x + y) 调用 f(3)(5) 的值"""
    pass

# Q11
def make_greeting(greeting: str):
    """lambda 问候 >>> make_greeting('Hello')('World') == 'Hello, World!'"""
    pass

# Q12
def make_timer():
    """闭包计时器 >>> import time; t = make_timer(); time.sleep(0.1); t() > 0.09"""
    pass

if __name__ == "__main__":
    import doctest; doctest.testmod()
