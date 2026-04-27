# 线性代数 · 第七章 · 对角化、谱分解与 Jordan 标准形

← 前置: [06 — 特征值与特征向量](../06-特征值与特征向量/notes.md)
→ 延伸: [08 — 正定矩阵、投影与 QR 分解](../08-正定矩阵-投影与QR分解/notes.md)

---

## 1. 直觉引入：当对角化失败时

第六章告诉我们，$A = P\Lambda P^{-1}$ 是「梦寐以求」的分解——矩阵变成了各方向独立缩放。但并非所有矩阵都可对角化。

**不可对角化的例子**：$J = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$。特征值 $\lambda = 1$（二重），但只有一个线性无关的特征向量 $[1, 0]^T$。

问题：对于这种「顽固」矩阵，我们能得到**最接近对角化**的形式是什么？

> **核心洞察**：Jordan 标准形是对角化的「极限推广」——它把矩阵变成对角块 + 上三角偏移。谱定理则告诉我们：对「好矩阵」（如对称矩阵），对角化总成立且是**正交**对角化。

---

## 2. 谱定理 (Spectral Theorem)

### 2.1 实对称矩阵的谱定理

> **定理 1（谱定理，实对称版）**：若 $A = A^T \in \mathbb{R}^{n \times n}$，则存在正交矩阵 $Q$ 和对角矩阵 $\Lambda$ 使得：
>
> $$A = Q\Lambda Q^T = \sum_{i=1}^{n} \lambda_i \mathbf{q}_i \mathbf{q}_i^T$$
>
> 其中 $\lambda_i \in \mathbb{R}$ 是 $A$ 的特征值，$\mathbf{q}_i$ 是相应的标准正交特征向量（$Q$ 的第 $i$ 列）。

**这意味着**：
1. 所有特征值都是实数
2. 不同特征值的特征向量自动正交
3. $A$ 可被**正交**对角化（$Q^{-1} = Q^T$，更简洁！）

**几何意义**：实对称矩阵 = 在**正交**方向上独立缩放的变换。相当于先把空间旋转到特征方向（$Q^T$），在各方向缩放（$\Lambda$），再旋转回来（$Q$）。

### 2.2 一般方阵的 Schur 分解

> **定理 2（Schur 分解）**：任意方阵 $A \in \mathbb{C}^{n \times n}$，存在酉矩阵 $U$ 和上三角矩阵 $T$ 使得：
>
> $$A = U T U^*$$
>
> $T$ 的对角线元素是 $A$ 的特征值。

Schur 分解是谱定理的推广——任意方阵都可以酉三角化（但不一定能对角化）。

---

## 3. 谱分解 (Spectral Decomposition)

### 3.1 谱投影

对可对角化矩阵 $A = P\Lambda P^{-1}$，记 $\mathbf{p}_i$ 是 $P$ 的第 $i$ 列，$\mathbf{q}_i^T$ 是 $P^{-1}$ 的第 $i$ 行。则：

$$A = \sum_{i=1}^{n} \lambda_i \mathbf{p}_i \mathbf{q}_i^T$$

定义**谱投影矩阵** $P_i = \mathbf{p}_i \mathbf{q}_i^T$。则：

$$A = \sum_{i=1}^{n} \lambda_i P_i$$

**性质**：
- $P_i P_j = 0$（$i \neq j$）（幂等/正交投影）
- $P_i^2 = P_i$（幂等）
- $\sum P_i = I$

**几何直觉**：谱分解将 $A$ 拆成 $n$ 个「一维投影」的加权和。$P_i$ 是把任意向量投影到第 $i$ 个特征方向的算子，$\lambda_i$ 是在该方向的缩放因子。

### 3.2 谱映射

对于多项式函数 $f$，若 $A = P\Lambda P^{-1}$，则：

$$f(A) = P f(\Lambda) P^{-1} = P \begin{bmatrix} f(\lambda_1) & & \\ & \ddots & \\ & & f(\lambda_n) \end{bmatrix} P^{-1}$$

**应用**：矩阵指数 $e^A$（解微分方程 $\dot{\mathbf{x}} = A\mathbf{x}$），矩阵平方根 $\sqrt{A}$ 等。

---

## 4. Rayleigh 商

