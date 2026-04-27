# 线性代数 · 第六章 · 特征值与特征向量

← 前置: [05 — 行列式、逆、秩与矩阵范数](../05-行列式-逆-秩与矩阵范数/notes.md)
→ 延伸: [07 — 对角化、谱分解与 Jordan 标准形](../07-对角化-谱分解与Jordan标准形/notes.md)

---

## 1. 直觉引入：找到「不变的方向」

前面我们把矩阵看作线性变换。一个问题自然浮现：**是否存在某些特殊方向，变换后方向不变，只是被缩放？**

- 旋转矩阵 $R_{90^\circ} = \begin{bmatrix}0&-1\\1&0\end{bmatrix}$：所有向量都转了 $90^\circ$——**没有**方向保持不变。
- 拉伸矩阵 $D = \begin{bmatrix}2&0\\0&3\end{bmatrix}$：$x$ 轴上的向量方向不变（缩放 2 倍），$y$ 轴上的方向也不变（缩放 3 倍）。
- 剪切矩阵 $S = \begin{bmatrix}1&1\\0&1\end{bmatrix}$：$x$ 轴上的向量 $[1,0]^T$ 方向不变，但 $[0,1]^T$ 被「推」成了 $[1,1]^T$。

> **核心洞察**：特征向量 = 变换后方向不变的特殊方向。特征值 = 在这个方向上的缩放倍数。一个 $n \times n$ 矩阵最多有 $n$ 个独立的特征方向。

---

## 2. 形式化定义

> **定义 1（特征值与特征向量）**：对方阵 $A \in \mathbb{R}^{n \times n}$，若存在非零向量 $\mathbf{v} \neq \mathbf{0}$ 和标量 $\lambda \in \mathbb{C}$ 满足：
>
> $$A\mathbf{v} = \lambda \mathbf{v}$$
>
> 则 $\lambda$ 是 $A$ 的一个**特征值 (eigenvalue)**，$\mathbf{v}$ 是相应的**特征向量 (eigenvector)**。

**改写**：$(A - \lambda I)\mathbf{v} = \mathbf{0}$。$\mathbf{v} \neq \mathbf{0}$ 意味着 $A - \lambda I$ 有非平凡零空间，即 $A - \lambda I$ 奇异。

> **定义 2（特征多项式）**：
>
> $$p_A(\lambda) = \det(A - \lambda I)$$
>
> $p_A(\lambda) = 0$ 的所有根（包括复根）就是 $A$ 的全部特征值。

$p_A(\lambda)$ 是 $\lambda$ 的 $n$ 次多项式，$n$ 个根（计重数）。

### 2.1 小的例子

$A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$。

$$p_A(\lambda) = \det\begin{bmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3)$$

特征值：$\lambda_1 = 1$, $\lambda_2 = 3$。

- $\lambda_1 = 1$：$(A - I)\mathbf{v} = \begin{bmatrix}1&1\\1&1\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_1 = [1, -1]^T$
- $\lambda_2 = 3$：$(A - 3I)\mathbf{v} = \begin{bmatrix}-1&1\\1&-1\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_2 = [1, 1]^T$

**几何意义**：$A$ 在 $[1,-1]^T$ 方向保持长度不变（特征值 1），在 $[1,1]^T$ 方向拉伸 3 倍。

---

## 3. 特征多项式与重要关系

> **定理（Vieta 关系）**：对特征多项式 $p_A(\lambda) = \lambda^n - c_1\lambda^{n-1} + \cdots + (-1)^n c_n$：
>
> $$\operatorname{tr}(A) = \sum_{i=1}^{n} \lambda_i, \quad \det(A) = \prod_{i=1}^{n} \lambda_i$$

**这意味着**：
- 迹 = 特征值之和
- 行列式 = 特征值之积
- $\det A = 0 \iff 0$ 是特征值

---

## 4. 特征空间与代数/几何重数

### 4.1 动机：一个数 vs 一个维数

特征值 $\lambda = 3$ 在特征多项式中出现了 2 次。真正的问题是：能找出**几个线性无关的特征向量**属于 $\lambda = 3$？答案可能是 2 个（矩阵可对角化），也可能只有 1 个（矩阵有缺陷！）。

