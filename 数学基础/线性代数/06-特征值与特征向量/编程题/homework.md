# 线性代数 · 第六章 · 特征值与特征向量 — 编程作业

> 完成 `homework.py` 中的函数。运行 `python3 grader.py` 自动批改。
> 难度: ⭐ 基础 | ⭐⭐ 中等 | ⭐⭐⭐ 挑战

---

## Q1 ⭐ 2x2 特征多项式系数

实现 `char_poly_2x2(A)`。返回 $(a, b, c)$ 满足 $a\lambda^2 + b\lambda + c = 0$，其中 $a=1$, $b=-\operatorname{tr}(A)$, $c=\det(A)$。

```python
char_poly_2x2([[3, 0], [0, 5]])  → (1.0, -8.0, 15.0)
char_poly_2x2([[4, 1], [2, 3]])  → (1.0, -7.0, 10.0)
```

---

## Q2 ⭐ 2x2 特征值

实现 `eigenvalues_2x2(A)`。利用特征多项式 $\lambda^2 - \operatorname{tr}(A)\lambda + \det(A) = 0$ 求根。可能返回复数。

```python
eigenvalues_2x2([[3, 0], [0, 5]])  → [3.0, 5.0]
sorted(eigenvalues_2x2([[2, 1], [1, 2]]))  → [1.0, 3.0]
```

---

## Q3 ⭐ 验证特征向量

实现 `is_eigenvector(A, v)`。若 $\mathbf{v}$ 是 $A$ 的特征向量（$A\mathbf{v} = \lambda\mathbf{v}$），返回特征值 $\lambda$；否则返回 `None`。

```python
is_eigenvector([[4, 2], [1, 3]], [2, 1])  → 5.0
is_eigenvector([[4, 2], [1, 3]], [1, 1])  → None
```

---

## Q4 ⭐ 迹

实现 `trace(A)`，返回方阵的迹 $\operatorname{tr}(A) = \sum a_{ii}$。

```python
trace([[1, 2], [3, 4]])  → 5.0
```

---

## Q5 ⭐ 行列式 2x2

实现 `determinant_2x2(A)`。

```python
determinant_2x2([[3, 0], [0, 5]])  → 15.0
determinant_2x2([[1, 2], [3, 4]])  → -2.0
```

---

## Q6 ⭐⭐ 矩阵-向量乘

实现 `mat_vec_mul(A, x)`，返回 $A\mathbf{x}$。

```python
mat_vec_mul([[1, 2], [3, 4]], [5, 6])  → [17, 39]
```

---

## Q7 ⭐⭐ 对角化验证

实现 `check_diagonalization(A, P, Lambda)`。验证 $A \approx P\Lambda P^{-1}$（仅 2x2 矩阵）。

```python
A = [[2, 1], [1, 2]]
P = [[1, 1], [-1, 1]]
Lambda = [[1, 0], [0, 3]]
check_diagonalization(A, P, Lambda)  → True
```

---

## Q8 ⭐⭐ 特征值乘积 = 行列式

实现 `verify_eigenvalue_det(A)`。验证 2x2 矩阵的 $\lambda_1 \lambda_2 \approx \det(A)$。

```python
verify_eigenvalue_det([[3, 0], [0, 5]])  → True
verify_eigenvalue_det([[4, 1], [2, 3]])  → True
```

---

## Q9 ⭐⭐⭐ 幂迭代法

实现 `power_iteration(A, max_iter=1000, tol=1e-10)`。用幂迭代法求最大绝对值特征值及对应特征向量，返回 `(eigenvector, eigenvalue)`。

算法：从一个随机向量开始，反复做 $\mathbf{v}_{k+1} = A\mathbf{v}_k / \|A\mathbf{v}_k\|$，收敛到主特征向量；Rayleigh 商给出特征值。

```python
v, lam = power_iteration([[2, 1], [1, 2]])
# lam ≈ 3.0, v ≈ [1, 1] 方向
```

---

## Q10 ⭐⭐⭐ 三角矩阵特征值

实现 `eigenvalues_triangular(A)`。三角矩阵的特征值就是对角线元素本身。

```python
eigenvalues_triangular([[2, 5, -3], [0, -1, 4], [0, 0, 6]])  → [2.0, -1.0, 6.0]
```

---

## Q11 ⭐⭐ Rayleigh 商

实现 `rayleigh_quotient(A, v)`。返回 $R(A, \mathbf{v}) = \frac{\mathbf{v}^T A\mathbf{v}}{\mathbf{v}^T\mathbf{v}}$。

如果 $\mathbf{v}$ 是特征向量，$R(A, \mathbf{v})$ 就是特征值。

```python
rayleigh_quotient([[2, 0], [0, 3]], [1, 0])  → 2.0
```

---

## Q12 ⭐⭐⭐ 对角化计算矩阵幂

实现 `matrix_power_diag(A, k)`。通过对角化 $A = P\Lambda P^{-1}$ 计算 $A^k = P\Lambda^k P^{-1}$（仅 2x2，假设 $A$ 可对角化）。

```python
rounded = matrix_power_diag([[1, 2], [0, -1]], 2)
# → [[1.0, 0.0], [0.0, 1.0]]  (即 I)
```
