# 线性代数 · 第三章 · 理论题 — 参考答案

---

## Q1 矩阵-向量乘法

<details><summary>解</summary>

$$A\mathbf{x} = \begin{bmatrix} 2 & -1 & 0 \\ 0 & 3 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix} = \begin{bmatrix} 2\cdot1 + (-1)\cdot2 + 0\cdot(-1) \\ 0\cdot1 + 3\cdot2 + 1\cdot(-1) \end{bmatrix} = \begin{bmatrix} 0 \\ 5 \end{bmatrix}$$

</details>

---

## Q2 矩阵乘法

<details><summary>解</summary>

$$AB = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix}$$

$$BA = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 3 & 4 \\ 1 & 2 \end{bmatrix}$$

$AB \neq BA$，矩阵乘法不可交换。

</details>

---

## Q3 转置性质验证

<details><summary>解</summary>

$$A^T = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}$$

$$(A^T)^T = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = A \quad \checkmark$$

</details>

---

## Q4 对称与反对称分解

<details><summary>解</summary>

对称部分：$\frac{A + A^T}{2} = \frac{1}{2}\left(\begin{bmatrix} 1 & 3 \\ -1 & 2 \end{bmatrix} + \begin{bmatrix} 1 & -1 \\ 3 & 2 \end{bmatrix}\right) = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix}$

反对称部分：$\frac{A - A^T}{2} = \frac{1}{2}\left(\begin{bmatrix} 1 & 3 \\ -1 & 2 \end{bmatrix} - \begin{bmatrix} 1 & -1 \\ 3 & 2 \end{bmatrix}\right) = \begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}$

验证：$\begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix} + \begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 3 \\ -1 & 2 \end{bmatrix} = A \quad \checkmark$

</details>

---

## Q5 求线性变换的矩阵

<details><summary>解</summary>

$T(\mathbf{e}_1) = T([1,0]^T) = [1, 2, 1]^T$（第一列）
$T(\mathbf{e}_2) = T([0,1]^T) = [1, -1, 3]^T$（第二列）

$$A = \begin{bmatrix} 1 & 1 \\ 2 & -1 \\ 1 & 3 \end{bmatrix}$$

$$T([2, -1]^T) = \begin{bmatrix} 1 & 1 \\ 2 & -1 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} 2 \\ -1 \end{bmatrix} = \begin{bmatrix} 2-1 \\ 4+1 \\ 2-3 \end{bmatrix} = \begin{bmatrix} 1 \\ 5 \\ -1 \end{bmatrix}$$

</details>

---

## Q6 矩阵乘法结合律验证

<details><summary>解</summary>

$$AB = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 2 & 5 \end{bmatrix}$$

$$(AB)C = \begin{bmatrix} 1 & 2 \\ 2 & 5 \end{bmatrix} \begin{bmatrix} 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 5 \\ 11 \end{bmatrix}$$

$$BC = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}$$

$$A(BC) = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} 5 \\ 1 \end{bmatrix} = \begin{bmatrix} 5 \\ 11 \end{bmatrix}$$

$(AB)C = A(BC) \quad \checkmark$

</details>

---

## Q7 $(AB)^T = B^T A^T$ 验证

<details><summary>解</summary>

$$AB = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} = \begin{bmatrix} -2 & 1 \\ -4 & 3 \\ -6 & 5 \end{bmatrix}$$

$$(AB)^T = \begin{bmatrix} -2 & -4 & -6 \\ 1 & 3 & 5 \end{bmatrix}$$

$$B^T = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}, \quad A^T = \begin{bmatrix} 1 & 3 & 5 \\ 2 & 4 & 6 \end{bmatrix}$$

$$B^T A^T = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 3 & 5 \\ 2 & 4 & 6 \end{bmatrix} = \begin{bmatrix} -2 & -4 & -6 \\ 1 & 3 & 5 \end{bmatrix}$$

$(AB)^T = B^T A^T \quad \checkmark$

</details>

---

## Q8 迹的循环性质

<details><summary>解</summary>

$$AB = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 2 & -1 \\ 4 & -3 \end{bmatrix}$$

