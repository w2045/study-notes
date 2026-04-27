# 线性代数 · 第九章 · 奇异值分解 SVD — 编程作业

> 完成 `homework.py` 中的函数。运行 `python3 grader.py` 自动批改。
> 难度: ⭐ 基础 | ⭐⭐ 中等 | ⭐⭐⭐ 挑战

---

## Q1 ⭐ 矩阵转置

实现 `transpose(A)`，返回 $A^T$。

```python
transpose([[1, 2, 3], [4, 5, 6]])  → [[1, 4], [2, 5], [3, 6]]
```

---

## Q2 ⭐ 矩阵-向量乘

实现 `mat_vec_mul(A, x)`，返回 $A\mathbf{x}$。

```python
mat_vec_mul([[1, 2], [3, 4]], [5, 6])  → [17, 39]
```

---

## Q3 ⭐ 矩阵乘法

实现 `mat_mul(A, B)`，返回 $AB$。

```python
mat_mul([[1, 2], [3, 4]], [[0, 1], [1, 0]])  → [[2, 1], [4, 3]]
```

---

## Q4 ⭐ 向量范数

实现 `norm(v)`，返回 $\ell_2$ 范数。

```python
norm([3, 4])  → 5.0
```

---

## Q5 ⭐⭐ 幂迭代求最大奇异值

实现 `power_iteration_svd(A, max_iter=1000, tol=1e-10)`。用幂迭代法求最大奇异值及对应的左右奇异向量。返回 `(u, v, sigma)`。

算法：$\mathbf{v}$ 从随机初始化开始，反复 $\mathbf{v} \leftarrow A^T A \mathbf{v} / \|A^T A \mathbf{v}\|$ 直到收敛。

```python
u, v, sigma = power_iteration_svd([[3, 0], [4, 5]])
# sigma ≈ 最大奇异值
```

---

## Q6 ⭐⭐ $A^T A$ 计算

实现 `compute_AtA(A)`。

```python
compute_AtA([[1, 0], [0, 2], [0, 0]])  → [[1, 0], [0, 4]]
```

---

## Q7 ⭐⭐ 谱范数

实现 `spectral_norm(A)`。用幂迭代计算 $\|A\|_2 = \sigma_{\max}(A)$。

```python
spectral_norm([[3, 0], [0, 2]])  → 3.0
```

---

## Q8 ⭐⭐ Frobenius 范数

实现 `frobenius_norm(A)`。$\|A\|_F = \sqrt{\sum a_{ij}^2}$。

```python
frobenius_norm([[3, 0], [0, 4]])  → 5.0
```

---

## Q9 ⭐⭐⭐ 低秩近似

实现 `low_rank_approx(U, S, Vt, k)`。从截断 SVD 重建秩-$k$ 近似矩阵：

$$A_k = \sum_{i=1}^{k} \sigma_i \mathbf{u}_i \mathbf{v}_i^T$$

其中 $U$ 是 $m \times r$，$V_t$ 是 $r \times n$，$S$ 是长度为 $r$ 的奇异值列表。

```python
U = [[0.6, -0.8], [0.8, 0.6]]
S = [5.0, 3.0]
Vt = [[0.6, 0.8], [-0.8, 0.6]]
Ak = low_rank_approx(U, S, Vt, 1)
# Ak ≈ [[1.8, 2.4], [2.4, 3.2]]
```

---

## Q10 ⭐⭐⭐ SVD 重构误差

实现 `svd_reconstruction_error(A, U, S, Vt, k)`。计算原矩阵与秩-$k$ SVD 近似之间的 Frobenius 误差。

```python
A = [[3, 0], [4, 5]]
U, S, Vt = ..., k = 1
err = svd_reconstruction_error(A, U, S, Vt, 1)
# ≈ sigma_2 (被截断的奇异值)
```

---

## Q11 ⭐⭐ 条件数

实现 `condition_number(S)`。从奇异值列表计算条件数 $\kappa = \sigma_{\max} / \sigma_{\min}$。

```python
condition_number([5.0, 3.0])     → 1.6666666666666667
condition_number([100.0, 0.01])  → 10000.0
```

---

## Q12 ⭐⭐⭐ 图像压缩比

实现 `compress_ratio(H, W, k)`。用 SVD 做图像压缩时，原始存储 $H \times W$，截断到秩 $k$ 后存储 $k \times (H + W + 1)$。返回压缩比。

```python
compress_ratio(100, 100, 10)  → 49.75...  # 约 50 倍压缩
```
