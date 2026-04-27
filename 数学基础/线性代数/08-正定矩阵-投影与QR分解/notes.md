# 线性代数 · 第八章 · 正定矩阵、投影与 QR 分解

← 前置: [07 — 对角化、谱分解与 Jordan 标准形](../07-对角化-谱分解与Jordan标准形/notes.md)
→ 延伸: [09 — 奇异值分解 SVD](../09-奇异值分解SVD/notes.md)

---

## 1. 直觉引入：二次型的「曲率」

第七章描述了矩阵的谱（特征值）。现在问一个更几何的问题：$\mathbf{x}^T A \mathbf{x}$ 这个标量函数描绘了什么「曲面」？

- 若 $A = I$：$\mathbf{x}^T I \mathbf{x} = \|\mathbf{x}\|^2$ 是一个「碗」（凸向上）。
- 若 $A = \begin{bmatrix}1&0\\0&-1\end{bmatrix}$：$\mathbf{x}^T A \mathbf{x} = x_1^2 - x_2^2$ 是一个「马鞍面」。
- 若 $A = \begin{bmatrix}-1&0\\0&-1\end{bmatrix}$：$\mathbf{x}^T A \mathbf{x} = -\|\mathbf{x}\|^2$ 是一个「倒碗」。

> **核心洞察**：正定矩阵 = 二次型「永远向上凸」。它保证优化问题有唯一最小值，分解算法（如 Cholesky）稳定存在。QR 分解则从另一个角度——把矩阵分解成正交矩阵 $\times$ 上三角矩阵，是 Gram-Schmidt 的矩阵形式。

---

## 2. 二次型 (Quadratic Form)

> **定义 1（二次型）**：对称矩阵 $A$ 的**二次型**是标量函数：
>
> $$Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x} = \sum_{i=1}^{n}\sum_{j=1}^{n} a_{ij} x_i x_j$$

**例子**：$\mathbf{x}^T \begin{bmatrix}a&b\\b&c\end{bmatrix} \mathbf{x} = a x_1^2 + 2b x_1 x_2 + c x_2^2$

---

## 3. 正定性

> **定义 2（正定性）**：对称矩阵 $A$ 是：
>
> - **正定 (positive definite)**：$\mathbf{x}^T A \mathbf{x} > 0$ 对所有 $\mathbf{x} \neq \mathbf{0}$
> - **半正定 (positive semidefinite)**：$\mathbf{x}^T A \mathbf{x} \geq 0$ 对所有 $\mathbf{x}$
> - **负定 (negative definite)**：$\mathbf{x}^T A \mathbf{x} < 0$ 对所有 $\mathbf{x} \neq \mathbf{0}$

### 3.1 正定性的等价条件

以下各条等价（对实对称矩阵 $A$）：

1. $A$ 是正定的
2. 所有特征值 $\lambda_i > 0$
3. 所有前主子式 $> 0$（Sylvester 判据）
4. 存在可逆矩阵 $B$ 使得 $A = B^T B$
5. $A$ 的所有主元 $> 0$
6. Cholesky 分解 $A = LL^T$ 存在且 $L$ 的对角线元素 $> 0$

### 3.2 Sylvester 判据

> **定理（Sylvester 判据）**：对称矩阵 $A$ 正定 $\iff$ 所有前主子行列式 $> 0$：
>
> $$\det A_1 > 0,\ \det A_2 > 0,\ \ldots,\ \det A_n > 0$$
>
> 其中 $A_k$ 是 $A$ 的左上角 $k \times k$ 子矩阵。

**例子**：$A = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$。
$\det A_1 = 2 > 0$, $\det A_2 = 4 - 1 = 3 > 0$。$A$ 正定。

---

## 4. Cholesky 分解

> **定义 3（Cholesky 分解）**：若 $A$ 正定，则存在唯一的下三角矩阵 $L$，所有对角线元素 $> 0$，使得：
>
> $$A = L L^T$$

### 4.1 算法

对 $i = 1, \ldots, n$：

$$\ell_{ii} = \sqrt{a_{ii} - \sum_{k=1}^{i-1} \ell_{ik}^2}$$

对 $j = i+1, \ldots, n$：

$$\ell_{ji} = \frac{1}{\ell_{ii}}\left(a_{ji} - \sum_{k=1}^{i-1} \ell_{jk} \ell_{ik}\right)$$

### 4.2 与 LU 的关系

Cholesky 是 LU 分解的特例（$U = L^T$，$A$ 正定）。计算量为 LU 的一半。

---

## 5. 正交投影

### 5.1 到子空间的投影

> **定义 4（正交投影矩阵）**：到子空间 $W$（列空间 $\operatorname{col}(A)$）的正交投影矩阵：
>
> $$P = A(A^T A)^{-1} A^T$$

