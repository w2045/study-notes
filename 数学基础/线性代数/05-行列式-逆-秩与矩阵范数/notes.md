# 线性代数 · 第五章 · 行列式、逆、秩与矩阵范数

← 前置: [04 — 线性方程组与消元法](../04-线性方程组与消元法/notes.md)
→ 延伸: [06 — 特征值与特征向量](../06-特征值与特征向量/notes.md)

---

## 1. 直觉引入：三个核心问题

前四章建立了矩阵代数和消元法。现在回到三个基本问题：

1. **可逆性**：变换 $A$ 是否可逆？即能否从 $\mathbf{b} = A\mathbf{x}$ 唯一恢复 $\mathbf{x}$？
2. **「大小」度量**：矩阵 $A$ 能「拉伸」向量多少倍？矩阵本身有多「大」？
3. **秩**：矩阵到底携带了几个独立方向的「有效信息」？

> **核心洞察**：行列式（一个数）回答可逆性；范数（一个数）回答大小；秩（一个数）回答信息量。三个标量，三种视角，统一回答矩阵的基本性质。

---

## 2. 行列式 (Determinant)

### 2.1 几何直觉

行列式 $\det(A)$ 衡量 $A$ 对空间的「体积缩放因子」。

$\mathbb{R}^2$ 中：$\det(A)$ = 变换后平行四边形的**有向面积**。
$\mathbb{R}^3$ 中：$\det(A)$ = 变换后平行六面体的**有向体积**。

- $\det(A) = 0$：空间被「压扁」到更低维 → $A$ 不可逆
- $\det(A) > 0$：保持定向
- $\det(A) < 0$：反转定向（如反射）

### 2.2 公理化定义

> **定义 1（行列式公理）**：函数 $\det: \mathbb{R}^{n \times n} \to \mathbb{R}$ 满足：
>
> 1. **多重线性**：对每一列（或行）是线性的
>    $$\det([\cdots, c\mathbf{u} + \mathbf{v}, \cdots]) = c\det([\cdots, \mathbf{u}, \cdots]) + \det([\cdots, \mathbf{v}, \cdots])$$
>
> 2. **交错性**：若两列相同，则行列式为 0
>
> 3. **归一化**：$\det(I_n) = 1$

这三条公理**唯一**确定了行列式。

**由公理推出的性质**：
- 交换两列 → 行列式变号
- 将一列的倍数加到另一列 → 行列式不变
- 若有一列全为零 → 行列式为 0
- 列向量线性相关 $\iff \det = 0$

### 2.3 计算公式

**$2 \times 2$**：
$$\det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$$

**$3 \times 3$**（Sarrus 规则）：
$$\det \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} = aei + bfg + cdh - ceg - bdi - afh$$

**一般 $n \times n$**（Laplace 展开，沿第 $i$ 行）：
$$\det(A) = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} \det(M_{ij})$$

其中 $M_{ij}$ 是去掉第 $i$ 行第 $j$ 列的 $(n-1) \times (n-1)$ 子矩阵（余子式）。

### 2.4 关键性质

| 性质 | 公式 |
|------|------|
| 乘积 | $\det(AB) = \det(A)\det(B)$ |
| 转置 | $\det(A^T) = \det(A)$ |
| 逆 | $\det(A^{-1}) = 1 / \det(A)$ |
| 标量乘 | $\det(cA) = c^n \det(A)$ |
| 三角矩阵 | $\det = \prod a_{ii}$ |
| 对角矩阵 | $\det = \prod d_i$ |
| 相似变换 | $\det(P^{-1}AP) = \det(A)$ |

---

## 3. 逆矩阵

> **定义 2（逆矩阵）**：方阵 $A$ 的**逆** $A^{-1}$ 满足：
>
> $$AA^{-1} = A^{-1}A = I_n$$
>
> $A$ **可逆 (invertible)** 或**非奇异 (nonsingular)** $\iff A^{-1}$ 存在。

### 3.1 可逆性的等价条件

下列条件等价（任一条成立 $\iff$ 全部成立）：

