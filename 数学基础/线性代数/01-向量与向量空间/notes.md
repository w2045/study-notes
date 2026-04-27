# 线性代数 · 第一章 · 向量与向量空间

← 前置: 无（本系列起点）
→ 延伸: [02 — 内积空间、范数与正交性](../02-内积空间-范数与正交性/notes.md)

---

## 1. 直觉引入：向量的三种面孔

**物理面孔**：向量是空间中的箭头——有长度、有方向。两个箭头可以「接在一起」（平行四边形法则），也可以「拉长缩短」（标量乘法）。

**计算机面孔**：向量是有序的数字列表。一张 28×28 的灰度图片 = 784 个数 = $\mathbb{R}^{784}$ 中一个点。一个词嵌入 = $\mathbb{R}^{768}$ 中一个点。

**数学面孔**：向量是「可以加法、可以标量乘法、且满足八条公理」的抽象对象。多项式、矩阵、连续函数都可以是向量。

> **核心洞察**：三种面孔共享同一套代数规则。学会一套规则，在三个世界之间自由切换。

---

## 2. 向量的形式化定义

> **定义 1（$\mathbb{R}^n$ 中的向量）**：$n$ 维实向量是 $n$ 个实数的有序序列：
>
> $$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}, \quad v_i \in \mathbb{R}$$
>
> $v_i$ 称为 $\mathbf{v}$ 的第 $i$ 个**分量 (component)**。所有 $n$ 维实向量的集合记作 $\mathbb{R}^n$。

**符号约定**：向量用粗体小写 $\mathbf{v}, \mathbf{x}, \mathbf{w}$，标量用普通小写 $c, \lambda, \alpha$。默认列向量，横写时加转置 $[v_1, \ldots, v_n]^T$。

两向量相等 $\iff$ 维数相同且每个对应分量相等。

### 2.1 特殊向量

| 名称 | 记法 | 例子 ($\mathbb{R}^3$) |
|------|------|----------------------|
| 零向量 | $\mathbf{0}$ | $[0, 0, 0]^T$ |
| 标准基向量 | $\mathbf{e}_i$ | $\mathbf{e}_1 = [1,0,0]^T$, $\mathbf{e}_2 = [0,1,0]^T$, $\mathbf{e}_3 = [0,0,1]^T$ |
| 全 1 向量 | $\mathbf{1}$ | $[1, 1, 1]^T$ |

---

## 3. 向量运算：加法和标量乘法

### 3.1 向量加法

> **定义 2（向量加法）**：$\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$，逐分量相加：
>
> $$\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 \\ \vdots \\ u_n \end{bmatrix} + \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} u_1 + v_1 \\ \vdots \\ u_n + v_n \end{bmatrix}$$

**几何意义**：平行四边形法则——将 $\mathbf{v}$ 的起点移到 $\mathbf{u}$ 的终点，从 $\mathbf{u}$ 起点到 $\mathbf{v}$ 终点的箭头即 $\mathbf{u}+\mathbf{v}$。

**代数性质**（$\forall \mathbf{u}, \mathbf{v}, \mathbf{w} \in \mathbb{R}^n$）：
- 交换律：$\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$
- 结合律：$(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$
- 加法单位元：$\mathbf{v} + \mathbf{0} = \mathbf{v}$
- 加法逆元：$\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$，其中 $-\mathbf{v} = [-v_1, \ldots, -v_n]^T$

### 3.2 标量乘法

> **定义 3（标量乘法）**：对 $c \in \mathbb{R}$ 和 $\mathbf{v} \in \mathbb{R}^n$：
>
> $$c \cdot \mathbf{v} = c \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} c v_1 \\ \vdots \\ c v_n \end{bmatrix}$$

**几何意义**：$c > 1$ 拉伸，$0 < c < 1$ 压缩，$c < 0$ 反转方向同时缩放。

**代数性质**：
- 分配律 I：$c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$
- 分配律 II：$(c + d)\mathbf{v} = c\mathbf{v} + d\mathbf{v}$
- 结合律：$c(d\mathbf{v}) = (cd)\mathbf{v}$
- 单位元：$1 \cdot \mathbf{v} = \mathbf{v}$

---

## 4. 线性组合：代数的核心操作

