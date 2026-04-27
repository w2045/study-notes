# 线性代数 · 第八章 · 理论题 — 参考答案

---

## Q1 判断正定性

<details><summary>解</summary>

**(a)** $A$ 特征值 $3, 1 > 0$，**正定**。

**(b)** $B$ 特征值：$p(\lambda) = (2-\lambda)^2 - 9 = \lambda^2 - 4\lambda - 5 = (\lambda-5)(\lambda+1) = 0$，$\lambda_1 = 5, \lambda_2 = -1$。有负特征值，**不正定**（不定矩阵）。

</details>

---

## Q2 Sylvester 判据

<details><summary>解</summary>

$\det A_1 = 4 > 0$。$\det A_2 = 4 \cdot 1 - 1 \cdot 1 = 3 > 0$。所有前主子式 $> 0$，$A$ **正定**。

</details>

---

## Q3 正交投影（到直线）

<details><summary>解</summary>

$\mathbf{p} = \frac{\mathbf{b} \cdot \mathbf{a}}{\mathbf{a} \cdot \mathbf{a}} \mathbf{a} = \frac{3 \cdot 1 + 4 \cdot 0}{1} [1, 0]^T = [3, 0]^T$

</details>

---

## Q4 Cholesky 分解 (2x2)

<details><summary>解</summary>

正定性：$\det A_1 = 9 > 0$, $\det A_2 = 18 - 9 = 9 > 0$。正定。

Cholesky：
- $\ell_{11} = \sqrt{9} = 3$
- $\ell_{21} = 3/3 = 1$
- $\ell_{22} = \sqrt{2 - 1^2} = 1$

$$L = \begin{bmatrix} 3 & 0 \\ 1 & 1 \end{bmatrix}$$

验证：$LL^T = \begin{bmatrix}3&0\\1&1\end{bmatrix}\begin{bmatrix}3&1\\0&1\end{bmatrix} = \begin{bmatrix}9&3\\3&2\end{bmatrix}$ ✓

</details>

---

## Q5 二次型展开

<details><summary>解</summary>

$$Q(x_1, x_2) = 2x_1^2 + 4x_1x_2 + 3x_2^2 = \begin{bmatrix}x_1&x_2\end{bmatrix} \begin{bmatrix}2&2\\2&3\end{bmatrix} \begin{bmatrix}x_1\\x_2\end{bmatrix}$$

所以 $A = \begin{bmatrix}2&2\\2&3\end{bmatrix}$。注意 $x_1x_2$ 系数对半分入 $a_{12}$ 和 $a_{21}$。

正定性：$\det A_1 = 2 > 0$, $\det A_2 = 6 - 4 = 2 > 0$。正定。

</details>

---

## Q6 最小二乘

<details><summary>解</summary>

正规方程：$A^T A \mathbf{x} = A^T \mathbf{b}$。

$A^T A = \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix} = \begin{bmatrix}1&0\\0&1\end{bmatrix}$

$A^T \mathbf{b} = \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}\begin{bmatrix}2\\3\\4\end{bmatrix} = \begin{bmatrix}2\\3\end{bmatrix}$

解：$\mathbf{\hat{x}} = \begin{bmatrix}2\\3\end{bmatrix}$。几何上，$\mathbf{b}$ 的前两个分量被保留，第三个分量被忽略（$A$ 的列空间是前两个坐标面）。

</details>

---

## Q7 投影矩阵性质

<details><summary>解</summary>

$P^2 = \begin{bmatrix}1&0\\0&0\end{bmatrix}\begin{bmatrix}1&0\\0&0\end{bmatrix} = \begin{bmatrix}1&0\\0&0\end{bmatrix} = P$ ✓

$P^T = P$ ✓

$P$ 投影到 $x$ 轴（$\operatorname{span}\{[1,0]^T\}$）。$P[x,y]^T = [x,0]^T$——只保留 $x$ 分量。

</details>

---

## Q8 QR 分解 (2x2)

<details><summary>解</summary>

$\mathbf{a}_1 = [3, 4]^T$, $\|\mathbf{a}_1\| = 5$, $\mathbf{q}_1 = [0.6, 0.8]^T$。

$r_{12} = \mathbf{q}_1^T \mathbf{a}_2 = 0.6 \cdot 0 + 0.8 \cdot 5 = 4$。

$\mathbf{u}_2 = \mathbf{a}_2 - r_{12}\mathbf{q}_1 = [0, 5]^T - 4[0.6, 0.8]^T = [-2.4, 1.8]^T$。

$\|\mathbf{u}_2\| = \sqrt{5.76 + 3.24} = 3$, $\mathbf{q}_2 = [-0.8, 0.6]^T$。

