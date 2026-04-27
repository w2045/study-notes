# 线性代数 · 第一章 · 向量、线性组合与向量空间

← 前置: 无（本系列起点）
→ 延伸: [02 — 矩阵与线性变换](../02-矩阵与线性变换/notes.md)

---

## 1. 直觉引入：向量的三种面孔

在深入定义之前，先建立三种互补的直觉——它们分别来自物理、计算机和数学：

**物理面孔**：向量是空间中的箭头——有长度、有方向。两个箭头可以「接在一起 」（平行四边形法则），也可以「拉长缩短」（标量乘法）。

**计算机面孔**：向量是一个有序的数字列表。一张 28×28 的灰度手写数字图片 = 784 个数 = $\mathbb{R}^{784}$ 中的向量。一个 GPT embedding = $\mathbb{R}^{768}$ 中的向量。

**数学面孔**：向量是「可以加法、可以标量乘法、且满足八条公理」的抽象对象。多项式、矩阵、连续函数都可以是向量。

> **核心洞察**：这三种面孔共享同一套代数规则。学会一套规则后，你可以在物理、编程、数学三个世界之间自由切换。

---

## 2. 向量的形式化定义

> **定义 1（$\mathbb{R}^n$ 中的向量）**：一个 **n 维实向量** 是 $n$ 个实数的一个有序序列：
>
> $$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}, \quad v_i \in \mathbb{R}$$
>
> 其中 $v_i$ 称为 $\mathbf{v}$ 的第 $i$ 个**分量 (component)**。所有 $n$ 维实向量构成的集合记作 $\mathbb{R}^n$。

**符号约定**：本书中向量用粗体小写 $\mathbf{v}, \mathbf{x}, \mathbf{w}$，标量用普通小写 $c, \lambda, \alpha$。默认向量是**列向量**，横写时加转置 $[v_1, \ldots, v_n]^T$。

两个向量相等 $\iff$ 维数相同且每个对应分量相等。

### 2.1 特殊向量

| 名称 | 记法 | 例子 ($\mathbb{R}^3$) |
|------|------|----------------------|
| 零向量 | $\mathbf{0}$ | $[0, 0, 0]^T$ |
| 标准基向量 | $\mathbf{e}_i$ | $\mathbf{e}_1 = [1,0,0]^T$, $\mathbf{e}_2 = [0,1,0]^T$, $\mathbf{e}_3 = [0,0,1]^T$ |
| 全 1 向量 | $\mathbf{1}$ | $[1, 1, 1]^T$ |

---

## 3. 向量运算：加法和标量乘法

### 3.1 向量加法

> **定义 2（加法）**：$\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$，定义逐分量加法：
>
> $$\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 \\ \vdots \\ u_n \end{bmatrix} + \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} u_1 + v_1 \\ \vdots \\ u_n + v_n \end{bmatrix}$$

**几何意义**：平行四边形法则——将 $\mathbf{v}$ 的起点平移到 $\mathbf{u}$ 的终点，从 $\mathbf{u}$ 起点到 $\mathbf{v}$ 终点的箭头就是 $\mathbf{u}+\mathbf{v}$。

**代数性质**（$\forall \mathbf{u}, \mathbf{v}, \mathbf{w} \in \mathbb{R}^n$）：
- 交换律：$\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$
- 结合律：$(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$
- 加法单位元：$\mathbf{v} + \mathbf{0} = \mathbf{v}$
- 加法逆元：$\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$，其中 $-\mathbf{v} = [-v_1, \ldots, -v_n]^T$

### 3.2 标量乘法

> **定义 3（标量乘法）**：对 $c \in \mathbb{R}$ 和 $\mathbf{v} \in \mathbb{R}^n$：
>
> $$c \cdot \mathbf{v} = c \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} c v_1 \\ \vdots \\ c v_n \end{bmatrix}$$

**几何意义**：$c > 1$ 是拉伸，$0 < c < 1$ 是压缩，$c < 0$ 是反转方向同时缩放。这称为**缩放 (scaling)**。