这两个数字——特征根的重数 vs 特征空间的维数——是区分「好矩阵」和「坏矩阵」的关键。

### 4.2 定义

> **定义 3（特征空间）**：特征值 $\lambda$ 的**特征空间** $E_\lambda = \ker(A - \lambda I) = \operatorname{Null}(A - \lambda I)$。即所有满足 $A\mathbf{v} = \lambda \mathbf{v}$ 的向量（加上零向量）构成的子空间。

> **定义 4（两种重数）**：
> - **代数重数 (algebraic multiplicity)** $a(\lambda)$：$\lambda$ 作为特征多项式根的重数。例如 $p(\lambda) = (\lambda-3)^2(\lambda-1)$ 中 $a(3) = 2$, $a(1) = 1$。
> - **几何重数 (geometric multiplicity)** $g(\lambda)$：特征空间 $E_\lambda$ 的维数。即属于 $\lambda$ 的线性无关特征向量的最大个数。

**通用关系**：$1 \leq g(\lambda) \leq a(\lambda)$。几何重数永远不超过代数重数，也永远至少为 1（因为特征方程保证至少存在一个非零解）。

### 4.3 如何计算

**代数重数**：对 $p_A(\lambda)$ 做因式分解，直接读出各因式的指数。
**几何重数**：对每个 $\lambda$，解 $(A - \lambda I)\mathbf{x} = \mathbf{0}$。关键公式：
$$g(\lambda) = n - \operatorname{rank}(A - \lambda I)$$
这是因为零空间的维数 = $n$ - 矩阵的秩（秩-零化度定理，Ch05 §5.2）。操作上就是将 $A - \lambda I$ 化为 RREF，数自由变量的个数。

### 4.4 并排对比：相同代数重数，不同几何重数

**示例 1：缺陷矩阵** — $A = \begin{bmatrix} 3 & 1 \\ 0 & 3 \end{bmatrix}$。

$p(\lambda) = \det\begin{bmatrix}3-\lambda&1\\0&3-\lambda\end{bmatrix} = (3-\lambda)^2$ → $a(3) = 2$。

$(A - 3I) = \begin{bmatrix}0&1\\0&0\end{bmatrix}$，秩 = 1，故 $g(3) = n - \operatorname{rank}(A-3I) = 2 - 1 = 1$。

特征空间仅由 $[c, 0]^T$ 张成。$g(3) = 1 < a(3) = 2$ → **不可对角化**（有缺陷，需要 Jordan 型）。

**示例 2：可对角化矩阵** — $A = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}$。

$p(\lambda) = (3-\lambda)^2$ → $a(3) = 2$（同示例 1）。

$(A - 3I) = \begin{bmatrix}0&0\\0&0\end{bmatrix}$（零矩阵），秩 = 0，故 $g(3) = 2 - 0 = 2$。

特征空间是整个 $\mathbb{R}^2$。$g(3) = a(3) = 2$ → **可对角化**（已经是对角矩阵）。

**示例 3：$3 \times 3$ Jordan 块** — $A = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}$。

$p(\lambda) = (2-\lambda)^3$ → $a(2) = 3$。

$(A - 2I) = \begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}$，rank = 2（两个非零行），$g(2) = 3 - 2 = 1$。

只有一个独立特征向量 $[1,0,0]^T$，但需要 3 个 → **严重缺陷**，需要一个 $3 \times 3$ 的 Jordan 块。

| | 示例 1 (缺陷) | 示例 2 (好) | 示例 3 (Jordan) |
|---|---|---|---|
| 代数重数 $a$ | 2 | 2 | 3 |
| $\operatorname{rank}(A - \lambda I)$ | 1 | 0 | 2 |
| 几何重数 $g$ | 1 | 2 | 1 |
| 结论 | $g < a$ 不可对角化 | $g = a$ 可对角化 | $g < a$ 需 Jordan 块 |

### 4.5 缺陷性与 Jordan 型预告