**性质**：
- $P^2 = P$（幂等——投影一次后不再变化）
- $P^T = P$（对称）
- $P A = A$（$W$ 中向量不变）
- $I - P$ 投影到 $W^\perp$

### 5.2 最小二乘问题

回到 Ch02 中的直线投影：$\operatorname{proj}_{\mathbf{a}}(\mathbf{b}) = \frac{\mathbf{a}\cdot\mathbf{b}}{\mathbf{a}\cdot\mathbf{a}}\mathbf{a}$。那是到一维子空间的最小二乘。现在推广到多维。

$$\min_{\mathbf{x}} \|A\mathbf{x} - \mathbf{b}\|_2^2$$

**为什么残差正交意味着最优？** 对任意 $\mathbf{x}$，设 $\mathbf{\hat{x}}$ 满足 $\mathbf{b} - A\mathbf{\hat{x}} \perp \operatorname{col}(A)$：
$$\|A\mathbf{x} - \mathbf{b}\|^2 = \|A\mathbf{x} - A\mathbf{\hat{x}} + A\mathbf{\hat{x}} - \mathbf{b}\|^2 = \|A(\mathbf{x} - \mathbf{\hat{x}})\|^2 + \|A\mathbf{\hat{x}} - \mathbf{b}\|^2 \geq \|A\mathbf{\hat{x}} - \mathbf{b}\|^2$$
其中交叉项 $2\langle A(\mathbf{x} - \mathbf{\hat{x}}), A\mathbf{\hat{x}} - \mathbf{b} \rangle = 0$ 因为 $A(\mathbf{x} - \mathbf{\hat{x}}) \in \operatorname{col}(A)$ 而残差 $\perp \operatorname{col}(A)$。等号仅当 $A\mathbf{x} = A\mathbf{\hat{x}}$。故正交投影给出唯一最优逼近。

最优解满足**正规方程**：$A^T A \mathbf{x} = A^T \mathbf{b}$。（推导：残差 $\mathbf{b} - A\mathbf{x} \perp \operatorname{col}(A) \iff A^T(\mathbf{b} - A\mathbf{x}) = \mathbf{0}$。）

解的几何意义：$\mathbf{b}$ 投影到 $\operatorname{col}(A)$ 上 = $A\mathbf{\hat{x}} = P\mathbf{b}$。残差 $\mathbf{b} - A\mathbf{\hat{x}} \perp \operatorname{col}(A)$。

---

## 6. QR 分解

### 6.1 定义

> **定义 5（QR 分解）**：对 $A \in \mathbb{R}^{m \times n}$（$m \geq n$），存在列正交矩阵 $Q \in \mathbb{R}^{m \times n}$ 和上三角矩阵 $R \in \mathbb{R}^{n \times n}$，使得：
>
> $$A = QR, \quad Q^T Q = I_n$$

### 6.2 与 Gram-Schmidt 的关系

QR 分解就是 Gram-Schmidt 正交化的矩阵形式：
- $Q$ 的列 = Gram-Schmidt 生成的标准正交向量
- $R$ 记录 GS 过程中各向量的「系数」：$r_{ij} = \mathbf{q}_i^T \mathbf{a}_j$（$i \leq j$）

### 6.3 用 QR 解最小二乘

不用算 $(A^T A)^{-1}$ 这个条件数放大的矩阵：

1. 分解 $A = QR$
2. 计算 $\mathbf{c} = Q^T \mathbf{b}$
3. 回代解 $R\mathbf{x} = \mathbf{c}$

这比正规方程数值更稳定。

---

## 7. 概念演示：最小二乘拟合

> 本章的编程练习在 `编程题/` 目录下。运行 `python3 grader.py` 自动批改。

```python
import numpy as np

# 3 个数据点 → 拟合直线 y = ax + b
x = np.array([1., 2., 3.])
y = np.array([1., 2., 2.])

A = np.column_stack([x, np.ones_like(x)])  # 每行 [xi, 1]
coeffs = np.linalg.lstsq(A, y, rcond=None)[0]
a, b = coeffs
print(f"y = {a:.3f}x + {b:.3f}")  # y = 0.500x + 0.667
```

**要点**：`lstsq` 在后台对 $A$ 做 QR 分解（不是正规方程！），数值更稳定。几何上，它在找列空间中离 $\mathbf{b}$ 最近的点。

---

## 8. 例题

### 例 1：Cholesky 分解

对 $A = \begin{bmatrix} 4 & 2 \\ 2 & 5 \end{bmatrix}$ 计算 $L$。

<details><summary>解</summary>

