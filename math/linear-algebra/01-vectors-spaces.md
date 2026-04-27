# 第一章 · 向量、线性组合与向量空间

← 前置: 无（本系列起点）
→ 延伸: [02 — 矩阵与线性变换](../linear-algebra/02-matrices-transforms.md)

---

## 1. 直觉引入：为什么需要向量？

想象你在一张地图上描述一个点的位置。你可以说「向东走 3 公里，向北走 4 公里」。这两个数字 $(3, 4)$ 就完整地描述了从原点到目标点的位移。这就是一个**向量**——一组有序的数，合在一起才有意义。

再想象你有一个水果篮，里面有 2 个苹果、3 个香蕉、5 个橘子。这个篮子可以用 $(2, 3, 5)$ 来描述。这里每个数字代表不同「维度」——苹果维、香蕉维、橘子维。向量把不同性质的东西统一成同一种数学语言。

在机器学习中：
- 一张 28×28 的灰度手写数字图片 = 一个 784 维向量
- 一个英文句子经过 embedding 后 = 一个 768 维向量（GPT 中）
- 神经网络的某一层权重 = 一个矩阵（向量的集合）

**核心直觉**：向量就是把「多个相关的数」打包成一个数学对象，让我们可以在高维空间中进行运算和推理。我们平时生活在三维空间里，直觉来自于几何；但向量代数的威力在于，同样的规则可以推广到任意维度。

---

## 2. 向量的形式化定义

### 2.1 向量作为 n 元组

> **定义 1（向量）**：一个 **n 维实向量** 是 $n$ 个实数的一个有序序列，记作
>
> $$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \quad \text{或横写为} \quad \mathbf{v} = [v_1, v_2, \ldots, v_n]^T$$
>
> 其中 $v_i \in \mathbb{R}$ 称为 $\mathbf{v}$ 的第 $i$ 个**分量**。所有 $n$ 维实向量组成的集合记作 $\mathbb{R}^n$。

**符号约定**：本书中，向量用粗体小写英文字母表示（$\mathbf{v}, \mathbf{x}, \mathbf{w}$），标量用普通小写字母（$c, \lambda, \alpha$）。默认向量为列向量。

两个向量**相等**当且仅当它们维数相同，且每个对应分量相等。

### 2.2 几何视角

在 $\mathbb{R}^2$ 和 $\mathbb{R}^3$ 中，向量可以看作从原点出发的有向线段（箭头）。比如 $\mathbf{v} = [3, 2]^T$ 就是从 $(0,0)$ 指向 $(3,2)$ 的箭头。

这种几何直觉极为重要——当你在高维空间中感到迷茫时，请退回到 $\mathbb{R}^2$ 或 $\mathbb{R}^3$，画出图来思考。线性代数的大多数定理在二维和 $n$ 维中没有本质区别。

> **常见误区**：向量**不是**一个点，而是一个位移。点 $(3,2)$ 和向量 $[3,2]^T$ 有本质区别——向量可以平移而不改变其含义（你可以从 $(1,1)$ 走到 $(4,3)$，位移仍是 $[3,2]^T$），但点不行。不过，当我们固定了原点后，每个点对应唯一的从原点出发的向量，所以两者可以互相转换。

---

## 3. 向量运算

### 3.1 向量加法

> **定义 2（向量加法）**：对 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$，其和定义为逐分量相加：
>
> $$\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 \\ \vdots \\ u_n \end{bmatrix} + \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} u_1 + v_1 \\ \vdots \\ u_n + v_n \end{bmatrix}$$

**几何意义**：平行四边形法则——把 $\mathbf{v}$ 的尾巴接在 $\mathbf{u}$ 的头上，从 $\mathbf{u}$ 的尾巴到 $\mathbf{v}$ 的头的箭头就是 $\mathbf{u} + \mathbf{v}$。也叫「三角形法则」。

