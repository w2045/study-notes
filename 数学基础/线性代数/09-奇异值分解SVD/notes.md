# 线性代数 · 第九章 · 奇异值分解 (SVD)

← 前置: [08 — 正定矩阵、投影与 QR 分解](../08-正定矩阵-投影与QR分解/notes.md)
→ 延伸: [10 — 矩阵微积分](../10-矩阵微积分/notes.md)

---

## 1. 直觉引入：矩阵的「解剖」

前面我们学到了：
- 谱定理：$A = Q\Lambda Q^T$ ——只对**对称方阵**有效
- Jordan 型：$A = P J P^{-1}$ ——对一般方阵有效，但形式复杂

问题：对**任意**矩形矩阵 $A \in \mathbb{R}^{m \times n}$，有没有统一的「解剖」工具？

答案：**奇异值分解 (SVD)**。它说：**任何矩阵 = 旋转 × 缩放 × 旋转**。

$$A = U \Sigma V^T$$

- $U$：$\mathbb{R}^m$ 中的旋转（左奇异向量）
- $\Sigma$：对角缩放矩阵（奇异值）
- $V$：$\mathbb{R}^n$ 中的旋转（右奇异向量）

> **核心洞察**：SVD 把任意矩阵 $A$ 分解为三个「纯粹」部分的乘积——两组正交变换夹一个对角缩放。这是线性代数中最重要的分解，也是数据科学（PCA、压缩、推荐系统）的数学基础。

---

## 2. SVD 的形式化定义

> **定义 1（SVD）**：对 $A \in \mathbb{R}^{m \times n}$，存在正交矩阵 $U \in \mathbb{R}^{m \times m}$ 和 $V \in \mathbb{R}^{n \times n}$，以及对角矩阵 $\Sigma \in \mathbb{R}^{m \times n}$，使得：
>
> $$A = U \Sigma V^T$$
>
> 其中 $\Sigma$ 有非负对角元 $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0 = \sigma_{r+1} = \cdots = \sigma_{\min(m,n)}$。$\sigma_i$ 称为**奇异值**，$r = \operatorname{rank}(A)$。

**向量形式**：
$$A = \sum_{i=1}^{r} \sigma_i \mathbf{u}_i \mathbf{v}_i^T$$

其中 $\mathbf{u}_i$ 是 $U$ 的第 $i$ 列（左奇异向量），$\mathbf{v}_i$ 是 $V$ 的第 $i$ 列（右奇异向量）。

---

## 3. 几何解释

$A: \mathbb{R}^n \to \mathbb{R}^m$ 的 SVD 做三件事：

1. **$V^T$（旋转）**：将输入空间的基旋转，使变换的「主方向」对齐坐标轴
2. **$\Sigma$（缩放）**：沿各坐标轴方向独立缩放 $\sigma_i$ 倍
3. **$U$（旋转）**：再旋转到输出空间

**单位球在 $A$ 下变成了一个超椭球**，半轴方向 = $\mathbf{u}_i$，半轴长度 = $\sigma_i$。

---

## 4. 紧 SVD 与低秩近似

### 4.1 紧 SVD (Compact SVD)

只保留非零奇异值对应的部分：

$$A = U_r \Sigma_r V_r^T$$

其中 $U_r \in \mathbb{R}^{m \times r}$, $\Sigma_r = \operatorname{diag}(\sigma_1, \ldots, \sigma_r)$, $V_r \in \mathbb{R}^{n \times r}$。

### 4.2 Eckart-Young 定理（低秩近似）

> **定理（Eckart-Young）**：$A$ 的最佳秩-$k$ 近似（在 Frobenius 或谱范数下）由截断 SVD 给出：
>
> $$A_k = \sum_{i=1}^{k} \sigma_i \mathbf{u}_i \mathbf{v}_i^T$$
>
> 近似误差：$\|A - A_k\|_F = \sqrt{\sum_{i=k+1}^{r} \sigma_i^2}$，$\|A - A_k\|_2 = \sigma_{k+1}$。

**应用**：
- **图像压缩**：保留前 $k$ 个奇异值，压缩比约 $k(m+n+1)/(mn)$
- **PCA**：SVD 就是 PCA 的算法核心（中心化数据矩阵的 SVD）
- **推荐系统**：SVD 用于矩阵补全