当 $g(\lambda) < a(\lambda)$ 时，矩阵**有缺陷 (defective)**——缺少足够的特征向量来构成 $\mathbb{R}^n$ 的基。此时需要**广义特征向量 (generalized eigenvector)**：满足 $(A - \lambda I)^k \mathbf{v} = \mathbf{0}$（$k \geq 2$）的向量，以填补缺失的维数。这些广义特征向量构成 **Jordan 链**，详细见 Ch07 §5。

### 4.6 应用：$e^{At}$ 与微分方程

对于常系数线性微分方程 $\dot{\mathbf{x}} = A\mathbf{x}$，解为 $\mathbf{x}(t) = e^{At}\mathbf{x}(0)$。

- **若 $A$ 可对角化**（$g = a$ 对所有特征值）：$e^{At} = P \operatorname{diag}(e^{\lambda_1 t}, \ldots, e^{\lambda_n t}) P^{-1}$。简单明了。
- **若 $A$ 有缺陷**（$g < a$）：$e^{At}$ 包含形如 $t^k e^{\lambda t}$ 的项——纯指数 × 多项式。这使得解可能出现**瞬态增长**（$t e^{\lambda t}$ 型），即使 $\lambda < 0$。

这在控制系统和结构力学中至关重要：有缺陷的系统可能表现出比特征值预期更「慢」或更「不稳定」的行为。

### 4.7 复特征值处理

实矩阵可能有复共轭特征值对（如 $\lambda = a \pm bi$）。此时：
- 特征向量也是复共轭的：$\mathbf{v}$, $\overline{\mathbf{v}}$
- 在实空间中，变换表现为**旋转 + 缩放**
- $e^{At}$ 产生 $\sin/\cos$ 振荡项