**性质**：
- **交换律**：$\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$
- **结合律**：$(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$
- **零向量**：存在唯一的 $\mathbf{0} = [0, 0, \ldots, 0]^T$，使得 $\mathbf{v} + \mathbf{0} = \mathbf{v}$
- **加法逆元**：对每个 $\mathbf{v}$，存在 $-\mathbf{v} = [-v_1, \ldots, -v_n]^T$，使得 $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$

### 3.2 标量乘法

> **定义 3（标量乘法）**：对 $\mathbf{v} \in \mathbb{R}^n$ 和标量 $c \in \mathbb{R}$：
>
> $$c\mathbf{v} = c \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} c v_1 \\ \vdots \\ c v_n \end{bmatrix}$$

**几何意义**：$c > 1$ 是拉伸，$0 < c < 1$ 是压缩，$c < 0$ 是反转方向并缩放。

**性质**：
- **分配律 I**：$c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$
- **分配律 II**：$(c + d)\mathbf{v} = c\mathbf{v} + d\mathbf{v}$
- **结合律**：$c(d\mathbf{v}) = (cd)\mathbf{v}$
- **单位元**：$1 \cdot \mathbf{v} = \mathbf{v}$

---

## 4. 线性组合

### 4.1 定义

> **定义 4（线性组合）**：给定向量 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k \in \mathbb{R}^n$ 和标量 $c_1, c_2, \ldots, c_k \in \mathbb{R}$，称
>
> $$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k$$
>
> 为 $\mathbf{v}_1, \ldots, \mathbf{v}_k$ 的一个**线性组合**。$c_1, \ldots, c_k$ 称为**系数**。

线性组合是线性代数中最核心的操作。它回答了一个基本问题：「给定几个基础方向，我能抵达哪些地方？」

**例子**：在 $\mathbb{R}^2$ 中，取 $\mathbf{v}_1 = [1, 0]^T$（向东）和 $\mathbf{v}_2 = [0, 1]^T$（向北）。那么：
- $3\mathbf{v}_1 + 4\mathbf{v}_2 = [3, 4]^T$ — 任何点都可以通过这两个向量组合出来
- $2\mathbf{v}_1 + (-1)\mathbf{v}_2 = [2, -1]^T$ — 系数可以是负数

### 4.2 张成空间 (Span)

> **定义 5（张成空间）**：向量集合 $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ 的所有线性组合构成的集合称为它们的张成空间：
>
> $$\operatorname{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\} = \left\{ c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k \mid c_1,\ldots,c_k \in \mathbb{R} \right\}$$

**几何直觉**：
- 一个非零向量的 span = 一条穿过原点的直线
- 两个不共线向量的 span = 一个穿过原点的平面
- 三个不共面向量的 span = 整个 $\mathbb{R}^3$

### 4.3 线性无关与线性相关

> **定义 6（线性无关）**：向量 $\mathbf{v}_1, \ldots, \mathbf{v}_k$ 是**线性无关**的，如果方程
>
> $$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0}$$
>
> **只有**全零解 $c_1 = c_2 = \cdots = c_k = 0$。否则它们是**线性相关**的。

**直觉**：线性无关意味着集合中没有「冗余」——每个向量都提供了新的方向，不能被其他向量的组合所替代。

**关键判定**：
- 两个向量线性相关 $\iff$ 它们共线（一个是另一个的标量倍）
- 三个向量线性相关 $\iff$ 它们共面（其中一个落在另外两个张成的平面上）
- $\mathbb{R}^n$ 中，超过 $n$ 个向量必然线性相关（抽屉原理的向量版本）

---

## 5. 向量空间

### 5.1 公理化定义

前面我们一直在谈论 $\mathbb{R}^n$。但向量空间的概念远不止于此——$\mathbb{R}^n$ 只是最熟悉的例子。向量空间的威力在于**抽象**：凡是满足下面八条公理的对象，都可以像向量一样操作。