**证明思路**（Eckart-Young，谱范数情形）：

要证：对任意秩-$\leq k$ 的矩阵 $B$，$\|A - B\|_2 \geq \sigma_{k+1}$，且 $B = A_k$ 取等号。

1. 考虑 $V$ 的后 $k+1$ 个右奇异向量张成的子空间 $W = \operatorname{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_{k+1}\}$（维数 $k+1$）。
2. 对任意秩-$\leq k$ 的 $B$，$\ker(B)$ 维数 $\geq n - k$。由维数公式，$W \cap \ker(B) \neq \{\mathbf{0}\}$——存在单位向量 $\mathbf{w} \in W$ 使得 $B\mathbf{w} = \mathbf{0}$。
3. 写出 $\mathbf{w} = \sum_{i=1}^{k+1} c_i \mathbf{v}_i$，则 $\|(A - B)\mathbf{w}\| = \|A\mathbf{w}\| = \|\sum_{i=1}^{k+1} c_i \sigma_i \mathbf{u}_i\| \geq \sigma_{k+1}\|\sum c_i \mathbf{u}_i\| = \sigma_{k+1}$（因为 $\sigma_1 \geq \cdots \geq \sigma_{k+1}$ 且 $\mathbf{u}_i$ 正交）。
4. 故 $\|A - B\|_2 \geq \sigma_{k+1}$。而 $A_k$ 能达到此下界。证毕

---

## 5. SVD 与 $A^T A$ 和 $AA^T$ 的关系

$A^T A$ 的特征值 = 奇异值的平方：$A^T A \mathbf{v}_i = \sigma_i^2 \mathbf{v}_i$。

$AA^T$ 的特征值 = 奇异值的平方：$AA^T \mathbf{u}_i = \sigma_i^2 \mathbf{u}_i$。

**这给出了 SVD 的计算方法**：
- $V$ 的列 = $A^T A$ 的特征向量（右奇异向量）
- $U$ 的列 = $AA^T$ 的特征向量（左奇异向量）
- $\sigma_i = \sqrt{\lambda_i(A^T A)} = \sqrt{\lambda_i(AA^T)}$（非负平方根）

---

## 6. SVD 的性质

| 性质 | 公式/说明 |
|------|-----------|
| 秩 | $\operatorname{rank}(A) = $ 非零奇异值的个数 |
| 谱范数 | $\|A\|_2 = \sigma_{\max}$ |
| Frobenius 范数 | $\|A\|_F = \sqrt{\sum \sigma_i^2}$ |
| 核范数 | $\|A\|_* = \sum \sigma_i$ |
| 条件数 | $\kappa_2(A) = \sigma_{\max} / \sigma_{\min}$ |
| 伪逆 | $A^+ = V \Sigma^+ U^T$，其中 $\Sigma^+_{ii} = 1/\sigma_i$（非零） |
| 行列式 | $|\det A| = \prod \sigma_i$（方阵） |

---

## 7. 图像压缩演示原理

一副 $H \times W$ 灰度图像是 $H \times W$ 矩阵 $M$。SVD 给出：

$$M \approx \sum_{i=1}^{k} \sigma_i \mathbf{u}_i \mathbf{v}_i^T$$

存储 $k$ 个奇异值三元组需要 $k(H + W + 1)$ 个数，vs 原始 $HW$ 个数。

当 $k \ll \min(H, W)$ 时大幅压缩。前 $k$ 个奇异值占「能量」比例为：

$$\text{能量保留} = \frac{\sum_{i=1}^{k} \sigma_i^2}{\sum_{i=1}^{r} \sigma_i^2}$$

---

## 8. Moore-Penrose 伪逆 (Pseudoinverse)

### 8.1 动机：当逆矩阵不存在时

方阵可逆时，$A^{-1}$ 完美解 $A\mathbf{x} = \mathbf{b}$。但是：
- **矩形矩阵**（$m \neq n$）：变换改变了空间维数，不可能有双边逆
- **秩亏方阵**（$\det = 0$）：零空间非平凡，映射不可逆

我们需要一个**对所有矩阵都存在**的「广义逆」——Moore-Penrose 伪逆 $A^+$。

