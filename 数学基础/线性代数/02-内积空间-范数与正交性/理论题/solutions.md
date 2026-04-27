# 线性代数 · 第二章 · 理论题 — 参考答案

---

## Q1 内积计算

<details><summary>解</summary>

**(a)** $\mathbf{u} \cdot \mathbf{v} = 1 \cdot 3 + 2 \cdot (-1) + (-1) \cdot 1 = 3 - 2 - 1 = 0$。**正交**。

**(b)** $\mathbf{u} \cdot \mathbf{v} = 1 \cdot 0 + 0 \cdot 1 + 0 \cdot 0 = 0$。**正交**。

</details>

---

## Q2 范数计算

<details><summary>解</summary>

- $\ell_1$：$\|\mathbf{v}\|_1 = |3| + |{-4}| + |0| = 3 + 4 + 0 = 7$
- $\ell_2$：$\|\mathbf{v}\|_2 = \sqrt{3^2 + (-4)^2 + 0^2} = \sqrt{9 + 16} = 5$
- $\ell_{\infty}$：$\|\mathbf{v}\|_{\infty} = \max(|3|, |{-4}|, |0|) = 4$

</details>

---

## Q3 归一化

<details><summary>解</summary>

$\|\mathbf{v}\| = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = 10$

$$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|} = \begin{bmatrix} 6/10 \\ 8/10 \end{bmatrix} = \begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix}$$

验证：$\|\hat{\mathbf{v}}\| = \sqrt{0.36 + 0.64} = 1$ ✓

</details>

---

## Q4 余弦相似度

<details><summary>解</summary>

$\mathbf{u} \cdot \mathbf{v} = 1 \cdot 3 + 2 \cdot 4 = 11$

$\|\mathbf{u}\| = \sqrt{1 + 4} = \sqrt{5}$, $\|\mathbf{v}\| = \sqrt{9 + 16} = 5$

$$\cos\theta = \frac{11}{\sqrt{5} \cdot 5} = \frac{11}{5\sqrt{5}} \approx 0.9839$$

$\theta \approx 10.3^\circ$（接近同方向）。

</details>

---

## Q5 Cauchy-Schwarz 验证

<details><summary>解</summary>

$|\langle \mathbf{u}, \mathbf{v} \rangle| = |1 \cdot (-2) + 3 \cdot 1 + 5 \cdot 4| = |{-2} + 3 + 20| = |21| = 21$

$\|\mathbf{u}\| = \sqrt{1 + 9 + 25} = \sqrt{35}$

$\|\mathbf{v}\| = \sqrt{4 + 1 + 16} = \sqrt{21}$

$\|\mathbf{u}\| \cdot \|\mathbf{v}\| = \sqrt{35 \cdot 21} = \sqrt{735} \approx 27.11$

$21 < 27.11$，不等式成立。等号不成立（$\mathbf{u}$ 与 $\mathbf{v}$ 不共线）。✓

</details>

---

## Q6 正交补

<details><summary>解</summary>

$W^{\perp} = \{[x, y, z]^T \in \mathbb{R}^3 \mid [x,y,z]^T \cdot [1,2,-1]^T = 0\}$

$= \{[x, y, z]^T \mid x + 2y - z = 0\}$

$= \{[x, y, x+2y]^T\} = \operatorname{span}\{[1, 0, 1]^T, [0, 1, 2]^T\}$

基：$\{[1, 0, 1]^T, [0, 1, 2]^T\}$，$\dim W^{\perp} = 2$。

验证：$\dim W + \dim W^{\perp} = 1 + 2 = 3 = \dim \mathbb{R}^3$ ✓

</details>

---

## Q7 Gram-Schmidt 正交化

<details><summary>解</summary>

**(1)** $\mathbf{u}_1 = \mathbf{v}_1 = [1, 1, 0]^T$

**(2)** $\mathbf{u}_2 = \mathbf{v}_2 - \frac{\langle \mathbf{v}_2, \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1, \mathbf{u}_1 \rangle} \mathbf{u}_1$

$\langle \mathbf{v}_2, \mathbf{u}_1 \rangle = 0 \cdot 1 + 1 \cdot 1 + 1 \cdot 0 = 1$

$\langle \mathbf{u}_1, \mathbf{u}_1 \rangle = 1 + 1 + 0 = 2$

$\mathbf{u}_2 = [0, 1, 1]^T - \frac{1}{2}[1, 1, 0]^T = [-\frac{1}{2}, \frac{1}{2}, 1]^T$

