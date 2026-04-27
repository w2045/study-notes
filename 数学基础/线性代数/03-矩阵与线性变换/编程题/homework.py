"""
线性代数 · 第三章 · 矩阵与线性变换 — 编程作业

所有矩阵用 list[list[float]] 表示（行主序）。完成函数体后运行: python3 grader.py
"""

import math
from typing import List, Optional, Tuple


# ─── Q1 ⭐ 矩阵-向量乘法 ───

def mat_vec_mul(A: List[List[float]], x: List[float]) -> List[float]:
    """返回 b = A @ x (A: m×n, x: n维, b: m维)。

    >>> mat_vec_mul([[1, 2], [3, 4]], [5, 6])
    [17, 39]
    >>> mat_vec_mul([[1, 0, 0], [0, 1, 0]], [1, 2, 3])
    [1, 2]
    """
    pass


# ─── Q2 ⭐ 矩阵乘法 ───

def mat_mul(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """返回 C = A @ B。

    >>> mat_mul([[1, 2], [3, 4]], [[0, 1], [1, 0]])
    [[2, 1], [4, 3]]
    >>> mat_mul([[1, 0, 2], [0, 1, 1]], [[1, 0], [0, 1], [1, 1]])
    [[3, 2], [1, 2]]
    """
    pass


# ─── Q3 ⭐ 矩阵转置 ───

def transpose(A: List[List[float]]) -> List[List[float]]:
    """返回 A^T。

    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    >>> transpose([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    """
    pass


# ─── Q4 ⭐ 对称/反对称分解 ───

def sym_skew_split(A: List[List[float]]) -> Tuple[List[List[float]], List[List[float]]]:
    """将方阵 A 分解为 (对称部分, 反对称部分)。

    >>> sym, skew = sym_skew_split([[1, 3], [-1, 2]])
    >>> sym
    [[1.0, 1.0], [1.0, 2.0]]
    >>> skew
    [[0.0, 2.0], [-2.0, 0.0]]
    """
    pass


# ─── Q5 ⭐ 单位矩阵生成 ───

def identity(n: int) -> List[List[float]]:
    """返回 n×n 单位矩阵。

    >>> identity(3)
    [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    """
    pass


# ─── Q6 ⭐⭐ 迹 ───

def trace(A: List[List[float]]) -> float:
    """返回方阵 A 的迹（对角线元素之和）。

    >>> trace([[1, 2], [3, 4]])
    5.0
    >>> trace([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
    6.0
    """
    pass


# ─── Q7 ⭐⭐ 对称矩阵判定 ───

def is_symmetric(A: List[List[float]]) -> bool:
    """判断 A 是否为对称矩阵 (A^T = A)。

    >>> is_symmetric([[1, 2], [2, 1]])
    True
    >>> is_symmetric([[1, 2], [3, 4]])
    False
    """
    pass


# ─── Q8 ⭐⭐ 正交矩阵判定 ───

def is_orthogonal(A: List[List[float]]) -> bool:
    """判断方阵 A 是否为正交矩阵 (A^T @ A ≈ I)。

    >>> is_orthogonal([[1, 0], [0, 1]])
    True
    >>> is_orthogonal([[0, -1], [1, 0]])
    True
    >>> is_orthogonal([[1, 1], [1, -1]])
    False
    """
    pass


# ─── Q9 ⭐⭐ Frobenius 范数 ───

def frobenius_norm(A: List[List[float]]) -> float:
    """返回矩阵的 Frobenius 范数 sqrt(sum(a_ij^2))。

    >>> frobenius_norm([[3, 0], [0, 4]])
    5.0
    >>> frobenius_norm([[1, 2], [3, 4]])
    5.477225575051661
    """
    pass


# ─── Q10 ⭐⭐ 对角矩阵生成 ───

def diag_matrix(values: List[float]) -> List[List[float]]:
    """从对角线元素列表构造 n×n 对角矩阵。

    >>> diag_matrix([1, 2, 3])
    [[1.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 3.0]]
    """
    pass


# ─── Q11 ⭐⭐⭐ Kronecker 积 ───

def kronecker(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """返回 A ⊗ B (Kronecker 积)。

    >>> kronecker([[1, 0], [0, 1]], [[1, 2], [3, 4]])
    [[1.0, 2.0, 0.0, 0.0], [3.0, 4.0, 0.0, 0.0], [0.0, 0.0, 1.0, 2.0], [0.0, 0.0, 3.0, 4.0]]
    >>> kronecker([[1]], [[2, 3], [4, 5]])
    [[2.0, 3.0], [4.0, 5.0]]
    """
    pass


# ─── Q12 ⭐⭐⭐ 线性变换复合 ───

def compose_transforms(
    A: List[List[float]], B: List[List[float]], x: List[float]
) -> List[float]:
    """先应用变换 B，再应用变换 A：返回 A @ (B @ x)。

    >>> compose_transforms([[0, -1], [1, 0]], [[2, 0], [0, 1]], [1, 1])
    [-1.0, 2.0]
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