**代数性质**：
- 分配律 I：$c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$
- 分配律 II：$(c + d)\mathbf{v} = c\mathbf{v} + d\mathbf{v}$
- 结合律：$c(d\mathbf{v}) = (cd)\mathbf{v}$
- 单位元：$1 \cdot \mathbf{v} = \mathbf{v}$

---

## 4. 线性组合：代数的核心

> **定义 4（线性组合）**：给定向量 $\mathbf{v}_1, \ldots, \mathbf{v}_k \in \mathbb{R}^n$ 和标量 $c_1, \ldots, c_k \in \mathbb{R}$：
>
> $$\mathbf{w} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k$$
>
> 称 $\mathbf{w}$ 是 $\mathbf{v}_1, \ldots, \mathbf{v}_k$ 的一个**线性组合 (linear combination)**。$c_1, \ldots, c_k$ 称为**系数 (coefficients)**。

这是线性代数中最核心的操作——线性组合回答了这个问题：**给定几个基本方向，我能抵达哪些地方？**

**例子**：在 $\mathbb{R}^2$ 中，取 $\mathbf{v}_1 = [1, 0]^T$（向右）和 $\mathbf{v}_2 = [0, 1]^T$（向上）。则任意点 $[x, y]^T = x\mathbf{v}_1 + y\mathbf{v}_2$。

**例子**：如果 $\mathbf{v}_1 = [1, 0]^T$ 和 $\mathbf{v}_2 = [2, 0]^T$（同方向），组合只能产生 x 轴上的点。这说明线性组合的能力完全取决于「给的方向有多独立」。

---

## 5. 张成空间 (Span)

> **定义 5（张成空间）**：$\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ 的所有线性组合构成的集合叫做它们的**张成空间**：
>
> $$\operatorname{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\} = \left\{\sum_{i=1}^{k} c_i\mathbf{v}_i \;\middle|\; c_i \in \mathbb{R}\right\}$$

**几何直觉**：

| 情况 | Span 是什么 |
|------|------------|
| 一个非零向量 | 穿过原点的一条直线 |
| 两个不共线向量 | 穿过原点的平面 |
| 三个不共面向量 | 整个 $\mathbb{R}^3$ |
| 零向量 | 只有原点 $\{\mathbf{0}\}$ |

**重要定理**：$\operatorname{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ 总是 $\mathbb{R}^n$ 的**子空间**（后面证明）。

---

## 6. 线性无关与线性相关

> **定义 6（线性无关）**：向量 $\mathbf{v}_1, \ldots, \mathbf{v}_k$ 是**线性无关 (linearly independent)** 的，如果方程
>
> $$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0}$$
>
> **只有零解** $c_1 = c_2 = \cdots = c_k = 0$。如果存在非零解，则它们是**线性相关 (linearly dependent)** 的。

**直觉翻译**：线性无关 = 集合中没有冗余。每个向量都提供了「新的方向」，不能被其他向量组合出来。

**关键事实**：
- 两个向量线性相关 $\iff$ 共线（一个是另一个的标量倍）
- $\mathbb{R}^n$ 中，向量数 $k > n \implies$ 必然线性相关
- 如果集合包含零向量，必线性相关（取该向量的系数为 1，其余为 0）

**判定方法**：对于 $\mathbb{R}^n$ 中的 $k$ 个向量，把方程 $c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k = \mathbf{0}$ 写成一个 $n \times k$ 的齐次方程组。若唯一解为零解，则是线性无关的。（这将在第三章用高斯消元法系统解决。）

---

## 7. 向量空间：公理化定义

$\mathbb{R}^n$ 是我们最熟悉的例子，但向量空间的概念远不止于此。数学的力量在于抽象：把 $\mathbb{R}^n$ 中成立的规则提炼成公理，任何满足公理的对象都自动继承全部线性代数定理。

