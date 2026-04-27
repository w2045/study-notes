# 线性代数 · 第四章 · 编程题 — 参考答案

---

## Q1 增广矩阵构造

<details><summary>解</summary>

```python
def make_augmented(A, b):
    return [row + [b[i]] for i, row in enumerate(A)]
```

**要点**：在每行末尾追加 $\mathbf{b}$ 的对应分量。

</details>

---

## Q2 行交换

<details><summary>解</summary>

```python
def row_swap(M, i, j):
    result = [list(row) for row in M]
    result[i], result[j] = result[j], result[i]
    return result
```

</details>

---

## Q3 行缩放

<details><summary>解</summary>

```python
def row_scale(M, i, c):
    result = [list(row) for row in M]
    result[i] = [x * c for x in result[i]]
    return result
```

</details>

---

## Q4 行加减

<details><summary>解</summary>

```python
def row_add(M, target, source, c):
    result = [list(row) for row in M]
    result[target] = [result[target][k] + c * result[source][k] for k in range(len(result[0]))]
    return result
```

</details>

---

## Q5 前向消元（无选主元）

<details><summary>解</summary>

```python
def forward_elimination(A, b):
    A = [list(row) for row in A]
    b = list(b)
    m, n = len(A), len(A[0])
    row = 0
    for col in range(n):
        if row >= m:
            break
        if abs(A[row][col]) < 1e-12:
            continue
        pivot = A[row][col]
        for i in range(row + 1, m):
            factor = A[i][col] / pivot
            for j in range(col, n):
                A[i][j] -= factor * A[row][j]
            b[i] -= factor * b[row]
        row += 1
    return A, b
```

**要点**：逐列找主元，用乘数 `factor` 消去下方元素。

</details>

---

## Q6 回代

<details><summary>解</summary>

```python
def back_substitution(A, b):
    m, n = len(A), len(A[0])
    x = [0.0] * n
    for i in range(m - 1, -1, -1):
        pivot_col = -1
        for j in range(n):
            if abs(A[i][j]) > 1e-12:
                pivot_col = j
                break
        if pivot_col == -1:
            if abs(b[i]) > 1e-12:
                return None
            continue
        s = b[i]
        for j in range(pivot_col + 1, n):
            s -= A[i][j] * x[j]
        x[pivot_col] = s / A[i][pivot_col]
    return x
```

**要点**：从底向上，找到每行的主元列，解出该变量。零行 + 非零常数 = 无解。

</details>

---

## Q7 列主元前向消元

<details><summary>解</summary>

```python
def forward_elimination_pivot(A, b):
    A = [list(row) for row in A]
    b = list(b)
    m, n = len(A), len(A[0])
    row = 0
    for col in range(n):
        if row >= m:
            break
        pivot_row = max(range(row, m), key=lambda r: abs(A[r][col]))
        if abs(A[pivot_row][col]) < 1e-12:
            continue
        if pivot_row != row:
            A[row], A[pivot_row] = A[pivot_row], A[row]
            b[row], b[pivot_row] = b[pivot_row], b[row]
        pivot = A[row][col]
        for i in range(row + 1, m):
            factor = A[i][col] / pivot
            for j in range(col, n):
                A[i][j] -= factor * A[row][j]
            b[i] -= factor * b[row]
        row += 1
    return A, b
```

**要点**：与 Q5 的区别仅在于消元前先找该列绝对值最大的行并交换。

</details>

---

## Q8 LU 分解

<details><summary>解</summary>

```python
def lu_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            s = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - s
        L[i][i] = 1.0
        for j in range(i + 1, n):
            s = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (A[j][i] - s) / U[i][i]
    return L, U
```

**要点**：Doolittle 算法。先填充 $U$ 的第 $i$ 行，再填充 $L$ 的第 $i$ 列（$L_{ii}=1$）。

</details>

---

## Q9 前代

<details><summary>解</summary>

```python
def forward_substitution(L, b):
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        s = b[i]
        for j in range(i):
            s -= L[i][j] * y[j]
        y[i] = s / L[i][i]
    return y
```

**要点**：$L$ 是单位下三角（对角线全 1），从顶向下逐行解。

</details>

---

## Q10 高斯消元完整求解

<details><summary>解</summary>

```python
def gaussian_solve(A, b, use_pivoting=True):
    if use_pivoting:
        Aup, bup = forward_elimination_pivot(A, b)
    else:
        Aup, bup = forward_elimination(A, b)
    return back_substitution(Aup, bup)
```

**要点**：前向消元 + 回代。

</details>

---

## Q11 判断解的情况

<details><summary>解</summary>

```python
def classify_solution(A, b):
    m, n = len(A), len(A[0])
    rank_A = sum(1 for row in A if any(abs(x) > 1e-12 for x in row))
    rank_Ab = sum(1 for i in range(m) if any(abs(x) > 1e-12 for x in A[i]) or abs(b[i]) > 1e-12)
    if rank_A < rank_Ab:
        return 'none'
    elif rank_A < n:
        return 'infinite'
    else:
        return 'unique'
```

**要点**：比较 $\operatorname{rank}(A)$ 和 $\operatorname{rank}([A \mid \mathbf{b}])$，以及 $n$。

</details>

---

## Q12 用 LU 分解求解

<details><summary>解</summary>

```python
def lu_solve(L, U, b):
    y = forward_substitution(L, b)
    x = back_substitution(U, y)
    return x
```

**要点**：先前代解 $L\mathbf{y} = \mathbf{b}$，再回代解 $U\mathbf{x} = \mathbf{y}$。

</details>
