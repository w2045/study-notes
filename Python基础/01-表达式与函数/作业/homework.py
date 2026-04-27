"""
第一章 · 表达式与函数 — 作业代码

在对应的函数体中填写你的答案，然后运行:
    python3 grader.py

也可以单独运行 doctest:
    python3 -m doctest homework.py -v
"""

import math

# ─── Q1 ⭐ 华氏度转摄氏 ───

def f_to_c(f: float) -> float:
    """将华氏温度转为摄氏温度, 四舍五入到 1 位小数。

    >>> f_to_c(32)
    0.0
    >>> f_to_c(212)
    100.0
    """
    # 写下你的代码:
    pass


# ─── Q2 ⭐ 判断偶数 ───

def is_even(n: int) -> bool:
    """判断整数 n 是否为偶数。

    >>> is_even(4)
    True
    >>> is_even(7)
    False
    >>> is_even(0)
    True
    """
    # 写下你的代码:
    pass


# ─── Q3 ⭐ 球体积 ───

def sphere_volume(r: float) -> float:
    """返回半径为 r 的球的体积。

    >>> round(sphere_volume(1), 4)
    4.1888
    >>> round(sphere_volume(3), 4)
    113.0973
    """
    # 写下你的代码:
    pass


# ─── Q4 ⭐⭐ 三个数的中间值 ───

def middle(a: float, b: float, c: float) -> float:
    """返回三个数中大小居中的那个。不允许使用 sorted() 或 list.sort()。

    >>> middle(1, 2, 3)
    2
    >>> middle(5, 1, 9)
    5
    >>> middle(3, 3, 1)
    3
    >>> middle(7, 7, 7)
    7
    """
    # 写下你的代码:
    pass


# ─── Q5 ⭐⭐ 编写 doctest ───

def add_and_double(a: float, b: float) -> float:
    """返回 a + b 的两倍。

    在此处添加至少 3 个 doctest, 包括边界情况。
    """
    return 2 * (a + b)


# ─── Q6 ⭐⭐ 自由落体时间 ───

def fall_time(h: float) -> float:
    """给定下落距离 h (米), 计算下落时间 t (秒), 四舍五入到 2 位小数。

    g = 9.8 m/s², h ≥ 0。

    >>> fall_time(0)
    0.0
    >>> fall_time(4.9)
    1.0
    """
    # 写下你的代码:
    pass


# ─── Q7 ⭐⭐ 判断三角形 ───

def is_triangle(a: float, b: float, c: float) -> bool:
    """三边长能否构成三角形。

    >>> is_triangle(3, 4, 5)
    True
    >>> is_triangle(1, 1, 3)
    False
    >>> is_triangle(5, 5, 5)
    True
    >>> is_triangle(0, 4, 5)
    False
    """
    # 写下你的代码:
    pass


# ─── Q8 ⭐⭐ 数字反转 ───

def reverse_digits(n: int) -> int:
    """反转一个两位正整数的数字顺序。

    >>> reverse_digits(37)
    73
    >>> reverse_digits(90)
    9
    >>> reverse_digits(10)
    1
    """
    # 写下你的代码:
    pass


# ─── Q9 ⭐⭐ 距离公式 ───

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """返回两点之间的欧氏距离。

    >>> distance(0, 0, 3, 4)
    5.0
    >>> distance(1, 2, 4, 6)
    5.0
    >>> distance(0, 0, 0, 0)
    0.0
    """
    # 写下你的代码:
    pass


# ─── Q10 ⭐⭐ 找 bug ───

def square_of_sum(a: float, b: float) -> float:
    """返回 (a + b)^2。"""
    return a + b ** 2   # ← 这里有 bug, 请修复它


# ─── Q11 ⭐⭐ 四舍五入 ───

def round_to(n: float, decimals: int) -> float:
    """将浮点数 n 四舍五入到 decimals 位小数。不允许使用内置 round。

    >>> round_to(3.14159, 2)
    3.14
    >>> round_to(3.14159, 4)
    3.1416
    >>> round_to(2.5, 0)
    3.0
    """
    # 写下你的代码:
    pass


# ─── Q12 ⭐⭐⭐ 二次方程求根 ───

def solve_quadratic(a: float, b: float, c: float):
    """解 ax² + bx + c = 0。返回 (root1, root2) 从小到大; 无实根返回 None。

    >>> solve_quadratic(1, -3, 2)
    (1.0, 2.0)
    >>> solve_quadratic(1, -2, 1)
    (1.0, 1.0)
    >>> solve_quadratic(1, 0, 1) is None
    True
    """
    # 写下你的代码:
    pass


# ─── main (可忽略) ───
if __name__ == "__main__":
    import doctest
    doctest.testmod()
