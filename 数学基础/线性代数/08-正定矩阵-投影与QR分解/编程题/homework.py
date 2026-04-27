"""
线性代数 · 第八章 · 正定矩阵、投影与 QR 分解 — 编程作业

所有矩阵用 list[list[float]] 表示。完成函数体后运行: python3 grader.py
"""

import math
from typing import List, Optional, Tuple


# ─── Q1 ⭐ 二次型计算 ───

def quadratic_form(A: List[List[float]], x: List[float]) -> float:
    """计算 x^T A x。

    >>> quadratic_form([[2, 0], [0, 3]], [1, 1])
    5.0
    >>> quadratic_form([[1, 2], [2, 1]], [1, 0])
    1.0
    """
    pass


# ─── Q2 ⭐ 正定性（特征值） ───

def is_positive_definite_eigen(A: List[List[float]]) -> bool:
    """用特征值判断 2x2 对称矩阵是否正定（所有特征值 > 0）。

    >>> is_positive_definite_eigen([[3, 0], [0, 1]])
    True
    >>> is_positive_definite_eigen([[1, 2], [2, 1]])
    False
    """
    pass


# ─── Q3 ⭐ Sylvester 判据 ───

def is_positive_definite_sylvester(A: List[List[float]]) -> bool:
    """用前主子式判断 2x2 对称矩阵是否正定。

    >>> is_positive_definite_sylvester([[4, 1], [1, 1]])
    True
    >>> is_positive_definite_sylvester([[1, 2], [2, 0]])
    False
    """
    pass


# ─── Q4 ⭐ 直线上的正交投影 ───

def project_onto_line(a: List[float], b: List[float]) -> List[float]:
    """b 到 a 方向上的正交投影。

    >>> project_onto_line([1, 0], [3, 4])
    [3.0, 0.0]
    """
    pass


# ─── Q5 ⭐⭐ Cholesky 分解 (2x2) ───

def cholesky_2x2(A: List[List[float]]) -> Optional[List[List[float]]]:
    """返回 2x2 正定矩阵 A 的 Cholesky 分解 L（A = L @ L^T）。
    若不正定，返回 None。

    >>> cholesky_2x2([[4, 2], [2, 5]])
    [[2.0, 0.0], [1.0, 2.0]]
    >>> cholesky_2x2([[1, 2], [2, 1]]) is None
    True
    """
    pass


# ─── Q6 ⭐⭐ 投影矩阵构造 ───

def projection_matrix(A: List[List[float]]) -> List[List[float]]:
    """返回正交投影到 col(A) 的矩阵 P = A (A^T A)^{-1} A^T。
    仅支持 A 为 2 列矩阵。

    >>> P = projection_matrix([[1, 0], [0, 1], [0, 0]])
    >>> [[round(P[i][j], 6) for j in range(3)] for i in range(3)]
    [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]]
    """
    pass


# ─── Q7 ⭐⭐ 正规方程求解最小二乘 ───

def least_squares(A: List[List[float]], b: List[float]) -> Optional[List[float]]:
    """用正规方程解最小二乘 min ||Ax - b||。

    >>> least_squares([[1, 0], [0, 1], [0, 0]], [2, 3, 4])
    [2.0, 3.0]
    """
    pass


# ─── Q8 ⭐⭐ Gram-Schmidt (QR 的 Q) ───

def gram_schmidt_q(A: List[List[float]]) -> List[List[float]]:
    """对矩阵 A 的各列做 Gram-Schmidt 正交化+归一化，返回列正交矩阵 Q。

    >>> Q = gram_schmidt_q([[3, 0], [4, 5]])
    >>> all(math.isclose(sum(Q[j][i]**2 for j in range(2)), 1.0) for i in range(2))
    True
    """
    pass


# ─── Q9 ⭐⭐⭐ QR 分解 ───

def qr_decomposition(A: List[List[float]]) -> Tuple[List[List[float]], List[List[float]]]:
    """对 m×n 矩阵 A (m >= n) 做 QR 分解 (Gram-Schmidt 版)。
    返回 (Q, R)，其中 Q^T Q = I, R 为上三角。

    >>> Q, R = qr_decomposition([[3, 0], [4, 5]])
    >>> # 验证 A ≈ Q @ R
    >>> QR = [[sum(Q[i][k]*R[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    >>> all(math.isclose(QR[i][j], [[3,0],[4,5]][i][j]) for i in range(2) for j in range(2))
    True
    """
    pass


# ─── Q10 ⭐⭐⭐ 用 QR 解最小二乘 ───

def least_squares_qr(A: List[List[float]], b: List[float]) -> List[float]:
    """用 QR 分解解最小二乘 min ||Ax - b||。

    >>> import math
    >>> x = least_squares_qr([[1, 1], [1, 2], [1, 3]], [1, 2, 2])
    >>> all(math.isclose(x[i], [0.666666, 0.5][i], rel_tol=1e-4) for i in range(2))
    True
    """
    pass


# ─── Q11 ⭐⭐ 验证投影幂等性 ───

def is_projection(P: List[List[float]]) -> bool:
    """验证 P 是否为正交投影矩阵 (P^2 ≈ P, P^T ≈ P)。

    >>> is_projection([[1, 0], [0, 0]])
    True
    >>> is_projection([[1, 0], [0, 1]])
    True
    """
    pass


# ─── Q12 ⭐⭐⭐ Cholesky 分解 (n×n) ───

def cholesky(A: List[List[float]]) -> Optional[List[List[float]]]:
    """返回 n×n 正定矩阵 A 的 Cholesky 分解 L。
    若不正定（或数值问题），返回 None。

    >>> L = cholesky([[4, 2, 2], [2, 5, 1], [2, 1, 6]])
    >>> L is not None
    True
    >>> len(L) == 3 and len(L[0]) == 3
    True
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
