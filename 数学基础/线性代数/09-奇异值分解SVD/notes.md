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

## 8. 代码实现

```python
from typing import List, Tuple
import math


def svd_power_iteration(A: List[List[float]], k: int = 1) -> Tuple:
    """用幂迭代法计算前 k 大奇异值及向量（简化版）。"""
    m, n = len(A), len(A[0])
    # 此处为概念示意，完整实现用 numpy
    # 实际应用中用 numpy.linalg.svd
    pass


def low_rank_approx(
    U: List[List[float]], S: List[float], Vt: List[List[float]], k: int
) -> List[List[float]]:
    """从 SVD 重建秩-k 近似矩阵 A_k = sum_{i=1}^k sigma_i u_i v_i^T。"""
    m, n = len(U), len(Vt[0])
    result = [[0.0] * n for _ in range(m)]
    for idx in range(k):
        sigma = S[idx]
        u_col = [U[i][idx] for i in range(m)]
        v_row = Vt[idx]
        for i in range(m):
            for j in range(n):
                result[i][j] += sigma * u_col[i] * v_row[j]
    return result


def svd_error(A: List[List[float]], Ak: List[List[float]]) -> float:
    """计算 Frobenius 误差 ||A - A_k||_F。"""
    total = 0.0
    for i in range(len(A)):
        for j in range(len(A[0])):
            diff = A[i][j] - Ak[i][j]
            total += diff * diff
    return math.sqrt(total)
```

---

## 9. 例题

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
| 伪逆 | $A^+ = V\Sigma^+ U^T$ | 最小二乘的通解 |

---

← 前置: [08 — 正定矩阵、投影与 QR 分解](../08-正定矩阵-投影与QR分解/notes.md)
→ 延伸: [10 — 矩阵微积分](../10-矩阵微积分/notes.md)
