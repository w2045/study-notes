"""
线性代数 · 第九章 · 奇异值分解 SVD — 编程作业

所有矩阵用 list[list[float]] 表示。完成函数体后运行: python3 grader.py
"""

import math
from typing import List, Optional, Tuple


# ─── Q1 ⭐ 矩阵转置 ───

def transpose(A: List[List[float]]) -> List[List[float]]:
    """返回 A^T。

    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    pass


# ─── Q2 ⭐ 矩阵-向量乘 ───

def mat_vec_mul(A: List[List[float]], x: List[float]) -> List[float]:
    """返回 A @ x。

    >>> mat_vec_mul([[1, 2], [3, 4]], [5, 6])
    [17, 39]
    """
    pass


# ─── Q3 ⭐ 矩阵乘法 ───

def mat_mul(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """返回 A @ B。

    >>> mat_mul([[1, 2], [3, 4]], [[0, 1], [1, 0]])
    [[2, 1], [4, 3]]
    """
    pass


# ─── Q4 ⭐ 向量范数 ───

def norm(v: List[float]) -> float:
    """返回 L2 范数。

    >>> norm([3, 4])
    5.0
    """
    pass


# ─── Q5 ⭐⭐ 幂迭代求最大奇异向量 ───

def power_iteration_svd(
    A: List[List[float]], max_iter: int = 1000, tol: float = 1e-10
) -> Tuple[List[float], List[float], float]:
    """用幂迭代法求 A 的最大奇异值及对应左右奇异向量。
    返回 (u, v, sigma)。v 初始化为随机向量。

    >>> import random; random.seed(42)
    >>> u, v, sigma = power_iteration_svd([[3, 0], [4, 5]])
    >>> abs(sigma - 6.0) < 1.0  # 最大奇异值约 6.0+
    True
    """
    pass


# ─── Q6 ⭐⭐ $A^T A$ 计算 ───

def compute_AtA(A: List[List[float]]) -> List[List[float]]:
    """计算 A^T A。

    >>> compute_AtA([[1, 0], [0, 2], [0, 0]])
    [[1, 0], [0, 4]]
    """
    pass


# ─── Q7 ⭐⭐ 谱范数（最大奇异值近似） ───

def spectral_norm(A: List[List[float]]) -> float:
    """返回谱范数 ||A||_2（最大奇异值的近似，用幂迭代）。

    >>> spectral_norm([[3, 0], [0, 2]])
    3.0
    >>> abs(spectral_norm([[1, 2], [3, 4]]) - 5.5) < 2.0
    True
    """
    pass


# ─── Q8 ⭐⭐ Frobenius 范数 ───

def frobenius_norm(A: List[List[float]]) -> float:
    """返回 Frobenius 范数。

    >>> frobenius_norm([[3, 0], [0, 4]])
    5.0
    """
    pass


# ─── Q9 ⭐⭐⭐ 低秩近似 ───

def low_rank_approx(
    U: List[List[float]], S: List[float], Vt: List[List[float]], k: int
) -> List[List[float]]:
    """从截断 SVD 重建秩-k 近似矩阵 A_k = sum_{i=1}^k sigma_i u_i v_i^T。
    U 是 m×r, Vt 是 r×n, S 是 length=r 的列表。

    >>> U = [[0.6, -0.8], [0.8, 0.6]]
    >>> S = [5.0, 3.0]
    >>> Vt = [[0.6, 0.8], [-0.8, 0.6]]
    >>> Ak = low_rank_approx(U, S, Vt, 1)
    >>> [[round(Ak[i][j], 4) for j in range(2)] for i in range(2)]
    [[1.8, 2.4], [2.4, 3.2]]
    """
    pass


# ─── Q10 ⭐⭐⭐ SVD 重构误差 ───

def svd_reconstruction_error(
    A: List[List[float]], U: List[List[float]], S: List[float], Vt: List[List[float]], k: int
) -> float:
    """计算 A 与秩-k SVD 近似之间的 Frobenius 误差。

    >>> A = [[3, 0], [4, 5]]
    >>> U = [[0.6, -0.8], [0.8, 0.6]]
    >>> S = [6.0, 2.0]
    >>> Vt = [[0.6, 0.8], [-0.8, 0.6]]
    >>> err = svd_reconstruction_error(A, U, S, Vt, 1)
    >>> abs(err - 2.0) < 0.5  # sigma_2 ≈ 2
    True
    """
    pass


# ─── Q11 ⭐⭐ 条件数 ───

def condition_number(S: List[float]) -> float:
    """从奇异值列表计算条件数 = sigma_max / sigma_min（最小正奇异值）。

    >>> condition_number([5.0, 3.0])
    1.6666666666666667
    >>> condition_number([100.0, 0.01])
    10000.0
    """
    pass


# ─── Q12 ⭐⭐⭐ 图像压缩演示的简化 ───

def compress_ratio(H: int, W: int, k: int) -> float:
    """计算 SVD 图像压缩的压缩比。
    原始存储 = H*W, 压缩存储 = k*(H+W+1), 返回 H*W / (k*(H+W+1))。

    >>> compress_ratio(100, 100, 10)
    49.75124378109453
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
