# 线性代数 · 第一章 · 向量与向量空间 — 作业

> 完成 `homework.py` 中的函数。运行 `python3 grader.py` 自动批改。
> 难度: ⭐ 基础 | ⭐⭐ 中等 | ⭐⭐⭐ 挑战

---

## Q1 ⭐ 向量加减

实现 `vector_sum(u, v)` 和 `vector_diff(u, v)`，返回两个同维向量的和与差。

```python
vector_sum([1, 2], [3, 4])  → [4, 6]
vector_diff([5, 7], [2, 3]) → [3, 4]
```

---

## Q2 ⭐ 标量乘法

实现 `scalar_mult(c, v)`。

```python
scalar_mult(3, [1, 2, 3]) → [3, 6, 9]
scalar_mult(0, [5, 5])    → [0, 0]
scalar_mult(-2, [1, 2])   → [-2, -4]
```

---

## Q3 ⭐ 欧几里得范数

实现 `euclidean_norm(v)`，计算向量长度。**不允许使用 `math.hypot` 或 `numpy`。**

```python
euclidean_norm([3, 4])      → 5.0
euclidean_norm([1, 0, 0])  → 1.0
euclidean_norm([0, 0])     → 0.0
```

---

## Q4 ⭐ 点积

实现 `dot_product(u, v)`。

```python
dot_product([1, 2], [3, 4])   → 11
dot_product([1, 0], [0, 1])   → 0    # 正交
dot_product([2, 2], [2, 2])   → 8
```

---

## Q5 ⭐ 归一化

实现 `normalize(v)`，返回同方向的单位向量。零向量返回 `None`。

```python
normalize([3, 4])    → [0.6, 0.8]
normalize([0, 0])    → None
normalize([5, 0])    → [1.0, 0.0]
```

---

## Q6 ⭐⭐ 余弦相似度

实现 `cosine_similarity(u, v)`。如果任意向量为零向量，返回 `None`。

$$\operatorname{cosine\_sim} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$$

```python
cosine_similarity([1, 0], [0, 1])   → 0.0
cosine_similarity([1, 2], [2, 4])   → 1.0
cosine_similarity([1, 0], [-1, 0])  → -1.0
cosine_similarity([0, 0], [1, 1])   → None
```

---

## Q7 ⭐⭐ 判断正交性

实现 `is_orthogonal(u, v)`，判断两向量是否正交（夹角 90°）。使用 `math.isclose` 容差。

```python
is_orthogonal([1, 0], [0, 1])     → True
is_orthogonal([1, 2], [3, 4])     → False
is_orthogonal([1, 2], [-2, 1])    → True   # 内积 = -2+2 = 0
```

---

## Q8 ⭐⭐ 检查子空间条件

实现 `is_subspace_candidate(vectors)`。给定列表中的向量集合（按行给出），判断它们是否可能构成 $\mathbb{R}^n$ 的子空间（只检查「零向量是否在集合中」这一必要条件）。

```python
is_subspace_candidate([[1, 2], [0, 0], [3, 4]])  → True   # 含 [0,0]
is_subspace_candidate([[1, 2], [3, 4]])           → False  # 不含零向量
```

---

## Q9 ⭐⭐⭐ 线性组合计算

实现 `linear_combination(vectors, coeffs)`。给定向量列表和系数列表，计算线性组合。

```python
linear_combination([ [1, 0], [0, 1] ], [3, 4])  → [3, 4]
linear_combination([ [1, 2, 3] ], [5])           → [5, 10, 15]
```

---

## Q10 ⭐⭐ 判断共线性（二维）

实现 `are_collinear_2d(u, v)`，判断两个二维向量是否共线。利用性质：两向量共线 $\iff$ 它们的内积绝对值 = 范数乘积。

```python
are_collinear_2d([1, 2], [2, 4])   → True
are_collinear_2d([1, 2], [3, 4])   → False
are_collinear_2d([0, 0], [1, 2])   → True    # 零向量与任何向量共线
```

---

## Q11 ⭐⭐ 两个向量张成的平面面积（二维）

实现 `span_area_2d(u, v)`，计算 $\mathbb{R}^2$ 中两个向量所张成平行四边形的面积。

$$\text{Area} = |u_1 v_2 - u_2 v_1|$$

（这是行列式的绝对值，我们会在第四章正式学习。）

```python
span_area_2d([1, 0], [0, 1])   → 1.0
span_area_2d([3, 0], [0, 4])   → 12.0
span_area_2d([1, 2], [2, 4])   → 0.0    # 共线 → 面积为零
```

---

## Q12 ⭐⭐⭐ 三角形判定

实现 `is_triangle_vector(a, b, c)`。给定三角形三个顶点的坐标（每个是二维向量），判断它们是否能构成非退化三角形（面积 > 0）。三个顶点共线时构不成三角形。

```python
is_triangle_vector([0,0], [1,0], [0,1])   → True
is_triangle_vector([0,0], [1,1], [2,2])   → False   # 三点共线
is_triangle_vector([1,1], [1,1], [2,3])   → False   # 两点重合
```
