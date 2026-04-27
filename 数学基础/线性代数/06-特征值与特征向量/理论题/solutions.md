# 线性代数 · 第六章 · 理论题 — 参考答案

---

## Q1 求 2x2 特征值与特征向量

<details><summary>解</summary>

对角矩阵的特征值就是对角线元素：$\lambda_1 = 3$, $\lambda_2 = 5$。

- $\lambda_1=3$：$(A-3I)\mathbf{v} = \begin{bmatrix}0&0\\0&2\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_1 = [1, 0]^T$
- $\lambda_2=5$：$(A-5I)\mathbf{v} = \begin{bmatrix}-2&0\\0&0\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_2 = [0, 1]^T$

</details>

---

## Q2 求 2x2 特征多项式

<details><summary>解</summary>

$$p_A(\lambda) = \det\begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix} = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10$$

$p_A(\lambda) = (\lambda - 2)(\lambda - 5) = 0 \implies \lambda_1 = 2, \lambda_2 = 5$。

</details>

---

## Q3 验证特征值/向量关系

<details><summary>解</summary>

$A\mathbf{v} = \begin{bmatrix} 4 & 2 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 10 \\ 5 \end{bmatrix} = 5 \begin{bmatrix} 2 \\ 1 \end{bmatrix} = 5\mathbf{v}$

所以 $\mathbf{v}$ 是 $A$ 的特征向量，对应特征值 $\lambda = 5$。

</details>

---

## Q4 迹和行列式与特征值关系

<details><summary>解</summary>

$\operatorname{tr}(A) = \lambda_1 + \lambda_2 + \lambda_3 = 1 + 2 + 3 = 6$

$\det(A) = \lambda_1 \cdot \lambda_2 \cdot \lambda_3 = 1 \cdot 2 \cdot 3 = 6$

</details>

---

## Q5 3x3 特征值（三角矩阵）

<details><summary>解</summary>

上三角矩阵的特征值 = 对角线元素：$\lambda_1 = 2$, $\lambda_2 = -1$, $\lambda_3 = 6$。

这是因为 $A - \lambda I$ 仍是上三角，行列式 = $(2-\lambda)(-1-\lambda)(6-\lambda)$。

</details>

---

## Q6 对角化

<details><summary>解</summary>

$A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$，特征值 $\lambda_1 = 1$, $\lambda_2 = 3$。

- $\lambda_1 = 1$：$(A-I)\mathbf{v} = \begin{bmatrix}1&1\\1&1\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_1 = [1, -1]^T$
- $\lambda_2 = 3$：$(A-3I)\mathbf{v} = \begin{bmatrix}-1&1\\1&-1\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_2 = [1, 1]^T$

$$P = \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}, \quad \Lambda = \begin{bmatrix} 1 & 0 \\ 0 & 3 \end{bmatrix}$$

$\det P = 2$, $P^{-1} = \frac{1}{2}\begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}$

验证：$P\Lambda P^{-1} = \frac{1}{2}\begin{bmatrix}1&3\\-1&3\end{bmatrix}\begin{bmatrix}1&-1\\1&1\end{bmatrix} = \frac{1}{2}\begin{bmatrix}4&2\\2&4\end{bmatrix} = \begin{bmatrix}2&1\\1&2\end{bmatrix} = A$ ✓

</details>

---

## Q7 判断可对角化

<details><summary>解</summary>

**$A = I$**：当然可对角化。$A = I I I^{-1}$，$P$ 可以是任何可逆矩阵。

**$B = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$**：特征多项式 $(1-\lambda)^2$，$\lambda = 1$（代数重数 2）。$(B-I)\mathbf{v} = \begin{bmatrix}0&1\\0&0\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v} = [c, 0]^T$。几何重数 = 1 < 2，**不可对角化**。

</details>

---

## Q8 特征空间维数

<details><summary>解</summary>

$A = \operatorname{diag}(2, 2, 3)$。

- $\lambda = 2$：代数重数 = 2，$(A-2I) = \operatorname{diag}(0, 0, 1)$，零空间维数 = 2。几何重数 = 2。
- $\lambda = 3$：代数重数 = 1，$(A-3I) = \operatorname{diag}(-1, -1, 0)$，零空间维数 = 1。几何重数 = 1。

所有特征值的几何重数 = 代数重数 → 可对角化（显然，本身已是对角矩阵）。

</details>

---

## Q9 幂迭代法原理

