"""
线性代数 · 第一章 · 向量与向量空间 — 作业代码

所有函数使用普通 list 表示向量，不依赖 Vector 类。
完成函数体后运行: python3 grader.py
"""

import math
from typing import List, Optional


# ─── Q1 ⭐ 向量加减 ───

def vector_sum(u: List[float], v: List[float]) -> List[float]:
    """返回 u + v。

    >>> vector_sum([1, 2], [3, 4])
    [4, 6]
    """
    pass


def vector_diff(u: List[float], v: List[float]) -> List[float]:
    """返回 u - v。

    >>> vector_diff([5, 7], [2, 3])
    [3, 4]
    """
    pass


# ─── Q2 ⭐ 标量乘法 ───

def scalar_mult(c: float, v: List[float]) -> List[float]:
    """返回 c * v。

    >>> scalar_mult(3, [1, 2, 3])
    [3, 6, 9]
    >>> scalar_mult(0, [5, 5])
    [0, 0]
    """
    pass


# ─── Q3 ⭐ 欧几里得范数 ───

def euclidean_norm(v: List[float]) -> float:
    """返回 ||v||_2。不允许用 math.hypot 或 numpy。

    >>> euclidean_norm([3, 4])
    5.0
    >>> euclidean_norm([0, 0])
    0.0
    """
    pass


# ─── Q4 ⭐ 点积 ───

def dot_product(u: List[float], v: List[float]) -> float:
    """返回 u · v。

    >>> dot_product([1, 2], [3, 4])
    11
    >>> dot_product([1, 0], [0, 1])
    0
    """
    pass


# ─── Q5 ⭐ 归一化 ───

def normalize(v: List[float]) -> Optional[List[float]]:
    """返回 v / ||v||。零向量返回 None。

    >>> normalize([3, 4])
    [0.6, 0.8]
    >>> normalize([0, 0]) is None
    True
    """
    pass


# ─── Q6 ⭐⭐ 余弦相似度 ───

def cosine_similarity(u: List[float], v: List[float]) -> Optional[float]:
    """返回 u, v 的余弦相似度。任意为零向量则返回 None。

    >>> cosine_similarity([1, 0], [0, 1])
    0.0
    >>> cosine_similarity([1, 2], [2, 4])
    1.0
    >>> cosine_similarity([0, 0], [1, 1]) is None
    True
    """
    pass


# ─── Q7 ⭐⭐ 判断正交性 ───

def is_orthogonal(u: List[float], v: List[float]) -> bool:
    """判断 u 和 v 是否正交 (u·v ≈ 0)。

    >>> is_orthogonal([1, 0], [0, 1])
    True
    >>> is_orthogonal([1, 2], [3, 4])
    False
    """
    pass


# ─── Q8 ⭐⭐ 检查子空间条件 ───

def is_subspace_candidate(vectors: List[List[float]]) -> bool:
    """检查向量列表中是否包含零向量 (子空间必要条件)。

    >>> is_subspace_candidate([[1, 2], [0, 0], [3, 4]])
    True
    >>> is_subspace_candidate([[1, 2], [3, 4]])
    False
    """
    pass


# ─── Q9 ⭐⭐⭐ 线性组合 ───

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


# ─── Q10 ⭐⭐ 判断共线性 (二维) ───

def are_collinear_2d(u: List[float], v: List[float]) -> bool:
    """判断两个二维向量是否共线 (夹角 0° 或 180°, 或含零向量)。

    >>> are_collinear_2d([1, 2], [2, 4])
    True
    >>> are_collinear_2d([1, 2], [3, 4])
    False
    >>> are_collinear_2d([0, 0], [1, 2])
    True
    """
    pass


# ─── Q11 ⭐⭐ 平行四边形面积 ───

def span_area_2d(u: List[float], v: List[float]) -> float:
    """返回 u, v 张成的平行四边形面积 (二维)。

    >>> span_area_2d([1, 0], [0, 1])
    1.0
    >>> span_area_2d([3, 0], [0, 4])
    12.0
    >>> span_area_2d([1, 2], [2, 4])
    0.0
    """
    pass


# ─── Q12 ⭐⭐⭐ 三角形判定 ───

def is_triangle_vector(a: List[float], b: List[float], c: List[float]) -> bool:
    """三点 (各为二维向量) 能否构成非退化三角形 (面积 > 0)?

    >>> is_triangle_vector([0, 0], [1, 0], [0, 1])
    True
    >>> is_triangle_vector([0, 0], [1, 1], [2, 2])
    False
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