> **定义 7（实向量空间）**：一个**实向量空间**由非空集合 $V$、加法 $+$、标量乘法 $\cdot$ 组成，满足以下 **10 条公理**（$\forall \mathbf{u}, \mathbf{v}, \mathbf{w} \in V,\; c, d \in \mathbb{R}$）：
>
> | # | 公理 | 名称 |
> |---|------|------|
> | 1 | $\mathbf{u} + \mathbf{v} \in V$ | 加法封闭 |
> | 2 | $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ | 加法交换律 |
> | 3 | $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$ | 加法结合律 |
> | 4 | $\exists \mathbf{0} \in V: \mathbf{u} + \mathbf{0} = \mathbf{u}$ | 零元存在 |
> | 5 | $\exists (-\mathbf{u}) \in V: \mathbf{u} + (-\mathbf{u}) = \mathbf{0}$ | 加法逆元存在 |
> | 6 | $c \cdot \mathbf{u} \in V$ | 标量乘法封闭 |
> | 7 | $c \cdot (\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$ | 分配律 I |
> | 8 | $(c + d) \cdot \mathbf{u} = c\mathbf{u} + d\mathbf{u}$ | 分配律 II |
> | 9 | $c \cdot (d \cdot \mathbf{u}) = (cd) \cdot \mathbf{u}$ | 标量结合律 |
> | 10 | $1 \cdot \mathbf{u} = \mathbf{u}$ | 标量单位元 |

**核心思想**：10 条公理 = 一句话——「加法和标量乘法可以像 $\mathbb{R}^n$ 一样安全地操作」。

### 7.1 超越 $\mathbb{R}^n$ 的例子

| 向量空间 | 元素 | 「向量」的样子 | 维数 |
|----------|------|---------------|------|
| $\mathbb{R}^n$ | n 维实数组 | $[v_1, \ldots, v_n]^T$ | $n$ |
| $P_n$ | 次数 ≤ $n$ 的多项式 | $a_0 + a_1x + \cdots + a_nx^n$ | $n+1$ |
| $M_{m \times n}$ | $m \times n$ 矩阵 | $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ | $mn$ |
| $C[a,b]$ | $[a,b]$ 上的连续函数 | $f(x) = \sin(x)$ | 无穷 |
| $\ell^2$ | 平方可和序列 | $(a_1, a_2, \ldots)$ | 无穷 |

> **关键洞察**：多项式 $3 + 2x - x^3$ 可看作系数向量 $[3, 2, 0, -1]^T$。$f(x) = \sin(x)$ 的泰勒级数是无穷维向量。**任何可以表示为「一组系数的线性组合」的东西，全部线性代数定理都对它适用**。这就是为什么线性代数在 ML 中无处不在。

---

## 8. 子空间

> **定义 8（子空间）**：$V$ 的子集 $W \subseteq V$ 是**子空间**，如果 $W$ 本身也是向量空间（在 $V$ 的加法和标量乘法下）。

要验证 $W$ 是子空间，只需检查**三条**（其余七条公理自动从 $V$ 继承）：

1. $\mathbf{0} \in W$（零向量在 $W$ 中）
2. $\mathbf{u}, \mathbf{v} \in W \implies \mathbf{u} + \mathbf{v} \in W$（加法封闭）
3. $\mathbf{u} \in W, c \in \mathbb{R} \implies c\mathbf{u} \in W$（标量乘法封闭）

### 8.1 经典例子

**例 1**：$W = \{[x, y]^T \in \mathbb{R}^2 \mid y = 3x\}$（经过原点的直线）

验证：
1. $[0,0]^T$ 满足 $0 = 3 \cdot 0$ ✓
2. $[x_1, 3x_1]^T + [x_2, 3x_2]^T = [x_1+x_2, 3(x_1+x_2)]^T \in W$ ✓
3. $c[x, 3x]^T = [cx, 3cx]^T \in W$ ✓

所以 $W$ 是 $\mathbb{R}^2$ 的子空间。注意 $\dim W = 1$，因为 $W = \operatorname{span}\{[1, 3]^T\}$。

**例 2**：$S = \{[x, y]^T \in \mathbb{R}^2 \mid y = x + 1\}$（不经过原点的直线）

$[0, 0]^T$ 不满足 $y = x + 1$，所以 $\mathbf{0} \notin S$。$S$ 不是子空间。

> **几何记忆**：只有**经过原点**的直线/平面/超平面才可能是子空间。

### 8.2 子空间交

> **定理**：若 $U$ 和 $W$ 是 $V$ 的子空间，则 $U \cap W$ 也是 $V$ 的子空间。

**证明**：
1. $\mathbf{0} \in U \cap W$（它在两者中） ✓
2. $\mathbf{x}, \mathbf{y} \in U \cap W \implies \mathbf{x}+\mathbf{y} \in U$ 且 $\in W \implies \mathbf{x}+\mathbf{y} \in U \cap W$ ✓
3. 同理于标量乘法 ✓

> **警告**：$U \cup W$ 一般**不是**子空间！如 $\mathbb{R}^2$ 中 x 轴 ∪ y 轴：$[1,0]^T + [0,1]^T = [1,1]^T \notin$ 并集。

---

## 9. 基与维数

### 9.1 基的定义

> **定义 9（基）**：向量空间 $V$ 的一组**基 (basis)** 是一组向量 $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$，满足：
> 1. $\mathcal{B}$ 是线性无关的
> 2. $\operatorname{span}(\mathcal{B}) = V$

**直觉**：「描述整个空间所需的最少向量」。每个 $\mathbf{v} \in V$ 都**唯一地**写成基向量的线性组合：

$$\mathbf{v} = c_1\mathbf{b}_1 + c_2\mathbf{b}_2 + \cdots + c_n\mathbf{b}_n$$

**唯一性证明**：若 $\mathbf{v} = \sum c_i \mathbf{b}_i = \sum d_i \mathbf{b}_i$，则 $\sum (c_i - d_i)\mathbf{b}_i = \mathbf{0}$。由线性无关性，$c_i - d_i = 0$，即 $c_i = d_i$。$\square$

### 9.2 维数

> **定义 10（维数）**：$\dim V =$ 基中向量的个数。

核心定理：**一个向量空间的所有基都有相同数量的向量**。这保证了维数定义的良定性。

**标准基的例子**：

| 空间 | 标准基 | $\dim$ |
|------|--------|--------|
| $\mathbb{R}^n$ | $\mathbf{e}_1, \ldots, \mathbf{e}_n$ | $n$ |
| $P_2$ | $\{1, x, x^2\}$ | $3$ |
| $M_{2 \times 2}$ | $\left\{\begin{bmatrix}1&0\\0&0\end{bmatrix}, \begin{bmatrix}0&1\\0&0\end{bmatrix}, \begin{bmatrix}0&0\\1&0\end{bmatrix}, \begin{bmatrix}0&0\\0&1\end{bmatrix}\right\}$ | $4$ |

### 9.3 维数公式

> **定理**：若 $W$ 是 $V$ 的子空间，则 $\dim W \leq \dim V$。等号成立 $\iff W = V$。

> **定理（维数公式）**：对 $V$ 的任意两个子空间 $U, W$：
>
> $$\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$$
>
> 其中 $U + W = \{\mathbf{u} + \mathbf{w} \mid \mathbf{u} \in U, \mathbf{w} \in W\}$。

> **推论**：对 $\mathbb{R}^3$ 中两个穿过原点的不同平面（每个 $\dim = 2$），它们交集是直线（$\dim = 1$）：$2 + 2 - 1 = 3$（整个 $\mathbb{R}^3$）。

---

## 10. 内积与范数

### 10.1 点积

> **定义 11（标准内积/点积）**：对 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$：
>
> $$\mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + \cdots + u_nv_n = \sum_{i=1}^{n} u_i v_i$$

**几何意义**：$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos \theta$，其中 $\theta$ 是两向量夹角。

由此得出关键判定：
- $\mathbf{u} \cdot \mathbf{v} = 0 \iff \mathbf{u} \perp \mathbf{v}$（垂直/正交）
- $\mathbf{u} \cdot \mathbf{v} > 0 \iff$ 夹角 < 90°（方向相似）
- $\mathbf{u} \cdot \mathbf{v} < 0 \iff$ 夹角 > 90°（方向相反）

### 10.2 范数（长度）

> **定义 12（欧几里得范数/$\ell_2$ 范数）**：
>
> $$\|\mathbf{v}\|_2 = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2} = \sqrt{\mathbf{v} \cdot \mathbf{v}}$$

