# 线性代数 · 第二章 · 编程题 — 参考答案

---

## Q1 点积

<details><summary>解</summary>

```python
def dot_product(u, v):
    return sum(a * b for a, b in zip(u, v))
```

</details>

---

## Q2 ℓ2 范数

<details><summary>解</summary>

```python
def norm_l2(v):
    return math.sqrt(sum(x ** 2 for x in v))
```

</details>

---

## Q3 ℓ1 与 ℓ∞ 范数

<details><summary>解</summary>

```python
def norm_l1(v):
    return sum(abs(x) for x in v)

def norm_linf(v):
    return max(abs(x) for x in v)
```

</details>

---

## Q4 归一化

<details><summary>解</summary>

```python
def normalize(v):
    n = math.sqrt(sum(x ** 2 for x in v))
    if n == 0:
        return None
    return [x / n for x in v]
```

</details>

---

## Q5 余弦相似度

<details><summary>解</summary>

```python
def cosine_similarity(u, v):
    nu = math.sqrt(sum(x ** 2 for x in u))
    nv = math.sqrt(sum(x ** 2 for x in v))
    if nu == 0 or nv == 0:
        return None
    return sum(a * b for a, b in zip(u, v)) / (nu * nv)
```

</details>

---

## Q6 正交判定

<details><summary>解</summary>

```python
def is_orthogonal(u, v):
    return math.isclose(sum(a * b for a, b in zip(u, v)), 0)
```

**要点**：零向量与任意向量内积为 0，故正交。

</details>

---

## Q7 正交投影

<details><summary>解</summary>

```python
def projection(u, v):
    coeff = sum(a * b for a, b in zip(v, u)) / sum(x ** 2 for x in u)
    return [coeff * x for x in u]
```

</details>

---

## Q8 Gram-Schmidt 一步

<details><summary>解</summary>

```python
def gram_schmidt_step(v, existing):
    u = list(v)
    for e in existing:
        coeff = sum(a * b for a, b in zip(v, e)) / sum(x ** 2 for x in e)
        u = [u[i] - coeff * e[i] for i in range(len(u))]
    return u
```

**要点**：从 v 中逐个减去在已有正交向量上的投影分量。

</details>

---

## Q9 完整 Gram-Schmidt

<details><summary>解</summary>

```python
def gram_schmidt(vectors):
    result = []
    for v in vectors:
        u = list(v)
        for existing in result:
            coeff = sum(a * b for a, b in zip(v, existing)) / sum(x ** 2 for x in existing)
            u = [u[i] - coeff * existing[i] for i in range(len(u))]
        result.append(u)
    return result
```

</details>

---

## Q10 Cauchy-Schwarz 验证

<details><summary>解</summary>

```python
def satisfies_cauchy_schwarz(u, v):
    dot_abs = abs(sum(a * b for a, b in zip(u, v)))
    return dot_abs <= math.sqrt(sum(x**2 for x in u)) * math.sqrt(sum(x**2 for x in v)) + 1e-12
```

</details>

---

## Q11 三角不等式验证

<details><summary>解</summary>

```python
def satisfies_triangle(u, v):
    s = [u[i] + v[i] for i in range(len(u))]
    n_sum = math.sqrt(sum(x**2 for x in s))
    n_u = math.sqrt(sum(x**2 for x in u))
    n_v = math.sqrt(sum(x**2 for x in v))
    return n_sum <= n_u + n_v + 1e-12
```

</details>

---

## Q12 正交向量组判定

<details><summary>解</summary>

```python
def is_orthogonal_set(vectors):
    for v in vectors:
        if all(math.isclose(x, 0) for x in v):
            return False  # 不含零向量
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            if not math.isclose(sum(a * b for a, b in zip(vectors[i], vectors[j])), 0):
                return False
    return True
```

**要点**：检查所有对 $(i, j)$ 的内积 + 排除零向量。

</details>
