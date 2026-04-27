# 线性代数 · 第一章 · 理论题 — 参考答案

---

## Q1 线性组合表示

<details><summary>解</summary>

设 $\mathbf{w} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2$：

$$\begin{cases} c_1 + 3c_2 = 7 \\ 2c_1 + c_2 = 11 \end{cases}$$

由①得 $c_1 = 7 - 3c_2$，代入②：
$2(7 - 3c_2) + c_2 = 14 - 5c_2 = 11 \implies c_2 = \frac{3}{5}$

回代：$c_1 = 7 - 3 \cdot \frac{3}{5} = \frac{26}{5}$

$$\mathbf{w} = \frac{26}{5}\begin{bmatrix}1\\2\end{bmatrix} + \frac{3}{5}\begin{bmatrix}3\\1\end{bmatrix}$$

验证：$\frac{26}{5}[1,2]^T + \frac{3}{5}[3,1]^T = [\frac{26}{5} + \frac{9}{5}, \frac{52}{5} + \frac{3}{5}]^T = [7, 11]^T$。

</details>

---

## Q2 线性相关/无关判定

<details><summary>解</summary>

**(a)** $\mathbf{v}_2 = 2\mathbf{v}_1$，所以**线性相关**。非零组合：$2\mathbf{v}_1 - \mathbf{v}_2 = \mathbf{0}$。

**(b)** 设 $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0}$：

$$\begin{cases} c_1 + c_3 = 0 \\ c_2 + c_3 = 0 \\ c_1 + c_3 = 0 \end{cases}$$

由①：$c_1 = -c_3$，由②：$c_2 = -c_3$。取 $c_3 = 1$，得非零解 $(-1, -1, 1)$。所以**线性相关**。

非零组合：$-\mathbf{v}_1 - \mathbf{v}_2 + \mathbf{v}_3 = \mathbf{0}$（即 $\mathbf{v}_3 = \mathbf{v}_1 + \mathbf{v}_2$）。

</details>

---

## Q3 判断子空间

<details><summary>解</summary>

**(a) $W_1$**：是子空间。
- $\mathbf{0} \in W_1$（$0 = 2 \cdot 0$）
- $[x_1, 2x_1]^T + [x_2, 2x_2]^T = [x_1+x_2, 2(x_1+x_2)]^T \in W_1$
- $c[x, 2x]^T = [cx, 2cx]^T \in W_1$

**(b) $W_2$**：不是子空间。$\mathbf{0} = [0,0]^T$ 不满足 $0 = 2 \cdot 0 + 1 = 1$。

**(c) $W_3$**：不是子空间。标量乘法封闭性失败——$-1 \cdot [1, 0]^T = [-1, 0]^T \notin W_3$（第一象限不封闭于负标量）。

</details>

---

## Q4 Span 的几何含义

<details><summary>解</summary>

| 题号 | 向量组 | Span | 几何对象 |
|------|--------|------|----------|
| (a) | $[1,2,3]^T$ | $\{c[1,2,3]^T \mid c \in \mathbb{R}\}$ | 过原点的直线 |
| (b) | $[1,0,0]^T, [0,1,0]^T$ | $\{[x,y,0]^T\}$ | $xy$ 平面 |
| (c) | $[1,0,1]^T, [2,0,2]^T$ | 同 (a) | 直线（两向量共线） |
| (d) | $[1,0,0]^T, [0,1,0]^T, [1,1,0]^T$ | 同 (b) | $xy$ 平面（第三个是前两个的和，线性相关） |

</details>

---

## Q5 求基与维数

<details><summary>解</summary>

由 $x + y + z = 0$ 得 $z = -x - y$。任意 $\mathbf{w} \in W$：

$$\mathbf{w} = \begin{bmatrix} x \\ y \\ -x-y \end{bmatrix} = x\begin{bmatrix} 1 \\ 0 \\ -1 \end{bmatrix} + y\begin{bmatrix} 0 \\ 1 \\ -1 \end{bmatrix}$$

$\mathcal{B} = \{[1,0,-1]^T, [0,1,-1]^T\}$ 是一组基（两向量不共线，线性无关），$\dim W = 2$。

</details>

---

## Q6 验证向量空间公理

<details><summary>解</summary>

$V = \{[0, y]^T \mid y \in \mathbb{R}\}$（$y$ 轴）。

1. **加法封闭**：$[0, y_1]^T + [0, y_2]^T = [0, y_1 + y_2]^T \in V$ ✓
2. **标量乘法封闭**：$c[0, y]^T = [0, cy]^T \in V$ ✓
3. **零元存在**：$[0, 0]^T \in V$ ✓

因此 $V$ 是 $\mathbb{R}^2$ 的子空间（从而是向量空间），$\dim V = 1$。

</details>

---

## Q7 线性无关的一般性质

<details><summary>解</summary>

**(a)** 设 $a(\mathbf{u} + \mathbf{v}) + b(\mathbf{u} - \mathbf{v}) = \mathbf{0}$。

展开：$(a+b)\mathbf{u} + (a-b)\mathbf{v} = \mathbf{0}$。

由于 $\mathbf{u}, \mathbf{v}$ 线性无关：
$$\begin{cases} a + b = 0 \\ a - b = 0 \end{cases} \implies a = b = 0$$

