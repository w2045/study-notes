# 线性代数 · 第九章 · 理论题 — 参考答案

---

## Q1 SVD 的基本形式

<details><summary>解</summary>

$A$ 已是对角矩阵。奇异值 $\sigma_1 = 3$, $\sigma_2 = 2$。归一化得：

$U = I_2$, $\Sigma = \begin{bmatrix}3&0\\0&2\end{bmatrix}$, $V = I_2$。

验证：$U\Sigma V^T = I \cdot \operatorname{diag}(3,2) \cdot I = A$ ✓

</details>

---

## Q2 奇异值与范数

<details><summary>解</summary>

$\|A\|_2 = \sigma_{\max} = 5$

$\|A\|_F = \sqrt{\sigma_1^2 + \sigma_2^2} = \sqrt{25 + 9} = \sqrt{34} \approx 5.831$

</details>

---

## Q3 紧 SVD

<details><summary>解</summary>

$A = \begin{bmatrix}1&2\\2&4\end{bmatrix}$，第二列 = 2$\times$第一列，秩 = 1。

右奇异向量 $\mathbf{v}_1 = \frac{1}{\sqrt{5}}[1, 2]^T$（规范化的行空间基）。

左奇异向量 $\mathbf{u}_1 = \frac{1}{\sqrt{5}}[1, 2]^T$（规范化的列空间基）。

$\sigma_1 = \sqrt{1^2+2^2+2^2+4^2} \cdot \frac{1}{\sqrt{5}} = \sqrt{25}/\sqrt{5} \cdot ?$ 换个方式：$A^T A = \begin{bmatrix}5&10\\10&20\end{bmatrix}$，特征值 25, 0。$\sigma_1 = 5$。

紧 SVD：$A = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^T = 5 \cdot \frac{1}{\sqrt{5}}\begin{bmatrix}1\\2\end{bmatrix} \cdot \frac{1}{\sqrt{5}}\begin{bmatrix}1&2\end{bmatrix} = \begin{bmatrix}1&2\\2&4\end{bmatrix}$ ✓

</details>

---

## Q4 $A^T A$ 与奇异值关系

<details><summary>解</summary>

$A^T A = \begin{bmatrix}1&0&0\\0&2&0\end{bmatrix}\begin{bmatrix}1&0\\0&2\\0&0\end{bmatrix} = \begin{bmatrix}1&0\\0&4\end{bmatrix}$

特征值：$\lambda_1 = 4$, $\lambda_2 = 1$。

奇异值：$\sigma_1 = \sqrt{4} = 2$, $\sigma_2 = \sqrt{1} = 1$。$\sigma_3 = 0$（因为 $A$ 是 $3\times 2$ 非方阵，但 $A^T A$ 是 $2\times 2$ 矩阵，所以有两个奇异值。实际上 $A$ 最大有两个非零奇异值）。

</details>

---

## Q5 SVD 中的正交矩阵验证

<details><summary>解</summary>

验证：$A\mathbf{v}_1 = \begin{bmatrix}2&0\\0&1\end{bmatrix}\begin{bmatrix}1\\0\end{bmatrix} = \begin{bmatrix}2\\0\end{bmatrix} = 2\begin{bmatrix}1\\0\end{bmatrix} = \sigma_1 \mathbf{u}_1$ ✓

$A\mathbf{v}_2 = \begin{bmatrix}2&0\\0&1\end{bmatrix}\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}0\\1\end{bmatrix} = 1 \cdot \begin{bmatrix}0\\1\end{bmatrix} = \sigma_2 \mathbf{u}_2$ ✓

$\mathbf{u}_2$ 的方向是 $[0,1]^T$。可以取 $-\mathbf{u}_2$ 也是合法的（$U$ 的列可以取反号，只需保证 $\Sigma$ 的对角元为正和 $U^T U = I$）。

</details>

---

## Q6 低秩近似的 Eckart-Young 定理

<details><summary>解</summary>

$A = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^T + \sigma_2 \mathbf{u}_2 \mathbf{v}_2^T$。秩-1 近似：

$$A_1 = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^T = 4 \cdot \frac{1}{\sqrt{2}}\begin{bmatrix}1\\1\end{bmatrix} \cdot \frac{1}{\sqrt{2}}\begin{bmatrix}1&1\end{bmatrix} = \begin{bmatrix}2&2\\2&2\end{bmatrix}$$

$$\|A - A_1\|_F = \sigma_2 = 2$$

（Eckart-Young 定理：$\|A - A_1\|_F = \sqrt{\sum_{i=2}^r \sigma_i^2} = \sqrt{2^2} = 2$。）

