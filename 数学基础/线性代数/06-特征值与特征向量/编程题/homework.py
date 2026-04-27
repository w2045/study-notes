"""
线性代数 · 第六章 · 特征值与特征向量 — 编程作业

所有矩阵用 list[list[float]] 表示。完成函数体后运行: python3 grader.py
"""

import math
from typing import List, Optional, Tuple


# ─── Q1 ⭐ 2x2 特征多项式系数 ───

def char_poly_2x2(A: List[List[float]]) -> Tuple[float, float, float]:
    """返回 2x2 矩阵特征多项式的系数 (a, b, c)，即 aλ² + bλ + c = 0。
    其中 a=1, b=-tr(A), c=det(A)。

    >>> char_poly_2x2([[3, 0], [0, 5]])
    (1.0, -8.0, 15.0)
    >>> char_poly_2x2([[4, 1], [2, 3]])
    (1.0, -7.0, 10.0)
    """
    pass


# ─── Q2 ⭐ 2x2 特征值 ───

def eigenvalues_2x2(A: List[List[float]]) -> List[complex]:
    """返回 2x2 矩阵的特征值（可能为复数）。

    >>> eigenvalues_2x2([[3, 0], [0, 5]])
    [3.0, 5.0]
    >>> sorted(eigenvalues_2x2([[2, 1], [1, 2]]))
    [1.0, 3.0]
    """
    pass


# ─── Q3 ⭐ 验证特征向量 ───

def is_eigenvector(A: List[List[float]], v: List[float]) -> Optional[float]:
    """若 v 是 A 的特征向量，返回对应的特征值；否则返回 None。

    >>> is_eigenvector([[4, 2], [1, 3]], [2, 1])
    5.0
    >>> is_eigenvector([[4, 2], [1, 3]], [1, 1]) is None
    True
    """
    pass


# ─── Q4 ⭐ 迹 (trace) ───

def trace(A: List[List[float]]) -> float:
    """返回方阵 A 的迹。

    >>> trace([[1, 2], [3, 4]])
    5.0
    """
    pass


# ─── Q5 ⭐ 行列式 2x2 ───

def determinant_2x2(A: List[List[float]]) -> float:
    """返回 2x2 矩阵的行列式。

    >>> determinant_2x2([[3, 0], [0, 5]])
    15.0
    >>> determinant_2x2([[1, 2], [3, 4]])
    -2.0
    """
    pass


# ─── Q6 ⭐⭐ 矩阵-向量乘 ───

def mat_vec_mul(A: List[List[float]], x: List[float]) -> List[float]:
    """返回 A @ x。

    >>> mat_vec_mul([[1, 2], [3, 4]], [5, 6])
    [17, 39]
    """
    pass


# ─── Q7 ⭐⭐ 对角化验证 ───

def check_diagonalization(
    A: List[List[float]], P: List[List[float]], Lambda: List[List[float]]
) -> bool:
    """验证 A ≈ P @ Lambda @ P^{-1}。仅对 2x2 矩阵。

    >>> A = [[2, 1], [1, 2]]
    >>> P = [[1, 1], [-1, 1]]
    >>> Lambda = [[1, 0], [0, 3]]
    >>> check_diagonalization(A, P, Lambda)
    True
    """
    pass


# ─── Q8 ⭐⭐ 特征值乘积 = 行列式 ───

def verify_eigenvalue_det(A: List[List[float]]) -> bool:
    """验证 2x2 矩阵：特征值乘积 ≈ 行列式。

    >>> verify_eigenvalue_det([[3, 0], [0, 5]])
    True
    >>> verify_eigenvalue_det([[4, 1], [2, 3]])
    True
    """
    pass


# ─── Q9 ⭐⭐⭐ 幂迭代法 ───

def power_iteration(
    A: List[List[float]], max_iter: int = 1000, tol: float = 1e-10
) -> Tuple[List[float], float]:
    """用幂迭代法求 A 的最大绝对值特征值及对应特征向量。
    返回 (eigenvector, eigenvalue)。

    >>> import random; random.seed(42)
    >>> v, lam = power_iteration([[2, 1], [1, 2]])
    >>> abs(lam - 3.0) < 1e-6
    True
    >>> abs(abs(v[0]/v[1]) - 1.0) < 1e-6  # 主特征向量 [1,1] 方向
    True
    """
    pass


# ─── Q10 ⭐⭐⭐ 三角矩阵特征值 ───

def eigenvalues_triangular(A: List[List[float]]) -> List[float]:
    """对于上（或下）三角方阵，返回对角线元素作为特征值。

    >>> eigenvalues_triangular([[2, 5, -3], [0, -1, 4], [0, 0, 6]])
    [2.0, -1.0, 6.0]
    """
    pass


# ─── Q11 ⭐⭐ Rayleigh 商 ───

def rayleigh_quotient(A: List[List[float]], v: List[float]) -> float:
    """返回 Rayleigh 商 R(A, v) = v^T A v / v^T v。

    >>> rayleigh_quotient([[2, 0], [0, 3]], [1, 0])
    2.0
    """
    pass


# ─── Q12 ⭐⭐⭐ 对角化计算矩阵幂 ───

def matrix_power_diag(
    A: List[List[float]], k: int
) -> List[List[float]]:
    """通过对角化计算 2x2 矩阵 A 的 k 次幂 A^k。
    (假设 A 可对角化且特征值已知。)

    >>> rounded = [[round(x, 6) for x in row] for row in matrix_power_diag([[1, 2], [0, -1]], 2)]
    >>> rounded
    [[1.0, 0.0], [0.0, 1.0]]
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
