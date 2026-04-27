# 线性代数 · 第二章 · 内积空间、范数与正交性

← 前置: [01 — 向量与向量空间](../01-向量与向量空间/notes.md)
→ 延伸: [03 — 矩阵与线性变换](../03-矩阵与线性变换/notes.md)

---

## 1. 直觉引入：为什么需要「长度」和「角度」？

第一章建立了向量的代数结构——加法、标量乘法、线性组合。但缺少两个基本几何概念：

- **长度**：$\mathbf{v}$ 有多长？→ 范数
- **角度**：$\mathbf{u}$ 和 $\mathbf{v}$ 的方向差多少？→ 内积

有了这两个概念，线性代数才真正和几何连接起来。本章从内积出发，导出范数和正交性。

---

## 2. 内积 (Inner Product)

### 2.1 标准内积（点积）

> **定义 1（标准内积/点积）**：对 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$：
>
> $$\mathbf{u} \cdot \mathbf{v} = \langle \mathbf{u}, \mathbf{v} \rangle = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n = \sum_{i=1}^{n} u_i v_i$$

结果是一个标量（不是向量），所以也叫**标量积 (scalar product)**。

**例子**：
- $[1, 2, 3]^T \cdot [4, 5, 6]^T = 1 \cdot 4 + 2 \cdot 5 + 3 \cdot 6 = 4 + 10 + 18 = 32$
- $[1, 0]^T \cdot [0, 1]^T = 0$（垂直 → 结果为零）

### 2.2 几何意义

$$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos \theta$$

其中 $\theta$ 是两向量之间的夹角。这是内积最重要的公式：

- $\mathbf{u} \cdot \mathbf{v} = 0 \iff \mathbf{u} \perp \mathbf{v}$（正交）
- $\mathbf{u} \cdot \mathbf{v} > 0 \iff \theta < 90^\circ$（锐角，方向相似）
- $\mathbf{u} \cdot \mathbf{v} < 0 \iff \theta > 90^\circ$（钝角，方向相反）

**应用——余弦相似度 (Cosine Similarity)**：
$$\cos\theta = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|} \in [-1, 1]$$
这是 ML 中衡量**方向相似性**的最常用度量——不受向量长度影响。文本嵌入 $\mathbf{e}_{\text{cat}}$ 和 $\mathbf{e}_{\text{dog}}$ 的余弦相似度接近 1（语义相近），而 $\mathbf{e}_{\text{cat}}$ 和 $\mathbf{e}_{\text{car}}$ 则接近 0。当 $\cos\theta = 1$ 时两向量共线同向，$\cos\theta = -1$ 时共线反向，$\cos\theta = 0$ 时正交。

### 2.3 代数性质

> **定理**：标准内积满足以下性质（$\forall \mathbf{u}, \mathbf{v}, \mathbf{w} \in \mathbb{R}^n, c \in \mathbb{R}$）：

| 性质 | 公式 |
|------|------|
| 对称性 | $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$ |
| 双线性 I | $(\mathbf{u} + \mathbf{v}) \cdot \mathbf{w} = \mathbf{u} \cdot \mathbf{w} + \mathbf{v} \cdot \mathbf{w}$ |
| 双线性 II | $(c\mathbf{u}) \cdot \mathbf{v} = c(\mathbf{u} \cdot \mathbf{v})$ |
| 正定性 | $\mathbf{v} \cdot \mathbf{v} \geq 0$，等号 $\iff \mathbf{v} = \mathbf{0}$ |

---

## 3. 一般内积空间

$\mathbb{R}^n$ 的标准内积只是一个特例。抽象的**内积空间**是任何定义了内积运算的向量空间。

> **定义 2（实内积空间）**：向量空间 $V$ 上的**内积**是一个函数 $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{R}$，满足：
>
> 1. **对称性**：$\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$
> 2. **线性性**：$\langle \mathbf{u} + \mathbf{v}, \mathbf{w} \rangle = \langle \mathbf{u}, \mathbf{w} \rangle + \langle \mathbf{v}, \mathbf{w} \rangle$
> 3. **齐次性**：$\langle c\mathbf{u}, \mathbf{v} \rangle = c\langle \mathbf{u}, \mathbf{v} \rangle$
> 4. **正定性**：$\langle \mathbf{v}, \mathbf{v} \rangle \geq 0$，等号 $\iff \mathbf{v} = \mathbf{0}$

配备了内积的向量空间称为**内积空间 (inner product space)**。