**性质**：
- $\|\mathbf{v}\| \geq 0$，且 $\|\mathbf{v}\| = 0 \iff \mathbf{v} = \mathbf{0}$
- $\|c\mathbf{v}\| = |c| \cdot \|\mathbf{v}\|$
- **三角不等式**：$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$

**单位向量**：$\|\mathbf{u}\| = 1$ 的向量。任何非零向量都可以归一化：$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}$。

### 10.3 余弦相似度

在 ML 中（尤其 NLP），经常用余弦相似度衡量两个向量的「方向接近程度」：

$$\operatorname{cosine\_sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|} = \cos \theta$$

值域 $[-1, 1]$。等于 $1$ = 同方向，$0$ = 正交，$-1$ = 反方向。

---

## 11. 代码实现

```python
from __future__ import annotations
import math
from typing import List, Optional


class Vector:
    """n 维实向量。"""

    def __init__(self, components: List[float]):
        if not components:
            raise ValueError("向量不能为空")
        self._data = list(components)

    @property
    def dim(self) -> int:
        return len(self._data)

    def __getitem__(self, i: int) -> float:
        return self._data[i]

    def __repr__(self) -> str:
        return f"Vector({self._data})"

    # ─── 加法 ───
    def __add__(self, other: Vector) -> Vector:
        if self.dim != other.dim:
            raise ValueError(f"维数不匹配: {self.dim} vs {other.dim}")
        return Vector([a + b for a, b in zip(self._data, other._data)])

    def __neg__(self) -> Vector:
        return Vector([-x for x in self._data])

    def __sub__(self, other: Vector) -> Vector:
        return self + (-other)

    # ─── 标量乘法 ───
    def __mul__(self, scalar: float) -> Vector:
        return Vector([x * scalar for x in self._data])

    def __rmul__(self, scalar: float) -> Vector:
        return self.__mul__(scalar)

    # ─── 相等判断（支持浮点误差） ───
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        if self.dim != other.dim:
            return False
        return all(math.isclose(a, b) for a, b in zip(self._data, other._data))

    # ─── 零向量 ───
    @staticmethod
    def zero(dim: int) -> Vector:
        return Vector([0.0] * dim)

    # ─── 范数 ───
    def norm(self, p: int = 2) -> float:
        """ℓ_p 范数。p=2 为欧氏长度（默认）。"""
        if p == 2:
            return math.sqrt(sum(x**2 for x in self._data))
        if p == 1:
            return sum(abs(x) for x in self._data)
        if p == float('inf'):
            return max(abs(x) for x in self._data)
        return sum(abs(x)**p for x in self._data) ** (1/p)

    def normalize(self) -> Vector:
        n = self.norm()
        if n == 0:
            raise ValueError("零向量不能归一化")
        return (1.0 / n) * self

    # ─── 内积 ───
    def dot(self, other: Vector) -> float:
        if self.dim != other.dim:
            raise ValueError(f"维数不匹配")
        return sum(a * b for a, b in zip(self._data, other._data))

    def cosine_sim(self, other: Vector) -> float:
        """余弦相似度。"""
        return self.dot(other) / (self.norm() * other.norm())

    # ─── 线性组合 ───
    @staticmethod
    def linear_combination(
        vectors: List[Vector], coefficients: List[float]
    ) -> Vector:
        """计算 c1*v1 + c2*v2 + ... + ck*vk。"""
        if len(vectors) != len(coefficients):
            raise ValueError("向量与系数数量必须相等")
        if not vectors:
            raise ValueError("列表不能为空")
        result = Vector.zero(vectors[0].dim)
        for c, v in zip(coefficients, vectors):
            result = result + c * v  # type: ignore
        return result

    # ─── 线性无关判定（将纳入下一章用矩阵重写） ───
    @staticmethod
    def are_linearly_independent(vectors: List[Vector]) -> bool:
        """用简单规则判定（仅适用于小维度/特殊情形）。"""
        n = len(vectors)
        if n == 0:
            return True
        if n > vectors[0].dim:
            return False   # ℝ^n 中超过 n 个向量必相关
        if n == 1:
            return vectors[0].norm() != 0
        if n == 2:
            a, b = vectors[0], vectors[1]
            return abs(a.dot(b)) != a.norm() * b.norm()  # 共线 ⇔ 余弦绝对值=1
        # 一般情况：需要秩或行列式 → 后续章节补充
        raise NotImplementedError("3 个及以上向量的一般判定见第 3-4 章")
```