> **定义 1（Rayleigh 商）**：对 Hermitian 矩阵 $A$（$A^* = A$）和非零向量 $\mathbf{x}$：
>
> $$R(A, \mathbf{x}) = \frac{\mathbf{x}^T A \mathbf{x}}{\mathbf{x}^T \mathbf{x}}$$

> **定理 3（Rayleigh-Ritz）**：
>
> $$\lambda_{\min}(A) \leq R(A, \mathbf{x}) \leq \lambda_{\max}(A)$$
>
> 等号成立当 $\mathbf{x}$ 是对应极值的特征向量。

**实用价值**：
- 无需计算全部特征值即可估计特征值范围
- 第 06 章的幂迭代法就是取 $R(A, \mathbf{v}_k)$ 逼近主特征值

**Courant-Fischer 定理（推广）**：

$$\lambda_k = \min_{\dim V = k} \max_{\mathbf{x} \in V, \mathbf{x} \neq \mathbf{0}} R(A, \mathbf{x}) = \max_{\dim V = n-k+1} \min_{\mathbf{x} \in V, \mathbf{x} \neq \mathbf{0}} R(A, \mathbf{x})$$

---

## 5. Jordan 标准形

### 5.1 动机

当几何重数 < 代数重数时，矩阵不可对角化。Jordan 标准形是「最接近对角化」的形式。

> **定义 2（Jordan 块）**：$k \times k$ Jordan 块：
>
> $$J_k(\lambda) = \begin{bmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda & 1 & \cdots & 0 \\ 0 & 0 & \lambda & \ddots & \vdots \\ \vdots & \vdots & & \ddots & 1 \\ 0 & 0 & \cdots & 0 & \lambda \end{bmatrix}$$

> **定义 3（Jordan 标准形）**：任意方阵 $A$（在代数闭域上）相似于一个分块对角矩阵，每个块是 Jordan 块：
>
> $$A = P \, J \, P^{-1}, \quad J = \begin{bmatrix} J_{k_1}(\lambda_1) & & \\ & \ddots & \\ & & J_{k_m}(\lambda_m) \end{bmatrix}$$

### 5.2 Jordan 链

对于 Jordan 块 $J_k(\lambda)$，除了普通的特征向量（满足 $(A - \lambda I)\mathbf{v} = \mathbf{0}$），还有**广义特征向量**：

$$(A - \lambda I)\mathbf{v}_1 = \mathbf{0}$$
$$(A - \lambda I)\mathbf{v}_2 = \mathbf{v}_1$$
$$\vdots$$
$$(A - \lambda I)\mathbf{v}_k = \mathbf{v}_{k-1}$$

这 $k$ 个向量构成一个**Jordan 链**。

### 5.3 例子

$A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$。

特征值 $\lambda = 1$（二重代数），但只有一个特征向量 $\mathbf{v}_1 = [1, 0]^T$。
广义特征向量：$(A - I)\mathbf{v}_2 = \mathbf{v}_1 \implies \begin{bmatrix}0&1\\0&0\end{bmatrix}\mathbf{v}_2 = \begin{bmatrix}1\\0\end{bmatrix} \implies \mathbf{v}_2 = [0, 1]^T$。

Jordan 型：$A = \begin{bmatrix}1&0\\0&1\end{bmatrix} \begin{bmatrix}1&1\\0&1\end{bmatrix} \begin{bmatrix}1&0\\0&1\end{bmatrix}^{-1}$ = 本身已为 Jordan 块。

---

## 6. Jordan 型的威力：矩阵函数

对于 Jordan 块 $J_k(\lambda)$，函数 $f(J)$ 可通过以下公式计算：

$$f(J_k(\lambda)) = \begin{bmatrix} f(\lambda) & f'(\lambda) & \frac{f''(\lambda)}{2!} & \cdots & \frac{f^{(k-1)}(\lambda)}{(k-1)!} \\ 0 & f(\lambda) & f'(\lambda) & \cdots & \frac{f^{(k-2)}(\lambda)}{(k-2)!} \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & \cdots & f(\lambda) & f'(\lambda) \\ 0 & 0 & \cdots & 0 & f(\lambda) \end{bmatrix}$$

**特别地**：
$$e^{J_k(\lambda)t} = e^{\lambda t} \begin{bmatrix} 1 & t & \frac{t^2}{2} & \cdots \\ 0 & 1 & t & \cdots \\ 0 & 0 & 1 & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{bmatrix}$$

这直接给出微分方程 $\dot{\mathbf{x}} = A\mathbf{x}$ 的通解。

---

## 7. 对角化的充要条件总结

| 条件 | 结论 |
|------|------|
| $A$ 有 $n$ 个互不相同的特征值 | 可对角化（充分不必要） |
| 每个特征值的几何重数 = 代数重数 | 可对角化（充要） |
| $A = A^T$（实对称） | 可**正交**对角化 |
| $A^*A = AA^*$（正规矩阵） | 可**酉**对角化 |
| 极小多项式无重根 | 可对角化 |

---

## 8. 例题

### 例 1：谱分解

对 $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$，写出谱分解 $A = \lambda_1 P_1 + \lambda_2 P_2$。

<details><summary>解</summary>

特征值 $\lambda_1 = 1$, $\lambda_2 = 3$。标准正交特征向量：

$\mathbf{q}_1 = \frac{1}{\sqrt{2}}[1, -1]^T$, $\mathbf{q}_2 = \frac{1}{\sqrt{2}}[1, 1]^T$

$$P_1 = \mathbf{q}_1 \mathbf{q}_1^T = \frac{1}{2}\begin{bmatrix}1\\-1\end{bmatrix}\begin{bmatrix}1 & -1\end{bmatrix} = \frac{1}{2}\begin{bmatrix}1 & -1\\-1 & 1\end{bmatrix}$$

$$P_2 = \mathbf{q}_2 \mathbf{q}_2^T = \frac{1}{2}\begin{bmatrix}1\\1\end{bmatrix}\begin{bmatrix}1 & 1\end{bmatrix} = \frac{1}{2}\begin{bmatrix}1 & 1\\1 & 1\end{bmatrix}$$

验证：$A = 1 \cdot \frac{1}{2}\begin{bmatrix}1&-1\\-1&1\end{bmatrix} + 3 \cdot \frac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix} = \begin{bmatrix}2&1\\1&2\end{bmatrix}$ ✓

