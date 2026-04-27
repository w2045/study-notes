# 线性代数 · 第四章 · 线性方程组与消元法

← 前置: [03 — 矩阵与线性变换](../03-矩阵与线性变换/notes.md)
→ 延伸: [05 — 行列式、逆、秩与矩阵范数](../05-行列式-逆-秩与矩阵范数/notes.md)

---

## 1. 直觉引入：从「猜解」到「系统求解」

第三章告诉我们 $A\mathbf{x} = \mathbf{b}$ 是线性变换。但知道它是什么，不等于知道**怎么求 $\mathbf{x}$**。

初中学二元一次方程用代入消元，三元就头疼了。线性代数的答案是：**高斯消元法**——一种把任何线性方程组机械化求解的算法。

> **核心洞察**：消元 = 把矩阵变成「上三角」的阶梯形。从最后一行的「单变量方程」开始回代，逐行解出所有未知数。整个过程是确定性的、算法化的。

---

## 2. 线性方程组的形式

> **定义 1（线性方程组）**：$m$ 个方程、$n$ 个未知数的线性方程组：
>
> $$\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\ \quad \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m \end{cases}$$

**矩阵形式**：$A\mathbf{x} = \mathbf{b}$，其中 $A \in \mathbb{R}^{m \times n}$ 是系数矩阵，$\mathbf{x} \in \mathbb{R}^n$ 是未知向量，$\mathbf{b} \in \mathbb{R}^m$ 是常数向量。

**增广矩阵**：$[A \mid \mathbf{b}]$，将 $A$ 和 $\mathbf{b}$ 并排写在一起。

---

## 3. 高斯消元法 (Gaussian Elimination)

### 3.1 三种初等行操作

消元法基于三种不改变解集的**初等行操作**：

| # | 操作 | 记法 | 意义 |
|---|------|------|------|
| 1 | 交换两行 | $R_i \leftrightarrow R_j$ | 重排方程顺序 |
| 2 | 某行乘非零标量 | $R_i \leftarrow cR_i$, $c \neq 0$ | 两边同乘 |
| 3 | 某行加另一行的倍数 | $R_i \leftarrow R_i + cR_j$ | 消去变量 |

### 3.2 前向消元 (Forward Elimination)

目标：将 $A$ 化为**行阶梯形 (Row Echelon Form, REF)**。

**REF 条件**：
1. 全零行在最底部
2. 每行的第一个非零元素（主元，pivot）在其上一行主元的严格右侧

**算法**（逐列处理）：
1. 选第 $k$ 列：找 $k$ 行及以下中绝对值最大的元素作**主元**
2. 若该列全零，跳到下一列
3. 将主元交换到第 $k$ 行
4. 主元归一化（可选）：$R_k \leftarrow R_k / a_{kk}$
5. 消去下面的行：对 $i = k+1, \ldots, m$，$R_i \leftarrow R_i - a_{ik} R_k$

### 3.3 回代 (Back Substitution)

前向消元后得到上三角方程组。从最后一行开始逐行求解：

对 $i = n, n-1, \ldots, 1$：
$$x_i = \left(b_i - \sum_{j=i+1}^{n} a_{ij} x_j\right) \Big/ a_{ii}$$

**前提**：$a_{ii} \neq 0$（主元非零）。若有零主元，方程组可能无解或有无穷多解。

---

## 4. 列主元消元法 (Partial Pivoting)

### 4.1 为什么需要选主元？

经典的逐个消元可能遇到**零主元**（无法归一化）或**极小主元**（导致数值不稳定）。

**例子**：$\begin{cases} 0.0001 x_1 + x_2 = 1 \\ x_1 + x_2 = 2 \end{cases}$

若不选主元，直接用 $0.0001$ 归一化会产生巨大舍入误差。

### 4.2 列主元策略

在消去第 $k$ 列时，从第 $k$ 行到第 $m$ 行中选绝对值最大的元素所在行作主元行，将该行交换到第 $k$ 行。

**效果**：数值稳定 + 避免零主元（除非整列为零）。

**全主元 (Full Pivoting)**：同时考虑行和列的交换。更稳定但通常不必需。

---

## 5. 解的三种情况

对 $A\mathbf{x} = \mathbf{b}$（$A$ 为 $m \times n$）：

| 情况 | 条件 | 解数 |
|------|------|------|
| 唯一解 | $\operatorname{rank}(A) = \operatorname{rank}([A\mid\mathbf{b}]) = n$ | 1 |
| 无穷多解 | $\operatorname{rank}(A) = \operatorname{rank}([A\mid\mathbf{b}]) < n$ | $\infty$（$n - \operatorname{rank}$ 个自由变量） |
| 无解 | $\operatorname{rank}(A) < \operatorname{rank}([A\mid\mathbf{b}])$ | 0 |

