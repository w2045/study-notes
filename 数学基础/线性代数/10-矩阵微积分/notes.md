# 线性代数 · 第十章 · 矩阵微积分

← 前置: [09 — 奇异值分解 SVD](../09-奇异值分解SVD/notes.md)
→ 延伸: 微积分/凸优化后续课程

---

## 1. 直觉引入：梯度在矩阵世界

前九章都是线性世界。但机器学习和优化的核心操作是**梯度下降**：$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla_\mathbf{w} L$。

这就需要回答：函数 $f(\mathbf{x})$ 对向量 $\mathbf{x}$ 的导数是什么？$f(X)$ 对矩阵 $X$ 的导数呢？

> **核心洞察**：矩阵微积分 = 把标量微积分推广到多变量。通过**链式法则 + 微分外积**，所有矩阵求导都可以机械化完成。

---

## 2. 标量对向量的导数

### 2.1 梯度 (Gradient)

> **定义 1（梯度）**：$f: \mathbb{R}^n \to \mathbb{R}$ 的**梯度**是偏导数的列向量：
>
> $$\nabla_\mathbf{x} f = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}$$

**几何意义**：梯度指向 $f$ 增长最快的方向，大小 = 该方向的变化率。

### 2.2 常见公式

| $f(\mathbf{x})$ | $\nabla_\mathbf{x} f$ |
|-----------------|----------------------|
| $\mathbf{a}^T \mathbf{x}$ | $\mathbf{a}$ |
| $\mathbf{x}^T \mathbf{x} = \|\mathbf{x}\|^2$ | $2\mathbf{x}$ |
| $\mathbf{x}^T A \mathbf{x}$（$A$ 对称） | $2A\mathbf{x}$ |
| $\mathbf{x}^T A \mathbf{x}$（$A$ 一般） | $(A + A^T)\mathbf{x}$ |
| $\|A\mathbf{x} - \mathbf{b}\|^2$ | $2A^T(A\mathbf{x} - \mathbf{b})$ |
| $\log(\mathbf{a}^T \mathbf{x})$ | $\mathbf{a} / (\mathbf{a}^T \mathbf{x})$ |

### 2.3 推导演示：从定义出发

**示例 1**：$f(\mathbf{x}) = \mathbf{b}^T \mathbf{x} = \sum_i b_i x_i$。

逐分量：$\frac{\partial f}{\partial x_j} = \frac{\partial}{\partial x_j} (b_1 x_1 + \cdots + b_j x_j + \cdots + b_n x_n) = b_j$。

所有偏导拼成向量：$\nabla_\mathbf{x} f = [b_1, \ldots, b_n]^T = \mathbf{b}$。简洁明了——线性函数的梯度就是系数向量。

**示例 2**：$f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x} = \sum_{i,j} a_{ij} x_i x_j$（$A$ 对称）。

逐分量（对 $x_k$ 求偏导）：
- $i=k, j=k$：项 $a_{kk} x_k^2$，导数为 $2a_{kk} x_k$
- $i=k, j \neq k$：项 $a_{kj} x_k x_j$，导数为 $a_{kj} x_j$
- $i \neq k, j=k$：项 $a_{ik} x_i x_k$，导数为 $a_{ik} x_i$

全部加和：
$$\frac{\partial f}{\partial x_k} = 2a_{kk} x_k + \sum_{j \neq k} a_{kj} x_j + \sum_{i \neq k} a_{ik} x_i$$

由于 $A$ 对称（$a_{ik} = a_{ki}$），后两项合并为 $2\sum_{j \neq k} a_{kj} x_j$。故 $\frac{\partial f}{\partial x_k} = 2\sum_j a_{kj} x_j$ = $2(A\mathbf{x})_k$。

所有偏导拼成向量：$\nabla_\mathbf{x} f = 2A\mathbf{x}$。

如果 $A$ 不对称呢？后两项分别为 $\sum a_{kj} x_j$（来自 $i=k$）和 $\sum a_{ik} x_i$（来自 $j=k$）：
$$\nabla_\mathbf{x} f = A\mathbf{x} + A^T \mathbf{x} = (A + A^T)\mathbf{x}$$

### 2.4 布局约定说明

矩阵微积分有两个主流约定，**不可混用**：

| | 分母布局 (Denominator layout) | 分子布局 (Numerator layout) |
|---|---|---|
| $\nabla_\mathbf{x} f$ | **列向量**（与 $\mathbf{x}$ 同形） | 行向量 |
| $\frac{\partial \mathbf{f}}{\partial \mathbf{x}}$ | $n \times m$（Jacobian 的转置） | $m \times n$ |
| $\frac{\partial f}{\partial X}$ | 与 $X^T$ 同形 | 与 $X$ 同形 |