<details><summary>解</summary>

设 $A = P\Lambda P^{-1}$，初始向量 $\mathbf{v}_0 = \sum c_i \mathbf{p}_i$（特征向量展开）。则：

$$\mathbf{v}_k = A^k \mathbf{v}_0 = \sum c_i \lambda_i^k \mathbf{p}_i$$

归一化后：
$$\frac{\mathbf{v}_k}{\|\mathbf{v}_k\|} \approx \frac{c_1 \lambda_1^k \mathbf{p}_1}{\|c_1 \lambda_1^k \mathbf{p}_1\|} = \pm \frac{\mathbf{p}_1}{\|\mathbf{p}_1\|}$$

因为 $|\lambda_1| > |\lambda_i|$（$i \geq 2$）时，$(\lambda_i/\lambda_1)^k \to 0$。所以 $\mathbf{v}_k$ 收敛到主特征向量 $\mathbf{p}_1$。

Rayleigh 商 $\frac{\mathbf{v}_k^T A\mathbf{v}_k}{\mathbf{v}_k^T\mathbf{v}_k} \to \lambda_1$。

</details>

---

## Q10 对角化的应用：矩阵幂

<details><summary>解</summary>

$A = \begin{bmatrix} 1 & 2 \\ 0 & -1 \end{bmatrix}$。

$p(\lambda) = (1-\lambda)(-1-\lambda)$，$\lambda_1 = 1$, $\lambda_2 = -1$。

- $\lambda_1=1$：$(A-I)\mathbf{v} = \begin{bmatrix}0&2\\0&-2\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_1 = [1, 0]^T$
- $\lambda_2=-1$：$(A+I)\mathbf{v} = \begin{bmatrix}2&2\\0&0\end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_2 = [1, -1]^T$

$P = \begin{bmatrix}1&1\\0&-1\end{bmatrix}$, $P^{-1} = \begin{bmatrix}1&1\\0&-1\end{bmatrix}$（验证：$\det = -1$）

$$A^{10} = P\Lambda^{10}P^{-1} = \begin{bmatrix}1&1\\0&-1\end{bmatrix} \begin{bmatrix}1^{10}&0\\0&(-1)^{10}\end{bmatrix} \begin{bmatrix}1&1\\0&-1\end{bmatrix}$$

$= \begin{bmatrix}1&1\\0&-1\end{bmatrix} \begin{bmatrix}1&0\\0&1\end{bmatrix} \begin{bmatrix}1&1\\0&-1\end{bmatrix} = \begin{bmatrix}1&1\\0&-1\end{bmatrix} \begin{bmatrix}1&1\\0&-1\end{bmatrix}$

$= \begin{bmatrix}1&0\\0&1\end{bmatrix} = I$

实际上 $A^2 = I$（验证：直接算也成立），所以 $A^{10} = (A^2)^5 = I^5 = I$。

</details>

---

## Q11 相似矩阵的特征值

<details><summary>解</summary>

$$\det(B - \lambda I) = \det(P^{-1}AP - \lambda I) = \det(P^{-1}AP - \lambda P^{-1}P)$$
$$= \det(P^{-1}(A - \lambda I)P) = \det(P^{-1}) \cdot \det(A - \lambda I) \cdot \det(P)$$
$$= \frac{1}{\det P} \cdot \det(A - \lambda I) \cdot \det P = \det(A - \lambda I)$$

所以 $p_B(\lambda) = p_A(\lambda)$，特征值相同。证毕

</details>

---

## Q12 特征值的几何应用

<details><summary>解</summary>

$A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$，特征值 $\lambda_1 = 1$, $\lambda_2 = 3$。

- **$\mathbf{v}_1 = [1, -1]^T$ (特征值 1)**：沿此方向，$A$ 保持长度不变（等距）。
- **$\mathbf{v}_2 = [1, 1]^T$ (特征值 3)**：沿此方向，$A$ 拉伸为原来的 3 倍。

几何上，$A$ 将单位圆 $x^2 + y^2 = 1$ 映射为椭圆。在特征方向坐标系中，椭圆方程为：
$$\left(\frac{x'}{1}\right)^2 + \left(\frac{y'}{3}\right)^2 = 1$$

即短半轴长度 1（沿 $[1,-1]^T$ 方向），长半轴长度 3（沿 $[1,1]^T$ 方向）。特征向量给出了椭圆的主轴方向，特征值给出半轴长度。

</details>
