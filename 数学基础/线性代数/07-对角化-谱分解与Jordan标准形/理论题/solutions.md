# 线性代数 · 第七章 · 理论题 — 参考答案

---

## Q1 判断可正交对角化

<details><summary>解</summary>

**(a)** $A = A^T$，实对称矩阵，**可正交对角化**。特征值 $\lambda_1 = -1$, $\lambda_2 = 3$，对应标准正交特征向量。

**(b)** $B \neq B^T$，非对称。特征值 $\lambda = 1$（二重），几何重数 = 1 < 2。**不可正交对角化**（甚至不可对角化）。

**(c)** $C = C^T = 3I$，**可正交对角化**（实质上已是对角矩阵，任意正交矩阵都行）。

</details>

---

## Q2 Rayleigh 商计算

<details><summary>解</summary>

$$R(A, \mathbf{x}) = \frac{\begin{bmatrix}2&1\end{bmatrix}\begin{bmatrix}4&0\\0&1\end{bmatrix}\begin{bmatrix}2\\1\end{bmatrix}}{\begin{bmatrix}2&1\end{bmatrix}\begin{bmatrix}2\\1\end{bmatrix}} = \frac{8 + 1}{4 + 1} = \frac{9}{5} = 1.8$$

$\lambda_{\min} = 1$, $\lambda_{\max} = 4$，$1 \leq 1.8 \leq 4$ ✓。

</details>

---

## Q3 谱分解基础

<details><summary>解</summary>

特征值 $\lambda_1 = 3$（特征向量 $\mathbf{q}_1 = [1,0]^T$），$\lambda_2 = 2$（特征向量 $\mathbf{q}_2 = [0,1]^T$）。

$$P_1 = \mathbf{q}_1\mathbf{q}_1^T = \begin{bmatrix}1&0\\0&0\end{bmatrix}, \quad P_2 = \mathbf{q}_2\mathbf{q}_2^T = \begin{bmatrix}0&0\\0&1\end{bmatrix}$$

$A = 3P_1 + 2P_2 = \begin{bmatrix}3&0\\0&2\end{bmatrix}$ ✓

$P_1 + P_2 = \begin{bmatrix}1&0\\0&1\end{bmatrix} = I$ ✓

$P_1 P_2 = \begin{bmatrix}0&0\\0&0\end{bmatrix} = 0$ ✓

</details>

---

## Q4 Schur 分解实例

<details><summary>解</summary>

$U = I$（单位矩阵），$T = A$。显然 $A = I \cdot A \cdot I^*$ 是 Schur 分解。

$U = I$ 是酉矩阵（$U^* U = I$），且 $T$ 是上三角矩阵。

</details>

---

## Q5 谱定理应用：求 $A^5$

<details><summary>解</summary>

$A$ 的特征值 $\lambda_1 = 1$, $\lambda_2 = 3$。标准正交特征向量：

$\mathbf{q}_1 = \frac{1}{\sqrt{2}}[1,-1]^T$, $\mathbf{q}_2 = \frac{1}{\sqrt{2}}[1,1]^T$

$Q = \frac{1}{\sqrt{2}}\begin{bmatrix}1&1\\-1&1\end{bmatrix}$, $\Lambda = \begin{bmatrix}1&0\\0&3\end{bmatrix}$

$\Lambda^5 = \begin{bmatrix}1^5&0\\0&3^5\end{bmatrix} = \begin{bmatrix}1&0\\0&243\end{bmatrix}$

$$A^5 = Q\Lambda^5 Q^T = \frac{1}{\sqrt{2}}\begin{bmatrix}1&1\\-1&1\end{bmatrix} \begin{bmatrix}1&0\\0&243\end{bmatrix} \frac{1}{\sqrt{2}}\begin{bmatrix}1&-1\\1&1\end{bmatrix}$$

$= \frac{1}{2}\begin{bmatrix}1+243 & -1+243 \\ -1+243 & 1+243\end{bmatrix} = \begin{bmatrix}122 & 121 \\ 121 & 122\end{bmatrix}$

</details>

---

## Q6 Jordan 块与 Jordan 标准形

<details><summary>解</summary>

**(a)** $A$ 已经是 $J_2(2)$——一个 $2 \times 2$ Jordan 块，特征值 2。

**(b)** $B = 2I$，已是对角矩阵，Jordan 型 = $B$ 本身。两个 $1\times 1$ Jordan 块 $J_1(2)$。

**(c)** $C = \begin{bmatrix} J_2(2) & 0 \\ 0 & J_1(3) \end{bmatrix}$。$J = \begin{bmatrix}2&1&0\\0&2&0\\0&0&3\end{bmatrix}$ 就是 Jordan 标准形。

</details>

---

## Q7 Jordan 链

<details><summary>解</summary>

$A = J_3(1)$，特征值 $\lambda = 1$（三重）。

- $\mathbf{v}_1$：$(A-I)\mathbf{v}_1 = \mathbf{0} \implies \begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}\mathbf{v}_1 = \mathbf{0} \implies \mathbf{v}_1 = [1, 0, 0]^T$