**齐次方程组 $A\mathbf{x} = \mathbf{0}$**：必有零解。非零解存在 $\iff \operatorname{rank}(A) < n$。

---

## 6. 行阶梯形的进一步：行最简形 (RREF)

**RREF (Reduced Row Echelon Form)** 在 REF 基础上再加条件：
- 每个主元都是 1
- 每个主元所在列的其余元素都是 0

RREF 是解空间的「标准形式」。从 RREF 可以直接读出基础解系。

---

## 7. LU 分解

### 7.1 动机

如果要对多个不同的 $\mathbf{b}$ 解 $A\mathbf{x} = \mathbf{b}$，每次都做消元太低效。LU 分解将工作一分为二：
- **分解**（一次性）：$A = LU$
- **求解**（多次快速）：$L\mathbf{y} = \mathbf{b}$ → $U\mathbf{x} = \mathbf{y}$

### 7.2 定义

> **定义 2（LU 分解）**：将方阵 $A$ 分解为 $A = LU$，其中：
> - $L$ 是**下三角矩阵**（对角线全为 1，单位下三角）
> - $U$ 是**上三角矩阵**

**存在条件**：$A$ 的所有前主子式非零（即不需要行交换时）。

### 7.3 算法（Doolittle 方法）

对 $k = 1, \ldots, n$：

1. **计算 $U$ 的第 $k$ 行**：$u_{kj} = a_{kj} - \sum_{i=1}^{k-1} \ell_{ki} u_{ij}$，$j = k, \ldots, n$

2. **计算 $L$ 的第 $k$ 列**（$i = k+1, \ldots, n$）：
   $$\ell_{ik} = \left(a_{ik} - \sum_{j=1}^{k-1} \ell_{ij} u_{jk}\right) \Big/ u_{kk}$$

**与消元的关系**：消元过程中的乘数 $m_{ik} = a_{ik}^{(k)} / a_{kk}^{(k)}$ 正是 $\ell_{ik}$！

### 7.4 带行交换的 LU：PLU 分解

如果选主元时交换了行，则 $PA = LU$，其中 $P$ 是**置换矩阵**。

**求解 $A\mathbf{x} = \mathbf{b}$**：
1. 置换：$\mathbf{b}' = P\mathbf{b}$
2. 前代：解 $L\mathbf{y} = \mathbf{b}'$
3. 回代：解 $U\mathbf{x} = \mathbf{y}$

---

## 8. LU 分解的几何直觉

$A = LU$ 可理解为把复杂变换 $A$ 拆成两步：

1. $U$：先做消元（把原来的空间变成上三角结构）
2. $L$：再逆向恢复消元过程的「记录」

消元过程本身是可逆的（只要不做除以零的操作）——这意味着 $A$ 蕴含的信息可以无损分解。

---

## 9. 代码实现

```python
from typing import List, Tuple, Optional
import math


def forward_elimination(
    A: List[List[float]], b: List[float], use_pivoting: bool = True
) -> Tuple[List[List[float]], List[float]]:
    """前向消元（可选列主元），返回 (A, b) 的行阶梯形。"""
    A = [list(row) for row in A]
    b = list(b)
    m, n = len(A), len(A[0])
    row = 0
    for col in range(n):
        if row >= m:
            break
        # 选主元
        if use_pivoting:
            pivot_row = max(range(row, m), key=lambda r: abs(A[r][col]))
            if abs(A[pivot_row][col]) < 1e-12:
                continue
            if pivot_row != row:
                A[row], A[pivot_row] = A[pivot_row], A[row]
                b[row], b[pivot_row] = b[pivot_row], b[row]
        else:
            if abs(A[row][col]) < 1e-12:
                continue
        # 消去下面的行
        pivot = A[row][col]
        for i in range(row + 1, m):
            factor = A[i][col] / pivot
            for j in range(col, n):
                A[i][j] -= factor * A[row][j]
            b[i] -= factor * b[row]
        row += 1
    return A, b


def back_substitution(A: List[List[float]], b: List[float]) -> Optional[List[float]]:
    """回代求解上三角方程组。无解或无穷解返回 None。"""
    m, n = len(A), len(A[0])
    x = [0.0] * n
    # 从最后一行往回
    for i in range(m - 1, -1, -1):
        # 找第一个非零列（主元列）
        pivot_col = -1
        for j in range(n):
            if abs(A[i][j]) > 1e-12:
                pivot_col = j
                break
        if pivot_col == -1:
            if abs(b[i]) > 1e-12:
                return None  # 0 = non-zero, 无解
            continue  # 0 = 0, 自由变量（暂时跳过）
        s = b[i]
        for j in range(pivot_col + 1, n):
            s -= A[i][j] * x[j]
        x[pivot_col] = s / A[i][pivot_col]
    return x


def lu_decomposition(
    A: List[List[float]]
) -> Tuple[List[List[float]], List[List[float]]]:
    """Doolittle LU 分解 (无选主元)，返回 (L, U)。"""
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        # U 的第 i 行
        for j in range(i, n):
            s = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - s
        # L 的第 i 列
        L[i][i] = 1.0
        for j in range(i + 1, n):
            s = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (A[j][i] - s) / U[i][i]
    return L, U
```