### 8.2 Penrose 四条件

> **定义（Moore-Penrose 伪逆）**：$A \in \mathbb{R}^{m \times n}$ 的伪逆 $A^+ \in \mathbb{R}^{n \times m}$ 是满足以下四个条件的**唯一**矩阵：
>
> 1. $A A^+ A = A$（$A^+$ 是 $A$ 的广义逆）
> 2. $A^+ A A^+ = A^+$（$A$ 是 $A^+$ 的广义逆）
> 3. $(A A^+)^T = A A^+$（$A A^+$ 是对称矩阵——它是正交投影）
> 4. $(A^+ A)^T = A^+ A$（$A^+ A$ 也是对称矩阵——它也是正交投影）

这四个条件看起来简洁，但它们**唯一确定**了 $A^+$。普通的逆 $A^{-1}$ 自然满足全部四条（此时 $A^+ = A^{-1}$）。

### 8.3 SVD 表达式

$$A = U \Sigma V^T \quad \implies \quad A^+ = V \Sigma^+ U^T$$

其中 $\Sigma^+$ 是对 $\Sigma$ 的每个非零奇异值取倒数、零保持为零的对角矩阵（适当转置形状）：
$$\Sigma = \begin{bmatrix} \sigma_1 & & & \\ & \ddots & & \\ & & \sigma_r & \\ & & & 0 \end{bmatrix}_{m \times n} \quad \implies \quad \Sigma^+ = \begin{bmatrix} 1/\sigma_1 & & & \\ & \ddots & & \\ & & 1/\sigma_r & \\ & & & 0 \end{bmatrix}_{n \times m}$$

验证 Penrose 条件：$A A^+ = U \Sigma V^T V \Sigma^+ U^T = U (\Sigma \Sigma^+) U^T$。而 $\Sigma \Sigma^+ = \begin{bmatrix} I_r & 0 \\ 0 & 0 \end{bmatrix}_{m \times m}$ 是对称幂等矩阵。$(A A^+)^T = A A^+$ ✓。其余同理。

### 8.4 伪逆与四个基本子空间（SVD 视角）

SVD 为四个基本子空间提供了**标准正交基**（对比 Ch04 §11 中从 RREF 提取的基）：

| 子空间 | 维数 | SVD 标准正交基 |
|--------|------|---------------|
| $\operatorname{Col}(A)$ | $r$ | $\{\mathbf{u}_1, \ldots, \mathbf{u}_r\}$ |
| $\operatorname{Row}(A)$ | $r$ | $\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$ |
| $\operatorname{Null}(A)$ | $n - r$ | $\{\mathbf{v}_{r+1}, \ldots, \mathbf{v}_n\}$ |
| $\operatorname{Null}(A^T)$ | $m - r$ | $\{\mathbf{u}_{r+1}, \ldots, \mathbf{u}_m\}$ |

其中 $\mathbf{u}_i$ 是 $U$ 的列（左奇异向量），$\mathbf{v}_i$ 是 $V$ 的列（右奇异向量）。

**正交投影关系**：
- $A A^+ = U_r U_r^T$ 是到 $\operatorname{Col}(A)$ 的**正交投影矩阵**
- $A^+ A = V_r V_r^T$ 是到 $\operatorname{Row}(A)$ 的**正交投影矩阵**
- $I - A A^+$ 是到 $\operatorname{Null}(A^T)$ 的正交投影
- $I - A^+ A$ 是到 $\operatorname{Null}(A)$ 的正交投影

这完美体现了 Ch04 §11.5 的四个子空间关系和正交直和分解——SVD 为这些分解提供了标准正交基。

### 8.5 伪逆解最小二乘

对于 $A\mathbf{x} = \mathbf{b}$，**不论 $A$ 是否可逆**：

$$\mathbf{x}^+ = A^+ \mathbf{b}$$

是以下最小二乘问题的**最小范数解**：
$$\mathbf{x}^+ = \arg\min_{\mathbf{x}} \|\mathbf{x}\|_2 \quad \text{s.t.} \quad \|A\mathbf{x} - \mathbf{b}\|_2 \text{ 最小}$$