验证：$\mathbf{u}_1 \cdot \mathbf{u}_2 = 1 \cdot (-\frac{1}{2}) + 1 \cdot \frac{1}{2} + 0 \cdot 1 = 0$ ✓

</details>

---

## Q8 正交投影

<details><summary>解</summary>

$\operatorname{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\langle \mathbf{v}, \mathbf{u} \rangle}{\langle \mathbf{u}, \mathbf{u} \rangle} \mathbf{u}$

$\langle \mathbf{v}, \mathbf{u} \rangle = 3 \cdot 1 + 4 \cdot 0 + 5 \cdot 0 = 3$

$\langle \mathbf{u}, \mathbf{u} \rangle = 1$

$$\operatorname{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{3}{1} \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 3 \\ 0 \\ 0 \end{bmatrix}$$

这正好是 $\mathbf{v}$ 的 $x$ 分量——投影到 $x$ 轴上。

</details>

---

## Q9 三角不等式证明

<details><summary>解</summary>

$$\|\mathbf{u} + \mathbf{v}\|^2 = \langle \mathbf{u} + \mathbf{v}, \mathbf{u} + \mathbf{v} \rangle$$
$$= \langle \mathbf{u}, \mathbf{u} \rangle + \langle \mathbf{u}, \mathbf{v} \rangle + \langle \mathbf{v}, \mathbf{u} \rangle + \langle \mathbf{v}, \mathbf{v} \rangle$$
$$= \|\mathbf{u}\|^2 + 2\langle \mathbf{u}, \mathbf{v} \rangle + \|\mathbf{v}\|^2$$
$$\leq \|\mathbf{u}\|^2 + 2|\langle \mathbf{u}, \mathbf{v} \rangle| + \|\mathbf{v}\|^2 \quad \text{（$x \leq |x|$）}$$
$$\leq \|\mathbf{u}\|^2 + 2\|\mathbf{u}\|\|\mathbf{v}\| + \|\mathbf{v}\|^2 \quad \text{（Cauchy-Schwarz）}$$
$$= (\|\mathbf{u}\| + \|\mathbf{v}\|)^2$$

两边开平方（范数非负）：$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$。$\square$

</details>

---

## Q10 正交向量与线性无关

<details><summary>解</summary>

设 $\mathbf{v}_1, \ldots, \mathbf{v}_k$ 两两正交且均非零。假设存在不全为零的系数 $c_i$ 使得 $\sum c_i \mathbf{v}_i = \mathbf{0}$。

对任意 $j$，与该等式做内积（利用正交性）：

$$\langle \sum_i c_i \mathbf{v}_i, \mathbf{v}_j \rangle = c_j \langle \mathbf{v}_j, \mathbf{v}_j \rangle = c_j \|\mathbf{v}_j\|^2 = 0$$

由于 $\|\mathbf{v}_j\|^2 > 0$（非零），必须 $c_j = 0$。这对所有 $j$ 成立，所以只有零解。线性无关。$\square$

</details>

---

## Q11 平行四边形法则

<details><summary>解</summary>

$$\|\mathbf{u} + \mathbf{v}\|^2 + \|\mathbf{u} - \mathbf{v}\|^2$$
$$= (\|\mathbf{u}\|^2 + 2\langle \mathbf{u}, \mathbf{v} \rangle + \|\mathbf{v}\|^2) + (\|\mathbf{u}\|^2 - 2\langle \mathbf{u}, \mathbf{v} \rangle + \|\mathbf{v}\|^2)$$
$$= 2\|\mathbf{u}\|^2 + 2\|\mathbf{v}\|^2 = 2(\|\mathbf{u}\|^2 + \|\mathbf{v}\|^2)$$

**几何意义**：平行四边形对角线长度的平方和等于四边长度平方和。这在平面几何中是平行四边形定理，内积空间保留了这一性质。反过来，满足此法则的范数**必**来自某个内积——这是内积范数的特征性质。

</details>

---

## Q12 函数空间的内积

<details><summary>解</summary>

$$\langle f, g \rangle = \int_0^1 1 \cdot (x - \tfrac{1}{2})\,dx = \left[\frac{x^2}{2} - \frac{x}{2}\right]_0^1$$

$$= (\frac{1}{2} - \frac{1}{2}) - (0 - 0) = 0$$

内积为零，$f \perp g$。两个函数在 $C[0,1]$ 上正交。

几何直觉：$f(x) = 1$ 是常数项，$g(x) = x - \frac{1}{2}$ 是中心化的 $x$，它们在这种内积下「不重叠」。

</details>
