# 线性代数 · 第三章 · 编程题 — 参考答案

---

## Q1 矩阵-向量乘法

<details><summary>解</summary>

```python
def mat_vec_mul(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(A[0])))
            for i in range(len(A))]
```

**要点**：对每行 $i$，计算 $\sum_j a_{ij}x_j$。

</details>

---

## Q2 矩阵乘法

<details><summary>解</summary>

```python
def mat_mul(A, B):
    m, n, p = len(A), len(A[0]), len(B[0])
    C = [[0.0] * p for _ in range(m)]
    for i in range(m):
        for k in range(n):
            if A[i][k] == 0:
                continue
            aik = A[i][k]
            for j in range(p):
                C[i][j] += aik * B[k][j]
    return C
```

**要点**：三重循环，利用内层未知的优化（跳过零元素）。

</details>

---

## Q3 矩阵转置

<details><summary>解</summary>

```python
def transpose(A):
    return [[A[i][j] for i in range(len(A))]
            for j in range(len(A[0]))]
```

**要点**：$(A^T)_{ji} = A_{ij}$，所以外层循环 $j$（新行），内层循环 $i$（新列）。

</details>

---

## Q4 对称/反对称分解

<details><summary>解</summary>

```python
def sym_skew_split(A):
    n = len(A)
    At = transpose(A)
    sym = [[(A[i][j] + At[i][j]) / 2 for j in range(n)] for i in range(n)]
    skew = [[(A[i][j] - At[i][j]) / 2 for j in range(n)] for i in range(n)]
    return sym, skew
```

**要点**：对称部分 = $(A+A^T)/2$，反对称部分 = $(A-A^T)/2$。

</details>

---

## Q5 单位矩阵生成

<details><summary>解</summary>

```python
def identity(n):
    return [[1.0 if i == j else 0.0 for j in range(n)]
            for i in range(n)]
```

**要点**：对角线 $i=j$ 为 1，其余为 0。

</details>

---

## Q6 迹

<details><summary>解</summary>

```python
def trace(A):
    return sum(A[i][i] for i in range(len(A)))
```

**要点**：仅取对角线元素 $a_{ii}$ 求和。

</details>

---

## Q7 对称矩阵判定

<details><summary>解</summary>

```python
def is_symmetric(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if not math.isclose(A[i][j], A[j][i]):
                return False
    return True
```

**要点**：检查每个元素 $a_{ij} \stackrel{?}{=} a_{ji}$。使用 `math.isclose` 处理浮点误差。

</details>

---

## Q8 正交矩阵判定

<details><summary>解</summary>

```python
def is_orthogonal(A):
    n = len(A)
    At = transpose(A)
    P = mat_mul(At, A)
    for i in range(n):
        for j in range(n):
            expected = 1.0 if i == j else 0.0
            if not math.isclose(P[i][j], expected):
                return False
    return True
```

**要点**：验证 $A^T A = I$，即对角线 $\approx 1$，非对角线 $\approx 0$。

</details>

---

## Q9 Frobenius 范数

<details><summary>解</summary>

```python
def frobenius_norm(A):
    return math.sqrt(sum(A[i][j] ** 2 for i in range(len(A))
                          for j in range(len(A[0]))))
```

**要点**：所有元素平方和开根号。

</details>

---

## Q10 对角矩阵生成

<details><summary>解</summary>

```python
def diag_matrix(values):
    n = len(values)
    return [[values[i] if i == j else 0.0 for j in range(n)]
            for i in range(n)]
```

**要点**：对角线填充给定值，其余填 0。

</details>

---

## Q11 Kronecker 积

<details><summary>解</summary>

```python
def kronecker(A, B):
    m, n = len(A), len(A[0])
    p, q = len(B), len(B[0])
    result = []
    for i in range(m):
        for r in range(p):
            row = []
            for j in range(n):
                val = A[i][j]
                for c in range(q):
                    row.append(val * B[r][c])
            result.append(row)
    return result
```

**要点**：对每个 $a_{ij}$，将 $a_{ij}B$ 放入对应的块位置。结果有 $mp$ 行，$nq$ 列。

</details>

---

## Q12 线性变换复合

<details><summary>解</summary>

```python
def compose_transforms(A, B, x):
    Bx = mat_vec_mul(B, x)
    return mat_vec_mul(A, Bx)
```

**要点**：先算 $B\mathbf{x}$ 得到中间向量，再算 $A(B\mathbf{x})$。等价于 $(AB)\mathbf{x}$。

</details>
