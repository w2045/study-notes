"""
线性代数 · 第一章 · 向量与向量空间 — 编程作业

所有函数通过 list[float] 表示向量（不用 numpy）。
完成函数体后运行: python3 grader.py
"""

import math
from typing import List, Optional


# ─── Q1 ⭐ 向量加法 ───

def vector_sum(u: List[float], v: List[float]) -> List[float]:
    """返回 u + v。

    >>> vector_sum([1, 2], [3, 4])
    [4, 6]
    """
    pass


# ─── Q2 ⭐ 向量减法 ───

def vector_diff(u: List[float], v: List[float]) -> List[float]:
    """返回 u - v。

    >>> vector_diff([5, 7], [2, 3])
    [3, 4]
    """
    pass


# ─── Q3 ⭐ 标量乘法 ───

def scalar_mult(c: float, v: List[float]) -> List[float]:
    """返回 c * v。

    >>> scalar_mult(3, [1, 2, 3])
    [3, 6, 9]
    >>> scalar_mult(0, [5, 5])
    [0, 0]
    """
    pass


# ─── Q4 ⭐⭐ 线性组合 ───

def linear_combination(
    vectors: List[List[float]], coeffs: List[float]
) -> List[float]:
    """返回 c1*v1 + c2*v2 + ... + ck*vk。

    >>> linear_combination([[1, 0], [0, 1]], [3, 4])
    [3.0, 4.0]
    >>> linear_combination([[1, 2, 3]], [5])
    [5.0, 10.0, 15.0]
    """
    pass


# ─── Q5 ⭐ 零向量判定 ───

def is_zero_vector(v: List[float]) -> bool:
    """判断 v 是否为零向量（所有分量 ≈ 0）。

    >>> is_zero_vector([0, 0, 0])
    True
    >>> is_zero_vector([1, 0, 0])
    False
    """
    pass


# ─── Q6 ⭐⭐ 标准基向量 ───

def standard_basis(i: int, n: int) -> List[float]:
    """返回 R^n 中第 i 个标准基向量 e_i (1-indexed)。

    >>> standard_basis(1, 3)
    [1.0, 0.0, 0.0]
    >>> standard_basis(3, 4)
    [0.0, 0.0, 1.0, 0.0]
    """
    pass


# ─── Q7 ⭐⭐ 二维线性无关判定 ───

def are_independent_2d(u: List[float], v: List[float]) -> bool:
    """判断两个二维向量是否线性无关（不共线，且都不为零）。

    >>> are_independent_2d([1, 0], [0, 1])
    True
    >>> are_independent_2d([1, 2], [2, 4])
    False
    >>> are_independent_2d([0, 0], [1, 2])
    False
    """
    pass


# ─── Q8 ⭐⭐ 二维 span 包含判定 ───

def is_in_span_2d(
    a: List[float], b: List[float]
) -> bool:
    """判断二维向量 b 是否在 a 的 span 中（即 b 与 a 共线或 a 为零向量时 b 也为零）。

    >>> is_in_span_2d([2, 3], [4, 6])
    True
    >>> is_in_span_2d([2, 3], [4, 5])
    False
    >>> is_in_span_2d([0, 0], [0, 0])
    True
    """
    pass


# ─── Q9 ⭐ 子空间必要条件 ───

def contains_zero_vector(vectors: List[List[float]]) -> bool:
    """判断向量列表中是否包含零向量（子空间的必要条件）。

    >>> contains_zero_vector([[1, 2], [0, 0], [3, 4]])
    True
    >>> contains_zero_vector([[1, 2], [3, 4]])
    False
    """
    pass


# ─── Q10 ⭐⭐⭐ 基坐标表示 ───

def coordinates_in_basis(
    basis: List[List[float]], v: List[float]
) -> Optional[List[float]]:
    """在 R^2 中，用给定基 {b1, b2} 表示 v。返回系数 [c1, c2]。
    前提：basis 是 R^2 的一组基（两个线性无关的二维向量）。
    若 basis 不是基（共线或含零向量），返回 None。

    >>> coordinates_in_basis([[1, 0], [0, 1]], [3, 4])
    [3.0, 4.0]
    >>> coordinates_in_basis([[1, 1], [1, -1]], [2, 0])
    [1.0, 1.0]
    >>> coordinates_in_basis([[1, 2], [2, 4]], [3, 5]) is None
    True
    """
    pass


# ─── Q11 ⭐⭐⭐ 三维线性无关判定 ───

def are_independent_3d(
    u: List[float], v: List[float], w: List[float]
) -> bool:
    """判断三个三维向量是否线性无关。
    提示：计算标量三重积 (u × v) · w 是否非零。

    >>> are_independent_3d([1, 0, 0], [0, 1, 0], [0, 0, 1])
    True
    >>> are_independent_3d([1, 0, 0], [0, 1, 0], [1, 1, 0])
    False
    >>> are_independent_3d([0, 0, 0], [1, 2, 3], [4, 5, 6])
    False
    """
    pass


# ─── Q12 ⭐⭐⭐ 扩充为基（二维） ───

def extend_to_basis_2d(v: List[float]) -> Optional[List[List[float]]]:
    """给定一个非零二维向量 v，找到另一个向量 u 使得 {v, u} 构成 R^2 的一组基。
    若 v 为零向量，返回 None。

    >>> extend_to_basis_2d([1, 0])
    [[1.0, 0.0], [0.0, 1.0]]
    >>> extend_to_basis_2d([3, 4])
    [[3.0, 4.0], [-4.0, 3.0]]
    >>> extend_to_basis_2d([0, 0]) is None
    True
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