> **定义 7（向量空间）**：一个**（实）向量空间**由一个非空集合 $V$、加法运算 $+$ 和标量乘法运算 $\cdot$ 组成，满足以下八条公理。对任意 $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ 和 $c, d \in \mathbb{R}$：
>
> 1. $\mathbf{u} + \mathbf{v} \in V$（加法封闭）
> 2. $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$（加法交换律）
> 3. $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$（加法结合律）
> 4. 存在 $\mathbf{0} \in V$，使 $\mathbf{u} + \mathbf{0} = \mathbf{u}$（零元存在）
> 5. 对每个 $\mathbf{u} \in V$，存在 $-\mathbf{u} \in V$，使 $\mathbf{u} + (-\mathbf{u}) = \mathbf{0}$（加法逆元）
> 6. $c \cdot \mathbf{u} \in V$（标量乘法封闭）
> 7. $c \cdot (\mathbf{u} + \mathbf{v}) = c \cdot \mathbf{u} + c \cdot \mathbf{v}$（标量分配律 I）
> 8. $(c + d) \cdot \mathbf{u} = c \cdot \mathbf{u} + d \cdot \mathbf{u}$（标量分配律 II）
> 9. $c \cdot (d \cdot \mathbf{u}) = (cd) \cdot \mathbf{u}$（标量结合律）
> 10. $1 \cdot \mathbf{u} = \mathbf{u}$（标量乘法单位元）

这十条规则看起来多，核心只有一句话：**加法和标量乘法可以像实数那样自然运作**。

### 5.2 经典例子

| 向量空间 | 元素 | 维数 |
|----------|------|------|
| $\mathbb{R}^n$ | n 维实向量 | $n$ |
| $\mathbb{C}^n$ | n 维复向量 | $n$（复维数） |
| $P_n$ | 次数 ≤ $n$ 的多项式 | $n+1$ |
| $M_{m \times n}$ | $m \times n$ 矩阵 | $mn$ |
| $C[a,b]$ | $[a,b]$ 上的连续函数 | 无穷维 |

> **关键洞察**：多项式 $3 + 2x - x^2$ 可以看作向量 $[3, 2, -1]^T$。连续函数可以看作无穷维向量。**这就是为什么线性代数在 ML 中无处不在**——任何东西，只要你可以把它表示为「一组系数的线性组合」，线性代数的全部武器库就都适用了。

### 5.3 子空间

> **定义 8（子空间）**：向量空间 $V$ 的非空子集 $W$ 是**子空间**，如果 $W$ 自身也是一个向量空间（在 $V$ 的加法和标量乘法下）。

要验证 $W$ 是子空间，只需检查三条（其余自动继承自 $V$）：
1. $\mathbf{0} \in W$
2. $\mathbf{u}, \mathbf{v} \in W \implies \mathbf{u} + \mathbf{v} \in W$（加法封闭）
3. $\mathbf{u} \in W, c \in \mathbb{R} \implies c\mathbf{u} \in W$（标量乘法封闭）

**常见子空间**：
- $\mathbb{R}^3$ 中穿过原点的平面：$W = \{[x, y, z]^T \mid 2x - y + z = 0\}$
- 多项式空间中次数 ≤ 3 的多项式是 $P_n$（$n \geq 3$）的子空间
- 矩阵空间中对称矩阵的集合是 $M_{n \times n}$ 的子空间

---

## 6. 基与维数

### 6.1 基的定义