### 11.1 使用示例

```python
# 标准基
e1, e2, e3 = Vector([1,0,0]), Vector([0,1,0]), Vector([0,0,1])

# 线性组合
v = Vector.linear_combination([e1, e2, e3], [3, 4, 5])
print(v)                     # Vector([3.0, 4.0, 5.0])

# 运算
w = Vector([1, -1, 0])
print(v + w)                 # Vector([4.0, 3.0, 5.0])
print(2.0 * v)               # Vector([6.0, 8.0, 10.0])

# 范数与归一化
print(v.norm())              # 7.071...
u = v.normalize()
print(u.norm())              # 1.0

# 内积与余弦相似度
print(e1.dot(e2))            # 0.0 (正交)
print(v.cosine_sim(2*v))    # 1.0 (同方向)
```

---

## 12. 重要的定理证明

### 12.1 零元唯一性

> **定理**：向量空间中零向量是唯一的。

**证明**：设 $\mathbf{0}_1$ 和 $\mathbf{0}_2$ 都满足零元性质。则：
$$\mathbf{0}_1 = \mathbf{0}_1 + \mathbf{0}_2 \quad\text{（因为 }\mathbf{0}_2\text{ 是零元）}$$
$$= \mathbf{0}_2 + \mathbf{0}_1 \quad\text{（加法交换律）}$$
$$= \mathbf{0}_2 \quad\text{（因为 }\mathbf{0}_1\text{ 是零元）}$$