### 3.1 复向量空间与 Hermitian 内积

当标量域扩展到复数 $\mathbb{C}$ 时，$\mathbb{R}^n$ 的标准内积 $\mathbf{u} \cdot \mathbf{v} = \sum u_i v_i$ 不再适用——它会导致 $\langle \mathbf{v}, \mathbf{v} \rangle$ 可能为复数甚至负数，违反正定性。

> **定义 3（Hermitian 内积）**：对 $\mathbf{u}, \mathbf{v} \in \mathbb{C}^n$，标准 Hermitian 内积为：
>
> $$\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u}^* \mathbf{v} = \sum_{i=1}^{n} \overline{u_i} v_i$$
>
> 其中 $\overline{u_i}$ 是 $u_i$ 的复共轭，$\mathbf{u}^* = \overline{\mathbf{u}}^T$ 是 **共轭转置 (conjugate transpose)**。

与实内积的关键区别：
| 性质 | 实内积 | Hermitian 内积 |
|------|-------|---------------|
| 对称性 | $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$ | $\langle \mathbf{u}, \mathbf{v} \rangle = \overline{\langle \mathbf{v}, \mathbf{u} \rangle}$（共轭对称） |
| 线性性 | 对两个参数均线性 | 对第二个参数线性，对第一个参数**共轭**线性 |
| 正定性 | $\langle \mathbf{v}, \mathbf{v} \rangle \geq 0$ | $\langle \mathbf{v}, \mathbf{v} \rangle = \sum |v_i|^2 \geq 0$（自动实数） |

**共轭转置的矩阵记法**：对复矩阵 $A$，$A^* = \overline{A}^T$（在物理学中常记作 $A^\dagger$）。$A^*$ 是内积空间中对偶算子的自然表示——这是正交矩阵推广到复数域的关键一步。

**Hermitian 内积计算示例**：$\mathbf{u} = [1+i,\; 2-i]^T$, $\mathbf{v} = [3,\; i]^T \in \mathbb{C}^2$。
$$\langle \mathbf{u}, \mathbf{v} \rangle = \overline{(1+i)} \cdot 3 + \overline{(2-i)} \cdot i = (1-i) \cdot 3 + (2+i) \cdot i = 3 - 3i + 2i + i^2 = 3 - i - 1 = 2 - i$$
验证共轭对称性：$\langle \mathbf{v}, \mathbf{u} \rangle = \overline{3}(1+i) + \overline{i}(2-i) = 3(1+i) + (-i)(2-i) = 3+3i-2i+i^2 = 3+i-1 = 2+i = \overline{\langle \mathbf{u}, \mathbf{v} \rangle}$ ✓

> **定义 4（酉矩阵）**：复方阵 $U$ 是**酉矩阵 (unitary matrix)** $\iff U^* U = U U^* = I$，即 $U^{-1} = U^*$。

酉矩阵是实正交矩阵在复数域的自然推广：它保持 Hermitian 内积不变（$\langle U\mathbf{x}, U\mathbf{y} \rangle = \langle \mathbf{x}, \mathbf{y} \rangle$）。酉矩阵在量子力学（时间演化算符）、信号处理（DFT 矩阵）和数值线性代数（Householder 变换的复版本）中都是核心工具。

**超越 $\mathbb{R}^n$ 的例子**：

| 空间 | 内积定义 | 用途 |
|------|----------|------|
| $C[a,b]$ | $\langle f, g \rangle = \int_a^b f(x)g(x)\,dx$ | 函数空间 |
| $M_{m \times n}$ | $\langle A, B \rangle = \operatorname{tr}(A^T B)$ | 矩阵空间（Frobenius 内积） |
| $\ell^2$ | $\langle x, y \rangle = \sum_{i=1}^{\infty} x_i y_i$ | 平方可和序列 |

---

## 4. 范数 (Norm)

### 4.1 由内积诱导的范数

> **定义 5（内积诱导范数）**：
>
> $$\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$$

在 $\mathbb{R}^n$ 中，这就是欧几里得范数（$\ell_2$ 范数）：
$$\|\mathbf{v}\|_2 = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}$$

**基本性质**：
- $\|\mathbf{v}\| \geq 0$，等号 $\iff \mathbf{v} = \mathbf{0}$（正定性）
- $\|c\mathbf{v}\| = |c| \cdot \|\mathbf{v}\|$（绝对齐次性）
- $\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$（三角不等式）

