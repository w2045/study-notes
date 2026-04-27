# 线性代数 · 第六章 · 编程题 — 参考答案

---

## Q1 2x2 特征多项式系数

<details><summary>解</summary>

```python
def char_poly_2x2(A):
    a = 1.0
    b = -(A[0][0] + A[1][1])
    c = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return a, b, c
```

**要点**：特征多项式 = $\lambda^2 - \operatorname{tr}(A)\lambda + \det(A)$。

</details>

---

## Q2 2x2 特征值

<details><summary>解</summary>

```python
def eigenvalues_2x2(A):
    a, b, c = 1.0, -(A[0][0] + A[1][1]), A[0][0]*A[1][1] - A[0][1]*A[1][0]
    disc = b*b - 4*a*c
    if disc >= 0:
        sqrt_d = math.sqrt(disc)
        return [(-b + sqrt_d)/(2*a), (-b - sqrt_d)/(2*a)]
    else:
        sqrt_d = math.sqrt(-disc)
        return [complex(-b/(2*a), sqrt_d/(2*a)),
                complex(-b/(2*a), -sqrt_d/(2*a))]
```

**要点**：用二次公式。判别式 $\geq 0$ 时返回实数，否则返回复数。

</details>

---

## Q3 验证特征向量

<details><summary>解</summary>

```python
def is_eigenvector(A, v):
    Av = [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]
    ratios = []
    for i in range(len(v)):
        if abs(v[i]) > 1e-12:
            ratios.append(Av[i] / v[i])
    if not ratios:
        return None
    first = ratios[0]
    if all(math.isclose(r, first) for r in ratios):
        return first
    return None
```

**要点**：计算 $A\mathbf{v}$ 与 $\mathbf{v}$ 的逐分量比值。若所有比值相等（非零分量），则为特征向量。

</details>

---

## Q4 迹

<details><summary>解</summary>

```python
def trace(A):
    return sum(A[i][i] for i in range(len(A)))
```

</details>

---

## Q5 行列式 2x2

<details><summary>解</summary>

```python
def determinant_2x2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]
```

</details>

---

## Q6 矩阵-向量乘

<details><summary>解</summary>

```python
def mat_vec_mul(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]
```

</details>

---

## Q7 对角化验证

<details><summary>解</summary>

```python
def check_diagonalization(A, P, Lambda):
    n = len(A)
    # 计算 P @ Lambda
    PL = [[sum(P[i][k] * Lambda[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    # 计算 P^{-1} (2x2 only)
    detP = P[0][0] * P[1][1] - P[0][1] * P[1][0]
    Pinv = [[P[1][1]/detP, -P[0][1]/detP], [-P[1][0]/detP, P[0][0]/detP]]
    # P @ Lambda @ P^{-1}
    result = [[sum(PL[i][k] * Pinv[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return all(math.isclose(result[i][j], A[i][j]) for i in range(n) for j in range(n))
```

**要点**：计算 $P\Lambda P^{-1}$，验证 $\approx A$。

</details>

---

## Q8 特征值乘积 = 行列式

<details><summary>解</summary>

```python
def verify_eigenvalue_det(A):
    evals = eigenvalues_2x2(A)
    prod = 1.0
    for ev in evals:
        prod *= ev.real if isinstance(ev, complex) else ev
    det = determinant_2x2(A)
    return math.isclose(prod, det)
```

</details>

---

## Q9 幂迭代法

<details><summary>解</summary>

```python
def power_iteration(A, max_iter=1000, tol=1e-10):
    import random
    n = len(A)
    v = [random.random() for _ in range(n)]
    nrm = math.sqrt(sum(x*x for x in v))
    v = [x/nrm for x in v]
    for _ in range(max_iter):
        Av = [sum(A[i][j]*v[j] for j in range(n)) for i in range(n)]
        nrm = math.sqrt(sum(x*x for x in Av))
        v_new = [x/nrm for x in Av]
        cos_sim = sum(a*b for a, b in zip(v, v_new))
        if abs(cos_sim) > 1 - tol:
            v = v_new
            break
        v = v_new
    Av = [sum(A[i][j]*v[j] for j in range(n)) for i in range(n)]
    rayleigh = sum(v[i]*Av[i] for i in range(n))
    return v, rayleigh
```

**要点**：反复归一化 $A\mathbf{v}$。Rayleigh 商给出特征值。收敛条件 $|\cos(\mathbf{v}_k, \mathbf{v}_{k+1})| \approx 1$。

</details>

---

## Q10 三角矩阵特征值

<details><summary>解</summary>

```python
def eigenvalues_triangular(A):
    return [A[i][i] for i in range(len(A))]
```

**要点**：三角矩阵的特征值 = 对角线元素。

</details>

---

## Q11 Rayleigh 商

<details><summary>解</summary>

```python
def rayleigh_quotient(A, v):
    Av = [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]
    numerator = sum(v[i] * Av[i] for i in range(len(v)))
    denominator = sum(x * x for x in v)
    return numerator / denominator
```

**要点**：$\frac{\mathbf{v}^T A \mathbf{v}}{\mathbf{v}^T \mathbf{v}}$。当 $\mathbf{v}$ 是特征向量时等于对应特征值。

</details>

---

## Q12 对角化计算矩阵幂

<details><summary>解</summary>

```python
def matrix_power_diag(A, k):
    ev = eigenvalues_2x2(A)
    l1, l2 = ev[0], ev[1]
    # 特征向量 (对 [[1,2],[0,-1]])
    # 不对，对于一般A，应当求特征向量
    # 简化：假设已传入2x2对角化矩阵，这里使用具体公式
    # 通用实现：
    tr = A[0][0] + A[1][1]
    detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    disc = math.sqrt(tr*tr - 4*detA)
    l1 = (tr + disc) / 2
    l2 = (tr - disc) / 2
    # 构造P, Lambda^k
    if abs(A[0][1]) < 1e-12 and abs(A[1][0]) < 1e-12:
        return [[A[0][0]**k, 0], [0, A[1][1]**k]]
    # 特征向量
    v1_0 = A[0][1]
    v1_1 = l1 - A[0][0]
    v2_0 = A[0][1]
    v2_1 = l2 - A[0][0]
    detP = v1_0 * v2_1 - v1_1 * v2_0
    Pinv = [[v2_1/detP, -v2_0/detP], [-v1_1/detP, v1_0/detP]]
    Lambda_k = [[l1**k, 0], [0, l2**k]]
    # P @ Lambda^k
    PL = [[v1_0*Lambda_k[0][0] + v2_0*Lambda_k[1][0], v1_0*Lambda_k[0][1] + v2_0*Lambda_k[1][1]],
          [v1_1*Lambda_k[0][0] + v2_1*Lambda_k[1][0], v1_1*Lambda_k[0][1] + v2_1*Lambda_k[1][1]]]
    # P Lambda^k P^{-1}
    result = [[sum(PL[i][k2]*Pinv[k2][j] for k2 in range(2)) for j in range(2)] for i in range(2)]
    return result
```

**要点**：$A^k = P\Lambda^k P^{-1}$。$\Lambda^k$ 只需将对角线元素各求 $k$ 次幂。

</details>