所以 $\mathbf{u}+\mathbf{v}$ 和 $\mathbf{u}-\mathbf{v}$ 线性无关。

**(b)**
- $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ 线性无关 $\implies$ $\{\mathbf{u}, \mathbf{v}\}$ 线性无关（因为若 $\{\mathbf{u}, \mathbf{v}\}$ 相关，加 $\mathbf{w}$ 后仍相关）。
- 反过来不成立：$\{\mathbf{u}, \mathbf{v}\}$ 线性无关，加第三个可能导致冗余（如 $\mathbf{w} = \mathbf{u} + \mathbf{v}$）。

</details>

---

## Q8 维数公式应用

<details><summary>解</summary>

**(a)**
- $\dim U = 2$（$xy$ 平面，基为 $\mathbf{e}_1, \mathbf{e}_2$）
- $\dim W = 2$（$yz$ 平面，基为 $\mathbf{e}_2, \mathbf{e}_3$）
- $U \cap W = \{[0, y, 0]^T\}$（$y$ 轴），$\dim(U \cap W) = 1$

**(b)** 维数公式：

$$\dim(U + W) = \dim U + \dim W - \dim(U \cap W) = 2 + 2 - 1 = 3$$

$\dim(U + W) = 3$ 且 $U + W \subseteq \mathbb{R}^3$，故 $U + W = \mathbb{R}^3$。

直接验证：$[1,0,0]^T \in U$, $[0,0,1]^T \in W$，加上 $[0,1,0]^T$ 同时在两者中，三者张成 $\mathbb{R}^3$。

</details>

---

## Q9 基的唯一表示

<details><summary>解</summary>

设 $\mathbf{v} \in V$ 有两个表示：

$$\mathbf{v} = \sum_{i=1}^{n} c_i \mathbf{b}_i = \sum_{i=1}^{n} d_i \mathbf{b}_i$$

相减：

$$\sum_{i=1}^{n} (c_i - d_i) \mathbf{b}_i = \mathbf{0}$$

由于 $\mathcal{B}$ 线性无关，必须 $c_i - d_i = 0$ 对每个 $i$ 成立，即 $c_i = d_i$。表示唯一。证毕

</details>

---

## Q10 子空间的交

<details><summary>解</summary>

**(a)** $U$：$x - y = 0 \implies x = y$。含 $\mathbf{0}$，加法、标量乘法均封闭 → 子空间。$U = \{[t, t, z]^T\}$。

$W$：$y - z = 0 \implies y = z$。同理，子空间。$W = \{[x, t, t]^T\}$。

**(b)** $U \cap W$ 同时满足 $x=y$ 且 $y=z$，即 $x=y=z$：

$$U \cap W = \{[t, t, t]^T \mid t \in \mathbb{R}\}$$

基：$\{[1, 1, 1]^T\}$，$\dim(U \cap W) = 1$。

</details>

---

## Q11 线性无关与 Span 的关系

<details><summary>解</summary>

若 $\mathbf{v}_1, \ldots, \mathbf{v}_k$ 线性相关，则存在不全为零的系数 $c_1, \ldots, c_k$ 使得 $\sum c_i \mathbf{v}_i = \mathbf{0}$。

设 $c_j \neq 0$（至少有一个非零），则可以解出：

$$\mathbf{v}_j = -\frac{1}{c_j} \sum_{i \neq j} c_i \mathbf{v}_i$$

即 $\mathbf{v}_j$ 可表示为其余向量的线性组合。证毕

**注意**：这并不意味着**每个**向量都能被其余向量表示——只保证至少有一个可以。例如 $\{[1,0]^T, [2,0]^T, [0,1]^T\}$ 线性相关，但第三个向量不能由前两个表示。

</details>

---

## Q12 多项式向量空间

<details><summary>解</summary>

**(a)** $P_2$ 的标准基：$\{1, x, x^2\}$，$\dim P_2 = 3$。

**(b)** 要验证 $\{1+x, 1-x, x^2\}$ 是否线性无关。设：

$$a(1+x) + b(1-x) + c(x^2) = 0$$

展开：$(a+b) + (a-b)x + c x^2 = 0 + 0x + 0x^2$

系数匹配：
$$\begin{cases} a + b = 0 \\ a - b = 0 \\ c = 0 \end{cases}$$

$a+b=0$ 且 $a-b=0 \implies a=b=0$，且 $c=0$。只有零解 → 线性无关。

3 个线性无关的多项式（$\dim P_2 = 3$），所以是 $P_2$ 的一组基。

**(c)** 设 $p(x) = 3 + 2x + 5x^2 = A(1+x) + B(1-x) + C x^2$：

$$(A+B) + (A-B)x + C x^2 = 3 + 2x + 5x^2$$

$$\begin{cases} A + B = 3 \\ A - B = 2 \\ C = 5 \end{cases}$$

解前两式：相加 $2A = 5 \implies A = \frac{5}{2}$，相减 $2B = 1 \implies B = \frac{1}{2}$。

$$p(x) = \frac{5}{2}(1+x) + \frac{1}{2}(1-x) + 5x^2$$

</details>