所以 $\mathbf{0}_1 = \mathbf{0}_2$。$\square$

### 12.2 子空间判别简化

> **定理**：$V$ 的非空子集 $W$ 是子空间 $\iff$ 对所有 $\mathbf{u}, \mathbf{v} \in W$ 和 $c \in \mathbb{R}$，有 $c\mathbf{u} + \mathbf{v} \in W$。

**证明**：这一条等价于同时验证加法封闭（$c=1$）和标量乘法封闭（$\mathbf{v}=\mathbf{0}$）。包含 $\mathbf{0}$ 由 $c=0, \mathbf{v}=\mathbf{u}$ 得到。$\square$

### 12.3 线性无关与 span

> **定理**：若 $\mathbf{v}_1, \ldots, \mathbf{v}_k$ 线性无关，且 $\mathbf{v}_{k+1} \notin \operatorname{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$，则 $\mathbf{v}_1, \ldots, \mathbf{v}_k, \mathbf{v}_{k+1}$ 也线性无关。

**证明**：设 $c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k + c_{k+1}\mathbf{v}_{k+1} = \mathbf{0}$。若 $c_{k+1} \neq 0$，则 $\mathbf{v}_{k+1} = -\frac{1}{c_{k+1}}\sum c_i \mathbf{v}_i \in \operatorname{span}$，矛盾。故 $c_{k+1} = 0$，归约到前 $k$ 个的线性无关性，得全零解。$\square$

---

## 13. 例题

### 例 1：判定向量空间

**问题**：$W = \{[x, y, z]^T \in \mathbb{R}^3 \mid 2x - y + z = 0\}$ 是否是 $\mathbb{R}^3$ 的子空间？若是，给出它的维数和一组基。

<details><summary>解</summary>

验证三条：
1. $\mathbf{0} = [0,0,0]^T$：$2\cdot0 - 0 + 0 = 0$ ✓
2. 设 $\mathbf{u} = [x_1, y_1, z_1]^T, \mathbf{v} = [x_2, y_2, z_2]^T \in W$。则 $2(x_1+x_2) - (y_1+y_2) + (z_1+z_2) = (2x_1-y_1+z_1) + (2x_2-y_2+z_2) = 0 + 0 = 0$ ✓
3. $c\mathbf{u}$：$2(cx_1) - (cy_1) + (cz_1) = c(2x_1 - y_1 + z_1) = 0$ ✓

所以 $W$ 是子空间。为求基，改写条件 $z = -2x + y$：

$$\mathbf{w} = \begin{bmatrix} x \\ y \\ -2x + y \end{bmatrix} = x\begin{bmatrix} 1 \\ 0 \\ -2 \end{bmatrix} + y\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$$

基 $\mathcal{B} = \{[1,0,-2]^T, [0,1,1]^T\}$，线性无关（不共线），$\dim W = 2$。

</details>

### 例 2：内积计算

**问题**：求 $\mathbf{u} = [3, 4]^T$ 和 $\mathbf{v} = [1, 2]^T$ 的内积、范数、夹角余弦。

<details><summary>解</summary>

$$\mathbf{u} \cdot \mathbf{v} = 3 \cdot 1 + 4 \cdot 2 = 11$$
$$\|\mathbf{u}\| = \sqrt{9+16} = 5,\quad \|\mathbf{v}\| = \sqrt{1+4} = \sqrt{5}$$
$$\cos\theta = \frac{11}{5\sqrt{5}} \approx 0.9839 \implies \theta \approx 10.3^\circ$$

</details>

### 例 3：线性无关判定

**问题**：判断 $\mathbf{v}_1 = [1, 2, 3]^T$，$\mathbf{v}_2 = [4, 5, 6]^T$，$\mathbf{v}_3 = [7, 8, 9]^T$ 是否线性无关。

<details><summary>解</summary>

设 $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0}$。写出方程组：
$$\begin{cases} c_1 + 4c_2 + 7c_3 = 0 \\ 2c_1 + 5c_2 + 8c_3 = 0 \\ 3c_1 + 6c_2 + 9c_3 = 0 \end{cases}$$

