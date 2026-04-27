# 线性代数 · 第八章 · 编程题 — 参考答案

---

## Q1 二次型计算

<details><summary>解</summary>

```python
def quadratic_form(A, x):
    n = len(x)
    return sum(x[i] * sum(A[i][j] * x[j] for j in range(n)) for i in range(n))
```

**要点**：$\mathbf{x}^T A \mathbf{x} = \sum_i x_i \sum_j a_{ij} x_j$。

</details>

---

## Q2 正定性（特征值）

<details><summary>解</summary>

```python
def is_positive_definite_eigen(A):
    tr = A[0][0] + A[1][1]
    detA = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    disc = tr * tr - 4 * detA
    if disc < 0:
        return False
    l1 = (tr + math.sqrt(disc)) / 2
    l2 = (tr - math.sqrt(disc)) / 2
    return l1 > 0 and l2 > 0
```

**要点**：2x2 特征值 = $(\operatorname{tr} \pm \sqrt{\operatorname{tr}^2 - 4\det})/2$。若特征值含虚部则不正定。

</details>

---

## Q3 Sylvester 判据

<details><summary>解</summary>

```python
def is_positive_definite_sylvester(A):
    d1 = A[0][0]
    d2 = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return d1 > 0 and d2 > 0
```

**要点**：2x2 正定 $\iff a_{11} > 0$ 且 $\det A > 0$。

</details>

---

## Q4 直线上的正交投影

<details><summary>解</summary>

```python
def project_onto_line(a, b):
    coeff = sum(bi * ai for bi, ai in zip(b, a)) / sum(ai * ai for ai in a)
    return [coeff * ai for ai in a]
```

</details>

---

## Q5 Cholesky 分解 (2x2)

<details><summary>解</summary>

```python
def cholesky_2x2(A):
    if A[0][0] <= 0:
        return None
    l11 = math.sqrt(A[0][0])
    l21 = A[1][0] / l11
    val = A[1][1] - l21 * l21
    if val <= 0:
        return None
    l22 = math.sqrt(val)
    return [[l11, 0.0], [l21, l22]]
```

**要点**：$\ell_{11} = \sqrt{a_{11}}$，$\ell_{21} = a_{21}/\ell_{11}$，$\ell_{22} = \sqrt{a_{22} - \ell_{21}^2}$。

</details>

---

## Q6 投影矩阵构造

<details><summary>解</summary>

```python
def projection_matrix(A):
    m, n = len(A), len(A[0])
    At = [[A[j][i] for j in range(m)] for i in range(n)]
    AtA = [[sum(At[i][k] * A[k][j] for k in range(m)) for j in range(n)] for i in range(n)]
    if n == 2:
        det = AtA[0][0] * AtA[1][1] - AtA[0][1] * AtA[1][0]
        inv = [[AtA[1][1]/det, -AtA[0][1]/det], [-AtA[1][0]/det, AtA[0][0]/det]]
    else:
        return None
    invAt = [[sum(inv[i][k] * At[k][j] for k in range(n)) for j in range(m)] for i in range(n)]
    P = [[sum(A[i][k] * invAt[k][j] for k in range(n)) for j in range(m)] for i in range(m)]
    return P
```

</details>

---

## Q7 正规方程求解最小二乘

<details><summary>解</summary>

```python
def least_squares(A, b):
    m, n = len(A), len(A[0])
    At = [[A[j][i] for j in range(m)] for i in range(n)]
    AtA = [[sum(At[i][k] * A[k][j] for k in range(m)) for j in range(n)] for i in range(n)]
    Atb = [sum(At[i][j] * b[j] for j in range(m)) for i in range(n)]
    # 解 2x2 系统 AtA x = Atb
    det = AtA[0][0] * AtA[1][1] - AtA[0][1] * AtA[1][0]
    if abs(det) < 1e-12:
        return None
    x1 = (AtA[1][1] * Atb[0] - AtA[0][1] * Atb[1]) / det
    x2 = (AtA[0][0] * Atb[1] - AtA[1][0] * Atb[0]) / det
    return [x1, x2]
```

</details>

---

## Q8 Gram-Schmidt (QR 的 Q)

<details><summary>解</summary>

```python
def gram_schmidt_q(A):
    m, n = len(A), len(A[0])
    cols = [[A[i][j] for i in range(m)] for j in range(n)]
    Q = []
    for a in cols:
        u = list(a)
        for q in Q:
            coeff = sum(a[i] * q[i] for i in range(m))
            u = [u[i] - coeff * q[i] for i in range(m)]
        norm = math.sqrt(sum(x*x for x in u))
        if norm > 1e-12:
            u = [x / norm for x in u]
        Q.append(u)
    return [[Q[j][i] for j in range(n)] for i in range(m)]
```

</details>

---

## Q9 QR 分解

<details><summary>解</summary>

```python
def qr_decomposition(A):
    m, n = len(A), len(A[0])
    cols = [[A[i][j] for i in range(m)] for j in range(n)]
    Q_cols = []
    R = [[0.0]*n for _ in range(n)]
    for j, a in enumerate(cols):
        u = list(a)
        for i, q in enumerate(Q_cols):
            r_ij = sum(a[k] * q[k] for k in range(m))
            R[i][j] = r_ij
            u = [u[k] - r_ij * q[k] for k in range(m)]
        norm_u = math.sqrt(sum(x*x for x in u))
        R[j][j] = norm_u
        if norm_u > 1e-12:
            u = [x / norm_u for x in u]
        Q_cols.append(u)
    Q = [[Q_cols[j][i] for j in range(n)] for i in range(m)]
    return Q, R
```

**要点**：对每列做 Gram-Schmidt，记录 $r_{ij} = \mathbf{q}_i^T \mathbf{a}_j$，$r_{jj} = \|\mathbf{u}_j\|$。

</details>

---

## Q10 用 QR 解最小二乘

<details><summary>解</summary>

```python
def least_squares_qr(A, b):
    Q, R = qr_decomposition(A)
    m, n = len(A), len(A[0])
    # c = Q^T b
    c = [sum(Q[i][j] * b[i] for i in range(m)) for j in range(n)]
    # 回代 R x = c
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = c[i]
        for j in range(i + 1, n):
            s -= R[i][j] * x[j]
        x[i] = s / R[i][i]
    return x
```

</details>

---

## Q11 验证投影幂等性

<details><summary>解</summary>

```python
def is_projection(P):
    n = len(P)
    # P^2
    P2 = [[sum(P[i][k] * P[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    # P^T
    Pt = [[P[j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not math.isclose(P2[i][j], P[i][j]):
                return False
            if not math.isclose(Pt[i][j], P[i][j]):
                return False
    return True
```

</details>

---

## Q12 Cholesky 分解 (n×n)

<details><summary>解</summary>

```python
def cholesky(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                val = A[i][i] - s
                if val <= 0:
                    return None
                L[i][j] = math.sqrt(val)
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]
    return L
```

**要点**：逐列计算。先对角线 $\ell_{ii} = \sqrt{a_{ii} - \sum \ell_{ik}^2}$，再下方 $\ell_{ji} = (a_{ji} - \sum \ell_{jk}\ell_{ik}) / \ell_{ii}$。

</details>