> **定义 9（基）**：向量空间 $V$ 的一组**基**是一组线性无关的向量 $\{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$，使得它们的张成空间等于整个 $V$：
>
> $$\operatorname{span}\{\mathbf{b}_1, \ldots, \mathbf{b}_n\} = V$$

**直觉**：基是「描述整个空间所需的最少向量」。每个向量都可以**唯一地**写成基向量的线性组合。

**唯一性证明**：若 $\mathbf{v} = \sum c_i \mathbf{b}_i = \sum d_i \mathbf{b}_i$，则 $\sum (c_i - d_i)\mathbf{b}_i = \mathbf{0}$。由线性无关性，$c_i - d_i = 0$，即 $c_i = d_i$。$\square$

### 6.2 维数

> **定义 10（维数）**：向量空间 $V$ 的**维数** $\dim V$ 是其基中向量的个数。

核心定理：**同一个向量空间的所有基都有相同数量的向量**。这保证了维数定义的良定性。

**例子**：
- $\mathbb{R}^n$ 的标准基：$\mathbf{e}_1 = [1,0,\ldots,0]^T, \mathbf{e}_2 = [0,1,\ldots,0]^T, \ldots, \mathbf{e}_n = [0,0,\ldots,1]^T$，$\dim = n$
- $P_n$（次数 ≤ $n$ 的多项式）的标准基：$\{1, x, x^2, \ldots, x^n\}$，$\dim = n+1$
- $M_{2 \times 2}$ 的标准基：$\begin{bmatrix}1&0\\0&0\end{bmatrix}, \begin{bmatrix}0&1\\0&0\end{bmatrix}, \begin{bmatrix}0&0\\1&0\end{bmatrix}, \begin{bmatrix}0&0\\0&1\end{bmatrix}$，$\dim = 4$

---

## 7. 代码实现

让我们从零实现一个 `Vector` 类，把上面的定义变成可运行的代码。

```python
from __future__ import annotations
import math
from typing import List, Union


class Vector:
    """n 维实向量的实现。"""

    def __init__(self, components: List[float]):
        if not components:
            raise ValueError("向量至少需要一个分量")
        self._data = list(components)

    @property
    def dim(self) -> int:
        """向量维数。"""
        return len(self._data)

    def __getitem__(self, i: int) -> float:
        """取第 i 个分量（0-indexed）。"""
        return self._data[i]

    def __repr__(self) -> str:
        return f"Vector({self._data})"

    # ─── 向量加法 ───
    def __add__(self, other: Vector) -> Vector:
        if self.dim != other.dim:
            raise ValueError(f"维数不匹配: {self.dim} vs {other.dim}")
        return Vector([a + b for a, b in zip(self._data, other._data)])

    # ─── 加法逆元 ───
    def __neg__(self) -> Vector:
        return Vector([-x for x in self._data])

    def __sub__(self, other: Vector) -> Vector:
        return self + (-other)

    # ─── 标量乘法 ───
    def __mul__(self, scalar: float) -> Vector:
        """标量乘法: v * c"""
        return Vector([x * scalar for x in self._data])

    def __rmul__(self, scalar: float) -> Vector:
        """标量乘法: c * v"""
        return self.__mul__(scalar)

    # ─── 相等判断（浮点数容差） ───
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        if self.dim != other.dim:
            return False
        return all(
            math.isclose(a, b, rel_tol=1e-9)
            for a, b in zip(self._data, other._data)
        )

    # ─── 零向量 ───
    @staticmethod
    def zero(dim: int) -> Vector:
        """构造 dim 维零向量。"""
        return Vector([0.0] * dim)

    # ─── 范数与距离 ───
    def norm(self, p: int = 2) -> float:
        """ℓ_p 范数。p=2 为欧几里得长度（默认）。"""
        if p == 2:
            return math.sqrt(sum(x ** 2 for x in self._data))
        if p == 1:
            return sum(abs(x) for x in self._data)
        if p == float('inf'):
            return max(abs(x) for x in self._data)
        return sum(abs(x) ** p for x in self._data) ** (1 / p)

    def normalize(self) -> Vector:
        """返回同方向的单位向量。"""
        n = self.norm()
        if n == 0:
            raise ValueError("零向量无法归一化")
        return self.__mul__(1.0 / n)

    # ─── 内积 ───
    def dot(self, other: Vector) -> float:
        """标准欧几里得内积（点积）。"""
        if self.dim != other.dim:
            raise ValueError(f"维数不匹配: {self.dim} vs {other.dim}")
        return sum(a * b for a, b in zip(self._data, other._data))

    # ─── 线性组合（核心！） ───
    @staticmethod
    def linear_combination(
        vectors: List[Vector], coefficients: List[float]
    ) -> Vector:
        """计算 c1*v1 + c2*v2 + ... + ck*vk。"""
        if not vectors:
            raise ValueError("向量列表不能为空")
        if len(vectors) != len(coefficients):
            raise ValueError("向量数量和系数数量必须相等")
        result = Vector.zero(vectors[0].dim)
        for c, v in zip(coefficients, vectors):
            result = result + c * v
        return result
```

**逐行解释**：
- `__add__` 和 `__mul__` 直接实现了定义 2 和定义 3
- `Vector.linear_combination` 是定义 4 的精确翻译——它是整个线性代数计算的入口
- `dot` 将在下一章发挥核心作用
- 所有操作都检查维数匹配，避免「对牛弹琴」式的错误

### 7.1 使用示例

```python
# 标准基向量
e1 = Vector([1, 0, 0])
e2 = Vector([0, 1, 0])
e3 = Vector([0, 0, 1])

# 线性组合: 3*e1 + 4*e2 + 5*e3 = (3, 4, 5)
v = Vector.linear_combination([e1, e2, e3], [3, 4, 5])
print(v)  # Vector([3.0, 4.0, 5.0])

# 加法: (3,4,5) + (1,-1,0) = (4,3,5)
w = Vector([1, -1, 0])
print(v + w)  # Vector([4.0, 3.0, 5.0])

# 标量乘法: 2 * (3,4,5) = (6,8,10)
print(2.0 * v)  # Vector([6.0, 8.0, 10.0])

# 长度
print(v.norm())  # sqrt(9+16+25) ≈ 7.071
```

---

## 8. 重要定理证明

### 8.1 线性无关的判别

> **定理**：$\mathbb{R}^n$ 中，如果 $k > n$，则任意 $k$ 个向量必线性相关。

**证明思路**（非构造）：这等价于「齐次方程组未知数多于方程数时必有非零解」，我们在第三章处理高斯消元后再严格证明。目前可以从几何直觉理解：在 $\mathbb{R}^2$ 中，给三个向量必然有一个是冗余的（它落在另外两个的张成平面内）。$\blacksquare$

### 8.2 子空间交依然是子空间

> **定理**：若 $U$ 和 $W$ 都是 $V$ 的子空间，则 $U \cap W$ 也是 $V$ 的子空间。

**证明**：验证三条闭包条件。
1. $\mathbf{0} \in U$ 且 $\mathbf{0} \in W$，故 $\mathbf{0} \in U \cap W$。✓
2. 若 $\mathbf{x}, \mathbf{y} \in U \cap W$，则 $\mathbf{x}+\mathbf{y} \in U$（$U$ 封闭）且 $\mathbf{x}+\mathbf{y} \in W$（$W$ 封闭），故 $\mathbf{x}+\mathbf{y} \in U \cap W$。✓
3. 若 $\mathbf{x} \in U \cap W$，对任意 $c \in \mathbb{R}$，$c\mathbf{x} \in U$ 且 $c\mathbf{x} \in W$，故 $c\mathbf{x} \in U \cap W$。✓

> **注意**：$U \cup W$ 一般**不是**子空间！例如 $\mathbb{R}^2$ 中 $U = \operatorname{span}\{[1,0]^T\}$（x 轴）和 $W = \operatorname{span}\{[0,1]^T\}$（y 轴），$[1,0]^T + [0,1]^T = [1,1]^T \notin U \cup W$。

---

## 9. 例题

### 例 1：验证向量空间公理

**问题**：判断下述集合是否为向量空间（在通常的加法和标量乘法下）：

$$S = \{[x, y]^T \in \mathbb{R}^2 \mid y = 2x\}$$

**解**：$S$ 是经过原点的直线，我们验证子空间三条：
1. 原点 $[0,0]^T$ 满足 $0 = 2 \cdot 0$，所以 $\mathbf{0} \in S$。✓
2. 设 $\mathbf{u} = [x_1, 2x_1]^T, \mathbf{v} = [x_2, 2x_2]^T \in S$，则 $\mathbf{u} + \mathbf{v} = [x_1+x_2, 2x_1+2x_2]^T = [x_1+x_2, 2(x_1+x_2)]^T \in S$。✓
3. $c\mathbf{u} = [cx_1, c\cdot 2x_1]^T = [cx_1, 2(cx_1)]^T \in S$。✓

所以 $S$ 是 $\mathbb{R}^2$ 的子空间，因此自身也是向量空间。$\dim S = 1$（例如 $\{[1,2]^T\}$ 是一组基）。

### 例 2：判定线性无关

**问题**：判断以下三个向量是否线性无关：

$$\mathbf{v}_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \quad
\mathbf{v}_2 = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}, \quad
\mathbf{v}_3 = \begin{bmatrix} 7 \\ 8 \\ 9 \end{bmatrix}$$

