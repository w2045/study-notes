# 线性代数 · 第二章 · 内积空间、范数与正交性 — 编程作业

> 完成 `homework.py` 中的函数。运行 `python3 grader.py` 自动批改。
> 难度: ⭐ 基础 | ⭐⭐ 中等 | ⭐⭐⭐ 挑战

---

## Q1 ⭐ 点积

实现 `dot_product(u, v)`，返回两向量的欧几里得内积。

```python
dot_product([1, 2], [3, 4])  → 11
dot_product([1, 0], [0, 1])  → 0
dot_product([], [])          → 0
```

---

## Q2 ⭐ ℓ2 范数

实现 `norm_l2(v)`，计算向量的欧几里得长度。

```python
norm_l2([3, 4])     → 5.0
norm_l2([1, 0, 0])  → 1.0
norm_l2([0, 0])     → 0.0
```

---

## Q3 ⭐ ℓ1 与 ℓ∞ 范数

实现 `norm_l1(v)` 和 `norm_linf(v)`。

$$\|\mathbf{v}\|_1 = \sum |v_i|, \quad \|\mathbf{v}\|_{\infty} = \max_i |v_i|$$

```python
norm_l1([3, -4])       → 7.0
norm_linf([3, -4, 2])  → 4.0
```

---

## Q4 ⭐ 归一化

实现 `normalize(v)`，返回 $\mathbf{v} / \|\mathbf{v}\|_2$。零向量返回 `None`。

```python
normalize([3, 4])    → [0.6, 0.8]
normalize([0, 0])    → None
normalize([5, 0])    → [1.0, 0.0]
```

---

## Q5 ⭐⭐ 余弦相似度

实现 `cosine_similarity(u, v)`。任意为零向量返回 `None`。

$$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$$

```python
cosine_similarity([1, 0], [0, 1])   → 0.0
cosine_similarity([1, 2], [2, 4])   → 1.0
cosine_similarity([1, 0], [-1, 0])  → -1.0
cosine_similarity([0, 0], [1, 1])   → None
```

---

## Q6 ⭐⭐ 正交判定

实现 `is_orthogonal(u, v)`，判断 $\mathbf{u} \cdot \mathbf{v} \approx 0$。

```python
is_orthogonal([1, 0], [0, 1])     → True
is_orthogonal([1, 2], [3, 4])     → False
is_orthogonal([1, 2], [-2, 1])    → True   # 1×(-2) + 2×1 = 0
```

---

## Q7 ⭐⭐ 正交投影

实现 `projection(u, v)`，计算 $\mathbf{v}$ 在 $\mathbf{u}$ 上的正交投影向量（$\mathbf{u} \neq \mathbf{0}$）。

$$\operatorname{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\mathbf{v} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}} \mathbf{u}$$

```python
projection([1, 0], [3, 4])    → [3.0, 0.0]
projection([0, 1], [3, 4])    → [0.0, 4.0]
projection([1, 1], [2, 2])    → [2.0, 2.0]
```

---

## Q8 ⭐⭐ Gram-Schmidt 一步

实现 `gram_schmidt_step(v, existing)`。从 $\mathbf{v}$ 中减去它在 `existing` 各向量上的投影（现有向量已经是正交组）。

```python
gram_schmidt_step([0, 1, 1], [[1, 1, 0]])  → [-0.5, 0.5, 1.0]
gram_schmidt_step([1, 2, 3], [])            → [1, 2, 3]
```

---

## Q9 ⭐⭐⭐ 完整 Gram-Schmidt 正交化

实现 `gram_schmidt(vectors)`。对线性无关向量组执行完整 Gram-Schmidt（不归一化，只正交化）。

```python
gram_schmidt([[1, 1, 0], [0, 1, 1]])  
# → [[1.0, 1.0, 0.0], [-0.5, 0.5, 1.0]]
```

---

## Q10 ⭐⭐⭐ Cauchy-Schwarz 验证

实现 `satisfies_cauchy_schwarz(u, v)`。验证 $|\mathbf{u} \cdot \mathbf{v}| \leq \|\mathbf{u}\| \|\mathbf{v}\|$。

```python
satisfies_cauchy_schwarz([1, 2], [3, 4])  → True
satisfies_cauchy_schwarz([1, 2], [2, 4])  → True  # 等号成立（共线）
```

---

## Q11 ⭐⭐ 三角不等式验证

实现 `satisfies_triangle(u, v)`。验证 $\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$。

```python
satisfies_triangle([1, 2], [3, 4])  → True
satisfies_triangle([1, 0], [2, 0])  → True
```

---

## Q12 ⭐⭐⭐ 正交向量组判定

实现 `is_orthogonal_set(vectors)`。判断向量组是否两两正交（且不含零向量）。

```python
is_orthogonal_set([[1, 0], [0, 1]])                       → True
is_orthogonal_set([[1, 0, 0], [0, 1, 0], [0, 0, 1]])     → True
is_orthogonal_set([[1, 0], [1, 1]])                       → False
is_orthogonal_set([[0, 0], [1, 1]])                       → False
```