> **定义 4（线性组合）**：给定向量 $\mathbf{v}_1, \ldots, \mathbf{v}_k \in \mathbb{R}^n$ 和标量 $c_1, \ldots, c_k \in \mathbb{R}$：
>
> $$\mathbf{w} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \sum_{i=1}^{k} c_i \mathbf{v}_i$$
>
> $c_i$ 称为**系数 (coefficients)**。

线性组合回答的问题是：**给定几个基本方向，我能抵达哪些地方？**

**例 1**：$\mathbb{R}^2$ 中，取 $\mathbf{v}_1 = [1, 0]^T$（向右）和 $\mathbf{v}_2 = [0, 1]^T$（向上）。任意点 $[x, y]^T = x\mathbf{v}_1 + y\mathbf{v}_2$——两个方向覆盖整个平面。

**例 2**：$\mathbf{v}_1 = [1, 0]^T$，$\mathbf{v}_2 = [2, 0]^T$ 同方向，组合只能产生 $x$ 轴上的点——冗余的方向限制了你。

> **关键认知**：线性组合的能力取决于「给的方向有多独立」。这就是下一节「线性无关」要量化的。

### 4.1 从线性组合到矩阵-向量乘法（桥接 Ch03）

将 $k$ 个向量 $\mathbf{v}_1, \ldots, \mathbf{v}_k \in \mathbb{R}^n$ 作为列排成一个 $n \times k$ 矩阵 $A$，将系数 $c_1, \ldots, c_k$ 放入向量 $\mathbf{x}$。则线性组合**等价于矩阵-向量乘法**：

$$\mathbf{w} = c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k = A\mathbf{x}, \quad A = [\mathbf{v}_1 \mid \cdots \mid \mathbf{v}_k], \quad \mathbf{x} = [c_1, \ldots, c_k]^T$$

这是线性代数**最核心的视角转换**：线性组合 → 矩阵乘向量 → 线性变换。从此「给定向量组能拼出什么」等价于「矩阵 $A$ 的列空间是什么」——这一思想贯穿全书。

---

## 5. 张成空间 (Span)

> **定义 5（张成空间）**：$\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ 的所有线性组合的集合：
>
> $$\operatorname{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\} = \left\{\sum_{i=1}^{k} c_i\mathbf{v}_i \;\middle|\; c_i \in \mathbb{R}\right\}$$

**几何直觉**：

| 情况 | Span 是什么 |
|------|------------|
| 一个非零向量 | 经过原点的一条直线 |
| 两个不共线向量 | 经过原点的平面 |
| 三个不共面向量 | 整个 $\mathbb{R}^3$ |
| 只有零向量 | 原点 $\{\mathbf{0}\}$ |

**运算视角**：「这些向量能生成什么？」——这是线性代数从头到尾反复问的问题。

**张成空间的计算演示**：$\mathbf{v}_1 = [1,0,1]^T$, $\mathbf{v}_2 = [2,1,0]^T$, $\mathbf{v}_3 = [1,1,-1]^T$ 张成什么？
将三个向量作为列排成矩阵，化为 REF：
$$\begin{bmatrix} 1 & 2 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & -1 \end{bmatrix} \xrightarrow{R_3-R_1} \begin{bmatrix} 1 & 2 & 1 \\ 0 & 1 & 1 \\ 0 & -2 & -2 \end{bmatrix} \xrightarrow{R_3+2R_2} \begin{bmatrix} 1 & 2 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}$$
秩 = 2 → 只有 2 个独立方向 → $\operatorname{span} = \mathbb{R}^3$ 中的一个二维平面。具体来说，$\mathbf{v}_3 = \mathbf{v}_2 - \mathbf{v}_1$（线性相关）。（消元法的系统介绍见 Ch04。）

---

## 6. 线性无关与线性相关

> **定义 6（线性无关）**：向量 $\mathbf{v}_1, \ldots, \mathbf{v}_k$ **线性无关** $\iff$
>
> $$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0}$$
>
> **只有零解** $c_1 = c_2 = \cdots = c_k = 0$。若存在非零解，则**线性相关**。

**直觉翻译**：线性无关 = 集合没有冗余——每个向量都提供了「新方向」，不能被其他向量拼出来。

**关键事实**：
- 两个向量线性相关 $\iff$ 共线（一个是另一个的标量倍）
- $\mathbb{R}^n$ 中向量数 $k > n \implies$ 线性相关（维数上界）
- 集合含零向量 $\implies$ 线性相关（取该向量系数为 1，其余为 0）