1. $A^{-1}$ 存在
2. $\det(A) \neq 0$
3. $\operatorname{rank}(A) = n$（满秩）
4. $A$ 各列线性无关
5. $A\mathbf{x} = \mathbf{0}$ 只有零解
6. $A\mathbf{x} = \mathbf{b}$ 对任意 $\mathbf{b}$ 有唯一解
7. 0 不是 $A$ 的特征值（见第 06 章）
8. $A$ 的行阶梯形（REF）有 $n$ 个主元

### 3.2 逆的计算

**2x2 公式**：
$$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \implies A^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

**伴随矩阵法**（$n \times n$）：
$$A^{-1} = \frac{1}{\det(A)} \operatorname{adj}(A)$$

其中 $\operatorname{adj}(A)$ 是**伴随矩阵**（余子式矩阵的转置）。

**Gauss-Jordan 消元法**（更实用）：对 $[A \mid I]$ 做行操作化为 $[I \mid A^{-1}]$。

### 3.3 逆的性质

- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1}A^{-1}$（顺序反转！）
- $(A^T)^{-1} = (A^{-1})^T$
- $(cA)^{-1} = \frac{1}{c}A^{-1}$（$c \neq 0$）

---

## 4. Cramer 法则

> **定理（Cramer 法则）**：若 $A$ 可逆，则 $A\mathbf{x} = \mathbf{b}$ 的解为：
>
> $$x_i = \frac{\det(A_i)}{\det(A)}$$
>
> 其中 $A_i$ 是将 $A$ 的第 $i$ 列替换为 $\mathbf{b}$ 所得的矩阵。

**实用性**：对大规模方程组计算量 $O(n!)$，远不如高斯消元 $O(n^3)$。但**理论上重要**——它显式表达了 $\mathbf{x}$ 作为 $\det$ 之比的解析形式。

---

## 5. 秩 (Rank)

> **定义 3（秩）**：矩阵 $A$ 的**秩** $\operatorname{rank}(A)$ 是 $A$ 中线性无关的列的最大个数（= 列秩 = 行秩）。

**几何意义**：$\operatorname{rank}(A)$ = 变换 $A$ 后「像空间」的维数。秩还回答了「$A\mathbf{x} = \mathbf{b}$ 的解空间有多大」。

### 5.1 秩的性质

- $\operatorname{rank}(A) \leq \min(m, n)$
- $\operatorname{rank}(AB) \leq \min(\operatorname{rank}(A), \operatorname{rank}(B))$
- $\operatorname{rank}(A) = \operatorname{rank}(A^T) = \operatorname{rank}(A^T A) = \operatorname{rank}(AA^T)$
- $\operatorname{rank}(A + B) \leq \operatorname{rank}(A) + \operatorname{rank}(B)$
- 满秩方阵 $\iff$ 可逆

### 5.2 秩-零化度定理

> **定理**：对 $m \times n$ 矩阵 $A$：
>
> $$\dim(\ker A) + \operatorname{rank}(A) = n$$
>
> 即 $\operatorname{rank}(A) = n - \dim(\ker A)$（输入维数 = 零空间维数 + 列空间维数）。

**零空间** $\ker A = \{\mathbf{x} \mid A\mathbf{x} = \mathbf{0}\}$。定理说：秩越大，零空间越小；满秩时零空间为零。

---

## 6. 迹 (Trace)

> **定义 4（迹）**：$\operatorname{tr}(A) = \sum_{i=1}^{n} a_{ii}$

**性质**：
- $\operatorname{tr}(A + B) = \operatorname{tr}(A) + \operatorname{tr}(B)$
- $\operatorname{tr}(cA) = c\operatorname{tr}(A)$
- $\operatorname{tr}(AB) = \operatorname{tr}(BA)$（循环不变性）
- $\operatorname{tr}(P^{-1}AP) = \operatorname{tr}(A)$（相似不变）
- $\operatorname{tr}(A) = \sum_{i=1}^{n} \lambda_i$（特征值之和，第 06 章）
- $\operatorname{tr}(A^T A) = \|A\|_F^2$

---

## 7. 矩阵范数

### 7.1 Frobenius 范数