**平行四边形法则 (Parallelogram Law)**：范数由内积诱导 $\iff$ 满足：
$$\|\mathbf{u} + \mathbf{v}\|^2 + \|\mathbf{u} - \mathbf{v}\|^2 = 2(\|\mathbf{u}\|^2 + \|\mathbf{v}\|^2)$$
几何意义：平行四边形对角线平方和 = 四边平方和。$\ell_2$ 范数满足此式；$\ell_1$ 和 $\ell_\infty$ 不满足——它们不由任何内积诱导。

### 4.2 $\ell_p$ 范数族

内积诱导的范数只是其中一种。一般 $\ell_p$ 范数定义：

> **定义 6（$\ell_p$ 范数）**：
>
> $$\|\mathbf{v}\|_p = \left(\sum_{i=1}^{n} |v_i|^p\right)^{1/p}, \quad p \geq 1$$

**三种最重要的 $\ell_p$ 范数**：

| 范数 | $p$ | 公式 | 几何（$\mathbb{R}^2$ 单位球） |
|------|-----|------|------------------------------|
| $\ell_1$ | 1 | $\sum \vert v_i \vert$ | 菱形 |
| $\ell_2$ | 2 | $\sqrt{\sum v_i^2}$ | 圆 |
| $\ell_{\infty}$ | $\infty$ | $\max_i \vert v_i \vert$ | 正方形 |

**$\ell_1$ vs $\ell_2$ 的差异**：
- $\ell_1$：分量绝对值的和（曼哈顿距离）
- $\ell_2$：欧几里得距离（直线距离）
- 在 ML 中，$\ell_1$ 正则化产生稀疏解，$\ell_2$ 正则化产生收缩解

### 4.3 一般范数公理

> **定义 7（范数公理）**：向量空间 $V$ 上的**范数**是函数 $\|\cdot\|: V \to \mathbb{R}$，满足：
>
> 1. $\|\mathbf{v}\| \geq 0$，等号 $\iff \mathbf{v} = \mathbf{0}$
> 2. $\|c\mathbf{v}\| = |c| \cdot \|\mathbf{v}\|$
> 3. $\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$

> **注意**：并非所有范数都来自内积。例如 $\ell_1$ 范数不满足平行四边形法则，因此不由任何内积诱导。

---

## 5. Cauchy-Schwarz 不等式

> **定理（Cauchy-Schwarz 不等式）**：对内积空间中的任意两向量：
>
> $$|\langle \mathbf{u}, \mathbf{v} \rangle| \leq \|\mathbf{u}\| \cdot \|\mathbf{v}\|$$
>
> 等号成立 $\iff \mathbf{u}$ 与 $\mathbf{v}$ 线性相关（共线）。

**在 $\mathbb{R}^n$ 中**：
$$\left|\sum_{i=1}^{n} u_i v_i\right| \leq \sqrt{\sum_{i=1}^{n} u_i^2} \cdot \sqrt{\sum_{i=1}^{n} v_i^2}$$

**证明**（标准技巧——构造二次函数）：

对任意 $t \in \mathbb{R}$，考虑 $\|\mathbf{u} - t\mathbf{v}\|^2 \geq 0$：
$$\langle \mathbf{u} - t\mathbf{v}, \mathbf{u} - t\mathbf{v} \rangle = \|\mathbf{u}\|^2 - 2t\langle \mathbf{u}, \mathbf{v} \rangle + t^2\|\mathbf{v}\|^2 \geq 0$$

这是 $t$ 的二次函数且恒非负。若 $\mathbf{v} = \mathbf{0}$，不等式显然成立（两边均为 0）。若 $\mathbf{v} \neq \mathbf{0}$，取 $t = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{v}\|^2}$ 代入得：
$$\|\mathbf{u}\|^2 - 2\frac{\langle \mathbf{u}, \mathbf{v} \rangle^2}{\|\mathbf{v}\|^2} + \frac{\langle \mathbf{u}, \mathbf{v} \rangle^2}{\|\mathbf{v}\|^2} = \|\mathbf{u}\|^2 - \frac{\langle \mathbf{u}, \mathbf{v} \rangle^2}{\|\mathbf{v}\|^2} \geq 0$$

整理即得 $|\langle \mathbf{u}, \mathbf{v} \rangle| \leq \|\mathbf{u}\| \cdot \|\mathbf{v}\|$。等号成立 $\iff \|\mathbf{u} - t\mathbf{v}\|^2 = 0 \iff \mathbf{u} = t\mathbf{v}$，即两向量共线。证毕