**示例**：$A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$（旋转 $90^\circ$）。$p(\lambda) = \lambda^2 + 1$，$\lambda = \pm i$。
- $\lambda = i$：$(A - iI)\mathbf{v} = \mathbf{0} \implies \mathbf{v} = [1, -i]^T$
- $\lambda = -i$：$\mathbf{v} = [1, i]^T$（前者的共轭）
- $e^{At} = \begin{bmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{bmatrix}$——这正是旋转矩阵！

---

## 5. 对角化

### 5.1 条件与定义

> **定义 5（可对角化）**：$A$ **可对角化** $\iff$ 存在可逆矩阵 $P$ 和对角矩阵 $\Lambda$ 使得：
>
> $$A = P\Lambda P^{-1}$$
>
> 其中 $P$ 的列是 $A$ 的特征向量，$\Lambda$ 的对角线是相应的特征值。

**可对角化的充分条件**：
1. $A$ 有 $n$ 个线性无关的特征向量（充要条件）
2. $A$ 有 $n$ 个互不相同的特征值（充分不必要）
3. $A$ 是实对称矩阵（更强——可**正交**对角化，即 $P$ 可选为正交矩阵）

### 5.2 对角化的威力

为什么对角化如此重要？因为 $A^k = P\Lambda^k P^{-1}$：

$$\Lambda^k = \begin{bmatrix} \lambda_1^k & & \\ & \ddots & \\ & & \lambda_n^k \end{bmatrix}$$

**应用**：
- 矩阵幂的计算（Markov 链、PageRank）
- 微分方程 $\dot{\mathbf{x}} = A\mathbf{x}$ 的解
- 主成分分析 (PCA)

---

## 6. 数值计算：幂迭代法 (Power Iteration)

### 6.1 动机

解析求特征多项式对 $n > 4$ 不实际（Abel-Ruffini：五次以上无根式解）。数值方法中，**幂迭代**是最简单的最大特征值算法。

### 6.2 算法

> **幂迭代**：求最大绝对值特征值（主特征值）及对应特征向量。

$$\mathbf{v}_{k+1} = \frac{A\mathbf{v}_k}{\|A\mathbf{v}_k\|}$$

$\mathbf{v}_k \to$ 主特征向量，$\lambda_{\max} \approx \frac{\mathbf{v}_k^T A \mathbf{v}_k}{\mathbf{v}_k^T \mathbf{v}_k}$（Rayleigh 商）。

**收敛条件**：$|\lambda_1| > |\lambda_2| \geq \cdots \geq |\lambda_n|$（主特征值严格大于其余）。

**收敛的几何直觉**：将初始向量 $\mathbf{v}_0$ 在特征基下展开：$\mathbf{v}_0 = \sum c_i \mathbf{v}_i$。每次乘以 $A$：$A^k \mathbf{v}_0 = \sum c_i \lambda_i^k \mathbf{v}_i = \lambda_1^k [c_1\mathbf{v}_1 + c_2(\lambda_2/\lambda_1)^k\mathbf{v}_2 + \cdots]$。若 $|\lambda_1| > |\lambda_2|$，则 $(\lambda_2/\lambda_1)^k \to 0$，$\mathbf{v}_k$ 逐渐趋向 $\mathbf{v}_1$ 的方向——即主特征向量。

**收敛速率**：$|\lambda_2 / \lambda_1|^k$。$|\lambda_2 / \lambda_1|$ 越小，收敛越快。

**不收敛的情况**：
- $|\lambda_1| = |\lambda_2|$（如 $\lambda_1 = 1, \lambda_2 = -1$）→ 幂迭代在两者间振荡，不收敛到单一向量
- $c_1 = 0$（初始向量恰好不含主特征方向的分量）→ 收敛到次大特征值（数值上极少发生）

---

## 7. 相似性与谱

> **定义 6（相似）**：$A, B$ 相似 $\iff \exists P$ 可逆，$B = P^{-1}AP$。

相似矩阵有相同的**特征值、迹、行列式、秩**。但不一定有相同的特征向量（$B$ 的是 $P^{-1}\mathbf{v}$）。

> **定义 7（谱）**：$A$ 的**谱 (spectrum)** $\sigma(A)$ 是全体特征值（含重数）。

---

## 8. 实对称矩阵与 Hermitian 矩阵的特殊性

> **定理（谱定理，实对称版）**：若 $A = A^T$，则
> 1. 所有特征值都是实数
> 2. 不同特征值对应的特征向量正交
> 3. $A$ 可**正交对角化**：$A = Q\Lambda Q^T$，$Q$ 为正交矩阵

这是线性代数最优美的定理之一。见第 07 章详细展开。

> **推广到复数域**：若 $A$ 是 **Hermitian 矩阵**（$A^* = A$），则：
> 1. 所有特征值都是实数（$\lambda_i \in \mathbb{R}$）
> 2. 不同特征值对应特征向量 Hermitian-正交（$\mathbf{v}_i^* \mathbf{v}_j = 0$）
> 3. $A$ 可**酉对角化**：$A = U\Lambda U^*$，$U$ 为酉矩阵

**为什么 Hermitian 矩阵的特征值是实数？** 设 $A\mathbf{v} = \lambda\mathbf{v}$，则 $\lambda\|\mathbf{v}\|^2 = \mathbf{v}^* A \mathbf{v} = (A\mathbf{v})^* \mathbf{v} = \overline{\lambda}\|\mathbf{v}\|^2$（用了 $A^* = A$）。故 $\overline{\lambda} = \lambda$，即 $\lambda \in \mathbb{R}$。证毕

这一性质使 Hermitian 矩阵在量子力学中天然适合表示「可观测量」——测量结果必须是实数。

---

## 9. 概念演示：幂迭代的收敛过程

> 本章的编程练习在 `编程题/` 目录下。运行 `python3 grader.py` 自动批改。

```python
import numpy as np

A = np.array([[2, 1],
              [1, 2]])  # 特征值 3 和 1
v = np.random.randn(2)
v = v / np.linalg.norm(v)

for k in range(10):
    v = A @ v
    v = v / np.linalg.norm(v)
    rayleigh = v @ A @ v / (v @ v)
    print(f"k={k+1:2d}: λ≈{rayleigh:.6f}, v={v}")

# 观察：Rayleigh 商从随机值快速逼近 3（主特征值）
# 收敛速率 ≈ (λ2/λ1)^k = (1/3)^k — 每步缩小约 3 倍
```

**要点**：幂迭代每次乘法 $A\mathbf{v}$ 都在放大主特征方向的分量比例。这正是特征分解在数值计算中的核心思想。

---

## 10. 例题

### 例 1：特征分解

对 $A = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$，求特征值和特征向量。

<details><summary>解</summary>

$p(\lambda) = \det\begin{bmatrix}3-\lambda&1\\0&2-\lambda\end{bmatrix} = (3-\lambda)(2-\lambda) = 0$

$\lambda_1 = 3$, $\lambda_2 = 2$。

- $\lambda_1=3$：$(A-3I)\mathbf{v} = \begin{bmatrix}0&1\\0&-1\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_1 = [1, 0]^T$
- $\lambda_2=2$：$(A-2I)\mathbf{v} = \begin{bmatrix}1&1\\0&0\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_2 = [1, -1]^T$

</details>

### 例 2：判断可对角化

$A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ 可对角化吗？

<details><summary>解</summary>

$p(\lambda) = (1-\lambda)^2$，$\lambda = 1$（代数重数 2）。

$(A - I)\mathbf{v} = \begin{bmatrix}0&1\\0&0\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v} = [c, 0]^T$。