$$\|A\|_F = \sqrt{\sum_{i=1}^{m}\sum_{j=1}^{n} a_{ij}^2} = \sqrt{\operatorname{tr}(A^T A)}$$

这是「把所有元素铺平成向量后的 $\ell_2$ 范数」。最易计算，但不反映矩阵作为算子的拉伸行为。

### 7.2 算子范数（诱导范数）

> **定义 5（算子范数）**：
>
> $$\|A\|_p = \sup_{\mathbf{x} \neq \mathbf{0}} \frac{\|A\mathbf{x}\|_p}{\|\mathbf{x}\|_p} = \max_{\|\mathbf{x}\|_p = 1} \|A\mathbf{x}\|_p$$
>
> 这是 $A$ 对向量施加的最大拉伸倍数。

**三种最重要的算子范数**：

| 范数 | $p$ | 计算公式 | 含义 |
|------|-----|----------|------|
| $\|A\|_1$ | 1 | $\max_j \sum_i |a_{ij}|$ | 最大列和范数 |
| $\|A\|_\infty$ | $\infty$ | $\max_i \sum_j |a_{ij}|$ | 最大行和范数 |
| $\|A\|_2$ | 2 | $\sigma_{\max}(A)$ | **谱范数**：最大奇异值 |

### 7.3 谱范数 (Spectral Norm)

$$\|A\|_2 = \sigma_{\max}(A) = \sqrt{\lambda_{\max}(A^T A)}$$

谱范数是 $A$ 对任意向量的最大拉伸倍数。在 SVD（第 09 章）中，$\sigma_{\max}$ 是最大的奇异值。

**关系**：$\|A\|_2 \leq \|A\|_F \leq \sqrt{\operatorname{rank}(A)} \cdot \|A\|_2$

### 7.4 核范数 (Nuclear Norm)

$$\|A\|_* = \sum_i \sigma_i(A)$$

即奇异值之和。在低秩矩阵恢复（矩阵补全）中用作秩的凸松弛。

---

## 8. 条件数 (Condition Number)

> **定义 6（条件数）**：可逆方阵 $A$ 的条件数（对 $\ell_2$ 范数）：
>
> $$\kappa_2(A) = \|A\|_2 \cdot \|A^{-1}\|_2 = \frac{\sigma_{\max}(A)}{\sigma_{\min}(A)}$$

**几何意义**：条件数衡量 $A$ 对向量拉伸的不均匀程度。
- $\kappa = 1$：$A$ 是正交矩阵（等距拉伸）
- $\kappa$ 大：$A$ 在某些方向极度拉伸，某些方向极度压缩（「病态」）

**为什么重要**：解 $A\mathbf{x} = \mathbf{b}$ 时，如果 $\kappa(A)$ 大，微小的 $\mathbf{b}$ 扰动会导致 $\mathbf{x}$ 巨大变化：

$$\frac{\|\Delta\mathbf{x}\|}{\|\mathbf{x}\|} \leq \kappa(A) \cdot \frac{\|\Delta\mathbf{b}\|}{\|\mathbf{b}\|}$$

**例子**：$A = \begin{bmatrix} 1 & 1 \\ 1 & 1.0001 \end{bmatrix}$。$\det(A) = 1\times 1.0001 - 1\times 1 = 0.0001$，接近奇异。条件数 $\approx 40000$——极度病态！

---

## 9. 重要定理证明

### 9.1 $\det(AB) = \det(A)\det(B)$

> **定理**：行列式的乘积性质。

**证明思路**：固定 $B$，定义 $f(A) = \det(AB) / \det(B)$。可验证 $f$ 满足行列式的三条公理（多重线性、交错性、归一化 $f(I) = 1$）。由公理的唯一性，$f(A) = \det(A)$。故 $\det(AB) = \det(A)\det(B)$。证毕

### 9.2 秩-零化度定理（思路）

考虑矩阵 $A$ 的列空间 $\operatorname{col}(A)$ 和零空间 $\ker(A)$。