$P_1 + P_2 = I$, $P_1 P_2 = 0$ ✓

</details>

### 例 2：Jordan 型

求 $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ 的 Jordan 标准形。

<details><summary>解</summary>

特征值 $\lambda = 0$（二重）。$(A - 0I)\mathbf{v} = \begin{bmatrix}0&1\\0&0\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_1 = [1, 0]^T$。只有一个特征方向。

广义特征向量：$A\mathbf{v}_2 = \mathbf{v}_1 \implies \begin{bmatrix}0&1\\0&0\end{bmatrix}\mathbf{v}_2 = \begin{bmatrix}1\\0\end{bmatrix} \implies \mathbf{v}_2 = [0, 1]^T$。

Jordan 块 $J_2(0) = \begin{bmatrix}0&1\\0&0\end{bmatrix}$，$A$ 自身已在 Jordan 标准形。

</details>

---

## 本章核心概念速查

| 概念 | 定义 | 一句话 |
|------|------|--------|
| 谱定理 | $A = Q\Lambda Q^T$ | 实对称矩阵的正交对角化 |
| Schur 分解 | $A = U T U^*$ | 任意方阵的酉三角化 |
| 谱分解 | $A = \sum \lambda_i P_i$ | 矩阵 = 加权投影之和 |
| Rayleigh 商 | $\mathbf{x}^T A\mathbf{x} / \mathbf{x}^T\mathbf{x}$ | 从向量估计特征值 |
| Jordan 块 | 对角 $\lambda$ + 上对角 1 | 不可对角化的「基本单元」 |
| Jordan 标准形 | $A = P J P^{-1}$ | 最接近对角化的形式 |
| 广义特征向量 | $(A - \lambda I)^k\mathbf{v} = \mathbf{0}$ | Jordan 链的元素 |
| 正规矩阵 | $A^*A = AA^*$ | 可酉对角化的矩阵族 |

---

← 前置: [06 — 特征值与特征向量](../06-特征值与特征向量/notes.md)
→ 延伸: [08 — 正定矩阵、投影与 QR 分解](../08-正定矩阵-投影与QR分解/notes.md)