**判定方法**（$\mathbb{R}^n$ 中）：把方程 $c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k = \mathbf{0}$ 写成 $n \times k$ 的齐次线性方程组。若唯一解为零解，则线性无关。（第三章用高斯消元系统解决。）

---

## 7. 向量空间：公理化定义

$\mathbb{R}^n$ 是我们最熟悉的例子，但向量空间的概念远远更大。数学的力量在于抽象——把 $\mathbb{R}^n$ 中成立的规则提炼成公理，任何满足公理的对象自动继承全部线性代数定理。

> **定义 7（实向量空间）**：非空集合 $V$ 配备加法 $+$ 和标量乘法 $\cdot$，满足以下 **10 条公理**（$\forall \mathbf{u}, \mathbf{v}, \mathbf{w} \in V,\; c, d \in \mathbb{R}$）：
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

**一句话总结**：10 条公理 =「加法和标量乘法可以像 $\mathbb{R}^n$ 一样安全地操作」。

### 7.1 超越 $\mathbb{R}^n$ 的例子

| 向量空间 | 元素 | 「向量」的样子 | 维数 |
|----------|------|---------------|------|
| $\mathbb{R}^n$ | $n$ 维实数组 | $[v_1, \ldots, v_n]^T$ | $n$ |
| $P_n$ | 次数 $\leq n$ 的多项式 | $a_0 + a_1x + \cdots + a_nx^n$ | $n+1$ |
| $M_{m \times n}$ | $m \times n$ 矩阵 | $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ | $mn$ |
| $C[a,b]$ | $[a,b]$ 上的连续函数 | $f(x) = \sin(x)$ | $\infty$ |
| $\ell^2$ | 平方可和序列 | $(a_1, a_2, \ldots)$ | $\infty$ |

> **关键洞察**：多项式 $3 + 2x - x^3$ 可视为系数向量 $[3, 2, 0, -1]^T$。$f(x) = \sin(x)$ 的泰勒级数是无穷维向量。**任何可以表示为「一组基系数的线性组合」的东西，全套线性代数定理都对它适用**。

**复向量空间 $\mathbb{C}^n$**：将标量域从 $\mathbb{R}$ 扩展到 $\mathbb{C}$，向量分量取复数。复向量空间的公理与实向量空间完全相同（10 条），但内积的定义需修正为 **Hermitian 内积**（见第 02 章）。复向量空间上保持内积的线性变换由**酉矩阵 (unitary matrix)** 表示——它是正交矩阵在复数域的自然推广：$U^* U = I$（$U^*$ 是共轭转置）。酉矩阵在量子力学和信号处理中至关重要，将在第 03、07 章深入讨论。

---

## 8. 子空间

> **定义 8（子空间）**：$V$ 的子集 $W \subseteq V$ 是**子空间**，若 $W$ 在 $V$ 的加法与标量乘法下自身也构成向量空间。

验证子空间只需检查**三条**（其余七条公理自动从 $V$ 继承）：

1. $\mathbf{0} \in W$
2. $\mathbf{u}, \mathbf{v} \in W \implies \mathbf{u} + \mathbf{v} \in W$（加法封闭）
3. $\mathbf{u} \in W, c \in \mathbb{R} \implies c\mathbf{u} \in W$（标量乘法封闭）

> 等价简化：只需验证一条——$c\mathbf{u} + \mathbf{v} \in W$ 对所有 $\mathbf{u}, \mathbf{v} \in W, c \in \mathbb{R}$ 成立。

### 8.1 经典例子

**例 1**：$W = \{[x, y]^T \in \mathbb{R}^2 \mid y = 3x\}$（经过原点的直线）

验证：
1. $\mathbf{0} = [0,0]^T$ 满足 $0 = 3 \cdot 0$ ✓
2. $[x_1, 3x_1]^T + [x_2, 3x_2]^T = [x_1+x_2, 3(x_1+x_2)]^T \in W$ ✓
3. $c[x, 3x]^T = [cx, 3cx]^T \in W$ ✓

$W$ 是 $\mathbb{R}^2$ 的子空间，$\dim W = 1$，因为 $W = \operatorname{span}\{[1, 3]^T\}$。

**例 2**：$S = \{[x, y]^T \in \mathbb{R}^2 \mid y = x + 1\}$（不经过原点的直线）

$[0, 0]^T$ 不满足 $y = x + 1$，$\mathbf{0} \notin S$。$S$ 不是子空间。

