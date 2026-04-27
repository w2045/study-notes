"""
线性代数 · 第四章 · 线性方程组与消元法 — 编程作业

所有矩阵用 list[list[float]] 表示（行主序）。完成函数体后运行: python3 grader.py
"""

import math
from typing import List, Optional, Tuple


# ─── Q1 ⭐ 增广矩阵构造 ───

def make_augmented(A: List[List[float]], b: List[float]) -> List[List[float]]:
    """将 A 和 b 合并为增广矩阵 [A | b]。

    >>> make_augmented([[1, 2], [3, 4]], [5, 6])
    [[1, 2, 5], [3, 4, 6]]
    """
    pass


# ─── Q2 ⭐ 初等行操作：交换 ───

def row_swap(M: List[List[float]], i: int, j: int) -> List[List[float]]:
    """返回交换第 i 行和第 j 行后的新矩阵（不改原矩阵）。

    >>> row_swap([[1, 2], [3, 4]], 0, 1)
    [[3, 4], [1, 2]]
    """
    pass


# ─── Q3 ⭐ 初等行操作：缩放 ───

def row_scale(M: List[List[float]], i: int, c: float) -> List[List[float]]:
    """返回第 i 行乘以 c 后的新矩阵。

    >>> row_scale([[1, 2], [3, 4]], 0, 2.0)
    [[2.0, 4.0], [3, 4]]
    """
    pass


# ─── Q4 ⭐ 初等行操作：加减 ───

def row_add(M: List[List[float]], target: int, source: int, c: float) -> List[List[float]]:
    """返回 R_target <- R_target + c * R_source 后的新矩阵。

    >>> row_add([[1, 2], [3, 4]], 1, 0, -3.0)
    [[1, 2], [0.0, -2.0]]
    """
    pass


# ─── Q5 ⭐⭐ 前向消元（无选主元） ───

def forward_elimination(
    A: List[List[float]], b: List[float]
) -> Tuple[List[List[float]], List[float]]:
    """对增广矩阵 [A|b] 执行前向消元（不选主元），返回 (A_upper, b_upper)。

    >>> A, b = forward_elimination([[1, 2], [3, 4]], [5, 11])
    >>> [[round(A[i][j], 6) for j in range(2)] for i in range(2)]
    [[1.0, 2.0], [0.0, -2.0]]
    >>> [round(b[i], 6) for i in range(2)]
    [5.0, -4.0]
    """
    pass


# ─── Q6 ⭐⭐ 回代 ───

def back_substitution(
    A: List[List[float]], b: List[float]
) -> Optional[List[float]]:
    """对上三角 A 和 b 进行回代，返回解 x。无解或无穷多解返回 None。

    >>> back_substitution([[1, 2], [0, -2]], [5, -4])
    [1.0, 2.0]
    >>> back_substitution([[1, 2, 1], [0, 1, 3], [0, 0, 2]], [4, 7, 2])
    [-3.0, 4.0, 1.0]
    """
    pass


# ─── Q7 ⭐⭐ 列主元前向消元 ───

def forward_elimination_pivot(
    A: List[List[float]], b: List[float]
) -> Tuple[List[List[float]], List[float]]:
    """带列主元的前向消元，返回 (A_upper, b_upper)。

    >>> A, b = forward_elimination_pivot([[0.0001, 1], [1, 1]], [1, 2])
    >>> # 应交换行（第1列第2行绝对值更大）
    >>> abs(A[0][0]) > abs(A[1][0])  # 原来的第2行被换到顶上
    True
    """
    pass


# ─── Q8 ⭐⭐ LU 分解 ───

def lu_decomposition(
    A: List[List[float]]
) -> Tuple[List[List[float]], List[List[float]]]:
    """Doolittle LU 分解（假设不需要行交换），返回 (L, U)。

    >>> L, U = lu_decomposition([[2, 1], [6, 8]])
    >>> all(math.isclose(L[i][j], [[1,0],[3,1]][i][j]) for i in range(2) for j in range(2))
    True
    >>> all(math.isclose(U[i][j], [[2,1],[0,5]][i][j]) for i in range(2) for j in range(2))
    True
    """
    pass


# ─── Q9 ⭐⭐ 前代（解 L y = b） ───

def forward_substitution(
    L: List[List[float]], b: List[float]
) -> List[float]:
    """解 L y = b（L 为单位下三角矩阵）。

    >>> forward_substitution([[1, 0], [3, 1]], [3, 10])
    [3.0, 1.0]
    """
    pass


# ─── Q10 ⭐⭐⭐ 高斯消元完整求解 ───

def gaussian_solve(
    A: List[List[float]], b: List[float], use_pivoting: bool = True
) -> Optional[List[float]]:
    """用高斯消元法（带列主元）解 A x = b，返回 x 或 None。

    >>> gaussian_solve([[1, 2, 1], [2, 6, 1], [1, 1, 4]], [2, 7, 3])
    [-3.0, 2.0, 1.0]
    """
    pass


# ─── Q11 ⭐⭐⭐ 判断解的情况 ───

def classify_solution(
    A: List[List[float]], b: List[float]
) -> str:
    """经消元后判断解的情况，返回 'unique', 'infinite' 或 'none'。

    >>> classify_solution([[1, 0], [0, 1]], [3, 4])
    'unique'
    >>> classify_solution([[1, 2], [0, 0]], [3, 0])
    'infinite'
    >>> classify_solution([[1, 2], [0, 0]], [3, 1])
    'none'
    """
    pass


# ─── Q12 ⭐⭐⭐ 用 LU 分解求解 ───

def lu_solve(
    L: List[List[float]], U: List[List[float]], b: List[float]
) -> List[float]:
    """给定 LU 分解，解 A x = b（先 L y = b，再 U x = y）。

    >>> L = [[1, 0], [3, 1]]
    >>> U = [[2, 1], [0, 5]]
    >>> lu_solve(L, U, [3, 10])
    [1.0, 1.0]
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