**重要推论**：
- 从几何角度，这等价于 $|\cos\theta| \leq 1$
- 三角不等式可由 Cauchy-Schwarz 直接推出
- 这是 Hölder 不等式在 $p=q=2$ 的特例

---

## 6. 正交性与正交补

### 6.1 正交性

> **定义 8（正交）**：两向量 $\mathbf{u}, \mathbf{v}$ **正交 (orthogonal)** $\iff \langle \mathbf{u}, \mathbf{v} \rangle = 0$。记作 $\mathbf{u} \perp \mathbf{v}$。

与「垂直」的区别：「垂直」是几何概念（仅适用于 $\mathbb{R}^2/\mathbb{R}^3$），「正交」是代数定义（适用于任何内积空间）。

### 6.2 正交补

> **定义 9（正交补）**：子空间 $W \subseteq V$ 的**正交补**：
>
> $$W^{\perp} = \{\mathbf{v} \in V \mid \langle \mathbf{v}, \mathbf{w} \rangle = 0 \text{ 对所有 } \mathbf{w} \in W\}$$

**性质**：
- $W^{\perp}$ 也是子空间
- $(W^{\perp})^{\perp} = W$（有限维空间）
- $V = W \oplus W^{\perp}$（直和分解）

**例子**：$\mathbb{R}^3$ 中，$W = \operatorname{span}\{[1, 0, 0]^T\}$（$x$ 轴），则 $W^{\perp}$ 是 $yz$ 平面（$\{[0, y, z]^T\}$）。

### 6.3 正交向量组

> **定义 10**：向量组 $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ 是**正交组** $\iff$ 两两正交：$\langle \mathbf{v}_i, \mathbf{v}_j \rangle = 0$（$i \neq j$）。

> **定理**：非零向量组成的正交组必然线性无关。

**证明**：设 $\sum c_i \mathbf{v}_i = \mathbf{0}$。对任意 $j$，两边与 $\mathbf{v}_j$ 做内积：$\langle \sum c_i \mathbf{v}_i, \mathbf{v}_j \rangle = \sum c_i \langle \mathbf{v}_i, \mathbf{v}_j \rangle = c_j \|\mathbf{v}_j\|^2 = 0$。因为 $\|\mathbf{v}_j\| \neq 0$，得 $c_j = 0$。证毕

**这为什么重要？** 正交基是数学上最「干净」的基——系数可以直接用内积计算，不需要解方程组。在复数域中，**酉矩阵的列**构成 $\mathbb{C}^n$ 的标准正交基（Hermitian 内积下），这是量子力学中「测量」算符的数学基础。

---

## 7. Gram-Schmidt 正交化

