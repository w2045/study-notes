# 线性代数 · 第九章 · 编程题 — 参考答案

---

## Q1 矩阵转置

<details><summary>解</summary>

```python
def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
```

</details>

---

## Q2 矩阵-向量乘

<details><summary>解</summary>

```python
def mat_vec_mul(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]
```

</details>

---

## Q3 矩阵乘法

<details><summary>解</summary>

```python
def mat_mul(A, B):
    m, n, p = len(A), len(A[0]), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(p)] for i in range(m)]
```

</details>

---

## Q4 向量范数

<details><summary>解</summary>

```python
def norm(v):
    return math.sqrt(sum(x * x for x in v))
```

</details>

---

## Q5 幂迭代求最大奇异向量

<details><summary>解</summary>

```python
def power_iteration_svd(A, max_iter=1000, tol=1e-10):
    import random
    m, n = len(A), len(A[0])
    v = [random.random() for _ in range(n)]
    nrm = math.sqrt(sum(x*x for x in v))
    v = [x/nrm for x in v]
    At = transpose(A)
    for _ in range(max_iter):
        Av = mat_vec_mul(A, v)
        u = [x/math.sqrt(sum(xi*xi for xi in Av)) for x in Av]
        Atu = mat_vec_mul(At, u)
        v_new = [x/math.sqrt(sum(xi*xi for xi in Atu)) for x in Atu]
        cos_sim = sum(a*b for a, b in zip(v, v_new))
        if abs(cos_sim) > 1 - tol:
            v = v_new
            break
        v = v_new
    Av = mat_vec_mul(A, v)
    sigma = math.sqrt(sum(x*x for x in Av))
    u = [x/sigma for x in Av]
    return u, v, sigma
```

**要点**：$\mathbf{v}_{k+1} = A^T A \mathbf{v}_k / \|A^T A \mathbf{v}_k\|$ 收敛到最大右奇异向量。然后 $A\mathbf{v} = \sigma \mathbf{u}$。

</details>

---

## Q6 $A^T A$ 计算

<details><summary>解</summary>

```python
def compute_AtA(A):
    At = transpose(A)
    return mat_mul(At, A)
```

</details>

---

## Q7 谱范数

<details><summary>解</summary>

```python
def spectral_norm(A):
    m, n = len(A), len(A[0])
    if min(m, n) == 1:
        return math.sqrt(sum(A[i][0]**2 for i in range(m))) if n == 1 else frobenius_norm(A)
    _, _, sigma = power_iteration_svd(A)
    return sigma
```

</details>

---

## Q8 Frobenius 范数

<details><summary>解</summary>

```python
def frobenius_norm(A):
    return math.sqrt(sum(A[i][j]**2 for i in range(len(A)) for j in range(len(A[0]))))
```

</details>

---

## Q9 低秩近似

<details><summary>解</summary>

```python
def low_rank_approx(U, S, Vt, k):
    m, n = len(U), len(Vt[0])
    result = [[0.0] * n for _ in range(m)]
    for idx in range(min(k, len(S))):
        sigma = S[idx]
        u_col = [U[i][idx] for i in range(m)]
        v_row = Vt[idx]
        for i in range(m):
            for j in range(n):
                result[i][j] += sigma * u_col[i] * v_row[j]
    return result
```

**要点**：$A_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^T$。

</details>

---

## Q10 SVD 重构误差

<details><summary>解</summary>

```python
def svd_reconstruction_error(A, U, S, Vt, k):
    Ak = low_rank_approx(U, S, Vt, k)
    total = 0.0
    for i in range(len(A)):
        for j in range(len(A[0])):
            diff = A[i][j] - Ak[i][j]
            total += diff * diff
    return math.sqrt(total)
```

</details>

---

## Q11 条件数

<details><summary>解</summary>

```python
def condition_number(S):
    sigma_max = max(S)
    sigma_min = min(s for s in S if s > 1e-12)
    return sigma_max / sigma_min
```

</details>

---

## Q12 图像压缩演示的简化

<details><summary>解</summary>

```python
def compress_ratio(H, W, k):
    original = H * W
    compressed = k * (H + W + 1)
    return original / compressed
```

**要点**：$k$ 个奇异值 + $kH$ 个左奇异向量分量 + $kW$ 个右奇异向量分量。

</details>
