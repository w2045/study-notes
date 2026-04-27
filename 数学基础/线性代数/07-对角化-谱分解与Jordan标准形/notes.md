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

**证明思路**（关键步骤）：
1. **特征值实数**：设 $A\mathbf{v} = \lambda\mathbf{v}$，则 $\lambda\|\mathbf{v}\|^2 = \mathbf{v}^T A \mathbf{v} = (A\mathbf{v})^T \mathbf{v} = \overline{\lambda}\|\mathbf{v}\|^2$（利用 $A=A^T$ 和实向量 $\overline{\mathbf{v}} = \mathbf{v}$），得 $\lambda = \overline{\lambda} \in \mathbb{R}$。
2. **特征向量正交**：若 $\lambda_1 \neq \lambda_2$，则 $\lambda_1\mathbf{v}_1^T\mathbf{v}_2 = \mathbf{v}_1^T A\mathbf{v}_2 = \lambda_2\mathbf{v}_1^T\mathbf{v}_2$，故 $(\lambda_1 - \lambda_2)\mathbf{v}_1^T\mathbf{v}_2 = 0 \implies \mathbf{v}_1 \perp \mathbf{v}_2$。
3. **正交对角化**：通过对维数做归纳法。取 $A$ 的任一单位特征向量 $\mathbf{q}_1$，扩充为标准正交基，写出 $A$ 在该基下的分块矩阵，由对称性得右下块仍对称，用归纳假设即可。证毕

**几何意义**：实对称矩阵 = 在**正交**方向上独立缩放的变换。相当于先把空间旋转到特征方向（$Q^T$），在各方向缩放（$\Lambda$），再旋转回来（$Q$）。

### 2.2 一般方阵的 Schur 分解

> **定理 2（Schur 分解）**：任意方阵 $A \in \mathbb{C}^{n \times n}$，存在酉矩阵 $U$ 和上三角矩阵 $T$ 使得：
>
> $$A = U T U^*$$
>
> $T$ 的对角线元素是 $A$ 的特征值。

Schur 分解是谱定理的推广——任意方阵都可以酉三角化（但不一定能对角化）。

**正规矩阵与酉对角化**：Schur 分解中 $T$ 何时是对角阵？答案是：当且仅当 $A$ 是**正规矩阵**（$A^*A = AA^*$）。

> **定理 3（正规矩阵的谱定理）**：$A$ 可酉对角化（$A = U\Lambda U^*$）$\iff$ $A$ 是正规矩阵。

正规矩阵族包括：
| 子族 | 条件 | 特征值位置 |
|------|------|-----------|
| Hermitian | $A^* = A$ | 实数轴 |
| 斜 Hermitian | $A^* = -A$ | 虚数轴 |
| 酉矩阵 | $U^* = U^{-1}$ | 单位圆 |

**与实矩阵的对应**：实正规 + 实特征值 → 实正交对角化（即实对称矩阵的谱定理）。但如果一个实正规矩阵有复特征值（如旋转矩阵），它不能实对角化——但可以酉对角化。

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

当几何重数 < 代数重数时，矩阵不可对角化。Jordan 标准形是「最接近对角化」的形式——它把矩阵变成对角线上是特征值、上对角线上可能有 1 的块对角矩阵。