取 $\ker(A)$ 的一组基 $\mathbf{v}_1, \ldots, \mathbf{v}_k$（$k = \dim\ker A$），扩充为 $\mathbb{R}^n$ 的基 $\mathbf{v}_1, \ldots, \mathbf{v}_k, \mathbf{u}_1, \ldots, \mathbf{u}_{n-k}$。

则 $A\mathbf{u}_1, \ldots, A\mathbf{u}_{n-k}$ 是 $\operatorname{col}(A)$ 的一组基。故 $\operatorname{rank}(A) = n - k = n - \dim(\ker A)$。证毕

---

## 10. 例题

### 例 1：计算行列式

求 $\det A$，其中 $A = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 3 & 1 \\ 0 & 1 & 2 \end{bmatrix}$。

<details><summary>解</summary>

沿第一行展开：
$$\det A = 2 \cdot \det\begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix} - 1 \cdot \det\begin{bmatrix} 1 & 1 \\ 0 & 2 \end{bmatrix} + 0$$

$= 2 \cdot (6 - 1) - 1 \cdot (2 - 0) = 10 - 2 = 8$

</details>

### 例 2：求逆并验证

求 $A = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}$ 的逆矩阵。

<details><summary>解</summary>

$\det A = 4 \times 6 - 7 \times 2 = 24 - 14 = 10$

$$A^{-1} = \frac{1}{10} \begin{bmatrix} 6 & -7 \\ -2 & 4 \end{bmatrix} = \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix}$$

验证：$AA^{-1} = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix} \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix} = \begin{bmatrix} 2.4 - 1.4 & -2.8 + 2.8 \\ 1.2 - 1.2 & -1.4 + 2.4 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ ✓

</details>

### 例 3：条件数

对 $A = \begin{bmatrix} 1 & 0 \\ 0 & 100 \end{bmatrix}$，求 $\kappa_2(A)$。

<details><summary>解</summary>

$A$ 是对角矩阵，特征值（= 奇异值）为 $\sigma_1 = 100$, $\sigma_2 = 1$。

$$\kappa_2(A) = \frac{\sigma_{\max}}{\sigma_{\min}} = \frac{100}{1} = 100$$

矩阵在 $x_2$ 方向拉伸比 $x_1$ 方向大 100 倍，条件数 100 意味着最多放大 100 倍误差。

</details>

---

## 11. 常见误区

| 误区 | 正确理解 |
|------|----------|
| 「$\det(A) = 0$ 意味着没解」 | 齐次方程有无穷多解；非齐次可能无解或无穷多解 |
| 「范数都一样」 | Frobenius 和谱范数不同：$\|A\|_2 \leq \|A\|_F$ |
| 「条件数大就一定坏」 | 取决于相对误差要求。$\kappa = 10^3$ 对 3 位精度致命，对 16 位精度可接受 |
| 「逆矩阵总是可以算的」 | 数值上若 $\kappa$ 很大，直接求逆可能是灾难 |
| 「$\det(A+B) = \det A + \det B$」 | 一般不成立！行列式不是线性的 |

---

## 本章核心概念速查

| 概念 | 定义 | 一句话 |
|------|------|--------|
| 行列式 | 体积缩放因子 | 一数判可逆 |
| 可逆 | $AA^{-1} = I$ | 变换可唯一逆转 |
| 秩 | 线性无关列数 | 「有效信息」维数 |
| 迹 | $\sum a_{ii}$ | 对角线之和 = 特征值之和 |
| Frobenius 范数 | $\sqrt{\sum a_{ij}^2}$ | 矩阵的「扁平长度」 |
| 谱范数 | $\sigma_{\max}$ | 矩阵的最大拉伸倍数 |
| 条件数 | $\sigma_{\max} / \sigma_{\min}$ | 「病态」度量 |
| Cramer 法则 | $x_i = \det(A_i)/\det(A)$ | 解的显式公式 |
| 秩-零化度定理 | $\dim\ker + \operatorname{rank} = n$ | 输入 = 解维数 + 像维数 |

---

← 前置: [04 — 线性方程组与消元法](../04-线性方程组与消元法/notes.md)
→ 延伸: [06 — 特征值与特征向量](../06-特征值与特征向量/notes.md)