本项目**统一使用分母布局**（$\nabla_\mathbf{x} f$ 是列向量，$\nabla_X f$ 与 $X$ 同形）。在阅读论文时需验证对方使用的约定——同一公式在两种约定下可能差一个转置。

### 2.5 全微分法（推荐用于复杂推导）
1. 对 $f$ 取全微分：$df = \sum_i \frac{\partial f}{\partial x_i} dx_i$
2. 整理为 $df = \mathbf{g}^T d\mathbf{x}$ 的形式
3. 则 $\nabla f = \mathbf{g}$

**例**：$f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$（$A$ 对称）。
$df = d\mathbf{x}^T A \mathbf{x} + \mathbf{x}^T A d\mathbf{x} = \mathbf{x}^T A^T d\mathbf{x} + \mathbf{x}^T A d\mathbf{x} = 2\mathbf{x}^T A d\mathbf{x}$。
所以 $\nabla f = 2A\mathbf{x}$。

---

## 3. 向量对向量的导数：Jacobian

> **定义 2（Jacobian 矩阵）**：$\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$ 的 **Jacobian** 是 $m \times n$ 矩阵：
>
> $$J = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n} \end{bmatrix}$$
>
> 第 $i$ 行是 $\nabla f_i^T$，第 $j$ 列是 $\frac{\partial \mathbf{f}}{\partial x_j}$。

**关键例子**：

| $\mathbf{f}(\mathbf{x})$ | $\frac{\partial \mathbf{f}}{\partial \mathbf{x}}$ |
|--------------------------|--------------------------------------------------|
| $A\mathbf{x}$ | $A$ |
| $\mathbf{x}$ | $I_n$ |
| $\mathbf{a}^T \mathbf{x} \mathbf{b}$ | $\mathbf{b} \mathbf{a}^T$ |

**链式法则**：$\frac{\partial \mathbf{h}(\mathbf{g}(\mathbf{x}))}{\partial \mathbf{x}} = \frac{\partial \mathbf{h}}{\partial \mathbf{g}} \cdot \frac{\partial \mathbf{g}}{\partial \mathbf{x}}$（矩阵乘法）。

---

## 4. Hessian 矩阵

> **定义 3（Hessian）**：$f: \mathbb{R}^n \to \mathbb{R}$ 的二阶导数矩阵：
>
> $$H = \nabla^2 f = \begin{bmatrix} \frac{\partial^2 f}{\partial x_1^2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial^2 f}{\partial x_n \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_n^2} \end{bmatrix}$$

$H$ 是对称矩阵（若 $f$ 的二阶混合偏导连续）。

**常见 Hessian**：

| $f(\mathbf{x})$ | $\nabla^2 f$ |
|-----------------|-------------|
| $\mathbf{x}^T \mathbf{x}$ | $2I$ |
| $\mathbf{x}^T A \mathbf{x}$（$A$ 对称） | $2A$ |
| $\mathbf{x}^T A \mathbf{x}$（$A$ 一般） | $A + A^T$ |
| $\|A\mathbf{x} - \mathbf{b}\|^2$ | $2A^T A$ |
| $-\log(\mathbf{a}^T \mathbf{x})$ | $\frac{\mathbf{a}\mathbf{a}^T}{(\mathbf{a}^T \mathbf{x})^2}$ |

**Hessian 的正定性**决定 $f$ 在该点的曲率：正定 $\to$ 局部极小，负定 $\to$ 局部极大，不定 $\to$ 鞍点。

---

## 5. 标量对矩阵的导数

> **定义 4（矩阵梯度）**：$f: \mathbb{R}^{m \times n} \to \mathbb{R}$ 的梯度是同形状矩阵：
>
> $$\nabla_X f = \begin{bmatrix} \frac{\partial f}{\partial x_{11}} & \cdots & \frac{\partial f}{\partial x_{1n}} \\ \vdots & \ddots & \vdots \\ \frac{\partial f}{\partial x_{m1}} & \cdots & \frac{\partial f}{\partial x_{mn}} \end{bmatrix}$$

**关键公式**（记牢！）：

| $f(X)$ | $\nabla_X f$ | 常用场景 |
|--------|-------------|----------|
| $\mathbf{a}^T X \mathbf{b}$ | $\mathbf{a} \mathbf{b}^T$ | 线性 |
| $\operatorname{tr}(X)$ | $I$ | 迹 |
| $\operatorname{tr}(AX)$ | $A^T$ | 迹-积 |
| $\operatorname{tr}(X^T A X)$ | $(A + A^T) X$ | 二次型 |
| $\operatorname{tr}(X^{-1} A)$ | $-X^{-T} A^T X^{-T}$ | 逆 |
| $\log \det X$ | $X^{-T}$ | 行列式对数 |
| $\|AX - B\|_F^2$ | $2A^T(AX - B)$ | 最小二乘 |