> **定义 2（Jordan 块）**：$k \times k$ Jordan 块：
>
> $$J_k(\lambda) = \begin{bmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda & 1 & \cdots & 0 \\ 0 & 0 & \lambda & \ddots & \vdots \\ \vdots & \vdots & & \ddots & 1 \\ 0 & 0 & \cdots & 0 & \lambda \end{bmatrix}$$

> **定义 3（Jordan 标准形）**：任意方阵 $A$（在代数闭域上）相似于分块对角矩阵：
>
> $$A = P \, J \, P^{-1}, \quad J = \begin{bmatrix} J_{k_1}(\lambda_1) & & \\ & \ddots & \\ & & J_{k_m}(\lambda_m) \end{bmatrix}$$

### 5.2 Jordan 链

对于大小为 $k$ 的 Jordan 块 $J_k(\lambda)$，存在一条**Jordan 链**（或广义特征向量链）：

$$(A - \lambda I)\mathbf{v}_1 = \mathbf{0}$$
$$(A - \lambda I)\mathbf{v}_2 = \mathbf{v}_1$$
$$\vdots$$
$$(A - \lambda I)\mathbf{v}_k = \mathbf{v}_{k-1}$$

$\mathbf{v}_1$ 是普通特征向量，$\mathbf{v}_2, \ldots, \mathbf{v}_k$ 是**广义特征向量**——它们满足 $(A - \lambda I)^k \mathbf{v}_k = \mathbf{0}$ 但 $(A - \lambda I)^{k-1} \mathbf{v}_k \neq \mathbf{0}$。

### 5.3 系统性算法：从任意矩阵求 Jordan 型

之前的所有例子都是「矩阵本身已经是 Jordan 型」——这不是算法。下面是对**任意**矩阵的系统性步骤。

**算法输入**：方阵 $A \in \mathbb{R}^{n \times n}$。

**步骤 1：求特征值与代数重数**
计算特征多项式 $p_A(\lambda) = \det(A - \lambda I)$，因式分解得各特征值 $\lambda_i$ 和代数重数 $a(\lambda_i)$。

**步骤 2：对每个特征值，计算几何重数**
几何重数 $g(\lambda) = n - \operatorname{rank}(A - \lambda I)$。这也是 **Jordan 块的个数**。

**步骤 3：通过 $\operatorname{rank}(A - \lambda I)^k$ 确定块大小（核心步骤！）**
计算数列：
$$r_k = \operatorname{rank}((A - \lambda I)^k), \quad k = 1, 2, 3, \ldots$$
直到 $r_k$ 稳定在 $n - a(\lambda)$（代数重数处停止）。

定义 $r_0 = n$。差分：
$$d_k = r_{k-1} - r_k \quad (\text{大小为至少 } k \text{ 的 Jordan 块的数量})$$
则大小为**恰好** $k$ 的 Jordan 块数量 = $d_k - d_{k+1}$。

**直觉**：每次乘 $(A - \lambda I)$ 会让秩下降，直到触及 $(A - \lambda I)$ 的零空间的最大维数。秩下降的速度直接反映 Jordan 块的尺寸分布。

**步骤 4：构造 Jordan 链（广义特征向量）**
对每个大小为 $k$ 的块：
1. 找 $\mathbf{v}_k \in \ker((A - \lambda I)^k)$ 但 $\mathbf{v}_k \notin \ker((A - \lambda I)^{k-1})$
2. 递推构造：$\mathbf{v}_{k-1} = (A - \lambda I)\mathbf{v}_k$, $\mathbf{v}_{k-2} = (A - \lambda I)\mathbf{v}_{k-1}$, ...
3. 将链 $\mathbf{v}_1, \ldots, \mathbf{v}_k$ 按顺序放入 $P$ 的列

**步骤 5**：组装 $P$ 和 $J$，验证 $P^{-1}AP = J$。

### 5.4 完整示例：一个非平凡的 $3 \times 3$ 矩阵

$$A = \begin{bmatrix} 5 & 4 & 2 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{bmatrix}$$

注意：$A$ 是否已经在 Jordan 型？不——$\lambda=3$ 的位置不是标准 Jordan 块结构。我们需要求出它的 Jordan 型。

**步骤 1**：$A$ 是上三角矩阵，特征值在对角线上：$\lambda_1 = 5$（$a = 1$），$\lambda_2 = 3$（$a = 2$）。

**步骤 2（对 $\lambda = 5$）**：$a(5) = 1$ → 必有一个 $1 \times 1$ Jordan 块。$g(5) = 1$。完成。

**步骤 3（对 $\lambda = 3$）**：
$$A - 3I = \begin{bmatrix} 2 & 4 & 2 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$$

消元：$R_1 - 2R_2$ 得 $\begin{bmatrix} 2 & 4 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$。$r_1 = \operatorname{rank}(A-3I) = 2$。故 $g(3) = n - r_1 = 3 - 2 = 1$ → 只有 **1 个** Jordan 块。

现在计算 $(A - 3I)^2$：
$$(A - 3I)^2 = \begin{bmatrix} 2 & 4 & 2 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 2 & 4 & 2 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 4 & 8 & 8 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

$r_2 = \operatorname{rank}((A-3I)^2) = 1$（行成比例）。$(A-3I)^3 = 0$ 矩阵（因为 $n - a(3) = 3 - 2 = 1$，$r_2$ 已稳定在 1 → 停止）。

**确定块大小**：
- $d_1 = r_0 - r_1 = 3 - 2 = 1$（有 1 个大小 ≥1 的块）
- $d_2 = r_1 - r_2 = 2 - 1 = 1$（有 1 个大小 ≥2 的块）
- $d_3 = r_2 - r_3 = 1 - 1 = 0$（没有大小 ≥3 的块）

块大小分布：$d_1 - d_2 = 0$（无 $1 \times 1$ 块），$d_2 - d_3 = 1$（有一个 $2 \times 2$ 块）。
→ 对于 $\lambda = 3$：一个 $2 \times 2$ Jordan 块。

**结论**：
$$J = \begin{bmatrix} 5 & 0 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{bmatrix}$$

**步骤 4：构造 Jordan 链并求 $P$**

对 $\lambda = 5$：普通特征向量。$(A - 5I)\mathbf{v} = \mathbf{0}$：
$$\begin{bmatrix} 0 & 4 & 2 \\ 0 & -2 & 1 \\ 0 & 0 & -2 \end{bmatrix} \mathbf{v} = \mathbf{0} \implies \mathbf{v} = [1, 0, 0]^T$$
故 $\mathbf{p}_1 = [1, 0, 0]^T$。

对 $\lambda = 3$（$2 \times 2$ 块，需要 Jordan 链）：
- $\mathbf{v}_1$（普通特征向量）：$(A - 3I)\mathbf{v}_1 = \mathbf{0}$。上面 $(A-3I)$ 的 RREF 为 $\begin{bmatrix}1&2&0\\0&0&1\\0&0&0\end{bmatrix}$。解：$x_3 = 0$，$x_1 + 2x_2 = 0$。取 $\mathbf{v}_1 = [2, -1, 0]^T$。$\mathbf{p}_2 = \mathbf{v}_1$。
- $\mathbf{v}_2$（广义特征向量）：解 $(A - 3I)\mathbf{v}_2 = \mathbf{v}_1$：
  $$\begin{bmatrix} 2 & 4 & 2 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 2 \\ -1 \\ 0 \end{bmatrix}$$
  第 2 行：$z = -1$。第 1 行：$2x + 4y + 2(-1) = 2 \implies 2x + 4y = 4 \implies x + 2y = 2$。取 $y = 0, x = 2$。得 $\mathbf{v}_2 = [2, 0, -1]^T$。$\mathbf{p}_3 = \mathbf{v}_2$。

组装：$P = [\mathbf{p}_1 \mid \mathbf{p}_2 \mid \mathbf{p}_3] = \begin{bmatrix} 1 & 2 & 2 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{bmatrix}$。

验证：
$$P^{-1} = \begin{bmatrix} 1 & 2 & 2 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{bmatrix}, \quad P^{-1}AP = \begin{bmatrix} 5 & 0 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{bmatrix} = J \quad \checkmark$$

### 5.5 实 Jordan 型（复特征值时的实数形式）

当矩阵有复共轭特征值对 $\lambda = a \pm bi$ 时，标准 Jordan 型包含复数。但在工程和物理中，我们往往希望在实数域内工作。

对共轭对 $a \pm bi$，用一个 $2 \times 2$ **实块**代替对角复数：
$$C(a, b) = \begin{bmatrix} a & -b \\ b & a \end{bmatrix}$$

实 Jordan 型中，每个 $2 \times 2$ 块 $C(a,b)$ 代替一对复共轭特征值，上对角 $(2 \times 2)$ 块为 $I_2$。

**示例**：$A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$（旋转 $90^\circ$）。特征值 $\lambda = \pm i$。其**复** Jordan 型为 $\begin{bmatrix} i & 0 \\ 0 & -i \end{bmatrix}$，**实** Jordan 型为 $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = C(0, 1)$——它自身就是一个实 Jordan 块。

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

### 例 1：Jordan 标准形（3×3）

求 $A = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}$ 的 Jordan 标准形。

