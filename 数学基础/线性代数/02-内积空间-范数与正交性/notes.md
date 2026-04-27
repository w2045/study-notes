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

**超越 $\mathbb{R}^n$ 的例子**：

| 空间 | 内积定义 | 用途 |
|------|----------|------|
| $C[a,b]$ | $\langle f, g \rangle = \int_a^b f(x)g(x)\,dx$ | 函数空间 |
| $M_{m \times n}$ | $\langle A, B \rangle = \operatorname{tr}(A^T B)$ | 矩阵空间（Frobenius 内积） |
| $\ell^2$ | $\langle x, y \rangle = \sum_{i=1}^{\infty} x_i y_i$ | 平方可和序列 |

---

## 4. 范数 (Norm)

### 4.1 由内积诱导的范数

> **定义 3（内积诱导范数）**：
>
> $$\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$$

在 $\mathbb{R}^n$ 中，这就是欧几里得范数（$\ell_2$ 范数）：
$$\|\mathbf{v}\|_2 = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}$$

**基本性质**：
- $\|\mathbf{v}\| \geq 0$，等号 $\iff \mathbf{v} = \mathbf{0}$（正定性）
- $\|c\mathbf{v}\| = |c| \cdot \|\mathbf{v}\|$（绝对齐次性）
- $\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$（三角不等式）

### 4.2 $\ell_p$ 范数族

内积诱导的范数只是其中一种。一般 $\ell_p$ 范数定义：

> **定义 4（$\ell_p$ 范数）**：
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

> **定义 5（范数公理）**：向量空间 $V$ 上的**范数**是函数 $\|\cdot\|: V \to \mathbb{R}$，满足：
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

**重要推论**：
- 从几何角度，这等价于 $|\cos\theta| \leq 1$（显然）
- 从代数角度，这是 Holder 不等式在 $p=q=2$ 的特例

---

## 6. 正交性与正交补

### 6.1 正交性

> **定义 6（正交）**：两向量 $\mathbf{u}, \mathbf{v}$ **正交 (orthogonal)** $\iff \langle \mathbf{u}, \mathbf{v} \rangle = 0$。记作 $\mathbf{u} \perp \mathbf{v}$。

与「垂直」的区别：「垂直」是几何概念（仅适用于 $\mathbb{R}^2/\mathbb{R}^3$），「正交」是代数定义（适用于任何内积空间）。

### 6.2 正交补

> **定义 7（正交补）**：子空间 $W \subseteq V$ 的**正交补**：
>
> $$W^{\perp} = \{\mathbf{v} \in V \mid \langle \mathbf{v}, \mathbf{w} \rangle = 0 \text{ 对所有 } \mathbf{w} \in W\}$$

**性质**：
- $W^{\perp}$ 也是子空间
- $(W^{\perp})^{\perp} = W$（有限维空间）
- $V = W \oplus W^{\perp}$（直和分解）

**例子**：$\mathbb{R}^3$ 中，$W = \operatorname{span}\{[1, 0, 0]^T\}$（$x$ 轴），则 $W^{\perp}$ 是 $yz$ 平面（$\{[0, y, z]^T\}$）。

### 6.3 正交向量组

> **定义 8**：向量组 $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ 是**正交组** $\iff$ 两两正交：$\langle \mathbf{v}_i, \mathbf{v}_j \rangle = 0$（$i \neq j$）。

> **定理**：非零向量组成的正交组必然线性无关。

**这为什么重要？** 正交基是数学上最「干净」的基——系数可以直接用内积计算，不需要解方程组。

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

**例子**：将 $\mathbf{v}_1 = [1, 1, 0]^T$, $\mathbf{v}_2 = [1, 0, 1]^T$, $\mathbf{v}_3 = [0, 1, 1]^T$ 正交化。

- $\mathbf{u}_1 = [1, 1, 0]^T$
- $\mathbf{u}_2 = \mathbf{v}_2 - \frac{\langle \mathbf{v}_2, \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1, \mathbf{u}_1 \rangle} \mathbf{u}_1 = [1,0,1]^T - \frac{1}{2}[1,1,0]^T = [\frac{1}{2}, -\frac{1}{2}, 1]^T$
- $\mathbf{u}_3 = \mathbf{v}_3 - \frac{\langle \mathbf{v}_3, \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1, \mathbf{u}_1 \rangle} \mathbf{u}_1 - \frac{\langle \mathbf{v}_3, \mathbf{u}_2 \rangle}{\langle \mathbf{u}_2, \mathbf{u}_2 \rangle} \mathbf{u}_2 = \cdots$
  $= [0,1,1]^T - \frac{1}{2}[1,1,0]^T - \frac{\frac{1}{2}}{\frac{3}{2}}[\frac{1}{2}, -\frac{1}{2}, 1]^T = [-\frac{2}{3}, \frac{2}{3}, \frac{2}{3}]^T$