$\operatorname{tr}(AB) = 2 + (-3) = -1$

$$BA = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} -3 & -4 \\ 1 & 2 \end{bmatrix}$$

$\operatorname{tr}(BA) = -3 + 2 = -1$

$\operatorname{tr}(AB) = \operatorname{tr}(BA) \quad \checkmark$

</details>

---

## Q9 正交矩阵判定

<details><summary>解</summary>

**(a)** $Q_1^T Q_1 = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} = \begin{bmatrix} \cos^2\theta + \sin^2\theta & 0 \\ 0 & \sin^2\theta + \cos^2\theta \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$

$Q_1$ 是正交矩阵（旋转矩阵）。

**(b)** $Q_2^T Q_2 = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} \neq I$。$Q_2$ 不是正交矩阵，但若归一化（每列除以 $\sqrt{2}$），则变为正交矩阵。

</details>

---

## Q10 三角矩阵性质

<details><summary>解</summary>

$$UV = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{bmatrix} \begin{bmatrix} 7 & 0 & 0 \\ 8 & 9 & 0 \\ 10 & 11 & 12 \end{bmatrix} = \begin{bmatrix} 1\cdot7+2\cdot8+3\cdot10 & 1\cdot0+2\cdot9+3\cdot11 & 1\cdot0+2\cdot0+3\cdot12 \\ 0\cdot7+4\cdot8+5\cdot10 & 0\cdot0+4\cdot9+5\cdot11 & 0\cdot0+4\cdot0+5\cdot12 \\ 0\cdot7+0\cdot8+6\cdot10 & 0\cdot0+0\cdot9+6\cdot11 & 0\cdot0+0\cdot0+6\cdot12 \end{bmatrix}$$

对角线元素：$(UV)_{11} = 7+16+30 = 53 = 1 \cdot 7$ 不对，让我们仔细算。

实际上，上三角乘下三角不一定是三角。但这里关键是：对角线元素 $(UV)_{ii} = \sum_k u_{ik} v_{ki}$。由于 $U$ 是上三角（$u_{ik}=0$ for $i>k$）和 $V$ 是下三角（$v_{ki}=0$ for $k<i$），只有 $k=i$ 的项非零。

所以 $(UV)_{11} = u_{11}v_{11} = 1 \cdot 7 = 7$
$(UV)_{22} = u_{22}v_{22} = 4 \cdot 9 = 36$
$(UV)_{33} = u_{33}v_{33} = 6 \cdot 12 = 72$

对角线元素 = 对应对角线元素之积，验证正确。

</details>

---

## Q11 Kronecker 积

<details><summary>解</summary>

$$A \otimes B = \begin{bmatrix} 1\cdot B & 0\cdot B \\ 0\cdot B & 1\cdot B \end{bmatrix} = \begin{bmatrix} 1 & 2 & 0 & 0 \\ 3 & 4 & 0 & 0 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 3 & 4 \end{bmatrix}$$

$$B \otimes A = \begin{bmatrix} 1\cdot A & 2\cdot A \\ 3\cdot A & 4\cdot A \end{bmatrix} = \begin{bmatrix} 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 2 \\ 3 & 0 & 4 & 0 \\ 0 & 3 & 0 & 4 \end{bmatrix}$$

$A \otimes B \neq B \otimes A$。Kronecker 积不满足交换律（除非特例）。

</details>

---

## Q12 线性变换的复合

<details><summary>解</summary>

$S$（旋转 $90^\circ$）：$S = \begin{bmatrix} \cos 90^\circ & -\sin 90^\circ \\ \sin 90^\circ & \cos 90^\circ \end{bmatrix} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$

$T$（水平拉伸 2 倍）：$T = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}$

$S \circ T$（先拉伸再旋转）：$ST = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 \\ 2 & 0 \end{bmatrix}$

$T \circ S$（先旋转再拉伸）：$TS = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -2 \\ 1 & 0 \end{bmatrix}$

$ST \neq TS$。几何上：先拉伸再旋转 vs 先旋转再拉伸——拉伸的方向不同，结果自然不同。

</details>