**解**：解方程 $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0}$：

$$\begin{cases}
c_1 + 4c_2 + 7c_3 = 0 \\
2c_1 + 5c_2 + 8c_3 = 0 \\
3c_1 + 6c_2 + 9c_3 = 0
\end{cases}$$

第二行减两倍第一行：$-3c_2 - 6c_3 = 0 \implies c_2 = -2c_3$

第三行减三倍第一行：$-6c_2 - 12c_3 = 0 \implies c_2 = -2c_3$（一致）

第一行代入：$c_1 + 4(-2c_3) + 7c_3 = c_1 - c_3 = 0 \implies c_1 = c_3$

取 $c_3 = 1$，得非零解 $(1, -2, 1)$。故向量线性相关。事实上，$\mathbf{v}_3 = 2\mathbf{v}_2 - \mathbf{v}_1$。

> **常见错误**：只看向量个数。$\mathbb{R}^3$ 中三个向量不一定线性无关——它们必须不共面才行。这里是共面的。

### 例 3：求基和维数

**问题**：求 $W = \{[x, y, z]^T \in \mathbb{R}^3 \mid x + y + z = 0\}$ 的一组基，并给出维数。

**解**：条件等价于 $z = -x - y$，因此任意 $\mathbf{w} \in W$ 可写为：