②−2×①：$-3c_2 - 6c_3 = 0 \implies c_2 = -2c_3$

③−3×①：$-6c_2 - 12c_3 = 0 \implies c_2 = -2c_3$（一致）

①：$c_1 + 4(-2c_3) + 7c_3 = c_1 - c_3 = 0 \implies c_1 = c_3$

取 $c_3 = 1$，得非零解 $(1, -2, 1)$。所以向量线性相关。事实上 $\mathbf{v}_3 = 2\mathbf{v}_2 - \mathbf{v}_1$。

</details>

---

## 14. 本章核心概念速查

| 概念 | 定义 | 几何直觉 |
|------|------|----------|
| 向量 | n 个有序实数 | 箭头 (ℝ²/ℝ³) 或数据点 (ℝⁿ) |
| 加法 | 逐分量相加 | 平行四边形法则 |
| 标量乘法 | 逐分量乘 | 拉伸/压缩/反转 |
| 线性组合 | $\sum c_i\mathbf{v}_i$ | 「从这个方向走 c₁ 步，那个方向走 c₂ 步」 |
| 张成 (span) | 所有线性组合的集合 | 「这些方向能到达的所有地方」 |
| 线性无关 | 只有零解 | 「没有冗余」 |
| 基 | 线性无关 + span 整个空间 | 「描述空间的最少向量组」 |
| 维数 | 基中向量个数 | 「空间有多少个独立方向」 |
| 子空间 | 继承向量空间结构的子集 | 经过原点的直线/平面 |
| 点积 | $\sum u_i v_i$ | $\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$ |
| 范数 | $\sqrt{\sum v_i^2}$ | 到原点的距离 |
| 余弦相似度 | $\frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}$ | 方向有多接近 |

---

← 前置: 无
→ 延伸: [02 — 矩阵与线性变换](../02-矩阵与线性变换/notes.md)
