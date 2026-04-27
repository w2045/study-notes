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

> **定义 3（特征空间）**：$\lambda$ 的特征空间 $E_\lambda = \ker(A - \lambda I)$。

> **定义 4**：
> - **代数重数**：$\lambda$ 作为特征多项式根的重数
> - **几何重数**：$\dim E_\lambda$（特征空间的维数 = 对应特征值线性无关特征向量的最大个数）

**关键事实**：$1 \leq \text{几何重数} \leq \text{代数重数}$。

当几何重数 < 代数重数时，矩阵不能对角化（需要 Jordan 型，见第 07 章）。

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

**收敛速率**：$|\lambda_2 / \lambda_1|^k$。

---

## 7. 相似性与谱

> **定义 6（相似）**：$A, B$ 相似 $\iff \exists P$ 可逆，$B = P^{-1}AP$。

相似矩阵有相同的**特征值、迹、行列式、秩**。但不一定有相同的特征向量（$B$ 的是 $P^{-1}\mathbf{v}$）。

> **定义 7（谱）**：$A$ 的**谱 (spectrum)** $\sigma(A)$ 是全体特征值（含重数）。

---

## 8. 实对称矩阵的特殊性

> **定理（谱定理，实对称版）**：若 $A = A^T$，则
> 1. 所有特征值都是实数
> 2. 不同特征值对应的特征向量正交
> 3. $A$ 可**正交对角化**：$A = Q\Lambda Q^T$，$Q$ 为正交矩阵

这是线性代数最优美的定理之一。见第 07 章详细展开。

---

## 9. 代码实现

```python
from typing import List, Tuple, Optional
import math


def characteristic_polynomial_2x2(A: List[List[float]]) -> Tuple[float, float, float]:
    """返回 2x2 矩阵的特征多项式系数 (a, b, c)，即 aλ² + bλ + c = 0。"""
    a = 1.0
    b = -(A[0][0] + A[1][1])  # -tr(A)
    c = A[0][0] * A[1][1] - A[0][1] * A[1][0]  # det(A)
    return a, b, c


def eigenvalues_2x2(A: List[List[float]]) -> List[complex]:
    """返回 2x2 矩阵的特征值列表。"""
    a, b, c = characteristic_polynomial_2x2(A)
    disc = b * b - 4 * a * c
    if disc >= 0:
        sqrt_disc = math.sqrt(disc)
        return [(-b + sqrt_disc) / (2*a), (-b - sqrt_disc) / (2*a)]
    else:
        sqrt_disc = math.sqrt(-disc)
        return [complex(-b/(2*a), sqrt_disc/(2*a)),
                complex(-b/(2*a), -sqrt_disc/(2*a))]


def power_iteration(
    A: List[List[float]], max_iter: int = 1000, tol: float = 1e-10
) -> Tuple[List[float], float]:
    """幂迭代法求最大特征值和对应特征向量。"""
    import random
    n = len(A)
    v = [random.random() for _ in range(n)]
    v_norm = math.sqrt(sum(x*x for x in v))
    v = [x / v_norm for x in v]

    for _ in range(max_iter):
        # A @ v
        Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
        norm_Av = math.sqrt(sum(x*x for x in Av))
        v_new = [x / norm_Av for x in Av]

        # 检查收敛
        cos_sim = sum(a * b for a, b in zip(v, v_new))
        if abs(cos_sim - 1.0) < tol:
            v = v_new
            break
        v = v_new

    # Rayleigh 商: λ ≈ v^T A v / v^T v
    Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
    rayleigh = sum(v[i] * Av[i] for i in range(n))
    return v, rayleigh
```

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
| 「所有矩阵都可对角化」 | 如 $\begin{bmatrix}1&1\\0&1\end{bmatrix}$ 不可对角化 |
| 「特征值必然是实数」 | 一般实矩阵的特征值可能是复数。仅实对称矩阵保证实数 |
| 「特征向量必然正交」 | 仅实对称（更一般：正规矩阵）的不同特征值对应特征向量正交 |
| 「$\det A = 0$ 就是 $A = 0$」 | $\det A = 0$ 意味着 0 是特征值，空间被「压扁」但可能还有其他方向 |

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