---

## 10. 例题

### 例 1：高斯消元完整过程

解方程组：
$$\begin{cases} x_1 + 2x_2 + x_3 = 2 \\ 2x_1 + 6x_2 + x_3 = 7 \\ x_1 + x_2 + 4x_3 = 3 \end{cases}$$

<details><summary>解</summary>

增广矩阵：
$$\begin{bmatrix} 1 & 2 & 1 & 2 \\ 2 & 6 & 1 & 7 \\ 1 & 1 & 4 & 3 \end{bmatrix}$$

$R_2 \leftarrow R_2 - 2R_1$：$\begin{bmatrix} 1 & 2 & 1 & 2 \\ 0 & 2 & -1 & 3 \\ 1 & 1 & 4 & 3 \end{bmatrix}$

$R_3 \leftarrow R_3 - R_1$：$\begin{bmatrix} 1 & 2 & 1 & 2 \\ 0 & 2 & -1 & 3 \\ 0 & -1 & 3 & 1 \end{bmatrix}$

$R_3 \leftarrow R_3 + \frac{1}{2}R_2$：$\begin{bmatrix} 1 & 2 & 1 & 2 \\ 0 & 2 & -1 & 3 \\ 0 & 0 & \frac{5}{2} & \frac{5}{2} \end{bmatrix}$

回代：
- $x_3 = \frac{5/2}{5/2} = 1$
- $2x_2 - 1 = 3 \implies x_2 = 2$
- $x_1 + 4 + 1 = 2 \implies x_1 = -3$

解：$[-3, 2, 1]^T$。

</details>

### 例 2：LU 分解

对 $A = \begin{bmatrix} 2 & 1 \\ 6 & 8 \end{bmatrix}$ 做 LU 分解。

<details><summary>解</summary>

消元步：$R_2 \leftarrow R_2 - 3R_1$，其中乘数 $3$ 存入 $L$。

$$L = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 2 & 1 \\ 0 & 5 \end{bmatrix}$$

验证：$LU = \begin{bmatrix} 2 & 1 \\ 6 & 8 \end{bmatrix} = A$。✓

</details>

---

## 11. 常见误区

| 误区 | 正确理解 |
|------|----------|
| 「消元可以任意顺序做」 | 必须逐列从左上到右下，否则前功尽弃 |
| 「有零主元就是无解」 | 可能有无穷多解（该列为自由变量） |
| 「LU 分解总是存在」 | 需要所有前主子式非零。否则需 $PA = LU$ |
| 「回代永远能得到解」 | 若消元后出现 $0 = c$（$c \neq 0$），则无解 |

---

## 本章核心概念速查

| 概念 | 定义 | 一句话 |
|------|------|--------|
| 增广矩阵 | $[A \mid \mathbf{b}]$ | 把方程组写成矩阵 |
| 初等行操作 | 交换/缩放/加倍数 | 不改变解集的三种操作 |
| 前向消元 | 化为行阶梯形 | 自顶向下消去变量 |
| 主元 | 每行第一个非零元素 | 消元的「支点」 |
| 列主元 | 选该列绝对值最大者 | 数值稳定的关键 |
| 回代 | 从下往上求解 | 上三角矩阵的「自然解法」 |
| REF | 行阶梯形 | 每行主元在上一行主元右侧 |
| RREF | 行最简形 | 主元 = 1，该列其余 = 0 |
| LU 分解 | $A = LU$ | 一次分解，多次求解 |
| PLU 分解 | $PA = LU$ | 带行交换的 LU |

---

← 前置: [03 — 矩阵与线性变换](../03-矩阵与线性变换/notes.md)
→ 延伸: [05 — 行列式、逆、秩与矩阵范数](../05-行列式-逆-秩与矩阵范数/notes.md)