<details><summary>解</summary>

特征值 $\lambda = 2$（代数重数 3）。$(A - 2I) = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$，秩 = 2，故 $\dim\ker(A-2I) = 3-2 = 1$——只有一个特征向量（几何重数 1）。

Jordan 链：$\mathbf{v}_1 = [1, 0, 0]^T$ 满足 $(A-2I)\mathbf{v}_1 = \mathbf{0}$。
$(A-2I)\mathbf{v}_2 = \mathbf{v}_1 \implies \mathbf{v}_2 = [0, 1, 0]^T$
$(A-2I)\mathbf{v}_3 = \mathbf{v}_2 \implies \mathbf{v}_3 = [0, 0, 1]^T$

因为几何重数 = 1，只有一个 Jordan 块：$J_3(2) = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}$。事实上 $A$ 自身已为 Jordan 块。

若 $\dim\ker(A-2I) = 2$（如 $A = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{bmatrix}$），则有两个 Jordan 块：$J_2(2) \oplus J_1(2)$。块的个数 = 几何重数，每块大小由 Jordan 链长度决定。

</details>

### 例 2：谱分解

对 $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$，写出谱分解 $A = \lambda_1 P_1 + \lambda_2 P_2$。

<details><summary>解</summary>

特征值 $\lambda_1 = 1$, $\lambda_2 = 3$。标准正交特征向量：