**特殊情况**：
- 若 $A$ 列满秩（$r = n$）：$A^+ = (A^T A)^{-1} A^T$，$\mathbf{x}^+$ 就是正规方程的唯一解
- 若 $A$ 行满秩（$r = m$）：$A^+ = A^T (A A^T)^{-1}$，$\mathbf{x}^+$ 是欠定系统的最小范数解
- 若 $A$ 可逆：$A^+ = A^{-1}$，$\mathbf{x}^+ = A^{-1}\mathbf{b}$（唯一解）

### 8.6 计算示例

$A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$（秩 1，不可逆）。SVD：$A = \begin{bmatrix} 1/\sqrt{5} & -2/\sqrt{5} \\ 2/\sqrt{5} & 1/\sqrt{5} \end{bmatrix} \begin{bmatrix} 5 & 0 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 1/\sqrt{5} & 2/\sqrt{5} \\ -2/\sqrt{5} & 1/\sqrt{5} \end{bmatrix}^T$

$$\Sigma^+ = \begin{bmatrix} 1/5 & 0 \\ 0 & 0 \end{bmatrix}, \quad A^+ = V \Sigma^+ U^T = \frac{1}{25} \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$$

验证：$A A^+ A = A$ ✓，$A^+ A A^+ = A^+$ ✓，$A A^+$ 对称 ✓，$A^+ A$ 对称 ✓。

---

## 9. 概念演示：SVD 低秩近似的压缩效果

> 本章的编程练习在 `编程题/` 目录下。运行 `python3 grader.py` 自动批改。

```python
import numpy as np

# 100x100 的低秩矩阵（秩=3）
U, _ = np.linalg.qr(np.random.randn(100, 3))
V, _ = np.linalg.qr(np.random.randn(100, 3))
A = U @ np.diag([100, 50, 10]) @ V.T

# 秩-1 近似
u, s, vt = np.linalg.svd(A, full_matrices=False)
A1 = s[0] * np.outer(u[:, 0], vt[0, :])

# 能量保留：σ1² / (σ1² + σ2² + σ3²)
energy_ratio = s[0]**2 / np.sum(s**2)
error = np.linalg.norm(A - A1)  # Frobenius

print(f"秩-1 能量保留: {energy_ratio:.1%}")  # ≈ 80%
print(f"误差 σ2: {error:.1f} vs σ2: {s[1]:.1f}")  # 误差 ≈ σ2 — Eckart-Young!
```

**要点**：`np.linalg.svd` 是数值计算 SVD 的标准工具。误差 $\|A - A_k\|_F = \sqrt{\sum_{i=k+1}^r \sigma_i^2}$，被截断的奇异值直接决定了信息损失。

---

## 10. 例题

### 例 1：2x2 SVD

求 $A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}$ 的 SVD。

<details><summary>解</summary>

$A^T A = \begin{bmatrix} 3 & 4 \\ 0 & 5 \end{bmatrix} \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix} = \begin{bmatrix} 25 & 20 \\ 20 & 25 \end{bmatrix}$

特征值：$(25-\lambda)^2 - 400 = 0 \implies \lambda^2 - 50\lambda + 225 = 0$
$\lambda = 45, 5$。$\sigma_1 = \sqrt{45} = 3\sqrt{5}$, $\sigma_2 = \sqrt{5}$。

$\lambda_1 = 45$：$(A^T A - 45I)\mathbf{v} = \begin{bmatrix}-20&20\\20&-20\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_1 = \frac{1}{\sqrt{2}}[1, 1]^T$

$\lambda_2 = 5$：$\mathbf{v}_2 = \frac{1}{\sqrt{2}}[1, -1]^T$

$\mathbf{u}_1 = \frac{1}{\sigma_1} A\mathbf{v}_1 = \frac{1}{3\sqrt{5}}\begin{bmatrix}3&0\\4&5\end{bmatrix}\frac{1}{\sqrt{2}}\begin{bmatrix}1\\1\end{bmatrix} = \frac{1}{\sqrt{10}}\begin{bmatrix}3\\9\end{bmatrix}$

