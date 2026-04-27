# 线性代数 · 第三章 · 矩阵与线性变换 — 编程作业

> 完成 `homework.py` 中的函数。运行 `python3 grader.py` 自动批改。
> 难度: ⭐ 基础 | ⭐⭐ 中等 | ⭐⭐⭐ 挑战

---

## Q1 ⭐ 矩阵-向量乘法

实现 `mat_vec_mul(A, x)`，计算 $\mathbf{b} = A\mathbf{x}$（$A: m \times n$, $\mathbf{x} \in \mathbb{R}^n$, $\mathbf{b} \in \mathbb{R}^m$）。

```python
mat_vec_mul([[1, 2], [3, 4]], [5, 6])       → [17, 39]
mat_vec_mul([[1, 0, 0], [0, 1, 0]], [1, 2, 3])  → [1, 2]
```

---

## Q2 ⭐ 矩阵乘法

实现 `mat_mul(A, B)`，计算 $C = AB$。

```python
mat_mul([[1, 2], [3, 4]], [[0, 1], [1, 0]])  → [[2, 1], [4, 3]]
mat_mul([[1, 0, 2], [0, 1, 1]], [[1, 0], [0, 1], [1, 1]])  → [[3, 2], [1, 2]]
```

---

## Q3 ⭐ 矩阵转置

实现 `transpose(A)`，返回 $A^T$。

```python
transpose([[1, 2, 3], [4, 5, 6]])  → [[1, 4], [2, 5], [3, 6]]
transpose([[1, 2], [3, 4]])        → [[1, 3], [2, 4]]
```

---

## Q4 ⭐ 对称/反对称分解

实现 `sym_skew_split(A)`。将方阵分解为 $A = S + K$，其中 $S = \frac{A + A^T}{2}$ 对称，$K = \frac{A - A^T}{2}$ 反对称。

```python
sym, skew = sym_skew_split([[1, 3], [-1, 2]])
# sym  → [[1.0, 1.0], [1.0, 2.0]]
# skew → [[0.0, 2.0], [-2.0, 0.0]]
```

---

## Q5 ⭐ 单位矩阵生成

实现 `identity(n)`，返回 $n \times n$ 单位矩阵 $I_n$。

```python
identity(3)  → [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
```

---

## Q6 ⭐⭐ 迹

实现 `trace(A)`，返回方阵的迹 $\operatorname{tr}(A) = \sum a_{ii}$。

```python
trace([[1, 2], [3, 4]])  → 5.0
trace([[1, 0, 0], [0, 2, 0], [0, 0, 3]])  → 6.0
```

---

## Q7 ⭐⭐ 对称矩阵判定

实现 `is_symmetric(A)`，判断 $A^T = A$。

```python
is_symmetric([[1, 2], [2, 1]])  → True
is_symmetric([[1, 2], [3, 4]])  → False
```

---

## Q8 ⭐⭐ 正交矩阵判定

实现 `is_orthogonal(A)`，判断 $A^T A \approx I$（使用 `math.isclose`）。

```python
is_orthogonal([[1, 0], [0, 1]])    → True
is_orthogonal([[0, -1], [1, 0]])   → True   # 旋转矩阵
is_orthogonal([[1, 1], [1, -1]])   → False
```

---

## Q9 ⭐⭐ Frobenius 范数

实现 `frobenius_norm(A)`，计算 $\|A\|_F = \sqrt{\sum_{i,j} a_{ij}^2}$。

```python
frobenius_norm([[3, 0], [0, 4]])  → 5.0
frobenius_norm([[1, 2], [3, 4]])  → 5.477225575051661
```

---

## Q10 ⭐⭐ 对角矩阵生成

实现 `diag_matrix(values)`。从对角线元素列表构造 $n \times n$ 对角矩阵。

```python
diag_matrix([1, 2, 3])  → [[1.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 3.0]]
```

---

## Q11 ⭐⭐⭐ Kronecker 积

实现 `kronecker(A, B)`，返回 $A \otimes B$。

若 $A$ 是 $m \times n$，$B$ 是 $p \times q$，则 $A \otimes B$ 是 $mp \times nq$ 的分块矩阵，第 $(i,j)$ 块为 $a_{ij} B$。

```python
kronecker([[1, 0], [0, 1]], [[1, 2], [3, 4]])
# → [[1.0, 2.0, 0.0, 0.0],
#    [3.0, 4.0, 0.0, 0.0],
#    [0.0, 0.0, 1.0, 2.0],
#    [0.0, 0.0, 3.0, 4.0]]
```

---

## Q12 ⭐⭐⭐ 线性变换复合

实现 `compose_transforms(A, B, x)`。先应用变换 $B$，再应用 $A$：返回 $A(B\mathbf{x})$。

```python
compose_transforms([[0, -1], [1, 0]], [[2, 0], [0, 1]], [1, 1])  → [-1.0, 2.0]
```