**推导方法—迹技巧 (trace trick)**：

矩阵求导的核心工具链：
1. **迹的循环不变性**：$\operatorname{tr}(AB) = \operatorname{tr}(BA)$（即使 $AB \neq BA$）
2. **微分的迹形式**：$d(\operatorname{tr} X) = \operatorname{tr}(dX)$
3. **提取梯度**：将全微分整理为 $df = \operatorname{tr}(G^T dX)$ 形式，则 $\nabla_X f = G$

**例 1**：$f(X) = \operatorname{tr}(X^T A X)$。
$$\begin{aligned} df &= \operatorname{tr}(dX^T A X + X^T A dX) \\ &= \operatorname{tr}(X^T A^T dX + X^T A dX) \quad (\text{因 } \operatorname{tr}(dX^T A X) = \operatorname{tr}(X^T A^T dX)) \\ &= \operatorname{tr}((A^T X + A X)^T dX) \end{aligned}$$
所以 $\nabla_X f = (A + A^T) X$。（若 $A$ 对称，则为 $2AX$。）

**例 2**：$f(X) = \|AX - B\|_F^2$（最小二乘的矩阵形式）。
$$\begin{aligned} f &= \operatorname{tr}((AX - B)^T(AX - B)) \\ df &= \operatorname{tr}((A dX)^T(AX - B) + (AX - B)^T A dX) \\ &= 2\operatorname{tr}((AX - B)^T A dX) = \operatorname{tr}((2A^T(AX - B))^T dX) \end{aligned}$$
所以 $\nabla_X f = 2A^T(AX - B)$。

**例 3**：$f(X) = \log \det X$（$X$ 正定）。
利用 Jacobi 公式 $d(\det X) = \det X \cdot \operatorname{tr}(X^{-1} dX)$：
$$d(\log \det X) = \frac{d(\det X)}{\det X} = \operatorname{tr}(X^{-1} dX) = \operatorname{tr}((X^{-T})^T dX)$$
所以 $\nabla_X f = X^{-T}$。

---

## 6. 矩阵对矩阵的导数

一般 $\frac{\partial F(X)}{\partial X}$ 是四维张量。但多数应用只涉及标量对矩阵（上面的形式）。

若 $F(X) = AXB$，则 $\frac{\partial F}{\partial X}$ 可用 Kronecker 积表示：$B^T \otimes A$。实用中通常不直接展开，而是通过向量化和链式法则处理。

---

## 7. 在机器学习中的应用

### 7.1 线性回归

$L(\mathbf{w}) = \frac{1}{2}\|X\mathbf{w} - \mathbf{y}\|^2$

$\nabla_\mathbf{w} L = X^T(X\mathbf{w} - \mathbf{y})$

正规方程：$X^T X \mathbf{w} = X^T \mathbf{y}$

### 7.2 Logistic 回归

$L(\mathbf{w}) = \sum_i [\log(1 + e^{\mathbf{x}_i^T \mathbf{w}}) - y_i \mathbf{x}_i^T \mathbf{w}]$

$\nabla_\mathbf{w} L = X^T(\sigma(X\mathbf{w}) - \mathbf{y})$

### 7.3 神经网络

反向传播 = 链式法则在计算图上的系统应用。每层的梯度由 Jacobian 矩阵乘积给出。

---

## 8. 导数/梯度速查表

### 8.1 向量运算

| 表达式 | 导数/梯度 |
|--------|----------|
| $\frac{\partial}{\partial \mathbf{x}} (\mathbf{a}^T \mathbf{x})$ | $\mathbf{a}$ |
| $\frac{\partial}{\partial \mathbf{x}} (\|\mathbf{x}\|^2)$ | $2\mathbf{x}$ |
| $\frac{\partial}{\partial \mathbf{x}} (\mathbf{x}^T A \mathbf{x})$ | $(A + A^T)\mathbf{x}$ |
| $\frac{\partial}{\partial \mathbf{x}} (\|A\mathbf{x} - \mathbf{b}\|^2)$ | $2A^T(A\mathbf{x} - \mathbf{b})$ |
| $\frac{\partial}{\partial \mathbf{x}} f(A\mathbf{x} + \mathbf{b})$ | $A^T \nabla f$ |
| $\frac{\partial}{\partial \mathbf{x}} (\mathbf{x}^T \mathbf{a} \mathbf{a}^T \mathbf{x})$ | $2\mathbf{a}\mathbf{a}^T \mathbf{x}$ |

