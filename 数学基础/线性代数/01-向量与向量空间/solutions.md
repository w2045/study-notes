# 线性代数 · 第一章 · 参考答案

---

## Q1 — 向量加减

<details><summary>点击查看答案</summary>

```python
def vector_sum(u, v):
    return [a + b for a, b in zip(u, v)]

def vector_diff(u, v):
    return [a - b for a, b in zip(u, v)]
```

**要点**: `zip` 逐对取出分量。注意维数应相同（grader 保证这一点）。
</details>

---

## Q2 — 标量乘法

<details><summary>点击查看答案</summary>

```python
def scalar_mult(c, v):
    return [c * x for x in v]
```
</details>

---

## Q3 — 欧几里得范数

<details><summary>点击查看答案</summary>

```python
def euclidean_norm(v):
    return math.sqrt(sum(x**2 for x in v))
```
</details>

---

## Q4 — 点积

<details><summary>点击查看答案</summary>

```python
def dot_product(u, v):
    return sum(a * b for a, b in zip(u, v))
```
</details>

---

## Q5 — 归一化

<details><summary>点击查看答案</summary>

```python
def normalize(v):
    n = math.sqrt(sum(x**2 for x in v))
    if n == 0:
        return None
    return [x / n for x in v]
```

**要点**: 零向量不能归一化，返回 `None`。不要忘记检查除零。
</details>

---

## Q6 — 余弦相似度

<details><summary>点击查看答案</summary>

```python
def cosine_similarity(u, v):
    nu = math.sqrt(sum(x**2 for x in u))
    nv = math.sqrt(sum(x**2 for x in v))
    if nu == 0 or nv == 0:
        return None
    return sum(a * b for a, b in zip(u, v)) / (nu * nv)
```

**要点**: 先检查零向量再除法，避免 `ZeroDivisionError`。
</details>

---

## Q7 — 判断正交性

<details><summary>点击查看答案</summary>

```python
def is_orthogonal(u, v):
    dot = sum(a * b for a, b in zip(u, v))
    return math.isclose(dot, 0.0, abs_tol=1e-9)
```

**要点**: 不要用 `dot == 0.0`——浮点运算有误差，用 `math.isclose`。
</details>

---

## Q8 — 检查子空间条件

<details><summary>点击查看答案</summary>

```python
def is_subspace_candidate(vectors):
    if not vectors:
        return False
    for v in vectors:
        if all(x == 0 for x in v):
            return True
    return False
```

**要点**: 子空间的必要条件：零向量必须在集合中。空集不是子空间。
</details>

---

## Q9 — 线性组合

<details><summary>点击查看答案</summary>

```python
def linear_combination(vectors, coeffs):
    if not vectors:
        return []
    dim = len(vectors[0])
    result = [0.0] * dim
    for c, v in zip(coeffs, vectors):
        for i in range(dim):
            result[i] += c * v[i]
    return result
```

**推导**：线性组合 = 逐分量累加 $c_j \cdot v_{j,i}$。
</details>

---

## Q10 — 判断共线性（二维）

<details><summary>点击查看答案</summary>

```python
def are_collinear_2d(u, v):
    nu = math.sqrt(u[0]**2 + u[1]**2)
    nv = math.sqrt(v[0]**2 + v[1]**2)
    if nu == 0 or nv == 0:
        return True          # 零向量与任意向量共线
    dot = u[0]*v[0] + u[1]*v[1]
    return math.isclose(abs(dot), nu * nv, rel_tol=1e-9)
```

**原理**：$|\mathbf{u}\cdot\mathbf{v}| = \|\mathbf{u}\|\|\mathbf{v}\| \iff$ 夹角为 0° 或 180°，即共线。
</details>

---

## Q11 — 平行四边形面积

<details><summary>点击查看答案</summary>

```python
def span_area_2d(u, v):
    return abs(u[0] * v[1] - u[1] * v[0])
```

**原理**：$\begin{vmatrix} u_1 & u_2 \\ v_1 & v_2 \end{vmatrix}$ 的绝对值等于平行四边形面积。这是行列式的几何意义。
</details>

---

## Q12 — 三角形判定（向量）

<details><summary>点击查看答案</summary>

```python
def is_triangle_vector(a, b, c):
    # 向量 ab = b - a, ac = c - a
    ab = [b[0] - a[0], b[1] - a[1]]
    ac = [c[0] - a[0], c[1] - a[1]]
    # 面积 = |ab × ac| (二维叉积)
    area = abs(ab[0] * ac[1] - ab[1] * ac[0])
    return area > 0  # 不是 math.isclose(area, 0)
```

**原理**：三点共线 $\iff$ $\overrightarrow{AB}$ 与 $\overrightarrow{AC}$ 共线 $\iff$ 叉积为零。退化三角形面积 = 0。
</details>