- $\mathbf{v}_2$：$(A-I)\mathbf{v}_2 = \mathbf{v}_1 \implies \mathbf{v}_2 = [0, 1, 0]^T$

- $\mathbf{v}_3$：$(A-I)\mathbf{v}_3 = \mathbf{v}_2 \implies \mathbf{v}_3 = [0, 0, 1]^T$

$P = \begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix} = I$, $J = A = J_3(1)$。

$A = I J I^{-1}$ 即 $A = J$。

</details>

---

## Q8 Rayleigh 商的极值性质

<details><summary>解</summary>

对 Hermitian $A$，由谱定理 $A = Q\Lambda Q^*$。令 $\mathbf{y} = Q^*\mathbf{x}$，则：

$$R(A, \mathbf{x}) = \frac{\mathbf{x}^*A\mathbf{x}}{\mathbf{x}^*\mathbf{x}} = \frac{\mathbf{y}^*\Lambda\mathbf{y}}{\mathbf{y}^*\mathbf{y}} = \frac{\sum \lambda_i |y_i|^2}{\sum |y_i|^2}$$

这是 $\lambda_i$ 的加权平均，因此 $\lambda_{\min} \leq R \leq \lambda_{\max}$。

取 $\mathbf{x}$ 为最小特征向量时 $R = \lambda_{\min}$；为最大特征向量时 $R = \lambda_{\max}$。

</details>

---

## Q9 谱分解与正交投影

<details><summary>解</summary>

$A$ 特征值 $\lambda_1 = 2$, $\lambda_2 = 4$。

标准正交特征向量：$\mathbf{q}_1 = \frac{1}{\sqrt{2}}[1, -1]^T$, $\mathbf{q}_2 = \frac{1}{\sqrt{2}}[1, 1]^T$。

$$P_1 = \frac{1}{2}\begin{bmatrix}1&-1\\-1&1\end{bmatrix}, \quad P_2 = \frac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix}$$

**几何含义**：$P_1$ 将任意向量投影到直线 $y = -x$ 上；$P_2$ 投影到直线 $y = x$ 上。两者正交且互补（$P_1 + P_2 = I$）。

$A$ 在原坐标系中先在 $y = -x$ 方向缩放 2，在 $y = x$ 方向缩放 4，再合成。

</details>

---

## Q10 判断可对角化的多种条件

<details><summary>解</summary>

**(a)** $p(\lambda) = \det\begin{bmatrix}-\lambda&1\\0&-\lambda\end{bmatrix} = \lambda^2$，$\lambda = 0$（二重）。

特征向量：$(A - 0I)\mathbf{v} = \begin{bmatrix}0&1\\0&0\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v} = [c, 0]^T$。只有 $[1, 0]^T$ 方向。

**(b)** 代数重数 = 2，几何重数 = 1。

**(c)** 几何重数 < 代数重数 $ \implies $ **不可对角化**。Jordan 标准形 = $J_2(0) = \begin{bmatrix}0&1\\0&0\end{bmatrix}$，$A$ 本身已为此形式。

</details>

---

## Q11 用 Jordan 型计算矩阵指数

<details><summary>解</summary>

$A = J_2(1)$。对 Jordan 块 $J_k(\lambda)$：

$$e^{J_2(1)} = e^1 \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} e & e \\ 0 & e \end{bmatrix}$$

验证：直接算 $e^A = I + A + \frac{A^2}{2!} + \cdots$：
$A^2 = \begin{bmatrix}1&2\\0&1\end{bmatrix}$, $A^3 = \begin{bmatrix}1&3\\0&1\end{bmatrix}$, $\ldots$

$e^A = \begin{bmatrix}\sum\frac{1}{n!} & \sum\frac{n}{n!}\\0 & \sum\frac{1}{n!}\end{bmatrix} = \begin{bmatrix}e & e\\0 & e\end{bmatrix}$ ✓

</details>

---

## Q12 Courant-Fischer 极小极大原理

<details><summary>解</summary>

Courant-Fischer 定理：
$$\lambda_k = \min_{\dim V = k} \max_{\mathbf{x}\in V,\mathbf{x}\neq 0} R(A,\mathbf{x})$$

对 $\lambda_2$，在所有与 $\mathbf{v}_1$ 正交的向量上最大化 $R$。因为与第一特征向量正交的方向上，$\lambda_1$ 的权重为 0，Rayleigh 商的最大值就是 $\lambda_2$。

**例**：$A = \begin{bmatrix}2&0\\0&5\end{bmatrix}$, $\lambda_1=5$（$\mathbf{v}_1=[0,1]^T$），$\lambda_2=2$。

与 $\mathbf{v}_1$ 正交的空间 = $\{[x,0]^T\}$。在此空间中 $R(A,[x,0]^T) = \frac{2x^2}{x^2} = 2 = \lambda_2$。✓

</details>
