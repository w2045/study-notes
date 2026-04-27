# 线性代数 · 第十章 · 理论题 — 参考答案

---

## Q1 标量对向量求导

<details><summary>解</summary>

$f(\mathbf{x}) = a_1 x_1 + a_2 x_2 + a_3 x_3$。

$$\nabla_\mathbf{x} f = \begin{bmatrix} \partial f/\partial x_1 \\ \partial f/\partial x_2 \\ \partial f/\partial x_3 \end{bmatrix} = \begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix} = \begin{bmatrix} 2 \\ -1 \\ 3 \end{bmatrix} = \mathbf{a}$$

</details>

---

## Q2 范数平方的梯度

<details><summary>解</summary>

$f(\mathbf{x}) = x_1^2 + x_2^2$。$\frac{\partial f}{\partial x_i} = 2x_i$。

$$\nabla_\mathbf{x} \|\mathbf{x}\|^2 = 2\mathbf{x}$$

在 $\mathbf{x} = [3, 4]^T$ 处：$\nabla f = [6, 8]^T$。

</details>

---

## Q3 线性回归梯度

<details><summary>解</summary>

$f(\mathbf{w}) = (X\mathbf{w} - \mathbf{y})^T (X\mathbf{w} - \mathbf{y}) = \mathbf{w}^T X^T X \mathbf{w} - 2\mathbf{y}^T X \mathbf{w} + \mathbf{y}^T \mathbf{y}$

第一项：$\nabla(\mathbf{w}^T X^T X \mathbf{w}) = 2X^T X \mathbf{w}$（$X^T X$ 对称）

第二项：$\nabla(-2\mathbf{y}^T X \mathbf{w}) = -2X^T \mathbf{y}$

第三项：常数为 0。

$$\nabla_\mathbf{w} f = 2X^T X \mathbf{w} - 2X^T \mathbf{y} = 2X^T (X\mathbf{w} - \mathbf{y})$$

</details>

---

## Q4 Jacobian 基础

<details><summary>解</summary>

$\mathbf{f}(\mathbf{x}) = A\mathbf{x} = \begin{bmatrix} x_1 + 2x_2 \\ 3x_1 + 4x_2 \end{bmatrix}$

$$J = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = A$$

对于线性变换，Jacobian = 变换矩阵 $A$。

</details>

---

## Q5 二次型的梯度

<details><summary>解</summary>

$A$ 对称，$\nabla_\mathbf{x} (\mathbf{x}^T A \mathbf{x}) = 2A\mathbf{x}$。

$$2A\mathbf{x} = 2\begin{bmatrix}2&1\\1&3\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix} = 2\begin{bmatrix}3\\4\end{bmatrix} = \begin{bmatrix}6\\8\end{bmatrix}$$

展开验证：$f = 2x_1^2 + 2x_1x_2 + 3x_2^2$。$\frac{\partial f}{\partial x_1} = 4x_1 + 2x_2$, $\frac{\partial f}{\partial x_2} = 2x_1 + 6x_2$。在 $[1,1]^T$ 处：$[6, 8]^T$ ✓。

</details>

---

## Q6 Hessian 计算

<details><summary>解</summary>

$f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$，$\nabla f = (A + A^T)\mathbf{x}$。

若 $A$ 对称：$\nabla f = 2A\mathbf{x}$。

Hessian：对 $\nabla f$ 的每个分量再求导。$\frac{\partial}{\partial x_j} (2A\mathbf{x})_i = \frac{\partial}{\partial x_j} (2\sum_k a_{ik} x_k) = 2a_{ij}$。

$$\nabla^2 f = 2A$$

当 $A$ 是对称矩阵时 Hessian 恰好是 $2A$。一般 $A$ 不对称时 Hessian = $A + A^T$。

</details>

---

## Q7 标量对矩阵的导数

<details><summary>解</summary>

$f(X) = \operatorname{tr}(AX) = \sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik} x_{ki}$

$\frac{\partial f}{\partial x_{ij}} = a_{ji}$（仅当 $k=i$ 且 $i=j$ 时求和项包含 $x_{ij}$，即 $a_{ji}$）。

$$\nabla_X \operatorname{tr}(AX) = A^T$$

**迹技巧**：$df = \operatorname{tr}(A \, dX) = \operatorname{tr}((A^T)^T dX)$，所以 $\nabla_X f = A^T$。

</details>

---

## Q8 链式法则应用

<details><summary>解</summary>

