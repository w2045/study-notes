# 线性代数 · 第八章 · 正定矩阵、投影与 QR 分解 — 编程作业

> 完成 `homework.py` 中的函数。运行 `python3 grader.py` 自动批改。
> 难度: ⭐ 基础 | ⭐⭐ 中等 | ⭐⭐⭐ 挑战

---

## Q1 ⭐ 二次型计算

实现 `quadratic_form(A, x)`，计算 $\mathbf{x}^T A \mathbf{x}$。

```python
quadratic_form([[2, 0], [0, 3]], [1, 1])  → 5.0
quadratic_form([[1, 2], [2, 1]], [1, 0])  → 1.0
```

---

## Q2 ⭐ 正定性判断（特征值法）

实现 `is_positive_definite_eigen(A)`。对 2x2 对称矩阵，用特征值判断正定性（所有 $\lambda_i > 0$）。

```python
is_positive_definite_eigen([[3, 0], [0, 1]])  → True
is_positive_definite_eigen([[1, 2], [2, 1]])  → False
```

---

## Q3 ⭐ Sylvester 判据

实现 `is_positive_definite_sylvester(A)`。对 2x2 对称矩阵，用前主子式判断正定性。

```python
is_positive_definite_sylvester([[4, 1], [1, 1]])  → True
is_positive_definite_sylvester([[1, 2], [2, 0]])  → False
```

---

## Q4 ⭐ 直线上的正交投影

实现 `project_onto_line(a, b)`。计算 $\mathbf{b}$ 到 $\mathbf{a}$ 方向上的正交投影。

$$\operatorname{proj}_{\mathbf{a}}(\mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\mathbf{a} \cdot \mathbf{a}} \mathbf{a}$$

```python
project_onto_line([1, 0], [3, 4])  → [3.0, 0.0]
```

---

## Q5 ⭐⭐ Cholesky 分解 (2x2)

实现 `cholesky_2x2(A)`。返回 2x2 正定矩阵的 Cholesky 分解 $L$（$A = LL^T$）。若不正定返回 `None`。

```python
cholesky_2x2([[4, 2], [2, 5]])  → [[2.0, 0.0], [1.0, 2.0]]
cholesky_2x2([[1, 2], [2, 1]])  → None  # 不正定
```

---

## Q6 ⭐⭐ 投影矩阵构造

实现 `projection_matrix(A)`。返回投影到 $\operatorname{col}(A)$ 的正交投影矩阵 $P = A(A^T A)^{-1}A^T$（仅支持 2 列）。

```python
P = projection_matrix([[1, 0], [0, 1], [0, 0]])
# → [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]]
```

---

## Q7 ⭐⭐ 正规方程求解最小二乘

实现 `least_squares(A, b)`。用正规方程 $A^T A \mathbf{x} = A^T \mathbf{b}$ 求解 $\min \|A\mathbf{x} - \mathbf{b}\|_2$。

```python
least_squares([[1, 0], [0, 1], [0, 0]], [2, 3, 4])  → [2.0, 3.0]
```

---

## Q8 ⭐⭐ Gram-Schmidt (QR 的 Q)

实现 `gram_schmidt_q(A)`。对矩阵的各列做 Gram-Schmidt 正交化 + 归一化，返回列正交矩阵 $Q$（$Q^T Q = I$）。

```python
Q = gram_schmidt_q([[3, 0], [4, 5]])
# Q 的各列范数为 1
```

---

## Q9 ⭐⭐⭐ QR 分解

实现 `qr_decomposition(A)`。对 $m \times n$ 矩阵做 Gram-Schmidt 版 QR 分解，返回 `(Q, R)`。

```python
Q, R = qr_decomposition([[3, 0], [4, 5]])
# A ≈ Q @ R,  Q^T Q ≈ I,  R 上三角
```

---

## Q10 ⭐⭐⭐ 用 QR 解最小二乘

实现 `least_squares_qr(A, b)`。用 QR 分解解 $\min \|A\mathbf{x} - \mathbf{b}\|_2$。先分解 $A = QR$，再解 $R\mathbf{x} = Q^T\mathbf{b}$。比正规方程数值更稳定。

```python
x = least_squares_qr([[1, 1], [1, 2], [1, 3]], [1, 2, 2])
# x ≈ [0.666..., 0.5]
```

---

## Q11 ⭐⭐ 验证投影幂等性

实现 `is_projection(P)`。验证 $P$ 是否为正交投影矩阵（$P^2 \approx P$ 且 $P^T \approx P$）。

```python
is_projection([[1, 0], [0, 0]])  → True
is_projection([[1, 0], [0, 1]])  → True
```

---

## Q12 ⭐⭐⭐ Cholesky 分解 (n*n)

实现 `cholesky(A)`。对 $n \times n$ 正定矩阵做 Cholesky 分解，返回下三角矩阵 $L$。若不正定返回 `None`。

```python
L = cholesky([[4, 2, 2], [2, 5, 1], [2, 1, 6]])
# L 非 None, 验证 A ≈ L @ L^T
```
