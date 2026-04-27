# 线性代数 · 第五章 · 理论题 — 参考答案

---

## Q1 计算 2x2 行列式

<details><summary>解</summary>

(a) $\det = 3 \cdot 4 - 5 \cdot 2 = 12 - 10 = 2$

(b) $\det = (-1)(-6) - 2 \cdot 3 = 6 - 6 = 0$

(b) 中两列线性相关（第二列 = $-2$ 倍第一列），行列式自然为 0。

</details>

---

## Q2 2x2 逆矩阵

<details><summary>解</summary>

$\det A = 2 \cdot 2 - 3 \cdot 1 = 4 - 3 = 1$

$$A^{-1} = \frac{1}{1} \begin{bmatrix} 2 & -3 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 2 & -3 \\ -1 & 2 \end{bmatrix}$$

验证：
$$AA^{-1} = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 2 & -3 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 4-3 & -6+6 \\ 2-2 & -3+4 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$ ✓

</details>

---

## Q3 计算 3x3 行列式

<details><summary>解</summary>

上三角矩阵的行列式 = 对角线元素之积：

$$\det = 1 \cdot 4 \cdot 6 = 24$$

原因：对三角矩阵，$\det$ = 对角线之积。这是消元法得到上三角矩阵后计算行列式的依据。

</details>

---

## Q4 求矩阵的秩

<details><summary>解</summary>

(a) 第二行 = $2 \times$ 第一行，线性相关。$\operatorname{rank}(A) = 1$。

(b) 前两行线性无关，第三行全零。$\operatorname{rank}(B) = 2$。

</details>

---

## Q5 行列式性质验证

<details><summary>解</summary>

(a) $\det(2A) = 2^3 \cdot \det(A) = 8 \cdot 5 = 40$

(b) $\det(A^T) = \det(A) = 5$

(c) $\det(A^{-1}) = 1 / \det(A) = 1/5$

(d) $\det(A^2) = \det(A) \cdot \det(A) = 25$

</details>

---

## Q6 秩-零化度定理

<details><summary>解</summary>

(a) $A$ 的所有行都是 $[1, 2, 3]$ 的倍数（第二行 = $2\times$，第三行 = $3\times$），$\operatorname{rank}(A) = 1$。

(b) $\ker A = \{\mathbf{x} \mid x_1 + 2x_2 + 3x_3 = 0\}$。这是一个平面，$\dim\ker A = 2$。

(c) 秩-零化度定理：$\dim\ker A + \operatorname{rank}(A) = 2 + 1 = 3 = n$。✓

</details>

---

## Q7 迹的性质

<details><summary>解</summary>

(a) $\operatorname{tr}(A) = 1 + 4 = 5$, $\operatorname{tr}(B) = 5 + 8 = 13$

(b) $A+B = \begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}$, $\operatorname{tr}(A+B) = 6 + 12 = 18 = 5 + 13$ ✓

(c) $AB = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$, $\operatorname{tr}(AB) = 19 + 50 = 69$

$BA = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 23 & 34 \\ 31 & 46 \end{bmatrix}$, $\operatorname{tr}(BA) = 23 + 46 = 69$

$\operatorname{tr}(AB) = \operatorname{tr}(BA)$ ✓（尽管 $AB \neq BA$！）

</details>

---

## Q8 Frobenius 范数 vs 谱范数

<details><summary>解</summary>

**(a)** $\|A\|_F = \sqrt{1^2 + 0^2 + 0^2 + 2^2} = \sqrt{5} \approx 2.236$

**(b)** 对角矩阵的奇异值 = 对角线绝对值，即 $\sigma_1 = 2$, $\sigma_2 = 1$。谱范数 = $\sigma_{\max} = 2$。

**(c)** $\|A\|_2 = 2 < \|A\|_F = \sqrt{5} \approx 2.236$。Frobenius 范数总 $\geq$ 谱范数。

</details>

---

## Q9 Cramer 法则

<details><summary>解</summary>

$A = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$, $\mathbf{b} = \begin{bmatrix} 5 \\ 10 \end{bmatrix}$

$\det(A) = 2 \cdot 3 - 1 \cdot 1 = 5$

$A_1 = \begin{bmatrix} 5 & 1 \\ 10 & 3 \end{bmatrix}$, $\det(A_1) = 5 \cdot 3 - 1 \cdot 10 = 5$

$A_2 = \begin{bmatrix} 2 & 5 \\ 1 & 10 \end{bmatrix}$, $\det(A_2) = 2 \cdot 10 - 5 \cdot 1 = 15$

$$x_1 = \frac{5}{5} = 1, \quad x_2 = \frac{15}{5} = 3$$

验证：$2(1) + 3 = 5$ ✓, $1 + 3(3) = 10$ ✓

</details>

---

## Q10 条件数

<details><summary>解</summary>

**(a)** $A$ 是对角矩阵，奇异值 = $|100| = 100$ 和 $|0.01| = 0.01$。$\sigma_{\max} = 100$, $\sigma_{\min} = 0.01$。

**(b)** $\kappa_2(A) = 100 / 0.01 = 10000$。

**(c)** 误差放大公式：
$$\frac{\|\Delta\mathbf{x}\|}{\|\mathbf{x}\|} \leq \kappa_2(A) \cdot \frac{\|\Delta\mathbf{b}\|}{\|\mathbf{b}\|} = 10000 \times 0.01 = 100$$

即 1% 的输入误差可能在解 $\mathbf{x}$ 中放大为 100 倍（10000%）的相对误差。矩阵极度病态！

</details>

---

## Q11 $\det(AB) = \det(A)\det(B)$ 的实例验证

<details><summary>解</summary>

$\det A = 2 \cdot 4 - 1 \cdot 3 = 8 - 3 = 5$

$\det B = 0 \cdot 0 - 1 \cdot (-1) = 1$

$AB = \begin{bmatrix} 2 & 1 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} = \begin{bmatrix} -1 & 2 \\ -4 & 3 \end{bmatrix}$

$\det(AB) = (-1) \cdot 3 - 2 \cdot (-4) = -3 + 8 = 5$

$\det A \cdot \det B = 5 \cdot 1 = 5 = \det(AB)$ ✓

</details>

---

## Q12 可逆性综合判断

<details><summary>解</summary>

**方法 1 行列式**：
$$\det A = 1 \cdot \det\begin{bmatrix}4&2\\1&0\end{bmatrix} - 2 \cdot \det\begin{bmatrix}2&2\\1&0\end{bmatrix} + 1 \cdot \det\begin{bmatrix}2&4\\1&1\end{bmatrix}$$

$= 1 \cdot (0-2) - 2 \cdot (0-2) + 1 \cdot (2-4) = -2 + 4 + (-2) = 0$

**方法 2 秩**：第一列 $\mathbf{c}_1 = [1,2,1]^T$，第二列 $\mathbf{c}_2 = [2,4,1]^T$，第三列 $\mathbf{c}_3 = [1,2,0]^T$。

$\mathbf{c}_2 = 2\mathbf{c}_1$，所以前两列线性相关。$\operatorname{rank}(A) < 3$。

**结论**：$\det = 0$ 且 $\operatorname{rank} < 3$，$A$ 不可逆。两种方法一致。

</details>