$$\mathbf{w} = \begin{bmatrix} x \\ y \\ -x-y \end{bmatrix}
= x\begin{bmatrix} 1 \\ 0 \\ -1 \end{bmatrix}
+ y\begin{bmatrix} 0 \\ 1 \\ -1 \end{bmatrix}$$

设 $\mathbf{b}_1 = [1, 0, -1]^T, \mathbf{b}_2 = [0, 1, -1]^T$。它们张成 $W$。

检查线性无关：设 $c_1\mathbf{b}_1 + c_2\mathbf{b}_2 = \mathbf{0}$，得 $[c_1, c_2, -c_1-c_2]^T = [0,0,0]^T$，故 $c_1 = c_2 = 0$。所以 $\{\mathbf{b}_1, \mathbf{b}_2\}$ 是 $W$ 的一组基，$\dim W = 2$。

> **几何直觉**：$x+y+z=0$ 是 $\mathbb{R}^3$ 中穿过原点的平面。一个平面是二维的——和我们的计算结果一致。

---

## 10. 练习题

### 题 1
判断 $\mathbf{v}_1 = [2, 1]^T$ 和 $\mathbf{v}_2 = [4, 2]^T$ 是否线性无关。用定义（而非直觉）回答。

<details><summary>点击查看答案</summary>

设 $c_1[2,1]^T + c_2[4,2]^T = [0,0]^T$：
$$\begin{cases} 2c_1 + 4c_2 = 0 \\ c_1 + 2c_2 = 0 \end{cases}$$
第二式乘 2 得 $2c_1 + 4c_2 = 0$，与第一式相同。方程有无穷多解，取 $c_1 = 2, c_2 = -1$ 即得非零解。故线性相关。
</details>

### 题 2
$S = \{[x, y]^T \in \mathbb{R}^2 \mid y = x + 1\}$ 是否是 $\mathbb{R}^2$ 的子空间？若不是，违反了哪条公理？

<details><summary>点击查看答案</summary>

不是。零向量 $[0,0]^T$ 不满足 $y = x + 1$（因为 $0 \neq 0 + 1$），所以 $\mathbf{0} \notin S$。违反了第 4 条公理。

几何上，$y = x + 1$ 是一条不经过原点的直线——它虽然是一条直线，但不是子空间。只有**经过原点**的直线/平面才可能是子空间。
</details>

### 题 3
写出 $M_{2 \times 2}$（$2 \times 2$ 矩阵构成的向量空间）的一组标准基，并验证其维数为 4。

<details><summary>点击查看答案</summary>

标准基：
$$E_{11} = \begin{bmatrix}1&0\\0&0\end{bmatrix},\;
E_{12} = \begin{bmatrix}0&1\\0&0\end{bmatrix},\;
E_{21} = \begin{bmatrix}0&0\\1&0\end{bmatrix},\;
E_{22} = \begin{bmatrix}0&0\\0&1\end{bmatrix}$$

