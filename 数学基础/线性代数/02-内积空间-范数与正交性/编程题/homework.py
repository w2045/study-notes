"""
线性代数 · 第二章 · 内积空间、范数与正交性 — 编程作业

所有函数用 list[float] 表示向量。完成函数体后运行: python3 grader.py
"""

import math
from typing import List, Optional


# ─── Q1 ⭐ 点积 ───

def dot_product(u: List[float], v: List[float]) -> float:
    """返回 u · v。

    >>> dot_product([1, 2], [3, 4])
    11
    >>> dot_product([1, 0], [0, 1])
    0
    """
    pass


# ─── Q2 ⭐ ℓ2 范数 ───

def norm_l2(v: List[float]) -> float:
    """返回 ||v||_2。

    >>> norm_l2([3, 4])
    5.0
    >>> norm_l2([0, 0])
    0.0
    """
    pass


# ─── Q3 ⭐ ℓ1 与 ℓ∞ 范数 ───

def norm_l1(v: List[float]) -> float:
    """返回 ||v||_1（分量绝对值之和）。

    >>> norm_l1([3, -4])
    7.0
    """
    pass


def norm_linf(v: List[float]) -> float:
    """返回 ||v||_∞（最大绝对值分量）。

    >>> norm_linf([3, -4, 2])
    4.0
    """
    pass


# ─── Q4 ⭐ 归一化 ───

def normalize(v: List[float]) -> Optional[List[float]]:
    """返回 v / ||v||_2。零向量返回 None。

    >>> normalize([3, 4])
    [0.6, 0.8]
    >>> normalize([0, 0]) is None
    True
    """
    pass


# ─── Q5 ⭐⭐ 余弦相似度 ───

def cosine_similarity(u: List[float], v: List[float]) -> Optional[float]:
    """返回 u, v 的余弦相似度。任意为零向量则返回 None。

    >>> cosine_similarity([1, 0], [0, 1])
    0.0
    >>> cosine_similarity([1, 2], [2, 4])
    1.0
    """
    pass


# ─── Q6 ⭐⭐ 正交判定 ───

def is_orthogonal(u: List[float], v: List[float]) -> bool:
    """判断 u 和 v 是否正交 (u·v ≈ 0)。

    >>> is_orthogonal([1, 0], [0, 1])
    True
    >>> is_orthogonal([1, 2], [3, 4])
    False
    """
    pass


# ─── Q7 ⭐⭐ 正交投影 ───

def projection(u: List[float], v: List[float]) -> List[float]:
    """v 到 u 上的正交投影向量（u 非零）。

    >>> projection([1, 0], [3, 4])
    [3.0, 0.0]
    """
    pass


# ─── Q8 ⭐⭐ Gram-Schmidt 一步 ───

def gram_schmidt_step(
    v: List[float], existing: List[List[float]]
) -> List[float]:
    """对 v 执行一步 Gram-Schmidt：减去 v 在 existing 中所有向量上的投影。
    existing 中的向量已是正交组。

    >>> gram_schmidt_step([0, 1, 1], [[1, 1, 0]])
    [-0.5, 0.5, 1.0]
    """
    pass


# ─── Q9 ⭐⭐⭐ 完整 Gram-Schmidt ───

def gram_schmidt(vectors: List[List[float]]) -> List[List[float]]:
    """对线性无关向量组执行完整 Gram-Schmidt 正交化（不归一化）。

    >>> gram_schmidt([[1, 1, 0], [0, 1, 1]])
    [[1.0, 1.0, 0.0], [-0.5, 0.5, 1.0]]
    """
    pass


# ─── Q10 ⭐⭐⭐ Cauchy-Schwarz 验证 ───

def satisfies_cauchy_schwarz(u: List[float], v: List[float]) -> bool:
    """验证 u, v 是否满足 Cauchy-Schwarz 不等式：|u·v| ≤ ||u||·||v||。

    >>> satisfies_cauchy_schwarz([1, 2], [3, 4])
    True
    """
    pass


# ─── Q11 ⭐⭐ 三角不等式验证 ───

def satisfies_triangle(u: List[float], v: List[float]) -> bool:
    """验证 ||u + v|| ≤ ||u|| + ||v||。

    >>> satisfies_triangle([1, 2], [3, 4])
    True
    """
    pass


# ─── Q12 ⭐⭐⭐ 正交向量组判定 ───

def is_orthogonal_set(vectors: List[List[float]]) -> bool:
    """判断向量组是否两两正交（不含零向量）。

    >>> is_orthogonal_set([[1, 0], [0, 1]])
    True
    >>> is_orthogonal_set([[1, 0], [1, 1]])
    False
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