$$Q = \begin{bmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{bmatrix}, \quad R = \begin{bmatrix} 5 & 4 \\ 0 & 3 \end{bmatrix}$$

验证：$QR = \begin{bmatrix}0.6&-0.8\\0.8&0.6\end{bmatrix}\begin{bmatrix}5&4\\0&3\end{bmatrix} = \begin{bmatrix}3&0\\4&5\end{bmatrix}$ ✓

</details>

---

## Q9 Cholesky (3x3)

<details><summary>解</summary>

正定性：前主子式 $\det A_1 = 4$, $\det A_2 = 20-4=16$, $\det A_3$：按第一行展开...
或直接 Cholesky 试算成功即正定。

$\ell_{11} = \sqrt{4} = 2$

$\ell_{21} = 2/2 = 1$, $\ell_{22} = \sqrt{5 - 1} = 2$

$\ell_{31} = 2/2 = 1$, $\ell_{32} = (1 - 1\cdot 1)/2 = 0$, $\ell_{33} = \sqrt{6 - 1^2 - 0^2} = \sqrt{5}$

$$L = \begin{bmatrix} 2 & 0 & 0 \\ 1 & 2 & 0 \\ 1 & 0 & \sqrt{5} \end{bmatrix}$$

验证：$LL^T$ 应等于 $A$。

</details>

---

## Q10 用 QR 解最小二乘

<details><summary>解</summary>

$A$ 的 QR（Gram-Schmidt）：

$\mathbf{a}_1 = [1,1,1]^T$, $\|\mathbf{a}_1\| = \sqrt{3}$, $\mathbf{q}_1 = \frac{1}{\sqrt{3}}[1,1,1]^T$。

$r_{11} = \sqrt{3}$。

$\mathbf{a}_2 = [1,2,3]^T$。$r_{12} = \mathbf{q}_1^T \mathbf{a}_2 = \frac{1}{\sqrt{3}}(1+2+3) = \frac{6}{\sqrt{3}} = 2\sqrt{3}$。

$\mathbf{u}_2 = \mathbf{a}_2 - r_{12}\mathbf{q}_1 = [1,2,3]^T - 2[1,1,1]^T = [-1, 0, 1]^T$。

$\|\mathbf{u}_2\| = \sqrt{2}$, $\mathbf{q}_2 = \frac{1}{\sqrt{2}}[-1, 0, 1]^T$, $r_{22} = \sqrt{2}$。

$Q = \begin{bmatrix}1/\sqrt{3} & -1/\sqrt{2} \\ 1/\sqrt{3} & 0 \\ 1/\sqrt{3} & 1/\sqrt{2}\end{bmatrix}$, $R = \begin{bmatrix}\sqrt{3} & 2\sqrt{3} \\ 0 & \sqrt{2}\end{bmatrix}$

$Q^T\mathbf{b} = \begin{bmatrix} (1+2+2)/\sqrt{3} \\ (-1+0+2)/\sqrt{2} \end{bmatrix} = \begin{bmatrix} 5/\sqrt{3} \\ 1/\sqrt{2} \end{bmatrix}$

回代 $R\mathbf{x} = Q^T\mathbf{b}$：

$\sqrt{2} x_2 = 1/\sqrt{2} \implies x_2 = 1/2$

$\sqrt{3} x_1 + 2\sqrt{3}(1/2) = 5/\sqrt{3} \implies x_1 + 1 = 5/3 \implies x_1 = 2/3$

$\mathbf{\hat{x}} = [2/3, 1/2]^T$。

</details>

---

## Q11 正定性与特征值

<details><summary>解</summary>

若 $A$ 正定，则所有特征值 $\lambda_i > 0$。$A^{-1}$ 的特征值为 $1/\lambda_i$（相同特征向量），全部为正。对称性：$(A^{-1})^T = (A^T)^{-1} = A^{-1}$。故 $A^{-1}$ 正定。证毕

</details>

---

## Q12 投影到平面

<details><summary>解</summary>

$$A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}, \quad A^T A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$

$$(A^T A)^{-1} = \frac{1}{3}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$$

$P = A(A^T A)^{-1}A^T = \frac{1}{3}A\begin{bmatrix}2&-1\\-1&2\end{bmatrix}A^T$

$\mathbf{p} = P\mathbf{b} = \frac{1}{3}\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}\begin{bmatrix}2&-1\\-1&2\end{bmatrix}\begin{bmatrix}1&0&1\\0&1&1\end{bmatrix}\begin{bmatrix}6\\0\\0\end{bmatrix}$

先算 $A^T\mathbf{b} = \begin{bmatrix}6\\0\end{bmatrix}$（或直接计算）。

$\mathbf{\hat{x}} = (A^T A)^{-1}A^T\mathbf{b} = \frac{1}{3}\begin{bmatrix}2&-1\\-1&2\end{bmatrix}\begin{bmatrix}6\\0\end{bmatrix} = \begin{bmatrix}4\\-2\end{bmatrix}$

$\mathbf{p} = A\mathbf{\hat{x}} = \begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}\begin{bmatrix}4\\-2\end{bmatrix} = \begin{bmatrix}4\\-2\\2\end{bmatrix}$

验证：$\mathbf{b} - \mathbf{p} = [2, 2, -2]^T$。对 $A$ 的每一列做内积：$[2,2,-2]^T \cdot [1,0,1]^T = 2+0-2=0$，$[2,2,-2]^T \cdot [0,1,1]^T = 0+2-2=0$。残差与列空间正交 ✓。

</details>
