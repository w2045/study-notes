# 线性代数 · 第一章 · 编程题 — 参考答案

---

## Q1 ⭐ 向量加法

<details><summary>解</summary>

```python
def vector_sum(u: List[float], v: List[float]) -> List[float]:
    return [a + b for a, b in zip(u, v)]
```

**要点**：`zip` 逐分量相加。

</details>

---

## Q2 ⭐ 向量减法

<details><summary>解</summary>

```python
def vector_diff(u: List[float], v: List[float]) -> List[float]:
    return [a - b for a, b in zip(u, v)]
```

</details>

---

## Q3 ⭐ 标量乘法

<details><summary>解</summary>

```python
def scalar_mult(c: float, v: List[float]) -> List[float]:
    return [c * x for x in v]
```

</details>

---

## Q4 ⭐⭐ 线性组合

<details><summary>解</summary>

```python
def linear_combination(
    vectors: List[List[float]], coeffs: List[float]
) -> List[float]:
    if not vectors:
        return []
    n = len(vectors[0])
    result = [0.0] * n
    for c, v in zip(coeffs, vectors):
        for i in range(n):
            result[i] += c * v[i]
    return result
```

**要点**：初始化为零向量，逐向量累加 $c_i \mathbf{v}_i$。

</details>

---

## Q5 ⭐ 零向量判定

<details><summary>解</summary>

```python
def is_zero_vector(v: List[float]) -> bool:
    return all(math.isclose(x, 0) for x in v)
```

</details>

---

## Q6 ⭐⭐ 标准基向量

<details><summary>解</summary>

```python
def standard_basis(i: int, n: int) -> List[float]:
    v = [0.0] * n
    v[i - 1] = 1.0
    return v
```

**要点**：`i` 是 1-indexed。

</details>

---

## Q7 ⭐⭐ 二维线性无关判定

<details><summary>解</summary>

```python
def are_independent_2d(u: List[float], v: List[float]) -> bool:
    if is_zero_vector(u) or is_zero_vector(v):
        return False
    cross = u[0] * v[1] - u[1] * v[0]
    return not math.isclose(abs(cross), 0)
```

**要点**：二维中两向量线性无关 $\iff$ 都不为零且不共线。共线判据：$u_1 v_2 = u_2 v_1$。

</details>

---

## Q8 ⭐⭐ 二维 span 包含判定

<details><summary>解</summary>

```python
def is_in_span_2d(a: List[float], b: List[float]) -> bool:
    if is_zero_vector(a):
        return is_zero_vector(b)
    cross = a[0] * b[1] - a[1] * b[0]
    return math.isclose(cross, 0)
```

**要点**：$\mathbf{b} \in \operatorname{span}\{\mathbf{a}\} \iff$ 共线。$\mathbf{a} = \mathbf{0}$ 时只有 $\mathbf{b} = \mathbf{0}$ 才在 span 中。

</details>

---

## Q9 ⭐ 子空间必要条件

<details><summary>解</summary>

```python
def contains_zero_vector(vectors: List[List[float]]) -> bool:
    return any(is_zero_vector(v) for v in vectors)
```

</details>

---

## Q10 ⭐⭐⭐ 基坐标表示

<details><summary>解</summary>

```python
def coordinates_in_basis(
    basis: List[List[float]], v: List[float]
) -> Optional[List[float]]:
    b1, b2 = basis[0], basis[1]
    det = b1[0] * b2[1] - b1[1] * b2[0]
    if math.isclose(det, 0):
        return None
    c1 = (v[0] * b2[1] - v[1] * b2[0]) / det
    c2 = (b1[0] * v[1] - b1[1] * v[0]) / det
    return [c1, c2]
```

**要点**：二维用 Cramer 法则解 $\begin{bmatrix}\mathbf{b}_1 & \mathbf{b}_2\end{bmatrix}\begin{bmatrix}c_1\\c_2\end{bmatrix} = \mathbf{v}$。行列式非零保证基的有效性。

</details>

---

## Q11 ⭐⭐⭐ 三维线性无关判定

<details><summary>解</summary>

```python
def are_independent_3d(
    u: List[float], v: List[float], w: List[float]
) -> bool:
    if is_zero_vector(u) or is_zero_vector(v) or is_zero_vector(w):
        return False
    # 标量三重积 (u × v) · w
    cross_x = u[1] * v[2] - u[2] * v[1]
    cross_y = u[2] * v[0] - u[0] * v[2]
    cross_z = u[0] * v[1] - u[1] * v[0]
    triple = cross_x * w[0] + cross_y * w[1] + cross_z * w[2]
    return not math.isclose(triple, 0)
```

**要点**：$\mathbb{R}^3$ 中三个向量线性无关 $\iff$ 标量三重积 $(u \times v) \cdot w \neq 0$（体积非零）。

</details>

---

## Q12 ⭐⭐⭐ 扩充为基（二维）

<details><summary>解</summary>

```python
def extend_to_basis_2d(v: List[float]) -> Optional[List[List[float]]]:
    if is_zero_vector(v):
        return None
    u = [-v[1], v[0]]
    return [v, u]
```

**要点**：旋转 90° 得 $[-y, x]^T$，与 $\mathbf{v}$ 不共线。叉积 $x^2 + y^2 > 0$，线性无关。
</details>