</details>

---

## Q7 伪逆与最小二乘

<details><summary>解</summary>

$A$ 的 SVD：$U = I_3$, $\Sigma = \begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}$, $V = I_2$。

$\Sigma^+ = \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}$

$A^+ = V\Sigma^+ U^T = \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}$

最小二乘解：$\mathbf{\hat{x}} = A^+\mathbf{b} = \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}\begin{bmatrix}2\\3\\4\end{bmatrix} = \begin{bmatrix}2\\3\end{bmatrix}$

</details>

---

## Q8 图像压缩原理

<details><summary>解</summary>

原始存储：$100 \times 100 = 10000$ 个数。

$k = 3$ 存储：$k \times (H + W + 1) = 3 \times (100 + 100 + 1) = 603$ 个数。

压缩比：$10000 / 603 \approx 16.6$。

能量保留：$\frac{\sum_{i=1}^3 \sigma_i^2}{\sum_{i=1}^r \sigma_i^2}$

$\sum_{i=1}^3 = 1000^2 + 500^2 + 100^2 = 1,260,000$

$\sum_{i=1}^r \approx 1,260,000 + \sum_{i=4}^{100} 10^2 \approx 1,260,000 + 97 \times 100 = 1,269,700$

能量保留 $\approx 1,260,000 / 1,269,700 \approx 99.2\%$。

只用 3 个奇异值就保留了 99% 以上的「信息能量」！

</details>

---

## Q9 奇异值与特征值的关系

<details><summary>解</summary>

若 $A = A^T$，则 $A$ 可正交对角化：$A = Q\Lambda Q^T$，$\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$。

取 $U = Q$, $V = Q \cdot \operatorname{sign}(\Lambda)$（对负特征值取符号），$\Sigma = \operatorname{diag}(|\lambda_1|, \ldots, |\lambda_n|)$。

则 $U\Sigma V^T = Q \cdot \operatorname{diag}(|\lambda_i|) \cdot \operatorname{sign}(\Lambda) Q^T = Q \Lambda Q^T = A$。

因此 $\sigma_i = |\lambda_i|$。证毕

</details>

---

## Q10 条件数与奇异值

<details><summary>解</summary>

$\kappa_2(A) = \sigma_{\max} / \sigma_{\min} = 100 / 0.01 = 10000$。

**病态原因**：奇异值极度不均衡——$x_1$ 方向拉伸 100 倍，$x_2$ 方向压缩到 0.01 倍。输入在 $x_2$ 方向上的微小变化被极度衰减，求逆时又被极度放大。$A$ 的「有效」信息几乎全在第一个奇异方向。

</details>

---

## Q11 SVD 与四个基本子空间

<details><summary>解</summary>

设 $r = \operatorname{rank}(A)$，$U = [\mathbf{u}_1, \ldots, \mathbf{u}_m]$, $V = [\mathbf{v}_1, \ldots, \mathbf{v}_n]$。

- **列空间** $\operatorname{col}(A)$ 的基：$\mathbf{u}_1, \ldots, \mathbf{u}_r$（前 $r$ 列）
- **行空间** $\operatorname{row}(A)$ 的基：$\mathbf{v}_1, \ldots, \mathbf{v}_r$（$V$ 的前 $r$ 列）
- **零空间** $\ker(A)$ 的基：$\mathbf{v}_{r+1}, \ldots, \mathbf{v}_n$（$V$ 的后 $n-r$ 列）
- **左零空间** $\ker(A^T)$ 的基：$\mathbf{u}_{r+1}, \ldots, \mathbf{u}_m$（$U$ 的后 $m-r$ 列）

SVD 一次性给出全部四个基本子空间的标准正交基！这是 SVD 的伟大之处。

</details>

---

## Q12 利用 SVD 做矩阵补全

<details><summary>解</summary>

**低秩假设**：用户-物品评分矩阵通常是低秩的，因为用户的偏好由少数几个「隐藏因素」（如电影类型偏好、年龄组等）决定。$r \ll \min(\#users, \#items)$。

**基本步骤**：
1. 对现有评分的矩阵 $\tilde{M}$（空缺处填 0 或均值）做 SVD
2. 取截断 SVD：$\tilde{M} \approx U_k \Sigma_k V_k^T$（秩-$k$ 近似）
3. 用 $U_k \Sigma_k V_k^T$ 中原来空缺位置的预测值填充

**为什么有效**：截断 SVD 强迫矩阵低秩，相当于从观测数据中学习隐藏因子（$U_k$ 的列 = 用户因子，$V_k$ 的列 = 物品因子），预测是基于因子向量内积的自然推广。

</details>