特征空间维数 = 1（几何重数 1 < 代数重数 2）。**不可对角化**。

</details>

---

## 11. 常见误区

| 误区 | 正确理解 |
|------|----------|
| 「特征向量只有一个」 | 一个特征值对应一个特征空间，里面有无穷多个特征向量（零向量除外） |
| 「所有矩阵都可对角化」 | 不可对角化的充要条件：存在某个 $\lambda$ 使 $g(\lambda) < a(\lambda)$ |
| 「特征值必然是实数」 | 一般实矩阵的特征值可能是复数。仅实对称/Hermitian 矩阵保证实数 |
| 「特征向量必然正交」 | 仅实对称（更一般：正规矩阵）的不同特征值对应特征向量正交 |
| 「$\det A = 0$ 就是 $A = 0$」 | $\det A = 0$ 意味着 0 是特征值，空间被「压扁」但可能还有其他方向 |
| 「代数重数 = 几何重数永远成立」 | 仅在矩阵可对角化时成立。$\begin{bmatrix}0&1\\0&0\end{bmatrix}$ 的 $\lambda=0$ 有 $a=2$, $g=1$ |
| 「$e^{At}$ 只含指数项」 | 若矩阵有缺陷，$e^{At}$ 含 $t^k e^{\lambda t}$ 项——瞬态多项式增长 |

---

## 本章核心概念速查

| 概念 | 定义 | 一句话 |
|------|------|--------|
| 特征值 | $A\mathbf{v} = \lambda\mathbf{v}$ 中 $\lambda$ | 方向上的缩放倍数 |
| 特征向量 | 同上 $\mathbf{v}$ | 变换后方向不变的特殊向量 |
| 特征多项式 | $\det(A - \lambda I)$ | 特征值即该多项式的根 |
| 特征空间 | $\ker(A - \lambda I)$ | 同一特征值的全部特征向量 |
| 可对角化 | $A = P\Lambda P^{-1}$ | 可分解为独立缩放 |
| 代数重数 | 根的重数 | 特征多项式中出现的次数 |
| 几何重数 | $\dim E_\lambda$ | 线性无关特征向量的个数 |
| 幂迭代 | $\mathbf{v}_{k+1} = A\mathbf{v}_k/\|A\mathbf{v}_k\|$ | 逼近最大特征值 |
| 谱 | 全体特征值的集合 | 矩阵的「指纹」 |
| Rayleigh 商 | $\mathbf{v}^T A\mathbf{v} / \mathbf{v}^T\mathbf{v}$ | 从向量估计特征值 |

---

← 前置: [05 — 行列式、逆、秩与矩阵范数](../05-行列式-逆-秩与矩阵范数/notes.md)
→ 延伸: [07 — 对角化、谱分解与 Jordan 标准形](../07-对角化-谱分解与Jordan标准形/notes.md)