$\mathbf{u}_2$ 同理。最终：
$$U = \frac{1}{\sqrt{10}}\begin{bmatrix}3 & -1 \\ 1 & 3\end{bmatrix}, \quad \Sigma = \begin{bmatrix}3\sqrt{5}&0\\0&\sqrt{5}\end{bmatrix}, \quad V^T = \frac{1}{\sqrt{2}}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$$

</details>

### 例 2：低秩近似（图像压缩思想）

原始 $4\times 3$ 矩阵 $M$ 的秩-1 近似。

<details><summary>解</summary>

$$M = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \\ 3 & 6 & 3 \end{bmatrix}$$

观察发现所有列是 $[1, 2, 1, 3]^T$ 的倍数，所有行是 $[1, 2, 1]$ 的倍数。秩 = 1。

奇异值只有一个非零：$\sigma_1 = \|[1,2,1,3]^T\| \cdot \|[1,2,1]^T\| = \sqrt{15} \cdot \sqrt{6} = \sqrt{90}$。

秩-1 近似 = 原矩阵本身（因为秩确实是 1）。这解释了为什么有些图像有极高压缩比。

</details>

---

## 11. 常见误区

| 误区 | 正确理解 |
|------|----------|
| 「SVD = 特征分解推广到非方阵」 | 不对。SVD 对**任意矩阵**存在，特征分解只对方阵存在。且 SVD 的 $U, V$ 是正交矩阵，不是特征向量矩阵 |
| 「奇异值 = 特征值」 | 仅对称半正定矩阵成立（此时 $\sigma_i = \lambda_i$）。一般矩阵的奇异值 ≠ 特征值 |
| 「奇异值就是 $A^T A$ 的特征值」 | 是 $A^T A$ 特征值的**平方根**：$\sigma_i = \sqrt{\lambda_i(A^T A)}$ |
| 「SVD 可以随便排序」 | 约定按 $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0$ 排序。重排会破坏 $U, V$ 的对应关系 |
| 「紧 SVD 的 $U_r$ 是方阵」 | 紧 SVD 中 $U_r \in \mathbb{R}^{m \times r}$，只有当 $m = r$ 时才是方阵 |
| 「低秩近似 = 随便删几个奇异值」 | Eckart-Young 定理保证截断 SVD 是**所有**同秩矩阵中的最优近似——这是 SVD 独有的性质 |
| 「伪逆就是 $(A^T A)^{-1} A^T$」 | 这个公式仅在 $A$ 列满秩时成立。一般公式是 $A^+ = V\Sigma^+ U^T$ |
| 「左/右奇异向量就是特征向量」 | 左奇异向量是 $AA^T$ 的特征向量，右奇异向量是 $A^T A$ 的特征向量——它们是不同矩阵的 |
| 「四个子空间只能从 RREF 求基」 | SVD 直接给出四个子空间的**标准正交基**，比 RREF 提取的基更「干净」 |

---

## 本章核心概念速查

| 概念 | 定义 | 一句话 |
|------|------|--------|
| SVD | $A = U\Sigma V^T$ | 任意矩阵的旋转-缩放-旋转解剖 |
| 奇异值 | $\sigma_i \geq 0$ | 各主方向的拉伸倍数 |
| 左奇异向量 | $\mathbf{u}_i$（$U$ 的列） | 输出空间的正交基 |
| 右奇异向量 | $\mathbf{v}_i$（$V$ 的列） | 输入空间的正交基 |
| 紧 SVD | $U_r \Sigma_r V_r^T$ | 只保留正奇异值 |
| 低秩近似 | $A_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i\mathbf{v}_i^T$ | 最佳秩-k 近似 |
| Eckart-Young | $\|A-A_k\|_2 = \sigma_{k+1}$ | 截断 SVD 最优 |
| 伪逆 | $A^+ = V\Sigma^+ U^T$ | 最小二乘的最小范数解 |
| Penrose 条件 | 4 条公理 | 伪逆的唯一定义 |
| 四子空间 (SVD) | $\mathbf{u}_i, \mathbf{v}_i$ 基 | SVD 给出四个子空间的标准正交基 |

---

← 前置: [08 — 正定矩阵、投影与 QR 分解](../08-正定矩阵-投影与QR分解/notes.md)
→ 延伸: [10 — 矩阵微积分](../10-矩阵微积分/notes.md)