- $\ell_{11} = \sqrt{4} = 2$
- $\ell_{21} = 2 / 2 = 1$
- $\ell_{22} = \sqrt{5 - 1^2} = \sqrt{4} = 2$

$$L = \begin{bmatrix} 2 & 0 \\ 1 & 2 \end{bmatrix}$$

验证：$LL^T = \begin{bmatrix} 4 & 2 \\ 2 & 5 \end{bmatrix} = A$ ✓

</details>

### 例 2：QR 分解 (Gram-Schmidt)

$A = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{bmatrix}$，求 $Q$ 和 $R$。

<details><summary>解</summary>

$\mathbf{a}_1 = [1, 1, 0]^T$。归一化：$\mathbf{q}_1 = \frac{1}{\sqrt{2}}[1, 1, 0]^T$。

$\mathbf{a}_2 = [0, 1, 1]^T$。投影到 $\mathbf{q}_1$：$r_{12} = \mathbf{q}_1^T \mathbf{a}_2 = \frac{1}{\sqrt{2}}$。

$\mathbf{u}_2 = \mathbf{a}_2 - r_{12}\mathbf{q}_1 = [0,1,1]^T - \frac{1}{2}[1,1,0]^T = [-\frac{1}{2}, \frac{1}{2}, 1]^T$。

$\|\mathbf{u}_2\| = \sqrt{\frac{1}{4} + \frac{1}{4} + 1} = \sqrt{\frac{3}{2}}$。

$\mathbf{q}_2 = \sqrt{\frac{2}{3}}[-\frac{1}{2}, \frac{1}{2}, 1]^T = \frac{1}{\sqrt{6}}[-1, 1, 2]^T$。

$r_{11} = \|\mathbf{a}_1\| = \sqrt{2}$, $r_{22} = \|\mathbf{u}_2\| = \sqrt{\frac{3}{2}}$。

$$Q = \begin{bmatrix} 1/\sqrt{2} & -1/\sqrt{6} \\ 1/\sqrt{2} & 1/\sqrt{6} \\ 0 & 2/\sqrt{6} \end{bmatrix}, \quad R = \begin{bmatrix} \sqrt{2} & 1/\sqrt{2} \\ 0 & \sqrt{3/2} \end{bmatrix}$$

</details>

---

## 9. 常见误区

| 误区 | 正确理解 |
|------|----------|
| 「正定 = 所有元素 > 0」 | 反例：$\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$ 元素全正但行列式为负，不正定。正定性由特征值 / 前主子式决定 |
| 「Cholesky 和 LU 是一回事」 | Cholesky 只适用于正定矩阵，计算量是 LU 的一半（利用对称性），且 $U = L^T$ |
| 「正规方程总是最好的最小二乘解法」 | 正规方程的条件数是 $\kappa(A)^2$，当 $A$ 病态时数值灾难。QR 解法条件数为 $\kappa(A)$，更稳定 |
| 「Gram-Schmidt 和 QR 是不同东西」 | QR 分解就是 Gram-Schmidt 的矩阵形式——$Q$ 的列是正交化结果，$R$ 记录投影系数 |
| 「投影矩阵一定不是单位阵」 | $I$ 也是投影矩阵——投影到整个空间，$I^2 = I$, $I^T = I$ |
| 「二次型可以随便用矩阵表示」 | 二次型 $\mathbf{x}^T A \mathbf{x}$ 中 $A$ 可以假设为对称（因为 $\mathbf{x}^T A \mathbf{x} = \mathbf{x}^T \frac{A+A^T}{2} \mathbf{x}$） |

---

## 本章核心概念速查

| 概念 | 定义 | 一句话 |
|------|------|--------|
| 二次型 | $\mathbf{x}^T A \mathbf{x}$ | 标量曲率函数 |
| 正定 | 所有特征值 $> 0$ | 二次型总为正 |
| Sylvester 判据 | 前主子式 > 0 | 正定性充要条件 |
| Cholesky | $A = LL^T$ | 正定矩阵的最优分解 |
| 正交投影 | $P = A(A^T A)^{-1}A^T$ | 到列空间的最近点映射 |
| 正规方程 | $A^T A\mathbf{x} = A^T\mathbf{b}$ | 最小二乘的必要条件 |
| QR 分解 | $A = QR$ | Gram-Schmidt 的矩阵形式 |
| 最小二乘 | $\min \|A\mathbf{x} - \mathbf{b}\|$ | 到子空间的最近点 |

---

← 前置: [07 — 对角化、谱分解与 Jordan 标准形](../07-对角化-谱分解与Jordan标准形/notes.md)
→ 延伸: [09 — 奇异值分解 SVD](../09-奇异值分解SVD/notes.md)