### 8.2 矩阵运算

| 表达式 | 梯度 |
|--------|------|
| $\frac{\partial}{\partial X} \operatorname{tr}(AX)$ | $A^T$ |
| $\frac{\partial}{\partial X} \operatorname{tr}(X A X^T)$ | $X(A + A^T)$ |
| $\frac{\partial}{\partial X} \operatorname{tr}(A X^{-1})$ | $-(X^{-1} A X^{-1})^T$ |
| $\frac{\partial}{\partial X} \det X$ | $\det(X) X^{-T}$ |
| $\frac{\partial}{\partial X} \log \det X$ | $X^{-T}$ |
| $\frac{\partial}{\partial X} \|X\|_F^2$ | $2X$ |

---

## 9. 例题

### 例 1：求梯度

求 $\nabla_\mathbf{x} (\mathbf{x}^T A \mathbf{x} + \mathbf{b}^T \mathbf{x})$（$A$ 对称）。

<details><summary>解</summary>

第一项：$\nabla(\mathbf{x}^T A \mathbf{x}) = 2A\mathbf{x}$（$A$ 对称）。
第二项：$\nabla(\mathbf{b}^T \mathbf{x}) = \mathbf{b}$。

$$\nabla = 2A\mathbf{x} + \mathbf{b}$$

</details>

### 例 2：链式法则

求 $\nabla_\mathbf{w} \|\sigma(X\mathbf{w}) - \mathbf{y}\|^2$，其中 $\sigma$ 是逐元素 sigmoid。

<details><summary>解</summary>

令 $\mathbf{z} = X\mathbf{w}$, $\mathbf{a} = \sigma(\mathbf{z})$, $L = \|\mathbf{a} - \mathbf{y}\|^2$。

$\frac{\partial L}{\partial \mathbf{a}} = 2(\mathbf{a} - \mathbf{y})^T$

$\frac{\partial \mathbf{a}}{\partial \mathbf{z}} = \operatorname{diag}(\sigma'(\mathbf{z})) = \operatorname{diag}(\mathbf{a} \odot (1 - \mathbf{a}))$

$\frac{\partial \mathbf{z}}{\partial \mathbf{w}} = X$

$$\nabla_\mathbf{w} L = X^T \operatorname{diag}(\mathbf{a} \odot (1 - \mathbf{a})) \cdot 2(\mathbf{a} - \mathbf{y}) = 2X^T [\mathbf{a} \odot (1 - \mathbf{a}) \odot (\mathbf{a} - \mathbf{y})]$$

</details>

---

## 10. 常见误区

| 误区 | 正确理解 |
|------|----------|
| 「梯度就是导数」 | 梯度是导数的多变量推广；对单变量 $f'(x)$，梯度 $\nabla f(x) = f'(x)$ |
| 「$\nabla (\mathbf{x}^T A \mathbf{x}) = 2A\mathbf{x}$ 总成立」 | 仅当 $A$ 对称！一般 = $(A + A^T)\mathbf{x}$ |
| 「Hessian 总是对称的」 | 若 $f$ 二阶连续可导则对；否则可能不对称 |
| 「对标量求导和布局无所谓」 | 分母布局（列向量梯度）vs 分子布局（行向量梯度）不可混用 |
| 「矩阵求导可以用标量规则」 | 需注意行列对应关系和迹技巧 |

---

## 本章核心概念速查

| 概念 | 定义 | 一句话 |
|------|------|--------|
| 梯度 | $\nabla_\mathbf{x} f$ | 增长最快的方向 |
| Jacobian | $\partial \mathbf{f} / \partial \mathbf{x}$ | 多输出函数的「导数」 |
| Hessian | $\nabla^2 f$ | 二阶曲率 |
| 矩阵梯度 | $\nabla_X f$ | 标量对矩阵各分量的偏导 |
| 全微分 | $df = \operatorname{tr}(G^T dX)$ | 矩阵求导的核心技巧 |
| 链式法则 | $\frac{\partial \mathbf{h}}{\partial \mathbf{x}} = \frac{\partial \mathbf{h}}{\partial \mathbf{g}} \frac{\partial \mathbf{g}}{\partial \mathbf{x}}$ | 逐层传播 |
| 迹技巧 | $\operatorname{tr}(AB) = \operatorname{tr}(BA) \implies df = \operatorname{tr}(G^T dX)$ | 矩阵求导三步：展开→交换迹→提取梯度 |

---

← 前置: [09 — 奇异值分解 SVD](../09-奇异值分解SVD/notes.md)
→ 延伸: 微积分/凸优化后续课程