任意 $2 \times 2$ 矩阵 $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ 可唯一表示为 $aE_{11} + bE_{12} + cE_{21} + dE_{22}$，故 $\dim = 4$。
</details>

### 题 4
设 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3 \in \mathbb{R}^n$ 线性无关。证明 $\mathbf{v}_1, \mathbf{v}_1 + \mathbf{v}_2, \mathbf{v}_1 + \mathbf{v}_2 + \mathbf{v}_3$ 也线性无关。

<details><summary>点击查看答案</summary>

设 $c_1\mathbf{v}_1 + c_2(\mathbf{v}_1 + \mathbf{v}_2) + c_3(\mathbf{v}_1 + \mathbf{v}_2 + \mathbf{v}_3) = \mathbf{0}$。

合并系数：$(c_1 + c_2 + c_3)\mathbf{v}_1 + (c_2 + c_3)\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0}$。

由 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ 线性无关：
$$\begin{cases} c_1 + c_2 + c_3 = 0 \\ c_2 + c_3 = 0 \\ c_3 = 0 \end{cases}$$

从下往上代入得 $c_3 = 0, c_2 = 0, c_1 = 0$。故线性无关。
</details>

### 题 5
用 Python 实现一个函数 `is_linear_combination(target, vectors)`，判断 `target` 是否可以表示为 `vectors` 中向量的线性组合。对于 $\mathbb{R}^2$，用求解 $2 \times k$ 线性方程组的方式判断。（提示：先只处理二维情况）

<details><summary>点击查看答案</summary>

```python
def is_linear_combination_2d(
    target: Vector, vectors: List[Vector]
) -> bool:
    """在 R^2 中判断 target 是否为 vectors 的线性组合。
    使用克莱姆法则求解 2x2 情况（仅当 k=2 时有效）。
    """
    assert target.dim == 2
    assert all(v.dim == 2 for v in vectors)

    # 暂时只处理两个向量的情况
    if len(vectors) == 1:
        v = vectors[0]
        # 需要 target = c * v，检查两个分量比是否一致
        if v[0] == 0 and v[1] == 0:
            return target[0] == 0 and target[1] == 0
        if v[0] != 0:
            c = target[0] / v[0]
            return math.isclose(c * v[1], target[1])
        else:
            c = target[1] / v[1]
            return math.isclose(c * v[0], target[0])

    if len(vectors) == 2:
        a, b = vectors[0], vectors[1]
        # 解 [a b] * [c1; c2] = target
        det = a[0] * b[1] - a[1] * b[0]
        if det == 0:
            # 两个向量共线，退化为一个向量的情况
            return is_linear_combination_2d(target, [vectors[0]])
        c1 = (target[0] * b[1] - target[1] * b[0]) / det
        c2 = (a[0] * target[1] - a[1] * target[0]) / det
        return True  # 任意 target 都可以表示

    # 三个及以上二维向量总能张成整个 R^2 (除非全部共线)
    return True
```

我们在第三章学了高斯消元法之后，这个问题会有更通用的解法。
</details>

---

## 本章核心概念速查

| 概念 | 一句话 |
|------|--------|
| 向量 | 有序的 n 个数，打包成一个数学对象 |
| 向量加法 | 逐分量相加，几何上是平行四边形法则 |
| 标量乘法 | 逐分量缩放，几何上是拉伸/压缩/反转 |
| 线性组合 | $c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k$，线性代数的核心运算 |
| 张成空间 (span) | 所有线性组合构成的集合 |
| 线性无关 | 没有冗余——任何向量都不能被其他向量组合出来 |
| 向量空间 | 满足 10 条公理的集合，加法/标量乘法封闭 |
| 子空间 | 向量空间内部的一个子集，自身也是向量空间 |
| 基 | 描述整个空间所需的最少向量组 |
| 维数 | 基中向量的个数，代表「自由度」 |

---

← 前置: 无（本系列起点）
→ 延伸: [02 — 矩阵与线性变换](02-matrices-transforms.md)