> **几何记忆**：只有**经过原点**的直线/平面/超平面才可能是子空间。

### 8.2 子空间之交

> **定理**：若 $U, W$ 均为 $V$ 的子空间，则 $U \cap W$ 也是 $V$ 的子空间。

**证明**：$\mathbf{0} \in U \cap W$；$\mathbf{x}, \mathbf{y} \in U \cap W \implies \mathbf{x}+\mathbf{y}$ 同时在 $U$ 和 $W$ 中；标量乘法同理。证毕

> **警告**：$U \cup W$ 一般**不是**子空间。如 $\mathbb{R}^2$ 中 $x$ 轴 $\cup$ $y$ 轴：$[1,0]^T + [0,1]^T = [1,1]^T \notin$ 并集。

---

## 9. 基与维数

### 9.1 基的定义

> **定义 9（基）**：向量空间 $V$ 的一组**基 (basis)** 是一组向量 $\mathcal{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$，满足：
> 1. $\mathcal{B}$ 是线性无关的
> 2. $\operatorname{span}(\mathcal{B}) = V$

**直觉**：基是「描述整个空间所需的最少向量组」。每个 $\mathbf{v} \in V$ 可**唯一**地写成基向量的线性组合：

$$\mathbf{v} = c_1\mathbf{b}_1 + c_2\mathbf{b}_2 + \cdots + c_n\mathbf{b}_n$$

**唯一性证明**：若 $\mathbf{v} = \sum c_i \mathbf{b}_i = \sum d_i \mathbf{b}_i$，则 $\sum (c_i - d_i)\mathbf{b}_i = \mathbf{0}$。由线性无关性，$c_i - d_i = 0$，即 $c_i = d_i$。证毕

### 9.2 维数

> **定义 10（维数）**：$\dim V =$ 基中向量的个数。

核心定理：**一个向量空间的所有基都有相同数量的向量**。

**标准基的例子**：

| 空间 | 标准基 | $\dim$ |
|------|--------|--------|
| $\mathbb{R}^n$ | $\{\mathbf{e}_1, \ldots, \mathbf{e}_n\}$ | $n$ |
| $P_2$ | $\{1, x, x^2\}$ | $3$ |
| $M_{2 \times 2}$ | $\left\{\begin{bmatrix}1&0\\0&0\end{bmatrix}, \begin{bmatrix}0&1\\0&0\end{bmatrix}, \begin{bmatrix}0&0\\1&0\end{bmatrix}, \begin{bmatrix}0&0\\0&1\end{bmatrix}\right\}$ | $4$ |

### 9.3 核心定理

> **定理**：若 $W$ 是 $V$ 的子空间，则 $\dim W \leq \dim V$。等号成立 $\iff W = V$。

> **定理（维数公式）**：对 $V$ 的任意子空间 $U, W$：
>
> $$\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$$
>
> 其中 $U + W = \{\mathbf{u} + \mathbf{w} \mid \mathbf{u} \in U, \mathbf{w} \in W\}$。

**推论**：$\mathbb{R}^3$ 中两个穿过原点且不同的平面（各 $\dim = 2$），它们的交是一条直线（$\dim = 1$）。代入公式：$2+2-1 = 3$（整个空间）。

### 9.4 维数的应用：构造基

> **扩充定理**：任何线性无关集都可以扩充为一组基。

算法：从已有线性无关集开始，逐次加入不在当前 span 中的向量，直到 span 覆盖整个空间。

---

## 10. 四个基本子空间（预告）

任何 $m \times n$ 矩阵 $A$ 定义了四个子空间（将在第 03-04 章展开）：

| 子空间 | 记法 | 所在空间 | 含义 |
|--------|------|----------|------|
| 列空间 | $\operatorname{col}(A)$ | $\mathbb{R}^m$ | $A$ 各列的所有线性组合 |
| 行空间 | $\operatorname{row}(A)$ | $\mathbb{R}^n$ | $A$ 各行的所有线性组合 |
| 零空间 | $\ker(A)$ | $\mathbb{R}^n$ | 满足 $A\mathbf{x} = \mathbf{0}$ 的所有 $\mathbf{x}$ |
| 左零空间 | $\ker(A^T)$ | $\mathbb{R}^m$ | 满足 $A^T\mathbf{y} = \mathbf{0}$ 的所有 $\mathbf{y}$ |

现在只需记住：这四个子空间是「线性组合」和「齐次方程解」两种思想的交汇点。

---

## 11. 概念演示：线性组合的可视化

> 本章的编程练习在 `编程题/` 目录下。运行 `python3 grader.py` 自动批改。

以代码直观感受「线性组合 = 用基本方向拼出目标点」：

```python
import numpy as np

# 标准基：向右 (e1) 和向上 (e2)
e1 = np.array([1, 0])
e2 = np.array([0, 1])

# 任意点 (3, 4) = 3*e1 + 4*e2
point = 3 * e1 + 4 * e2
print(point)  # [3 4]

# 不同的基产生不同的坐标系
b1 = np.array([1, 1])
b2 = np.array([-1, 1])
# 点 (2, 3) 在新基下的坐标 (c1, c2) 满足 c1*b1 + c2*b2 = (2, 3)
# 即 c1 - c2 = 2, c1 + c2 = 3 → c1=2.5, c2=0.5
coeffs = np.linalg.solve(np.column_stack([b1, b2]), [2, 3])
print(coeffs)  # [2.5 0.5]
```

**要点**：同一空间可以有多组基——这就是基变换的本质（第 07 章详述）。

---

## 12. 重要定理证明

### 12.1 零元唯一性

> **定理**：向量空间中零向量是唯一的。

**证明**：设 $\mathbf{0}_1$ 和 $\mathbf{0}_2$ 均满足零元公理。则
$\mathbf{0}_1 = \mathbf{0}_1 + \mathbf{0}_2$（$\mathbf{0}_2$ 是零元）$= \mathbf{0}_2 + \mathbf{0}_1$（交换律）$= \mathbf{0}_2$（$\mathbf{0}_1$ 是零元）。
所以 $\mathbf{0}_1 = \mathbf{0}_2$。证毕

### 12.2 加法逆元唯一性

> **定理**：每个 $\mathbf{v} \in V$ 的加法逆元是唯一的。

**证明**：设 $\mathbf{a}, \mathbf{b}$ 均为 $\mathbf{v}$ 的逆元。则
$\mathbf{a} = \mathbf{a} + \mathbf{0} = \mathbf{a} + (\mathbf{v} + \mathbf{b}) = (\mathbf{a} + \mathbf{v}) + \mathbf{b} = \mathbf{0} + \mathbf{b} = \mathbf{b}$。证毕

### 12.3 标量 0 产生零向量

> **定理**：$0 \cdot \mathbf{v} = \mathbf{0}$。

**证明**：$0 \cdot \mathbf{v} = (0+0)\mathbf{v} = 0\mathbf{v} + 0\mathbf{v}$。两边加 $-0\mathbf{v}$ 得 $0\mathbf{v} = \mathbf{0}$。证毕

### 12.4 线性无关扩充

> **定理**：若 $\mathbf{v}_1, \ldots, \mathbf{v}_k$ 线性无关，且 $\mathbf{v}_{k+1} \notin \operatorname{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$，则 $\mathbf{v}_1, \ldots, \mathbf{v}_{k+1}$ 也线性无关。

**证明**：设 $\sum_{i=1}^{k+1} c_i\mathbf{v}_i = \mathbf{0}$。若 $c_{k+1} \neq 0$，则 $\mathbf{v}_{k+1} = -\frac{1}{c_{k+1}}\sum_{i=1}^{k} c_i \mathbf{v}_i \in \operatorname{span}$，矛盾。故 $c_{k+1} = 0$，归约到前 $k$ 个的线性无关性，得全零解。证毕

---

## 13. 例题

### 例 1：判断线性无关

判断 $\mathbf{v}_1 = [1, 2, 3]^T$，$\mathbf{v}_2 = [4, 5, 6]^T$，$\mathbf{v}_3 = [7, 8, 9]^T$ 是否线性无关。

<details><summary>解</summary>

设 $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0}$。写出方程组：

$$\begin{cases} c_1 + 4c_2 + 7c_3 = 0 \\ 2c_1 + 5c_2 + 8c_3 = 0 \\ 3c_1 + 6c_2 + 9c_3 = 0 \end{cases}$$

② − 2×①：$-3c_2 - 6c_3 = 0 \implies c_2 = -2c_3$

③ − 3×①：$-6c_2 - 12c_3 = 0 \implies c_2 = -2c_3$（一致）

代入①：$c_1 + 4(-2c_3) + 7c_3 = c_1 - c_3 = 0 \implies c_1 = c_3$

取 $c_3 = 1$，得非零解 $(1, -2, 1)$。**线性相关**。事实上 $\mathbf{v}_3 = 2\mathbf{v}_2 - \mathbf{v}_1$。

</details>

### 例 2：判定子空间并求基

$W = \{[x, y, z]^T \in \mathbb{R}^3 \mid 2x - y + z = 0\}$ 是否为 $\mathbb{R}^3$ 的子空间？若是，求维数和基。

<details><summary>解</summary>

验证三条：
1. $\mathbf{0} = [0,0,0]^T$：$2\cdot 0 - 0 + 0 = 0$ ✓
2. $\mathbf{u} = [x_1, y_1, z_1]^T, \mathbf{v} = [x_2, y_2, z_2]^T \in W$：
   $2(x_1+x_2) - (y_1+y_2) + (z_1+z_2) = (2x_1-y_1+z_1) + (2x_2-y_2+z_2) = 0 + 0 = 0$ ✓
3. $c\mathbf{u}$：$2(cx_1) - (cy_1) + (cz_1) = c(2x_1 - y_1 + z_1) = 0$ ✓

$W$ 是子空间。改写 $z = -2x + y$：

$$\mathbf{w} = \begin{bmatrix} x \\ y \\ -2x + y \end{bmatrix} = x\begin{bmatrix} 1 \\ 0 \\ -2 \end{bmatrix} + y\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$$

基 $\mathcal{B} = \{[1,0,-2]^T, [0,1,1]^T\}$，两向量不共线（线性无关），$\dim W = 2$。

</details>

### 例 3：构造基

将 $\mathbf{v}_1 = [1, 1, 0]^T$ 扩充为 $\mathbb{R}^3$ 的一组基。

<details><summary>解</summary>

已有 $\mathbf{v}_1$，它是非零向量。选 $\mathbf{v}_2 = [1, 0, 0]^T$（不在 $\operatorname{span}\{\mathbf{v}_1\}$ 中，因为 $[1,0,0]^T \neq c[1,1,0]^T$）。再选 $\mathbf{v}_3 = [0, 0, 1]^T$（不在 $\mathbf{v}_1, \mathbf{v}_2$ 张成的平面中）。

验证线性无关：检查矩阵 $\begin{bmatrix}1&1&0\\1&0&0\\0&0&1\end{bmatrix}$ 的行列式 $-1 \neq 0$，线性无关。3 个线性无关向量张成 $\mathbb{R}^3$。

所以 $\{[1,1,0]^T, [1,0,0]^T, [0,0,1]^T\}$ 是 $\mathbb{R}^3$ 的一组基。

</details>

---

## 14. 常见误区

| 误区 | 正确理解 |
|------|----------|
| 「向量就是箭头」 | 向量是满足八条公理的任何数学对象 |
| 「子空间就是子集」 | 必须经过原点且对加法/标量乘法封闭 |
| 「基只有一种」 | 一个空间有无穷多组基（如一维空间中任意非零向量都是基） |
| 「线性无关 = 正交」 | 线性无关 $\neq$ 正交。$[1,1]^T$ 和 $[1,0]^T$ 不垂直但线性无关 |
| 「零向量不算向量」 | 零向量是任何向量空间的成员，唯一的零维向量空间就是 $\{\mathbf{0}\}$ |

---

## 本章核心概念速查

| 概念 | 定义 | 一句话 |
|------|------|--------|
| 向量 | $n$ 个有序实数 | 箭头、数据点、抽象对象 |
| 加法 | 逐分量相加 | 平行四边形法则 |
| 标量乘法 | 逐分量乘 | 拉伸/压缩/反转 |
| 线性组合 | $\sum c_i\mathbf{v}_i$ | 「从这些方向出发能走多远」 |
| Span | 所有线性组合的集合 | 「这些方向能到达的全部地方」 |
| 线性无关 | 零组合只有零解 | 「没有冗余方向」 |
| 基 | 线性无关 + span 全空间 | 「描述空间的最少向量组」 |
| 维数 | 基中向量个数 | 「空间有多少个独立方向」 |
| 子空间 | 继承向量空间结构的子集 | 经过原点的直线/平面 |
| 向量空间 | 满足 10 条公理的集合 | 可安全做加法与标量乘法的集合 |

---

← 前置: 无
→ 延伸: [02 — 内积空间、范数与正交性](../02-内积空间-范数与正交性/notes.md)