$\mathbf{q}_1 = \frac{1}{\sqrt{2}}[1, -1]^T$, $\mathbf{q}_2 = \frac{1}{\sqrt{2}}[1, 1]^T$

$$P_1 = \mathbf{q}_1 \mathbf{q}_1^T = \frac{1}{2}\begin{bmatrix}1\\-1\end{bmatrix}\begin{bmatrix}1 & -1\end{bmatrix} = \frac{1}{2}\begin{bmatrix}1 & -1\\-1 & 1\end{bmatrix}$$

$$P_2 = \mathbf{q}_2 \mathbf{q}_2^T = \frac{1}{2}\begin{bmatrix}1\\1\end{bmatrix}\begin{bmatrix}1 & 1\end{bmatrix} = \frac{1}{2}\begin{bmatrix}1 & 1\\1 & 1\end{bmatrix}$$

验证：$A = 1 \cdot \frac{1}{2}\begin{bmatrix}1&-1\\-1&1\end{bmatrix} + 3 \cdot \frac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix} = \begin{bmatrix}2&1\\1&2\end{bmatrix}$ ✓

$P_1 + P_2 = I$, $P_1 P_2 = 0$ ✓

</details>

### 例 3：Jordan 型（2×2 幂零）

求 $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ 的 Jordan 标准形。

<details><summary>解</summary>

特征值 $\lambda = 0$（二重）。$(A - 0I)\mathbf{v} = \begin{bmatrix}0&1\\0&0\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_1 = [1, 0]^T$。只有一个特征方向。

广义特征向量：$A\mathbf{v}_2 = \mathbf{v}_1 \implies \begin{bmatrix}0&1\\0&0\end{bmatrix}\mathbf{v}_2 = \begin{bmatrix}1\\0\end{bmatrix} \implies \mathbf{v}_2 = [0, 1]^T$。

Jordan 块 $J_2(0) = \begin{bmatrix}0&1\\0&0\end{bmatrix}$，$A$ 自身已在 Jordan 标准形。

</details>

---

## 9. 常见误区

| 误区 | 正确理解 |
|------|----------|
| 「实对称 = 唯一可对角化的矩阵」 | 大量非对称矩阵也可对角化（充要条件：几何重数 = 代数重数）。实对称的特殊之处在于**正交**对角化 |
| 「可对角化 = 可正交对角化」 | 正交对角化需要更强的条件（正规矩阵 + 实特征值） |
| 「Jordan 标准形只在复数域存在」 | 若所有特征值都是实数（如实矩阵的实特征值），Jordan 型完全在实数域内 |
| 「正规矩阵就是对称矩阵」 | 正规矩阵 $(A^*A = AA^*)$ 范围大得多——酉矩阵、斜 Hermitian 矩阵都是正规的 |
| 「谱分解就是特征分解」 | 谱分解是特征分解的投影形式 $A = \sum \lambda_i P_i$，强调投影算子的角色 |
| 「广义特征向量是随便选的」 | 必须满足 Jordan 链条件 $(A-\lambda I)\mathbf{v}_{k} = \mathbf{v}_{k-1}$，构成特定结构 |

---

## 本章核心概念速查

| 概念 | 定义 | 一句话 |
|------|------|--------|
| 谱定理 | $A = Q\Lambda Q^T$ | 实对称 → 正交对角化 |
| Hermitian 对角化 | $A = U\Lambda U^*$ | Hermitian → 酉对角化（特征值全实） |
| Schur 分解 | $A = U T U^*$ | 任意方阵 → 酉三角化 |
| 正规矩阵 | $A^*A = AA^*$ | 可酉对角化的充要条件 |
| 谱分解 | $A = \sum \lambda_i P_i$ | 矩阵 = 加权投影之和 |
| Rayleigh 商 | $\mathbf{x}^T A\mathbf{x} / \mathbf{x}^T\mathbf{x}$ | 从向量估计特征值 |
| Jordan 块 | 对角 $\lambda$ + 上对角 1 | 不可对角化的「基本单元」 |
| Jordan 标准形 | $A = P J P^{-1}$ | 最接近对角化的形式 |
| 广义特征向量 | $(A - \lambda I)^k\mathbf{v} = \mathbf{0}$ | Jordan 链的元素 |
| 酉矩阵 | $U^* U = I$ | 复正交矩阵；保 Hermitian 内积 |

---

← 前置: [06 — 特征值与特征向量](../06-特征值与特征向量/notes.md)
→ 延伸: [08 — 正定矩阵、投影与 QR 分解](../08-正定矩阵-投影与QR分解/notes.md)