> **算法（Gram-Schmidt）**：给定线性无关组 $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$，构造正交组 $\{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$：
>
> 1. **初始化**：$\mathbf{u}_1 = \mathbf{v}_1$
> 2. **正交化**（$j = 2, \ldots, k$）：
>
>    $$\mathbf{u}_j = \mathbf{v}_j - \sum_{i=1}^{j-1} \frac{\langle \mathbf{v}_j, \mathbf{u}_i \rangle}{\langle \mathbf{u}_i, \mathbf{u}_i \rangle} \mathbf{u}_i$$
>
> 3. **归一化（可选）**：$\mathbf{e}_j = \frac{\mathbf{u}_j}{\|\mathbf{u}_j\|}$

**直觉**：每一步从 $\mathbf{v}_j$ 中减去它在前 $j-1$ 个正交向量上的投影，留下正交分量。

**注意**：若输入向量线性相关，则某步 $\mathbf{u}_j = \mathbf{0}$（因为 $\mathbf{v}_j$ 完全落在前 $j-1$ 个向量的张成空间中）。此时应丢弃该向量（它不提供新方向），继续处理下一个。最终得到的是 $\operatorname{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ 的一组正交基，向量个数 = 秩。

**例子**：将 $\mathbf{v}_1 = [1, 1, 0]^T$, $\mathbf{v}_2 = [1, 0, 1]^T$, $\mathbf{v}_3 = [0, 1, 1]^T$ 正交化。

- $\mathbf{u}_1 = [1, 1, 0]^T$
- $\mathbf{u}_2 = \mathbf{v}_2 - \frac{\langle \mathbf{v}_2, \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1, \mathbf{u}_1 \rangle} \mathbf{u}_1 = [1,0,1]^T - \frac{1}{2}[1,1,0]^T = [\frac{1}{2}, -\frac{1}{2}, 1]^T$
- $\mathbf{u}_3 = \mathbf{v}_3 - \frac{\langle \mathbf{v}_3, \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1, \mathbf{u}_1 \rangle} \mathbf{u}_1 - \frac{\langle \mathbf{v}_3, \mathbf{u}_2 \rangle}{\langle \mathbf{u}_2, \mathbf{u}_2 \rangle} \mathbf{u}_2 = \cdots$
  $= [0,1,1]^T - \frac{1}{2}[1,1,0]^T - \frac{\frac{1}{2}}{\frac{3}{2}}[\frac{1}{2}, -\frac{1}{2}, 1]^T = [-\frac{2}{3}, \frac{2}{3}, \frac{2}{3}]^T$

验证：$\mathbf{u}_1 \cdot \mathbf{u}_2 = 0$, $\mathbf{u}_1 \cdot \mathbf{u}_3 = 0$, $\mathbf{u}_2 \cdot \mathbf{u}_3 = 0$。

---

## 8. 正交投影

> **定义 11（正交投影）**：向量 $\mathbf{v}$ 到子空间 $W$（有正交基 $\{\mathbf{w}_1, \ldots, \mathbf{w}_k\}$）的**正交投影**：
>
> $$\operatorname{proj}_W(\mathbf{v}) = \sum_{i=1}^{k} \frac{\langle \mathbf{v}, \mathbf{w}_i \rangle}{\langle \mathbf{w}_i, \mathbf{w}_i \rangle} \mathbf{w}_i$$

到单位向量的投影简化：
$$\operatorname{proj}_{\mathbf{u}}(\mathbf{v}) = \langle \mathbf{v}, \mathbf{u} \rangle \mathbf{u} \quad (\|\mathbf{u}\| = 1)$$

**投影与分解**：
- $\operatorname{proj}_W(\mathbf{v}) \in W$（投影在子空间内）
- $\mathbf{v} - \operatorname{proj}_W(\mathbf{v}) \in W^{\perp}$（误差与子空间正交）

> 换句话说：正交投影给出 $W$ 中与 $\mathbf{v}$「最接近」的向量。这是最小二乘法的基础（第 08 章）。

---

## 9. 单位向量与归一化

> **定义 12（单位向量）**：$\|\mathbf{u}\| = 1$ 的向量。

任何非零向量都可归一化：
$$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}$$

归一化后 $\|\hat{\mathbf{v}}\| = 1$。$\hat{\mathbf{v}}$ 保持原方向，只有长度变为 1。

---

## 10. 概念演示：内积与正交

> 本章的编程练习在 `编程题/` 目录下。运行 `python3 grader.py` 自动批改。

```python
import numpy as np

u = np.array([3, 4])
v = np.array([-4, 3])

# 内积 = 0 → 正交 → cos θ = 0 → θ = 90°
print(f"内积: {u @ v}")        # 0
print(f"∥u∥: {np.linalg.norm(u)}")   # 5.0

# Gram-Schmidt 的核心操作：减去投影
# 从 v 中减去在 u 上的投影，得到与 u 正交的分量
proj = (u @ v) / (u @ u) * u
orth_component = v - proj
print(f"投影: {proj}")           # [0. 0.]（v 本来就和 u 正交）
print(f"正交分量: {orth_component}")  # [-4.  3.]

# 示例：将非正交向量变为正交
a1 = np.array([1, 1])
a2 = np.array([1, 0])
proj_a2_on_a1 = (a2 @ a1) / (a1 @ a1) * a1  # = [0.5, 0.5]
u2 = a2 - proj_a2_on_a1                    # = [0.5, -0.5]
print(f"u1 · u2 = {a1 @ u2:.1f}")         # 0.0 ✓ 正交化成功
```

---

## 11. 例题

### 例 1：Cauchy-Schwarz 应用

验证 $\mathbf{u} = [1, 2, 3]^T$ 和 $\mathbf{v} = [4, 5, 6]^T$ 满足 Cauchy-Schwarz 不等式。

<details><summary>解</summary>

$|\langle \mathbf{u}, \mathbf{v} \rangle| = |32| = 32$
$\|\mathbf{u}\| = \sqrt{14} \approx 3.742$, $\|\mathbf{v}\| = \sqrt{77} \approx 8.775$
$\|\mathbf{u}\| \cdot \|\mathbf{v}\| \approx 32.83 \geq 32$。等号不成立（不共线）。✓

</details>

### 例 2：正交补

$\mathbb{R}^3$ 中 $W = \operatorname{span}\{[1, -1, 0]^T\}$，求 $W^{\perp}$ 的基。

<details><summary>解</summary>

$W^{\perp} = \{[x, y, z]^T \mid x - y = 0\} = \{[y, y, z]^T\} = \operatorname{span}\{[1, 1, 0]^T, [0, 0, 1]^T\}$。

验证：$[1, -1, 0]^T \cdot [1, 1, 0]^T = 0$，$[1, -1, 0]^T \cdot [0, 0, 1]^T = 0$。✓

</details>

---

## 12. 常见误区

| 误区 | 正确理解 |
|------|----------|
| 「内积就是点积」 | 点积是 $\mathbb{R}^n$ 上的标准内积；函数空间的内积是积分，矩阵空间的内积是 $\operatorname{tr}(A^T B)$ |
| 「所有范数都来自内积」 | $\ell_1$ 和 $\ell_{\infty}$ 不满足平行四边形法则，不由任何内积诱导 |
| 「正交 = 垂直」 | 「垂直」是 $\mathbb{R}^2/\mathbb{R}^3$ 的几何直觉；「正交」是任何内积空间中的代数条件 $\langle \mathbf{u}, \mathbf{v} \rangle = 0$ |
| 「Gram-Schmidt 不会出问题」 | 若输入线性相关，中间某步会产生零向量——需跳过该向量继续 |
| 「复内积和实内积一样」 | 复内积是 Hermitian（共轭对称），对第一个参数共轭线性而非线性 |
| 「酉矩阵就是复版本的正交矩阵而已」 | 本质正确，但 Hermitian 内积的共轭导致很多性质需要小心：$U^* U = I$ 而非 $U^T U = I$ |
| 「归一化就是除以长度」 | 对，但零向量不可归一化——方向不存在 |

---

## 本章核心概念速查

| 概念 | 定义 | 关键公式 |
|------|------|----------|
| 内积（点积） | $\sum u_i v_i$ | $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$ |
| Hermitian 内积 | $\sum \overline{u_i} v_i$ | 复向量空间的标准内积 |
| 共轭转置 | $A^* = \overline{A}^T$ | 复矩阵的伴随 |
| 酉矩阵 | $U^* U = I$ | 复正交矩阵；保 Hermitian 内积 |
| $\ell_2$ 范数 | $\sqrt{\sum v_i^2}$ | 欧几里得长度 |
| $\ell_1$ 范数 | $\sum \vert v_i \vert$ | 曼哈顿距离 |
| $\ell_{\infty}$ 范数 | $\max \vert v_i \vert$ | 最大分量 |
| Cauchy-Schwarz | $\vert\langle \mathbf{u},\mathbf{v} \rangle\vert \leq \|\mathbf{u}\|\|\mathbf{v}\|$ | 内积的绝对上界 |
| 正交 | $\langle \mathbf{u}, \mathbf{v} \rangle = 0$ | 广义垂直 |
| 正交补 | $\{\mathbf{v} \mid \mathbf{v} \perp W\}$ | 所有与子空间正交的向量 |
| Gram-Schmidt | $\mathbf{u}_j = \mathbf{v}_j - \sum \frac{\langle \mathbf{v}_j, \mathbf{u}_i \rangle}{\langle \mathbf{u}_i, \mathbf{u}_i \rangle} \mathbf{u}_i$ | 从任意基构造正交基 |
| 正交投影 | $\sum \frac{\langle \mathbf{v}, \mathbf{w}_i \rangle}{\langle \mathbf{w}_i, \mathbf{w}_i \rangle} \mathbf{w}_i$ | 到子空间的最近点 |
| 归一化 | $\mathbf{v}/\|\mathbf{v}\|$ | 长度变为 1 |

> **跨章连接**：本章的「到直线的正交投影」是 Ch08 最小二乘的基础。Gram-Schmidt 正交化在 Ch08 中以 **QR 分解**的矩阵形式重新出现——$A = QR$，其中 $Q$ 的列是正交化结果，$R$ 是上三角系数矩阵。

---

← 前置: [01 — 向量与向量空间](../01-向量与向量空间/notes.md)
→ 延伸: [03 — 矩阵与线性变换](../03-矩阵与线性变换/notes.md)