$f(\mathbf{x}) = \|\mathbf{x}\|_2$，则 $\nabla_\mathbf{x} f = \frac{\mathbf{x}}{\|\mathbf{x}\|}$（当 $\mathbf{x} \neq \mathbf{0}$）。

$g(\mathbf{w}) = \mathbf{x}_0 + B\mathbf{w}$，则 $\frac{\partial g}{\partial \mathbf{w}} = B$（Jacobian）。

链式法则：$\nabla_\mathbf{w} h(\mathbf{w}) = \left(\frac{\partial g}{\partial \mathbf{w}}\right)^T \nabla_\mathbf{x} f = B^T \frac{g(\mathbf{w})}{\|g(\mathbf{w})\|}$

$$\nabla_\mathbf{w} \|\mathbf{x}_0 + B\mathbf{w}\| = B^T \frac{\mathbf{x}_0 + B\mathbf{w}}{\|\mathbf{x}_0 + B\mathbf{w}\|}$$

</details>

---

## Q9 $\log\det$ 的梯度

<details><summary>解</summary>

全微分：$d(\log \det X) = \operatorname{tr}(X^{-1} dX)$（标准结果）。

写为 $df = \operatorname{tr}((X^{-T})^T dX)$ 的形式，则 $\nabla_X f = X^{-T}$。

$$\nabla_X \log \det X = X^{-T} = (X^{-1})^T$$

当 $X$ 对称正定时，$X^{-T} = X^{-1}$。

</details>

---

## Q10 矩阵二次型的梯度

<details><summary>解</summary>

$f(X) = \operatorname{tr}(X^T A X)$。

全微分：$df = \operatorname{tr}(dX^T A X) + \operatorname{tr}(X^T A \, dX)$

第一项：$\operatorname{tr}(dX^T A X) = \operatorname{tr}((AX)^T dX) = \operatorname{tr}(X^T A^T dX)$

第二项：$\operatorname{tr}(X^T A \, dX)$

$df = \operatorname{tr}((X^T A^T + X^T A) dX) = \operatorname{tr}((A X + A^T X)^T dX)$

$$\nabla_X f = (A + A^T) X$$

若 $A$ 对称，$\nabla_X f = 2AX$。

</details>

---

## Q11 Logistic 回归梯度推导

<details><summary>解</summary>

考虑第 $i$ 项：$\ell_i = \log(1 + e^{z_i}) - y_i z_i$，其中 $z_i = \mathbf{x}_i^T \mathbf{w}$。

$\frac{\partial \ell_i}{\partial z_i} = \frac{e^{z_i}}{1+e^{z_i}} - y_i = \sigma(z_i) - y_i$

$\nabla_\mathbf{w} z_i = \mathbf{x}_i$（因为 $z_i = \mathbf{x}_i^T \mathbf{w}$ 是 $\mathbf{w}$ 的线性函数）

由链式法则：$\nabla_\mathbf{w} \ell_i = (\sigma(z_i) - y_i) \mathbf{x}_i$

对所有样本求和：
$$\nabla_\mathbf{w} L = \sum_{i=1}^{n} (\sigma(\mathbf{x}_i^T \mathbf{w}) - y_i) \mathbf{x}_i$$

矩阵形式：令 $\boldsymbol{\sigma} = [\sigma(z_1), \ldots, \sigma(z_n)]^T$，则：

$$\nabla_\mathbf{w} L = X^T (\boldsymbol{\sigma} - \mathbf{y})$$

</details>

---

## Q12 Frobenius 范数的梯度

<details><summary>解</summary>

$f(X) = \frac{1}{2}\|AX - B\|_F^2 = \frac{1}{2}\operatorname{tr}((AX - B)^T (AX - B))$

展开：$= \frac{1}{2}\operatorname{tr}(X^T A^T A X) - \operatorname{tr}(X^T A^T B) + \frac{1}{2}\operatorname{tr}(B^T B)$

第一项：$\nabla_X(\frac{1}{2}\operatorname{tr}(X^T A^T A X)) = \frac{1}{2}(A^T A + (A^T A)^T) X = A^T A X$

第二项：$\nabla_X(-\operatorname{tr}(X^T A^T B)) = -A^T B$

$$\nabla_X f = A^T A X - A^T B = A^T (A X - B)$$

**一阶条件**（令梯度为 0）：$A^T A X = A^T B$。

这就是最小二乘的正规方程！当 $A^T A$ 可逆时：$X = (A^T A)^{-1} A^T B$。

</details>