验证：$\mathbf{u}_1 \cdot \mathbf{u}_2 = 0$, $\mathbf{u}_1 \cdot \mathbf{u}_3 = 0$, $\mathbf{u}_2 \cdot \mathbf{u}_3 = 0$。

---

## 8. 正交投影

> **定义 9（正交投影）**：向量 $\mathbf{v}$ 到子空间 $W$（有正交基 $\{\mathbf{w}_1, \ldots, \mathbf{w}_k\}$）的**正交投影**：
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

> **定义 10（单位向量）**：$\|\mathbf{u}\| = 1$ 的向量。

任何非零向量都可归一化：
$$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}$$

归一化后 $\|\hat{\mathbf{v}}\| = 1$。$\hat{\mathbf{v}}$ 保持原方向，只有长度变为 1。

---

## 10. 代码实现

```python
from __future__ import annotations
import math
from typing import List


def dot(u: List[float], v: List[float]) -> float:
    """向量点积。"""
    return sum(a * b for a, b in zip(u, v))


def norm(v: List[float], p: float = 2.0) -> float:
    """ℓp 范数。p=1, 2, float('inf')。"""
    if p == float('inf'):
        return max(abs(x) for x in v)
    return sum(abs(x) ** p for x in v) ** (1.0 / p)


def normalize(v: List[float]) -> List[float]:
    """归一化（ℓ2 范数）。"""
    n = norm(v)
    if n == 0:
        raise ValueError("零向量不可归一化")
    return [x / n for x in v]


def cosine_similarity(u: List[float], v: List[float]) -> float:
    """余弦相似度 = cos θ = (u·v)/(||u||·||v||)。"""
    return dot(u, v) / (norm(u) * norm(v))


def is_orthogonal(u: List[float], v: List[float]) -> bool:
    """判断是否正交。"""
    return math.isclose(dot(u, v), 0)


def projection(u: List[float], v: List[float]) -> List[float]:
    """v 到 u 上的正交投影（u 无需是单位向量）。"""
    coeff = dot(v, u) / dot(u, u)
    return [coeff * x for x in u]


def gram_schmidt(vectors: List[List[float]]) -> List[List[float]]:
    """给定线性无关组，返回正交组（非归一化）。"""
    result = []
    for v in vectors:
        u = list(v)
        for existing in result:
            coeff = dot(v, existing) / dot(existing, existing)
            u = [u[i] - coeff * existing[i] for i in range(len(u))]
        result.append(u)
    return result
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

## 本章核心概念速查

| 概念 | 定义 | 关键公式 |
|------|------|----------|
| 内积（点积） | $\sum u_i v_i$ | $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$ |
| $\ell_2$ 范数 | $\sqrt{\sum v_i^2}$ | 欧几里得长度 |
| $\ell_1$ 范数 | $\sum \vert v_i \vert$ | 曼哈顿距离 |
| $\ell_{\infty}$ 范数 | $\max \vert v_i \vert$ | 最大分量 |
| Cauchy-Schwarz | $\vert\langle \mathbf{u},\mathbf{v} \rangle\vert \leq \|\mathbf{u}\|\|\mathbf{v}\|$ | 内积的绝对上界 |
| 正交 | $\langle \mathbf{u}, \mathbf{v} \rangle = 0$ | 广义垂直 |
| 正交补 | $\{\mathbf{v} \mid \mathbf{v} \perp W\}$ | 所有与子空间正交的向量 |
| Gram-Schmidt | $\mathbf{u}_j = \mathbf{v}_j - \sum \frac{\langle \mathbf{v}_j, \mathbf{u}_i \rangle}{\langle \mathbf{u}_i, \mathbf{u}_i \rangle} \mathbf{u}_i$ | 从任意基构造正交基 |
| 正交投影 | $\sum \frac{\langle \mathbf{v}, \mathbf{w}_i \rangle}{\langle \mathbf{w}_i, \mathbf{w}_i \rangle} \mathbf{w}_i$ | 到子空间的最近点 |
| 归一化 | $\mathbf{v}/\|\mathbf{v}\|$ | 长度变为 1 |

---

← 前置: [01 — 向量与向量空间](../01-向量与向量空间/notes.md)
→ 延伸: [03 — 矩阵与线性变换](../03-矩阵与线性变换/notes.md)
