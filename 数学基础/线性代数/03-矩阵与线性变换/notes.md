# 线性代数 · 第三章 · 矩阵与线性变换

← 前置: [02 — 内积空间、范数与正交性](../02-内积空间-范数与正交性/notes.md)
→ 延伸: [04 — 线性方程组与消元法](../04-线性方程组与消元法/notes.md)

---

## 1. 直觉引入：矩阵的三种面孔

**数据面孔**：矩阵是一个二维数字表格。一张灰度图 = 像素值矩阵；一个数据集 = 样本×特征矩阵；一个图的邻接关系 = 邻接矩阵。

**运算面孔**：矩阵定义了一种「把输入向量变成输出向量」的规则。$A\mathbf{x} = \mathbf{b}$ 中，$A$ 是一个变换器——输入 $\mathbf{x}$，输出 $\mathbf{b}$。

**几何面孔**：矩阵乘以向量 = 对空间做变换。$\begin{bmatrix}2&0\\0&1\end{bmatrix}$ 是水平拉伸两倍；$\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ 是逆时针旋转 $90^\circ$。

> **核心洞察**：矩阵 = 线性变换的「配方」。矩阵乘法 = 变换的复合。本章打通这三张面孔。

---

## 2. 矩阵的形式化定义

> **定义 1（矩阵）**：$m \times n$ **实矩阵**是 $m$ 行 $n$ 列的矩形数组：
>
> $$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}, \quad a_{ij} \in \mathbb{R}$$
>
> $a_{ij}$ 是第 $i$ 行第 $j$ 列的元素。所有 $m \times n$ 实矩阵的集合记作 $\mathbb{R}^{m \times n}$。

**约定**：矩阵用大写粗体或大写字母 $A, B, M$；第 $i$ 行第 $j$ 列元素记作 $a_{ij}$ 或 $A_{ij}$。

两个矩阵相等 $\iff$ 同形状且每个对应元素相等。

### 2.1 矩阵表示向量

一个 $n$ 维列向量就是一个 $n \times 1$ 矩阵：

$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^{n \times 1}$$

这统一了向量和矩阵的记法。

### 2.2 矩阵-向量乘法（线性变换的核心操作）

> **定义 2（矩阵-向量乘法）**：$A \in \mathbb{R}^{m \times n}$ 乘以 $\mathbf{x} \in \mathbb{R}^n$ 得到 $\mathbf{b} \in \mathbb{R}^m$：
>
> $$b_i = \sum_{j=1}^{n} a_{ij} x_j, \quad i = 1, \ldots, m$$

**两种等价观点**：

1. **行观点（逐分量）**：$\mathbf{b}$ 的第 $i$ 个分量是 $A$ 第 $i$ 行与 $\mathbf{x}$ 的点积。
2. **列观点（线性组合）**：
   $$A\mathbf{x} = x_1 \begin{bmatrix} a_{11} \\ \vdots \\ a_{m1} \end{bmatrix} + x_2 \begin{bmatrix} a_{12} \\ \vdots \\ a_{m2} \end{bmatrix} + \cdots + x_n \begin{bmatrix} a_{1n} \\ \vdots \\ a_{mn} \end{bmatrix}$$

   $A\mathbf{x}$ 是 $A$ 各列的线性组合，系数为 $\mathbf{x}$ 的分量。**这是线性代数最核心的视角。**

---

## 3. 矩阵运算

### 3.1 加法与标量乘法

> **定义 3（矩阵加法）**：对同形状矩阵 $A, B \in \mathbb{R}^{m \times n}$：
>
> $$(A + B)_{ij} = a_{ij} + b_{ij}$$

> **定义 4（标量乘法）**：对 $c \in \mathbb{R}$：
>
> $$(cA)_{ij} = c \cdot a_{ij}$$

$\mathbb{R}^{m \times n}$ 是 $mn$ 维向量空间：它有加法、标量乘法，满足所有 10 条向量空间公理。

### 3.2 矩阵乘法

> **定义 5（矩阵乘法）**：$A \in \mathbb{R}^{m \times n}$ 乘以 $B \in \mathbb{R}^{n \times p}$ 得到 $C \in \mathbb{R}^{m \times p}$：
>
> $$c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$$
>
> $c_{ij}$ 是 $A$ 的第 $i$ 行与 $B$ 的第 $j$ 列的点积。

**几何意义**：$C = AB$ 表示先应用变换 $B$，再应用变换 $A$——即变换的复合。

**手算示例**（$2 \times 3$ 乘 $3 \times 2$）：
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}, \quad B = \begin{bmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{bmatrix}$$
$$c_{11} = 1\cdot7 + 2\cdot9 + 3\cdot11 = 7+18+33 = 58$$
$$c_{12} = 1\cdot8 + 2\cdot10 + 3\cdot12 = 8+20+36 = 64$$
$$c_{21} = 4\cdot7 + 5\cdot9 + 6\cdot11 = 28+45+66 = 139$$
$$c_{22} = 4\cdot8 + 5\cdot10 + 6\cdot12 = 32+50+72 = 154$$
$$AB = \begin{bmatrix} 58 & 64 \\ 139 & 154 \end{bmatrix}$$

用**列观点**理解：$AB$ 的第 1 列 = $A \cdot (B$ 的第 1 列$)$ = $7\begin{bmatrix}1\\4\end{bmatrix} + 9\begin{bmatrix}2\\5\end{bmatrix} + 11\begin{bmatrix}3\\6\end{bmatrix} = \begin{bmatrix}58\\139\end{bmatrix}$。这就是「线性组合的线性组合」。

**关键性质**：
- **结合律**：$(AB)C = A(BC)$（变换复合天然结合）
- **分配律**：$A(B + C) = AB + AC$，$(A + B)C = AC + BC$
- **标量可交换**：$c(AB) = (cA)B = A(cB)$
- **不交换**：一般 $AB \neq BA$（甚至形状不对无法乘）

> **警告**：矩阵乘法不满足交换律！$AB$ 和 $BA$ 通常完全不同。这与普通乘法根本不同。

### 3.3 转置

> **定义 6（转置）**：$A \in \mathbb{R}^{m \times n}$ 的**转置** $A^T \in \mathbb{R}^{n \times m}$：
>
> $$(A^T)_{ij} = a_{ji}$$

**几何意义**：转置是「行变列，列变行」——对换行和列的角色。

**关键性质**：
- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(cA)^T = cA^T$
- $(AB)^T = B^T A^T$（注意顺序反转！）
- $(A^T)^{-1} = (A^{-1})^T$（如果 $A$ 可逆）

**$(AB)^T = B^T A^T$ 的直觉**：变换的复合 $AB$，先 $B$ 后 $A$。转置后变成先 $A^T$ 后 $B^T$，顺序自然反转。

### 3.4 逆矩阵（初步定义）

> **定义 7（逆矩阵）**：方阵 $A \in \mathbb{R}^{n \times n}$ 的**逆** $A^{-1}$ 满足：
>
> $$A A^{-1} = A^{-1} A = I_n$$
>
> 若 $A^{-1}$ 存在，称 $A$ **可逆 (invertible)** 或**非奇异 (nonsingular)**。

**存在性**：
- 非方阵（$m \neq n$）没有双边逆——输出空间和输入空间维数不同，无法双向一一对应
- 矩形矩阵可以有**左逆**（若列满秩，$A^T A$ 可逆 → $A_{\text{left}}^{-1} = (A^T A)^{-1} A^T$）或**右逆**（若行满秩）
- 最一般的「广义逆」是 **Moore-Penrose 伪逆** $A^+$，它对任意矩阵存在（见 Ch09 §）

**基本性质**（证明见 Ch05 §3.3）：
- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1} A^{-1}$（顺序反转）
- $(A^T)^{-1} = (A^{-1})^T$

> 逆的计算方法（伴随矩阵法、Gauss-Jordan 消元法）和可逆性等价条件见 Ch05 §3。

---

## 4. 线性变换

> **定义 8（线性变换）**：映射 $T: \mathbb{R}^n \to \mathbb{R}^m$ 是**线性变换** $\iff$
> 1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
> 2. $T(c\mathbf{u}) = c\,T(\mathbf{u})$

### 4.1 矩阵表示定理

> **定理（矩阵表示）**：每个线性变换 $T: \mathbb{R}^n \to \mathbb{R}^m$ 都对应唯一一个 $m \times n$ 矩阵 $A$，使得 $T(\mathbf{x}) = A\mathbf{x}$。$A$ 的第 $j$ 列是 $T(\mathbf{e}_j)$（第 $j$ 个标准基向量的像）。
>
> $$A = \begin{bmatrix} | & | & & | \\ T(\mathbf{e}_1) & T(\mathbf{e}_2) & \cdots & T(\mathbf{e}_n) \\ | & | & & | \end{bmatrix}$$

**这意味着**：你只需要知道基向量变换到哪里，就能知道整个变换！这是线性性的本质威力。

**例子**：旋转 $90^\circ$（$\mathbb{R}^2$）：$\mathbf{e}_1 = [1,0]^T \to [0,1]^T$，$\mathbf{e}_2 = [0,1]^T \to [-1,0]^T$。矩阵：
$$R_{90^\circ} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$

### 4.2 核空间与像空间 (Kernel and Image)

线性变换 $T: V \to W$ 自然诱导出 $V$ 和 $W$ 中各一个重要子空间——这是理解「变换丢掉了什么信息」和「变换还保留了哪些方向」的关键。

> **定义 9（核空间 / Kernel）**：$T$ 的**核** $\ker(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}\}$。即所有被 $T$「压扁」到原点的向量。

> **定义 10（像空间 / Image）**：$T$ 的**像** $\operatorname{im}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\} \subseteq W$。即 $T$ 的输出能「到达」的所有向量。

**定理**：$\ker(T)$ 是 $V$ 的子空间，$\operatorname{im}(T)$ 是 $W$ 的子空间。

**与矩阵的对应（核心连接）**：若 $T(\mathbf{x}) = A\mathbf{x}$（$A \in \mathbb{R}^{m \times n}$），则：
- $\ker(T) = \operatorname{Null}(A) = \{\mathbf{x} \in \mathbb{R}^n \mid A\mathbf{x} = \mathbf{0}\}$——这称为 $A$ 的**零空间**
- $\operatorname{im}(T) = \operatorname{Col}(A) = A$ 各列的张成——这称为 $A$ 的**列空间**

> 「核空间」(kernel) 和「零空间」(null space) 是同一概念的两个名字——抽象线性映射中用 $\ker$，矩阵语境中用 $\operatorname{Null}$。

**定理（单射与满射的判据）**：
- $T$ 是单射（one-to-one）$\iff \ker(T) = \{\mathbf{0}\}$——核为零意味着每个输出最多来自一个输入
- $T$ 是满射（onto）$\iff \operatorname{im}(T) = W$——像填满整个目标空间

**计算示例**：$T: \mathbb{R}^3 \to \mathbb{R}^2$，$T([x,y,z]^T) = [x+y, \; y+z]^T$。

1. 写出 $T$ 的矩阵：$T(\mathbf{e}_1)=[1,0]^T$，$T(\mathbf{e}_2)=[1,1]^T$，$T(\mathbf{e}_3)=[0,1]^T$，故 $A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}$。

2. **求 $\ker(T)$**：解 $A\mathbf{x} = \mathbf{0}$：
   $$\begin{cases} x + y = 0 \\ y + z = 0 \end{cases} \implies x = -y,\; z = -y$$
   令 $y = t$，则 $\mathbf{x} = t[1, -1, 1]^T$。故 $\ker(T) = \operatorname{span}\{[1,-1,1]^T\}$，维数 $= 1$。

3. **求 $\operatorname{im}(T)$**：$A$ 的前两列 $\{[1,0]^T, [1,1]^T\}$ 已线性无关，张成全 $\mathbb{R}^2$。故 $\operatorname{im}(T) = \mathbb{R}^2$，维数 $= 2$。

4. **验证维数关系**：$\dim \ker(T) + \dim \operatorname{im}(T) = 1 + 2 = 3 = \dim(\mathbb{R}^3)$。这不是巧合——这是**秩-零化度定理**的特例（见 Ch05 §5.2）。

### 4.3 经典线性变换

| 变换 | $\mathbb{R}^2$ 矩阵 | 效果 |
|------|-------------------|------|
| 恒等变换 | $\begin{bmatrix}1&0\\0&1\end{bmatrix}$ | 不变 |
| $x$ 轴反射 | $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$ | 上下翻转 |
| 旋转 $\theta$ | $\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$ | 逆时针旋转 |
| 水平拉伸 $s$ | $\begin{bmatrix}s&0\\0&1\end{bmatrix}$ | $x$ 方向缩放 |
| 剪切 | $\begin{bmatrix}1&k\\0&1\end{bmatrix}$ | $x$ 方向倾斜 |
| 投影到 $x$ 轴 | $\begin{bmatrix}1&0\\0&0\end{bmatrix}$ | 压扁到 $x$ 轴 |

### 4.4 复合与矩阵乘法

若 $S(\mathbf{x}) = B\mathbf{x}$ 和 $T(\mathbf{x}) = A\mathbf{x}$ 是线性变换，则复合 $(T \circ S)(\mathbf{x}) = T(S(\mathbf{x})) = A(B\mathbf{x}) = (AB)\mathbf{x}$。

**矩阵乘法 = 变换复合**。这就是矩阵乘法定义如此「奇怪」的根本原因。

---

## 5. 特殊矩阵

### 5.1 方阵

> **定义 11（方阵）**：$m = n$ 的矩阵。$\mathbb{R}^{n \times n}$ 是所有 $n \times n$ 方阵的集合。

方阵的地位特殊，因为线性算子（输入输出同空间）用方阵表示。

### 5.2 零矩阵

$$0_{m \times n} = \begin{bmatrix} 0 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & 0 \end{bmatrix}$$

$A + 0 = A$，$0A = 0$，$A0 = 0$（注意形状）。

### 5.3 单位矩阵

$$I_n = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix}$$

$I_n A = A$（$A$ 为 $n \times p$），$A I_n = A$（$A$ 为 $m \times n$）。$I_n$ 对应恒等变换。

### 5.4 对角矩阵

$$D = \begin{bmatrix} d_1 & 0 & \cdots & 0 \\ 0 & d_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & d_n \end{bmatrix} = \operatorname{diag}(d_1, \ldots, d_n)$$

**几何意义**：对角矩阵在每个坐标轴方向上独立缩放。

**性质**：
- $D^k = \operatorname{diag}(d_1^k, \ldots, d_n^k)$
- $\det D = \prod d_i$
- 两个对角矩阵乘法可交换

### 5.5 三角矩阵

> **定义 12**：
> - **上三角矩阵**：$i > j$ 时 $a_{ij} = 0$（主对角线以下全零）
> - **下三角矩阵**：$i < j$ 时 $a_{ij} = 0$（主对角线以上全零）

**性质**：三角矩阵的乘积仍为三角；行列式 = 对角线元素之积。

### 5.6 对称矩阵与反对称矩阵

> **定义 13（对称矩阵）**：$A^T = A$，即 $a_{ij} = a_{ji}$。

> **定义 14（反对称矩阵）**：$A^T = -A$，即 $a_{ij} = -a_{ji}$（对角线必为零）。

**重要性**：任意方阵可唯一分解为对称部分 + 反对称部分：

$$A = \underbrace{\frac{A + A^T}{2}}_{\text{对称}} + \underbrace{\frac{A - A^T}{2}}_{\text{反对称}}$$

### 5.7 正交矩阵

> **定义 15（正交矩阵）**：方阵 $Q$ 满足 $Q^T Q = Q Q^T = I$，即 $Q^{-1} = Q^T$。

**几何意义**：正交矩阵的行（或列）组成一组标准正交基。正交矩阵表示**刚体变换**——旋转或反射，保持长度和角度。

**性质**：
- $\|Q\mathbf{x}\| = \|\mathbf{x}\|$（保长）
- $(Q\mathbf{x}) \cdot (Q\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$（保角）
- $|\det Q| = 1$

### 5.8 酉矩阵、Hermitian 与正规矩阵（复数域推广）

当矩阵元素取复数时，转置 $A^T$ 需替换为**共轭转置** $A^* = \overline{A}^T$（见 Ch02 §3.1）。

> **定义 16（Hermitian 矩阵）**：复方阵 $A$ 满足 $A^* = A$，即 $a_{ij} = \overline{a_{ji}}$。

Hermitian 矩阵是实对称矩阵在复数域的直接推广。对角线元素必为实数（因为 $a_{ii} = \overline{a_{ii}}$）。

> **定义 17（酉矩阵）**：复方阵 $U$ 满足 $U^* U = U U^* = I$，即 $U^{-1} = U^*$。

酉矩阵是实正交矩阵的复数推广，保持 Hermitian 内积不变。**DFT 矩阵** $F_{kj} = \frac{1}{\sqrt{n}} e^{-2\pi i kj / n}$ 是最重要的酉矩阵之一。

> **定义 18（正规矩阵）**：方阵 $A$ 满足 $A^* A = A A^*$。

正规矩阵是「可酉对角化」的充要条件（见 Ch07）。重要子族：
| 矩阵族 | 条件 | 特征值 |
|--------|------|--------|
| Hermitian | $A^* = A$ | 全为实数 |
| 酉矩阵 | $U^* = U^{-1}$ | 全在单位圆上 ($|\lambda|=1$) |
| 实对称 | $A^T = A$ | 全为实数，可正交对角化 |
| 实正交 | $Q^T = Q^{-1}$ | 在单位圆上 |

> **记忆**：Hermitian $\subset$ 正规矩阵，酉矩阵 $\subset$ 正规矩阵。正规矩阵 = 可酉对角化。

---

## 6. Kronecker 积

> **定义 19（Kronecker 积）**：$A \in \mathbb{R}^{m \times n}$ 与 $B \in \mathbb{R}^{p \times q}$ 的 Kronecker 积 $A \otimes B \in \mathbb{R}^{mp \times nq}$：
>
> $$A \otimes B = \begin{bmatrix} a_{11}B & a_{12}B & \cdots & a_{1n}B \\ a_{21}B & a_{22}B & \cdots & a_{2n}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mn}B \end{bmatrix}$$

每个元素 $a_{ij}$ 被 $a_{ij}B$ 这个 $p \times q$ 块代替。

**用途**：
- 高维数组运算的向量化
- 线性矩阵方程的求解（Lyapunov 方程等）
- 量子力学中的多粒子态

**性质**（假设可乘）：
- $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$
- $(A \otimes B)^T = A^T \otimes B^T$
- $(A \otimes B)^{-1} = A^{-1} \otimes B^{-1}$（若可逆）

**具体例子**：$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$, $B = I_2$，则：
$$A \otimes B = \begin{bmatrix} 1\cdot I_2 & 2\cdot I_2 \\ 3\cdot I_2 & 4\cdot I_2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 2 \\ 3 & 0 & 4 & 0 \\ 0 & 3 & 0 & 4 \end{bmatrix}$$
这在求解 **Sylvester 方程** $AX + XB = C$ 时出现——向量化后 $(I \otimes A + B^T \otimes I)\operatorname{vec}(X) = \operatorname{vec}(C)$。

---

## 7. 矩阵的内积与范数

### 7.1 Frobenius 内积

$$\langle A, B \rangle_F = \operatorname{tr}(A^T B) = \sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} b_{ij}$$

这等价于将矩阵「拉直」为 $mn$ 维向量后的标准内积。对复矩阵，Frobenius 内积为 $\langle A, B \rangle_F = \operatorname{tr}(A^* B)$。

### 7.2 Frobenius 范数（主定义位置）

$$\|A\|_F = \sqrt{\langle A, A \rangle_F} = \sqrt{\sum_{i,j} a_{ij}^2} = \sqrt{\operatorname{tr}(A^T A)}$$

这是矩阵所有元素平方和的平方根——最简单的矩阵范数。等价表达式 $\|A\|_F = \sqrt{\sum \sigma_i^2}$ 见 Ch09（SVD）。

> 后续章节（Ch05 §7.1, Ch09 §6）将给出 Frobenius 范数的等价定义，均指同一概念。

### 7.3 迹 (Trace)（主定义位置）

> **定义 20（迹）**：方阵 $A$ 的**迹**是主对角线元素之和：
>
> $$\operatorname{tr}(A) = \sum_{i=1}^{n} a_{ii}$$

**性质**：
- $\operatorname{tr}(A + B) = \operatorname{tr}(A) + \operatorname{tr}(B)$
- $\operatorname{tr}(cA) = c\operatorname{tr}(A)$
- $\operatorname{tr}(AB) = \operatorname{tr}(BA)$（循环性质！即使 $AB \neq BA$）
- $\operatorname{tr}(P^{-1}AP) = \operatorname{tr}(A)$（相似不变性）
- $\operatorname{tr}(A) = \sum \lambda_i$（特征值之和，见 Ch06）

> Ch05 §6 将回顾迹的性质，此处为主定义。

---

## 8. 变换的可视化理解

### 8.1 从单位正方形看变换

将单位正方形（由 $\mathbf{e}_1 = [1,0]^T$ 和 $\mathbf{e}_2 = [0,1]^T$ 围成）送入矩阵 $A$。

- 恒等变换：仍是正方形
- 对角矩阵 $\operatorname{diag}(2, 3)$：拉伸为 $2 \times 3$ 的矩形
- 旋转矩阵：正方形旋转，保持面积
- 剪切矩阵：正方形变平行四边形
- 投影矩阵：正方形压扁为线段

**面积变化** = $|\det A|$（第 05 章）——矩阵对应的线性变换对空间的「缩放因子」。

### 8.2 秩的直觉与形式化定义

> **定义 21（秩）**：矩阵 $A \in \mathbb{R}^{m \times n}$ 的**秩** $\operatorname{rank}(A)$ 是 $A$ 中线性无关列的最大个数：
>
> $$\operatorname{rank}(A) = \dim(\operatorname{Col}(A)) = \dim(\operatorname{im}(T_A))$$
>
> 其中 $T_A(\mathbf{x}) = A\mathbf{x}$。等价地，秩 = 行阶梯形中非零行的个数 = 主元列的个数。

- 满秩方阵：$\operatorname{rank}(A) = n$，不会缩维，可逆
- 秩亏方阵：$\operatorname{rank}(A) < n$，会把空间「压扁」到更低维
- 非方阵：从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$，秩 $\leq \min(m, n)$
- $\operatorname{rank}(A) = \operatorname{rank}(A^T)$（行秩 = 列秩）

> 秩的完整性质与秩-零化度定理见 Ch05 §5。

---

## 9. 概念演示：变换的复合

> 本章的编程练习在 `编程题/` 目录下。运行 `python3 grader.py` 自动批改。

```python
import numpy as np

# 旋转 90° + 水平拉伸 = 先拉伸再旋转
rotate = np.array([[0, -1],
                   [1,  0]])
stretch = np.array([[2, 0],
                    [0, 1]])

# 复合变换 = 矩阵乘法（注意顺序！先拉伸后旋转 = rotate @ stretch）
composite = rotate @ stretch  # [[0, -1], [2, 0]]

# 单位正方形顶点
square = np.array([[0, 1, 1, 0],
                   [0, 0, 1, 1]])
transformed = composite @ square
print(transformed)
# [[ 0 -1 -1  0]
#  [ 0  2  2  0]]  → 平行四边形
```

**要点**：$AB$ 的几何意义是「先应用 $B$ 变换，再应用 $A$ 变换」。矩阵乘法不交换的根本原因：变换的顺序不可随意调换。

---

## 10. 重要定理证明

### 10.1 矩阵乘法结合律

> **定理**：$(AB)C = A(BC)$。

**证明**：对任意 $i, j$：
$$[(AB)C]_{ij} = \sum_{k} (AB)_{ik} c_{kj} = \sum_{k} \left(\sum_{\ell} a_{i\ell} b_{\ell k}\right) c_{kj} = \sum_{\ell} a_{i\ell} \left(\sum_{k} b_{\ell k} c_{kj}\right) = [A(BC)]_{ij}$$

两次求和可交换顺序（有限和），得证。证毕

### 10.2 $(AB)^T = B^T A^T$

> **定理**：矩阵乘积的转置等于转置的逆序乘积。

**证明**：
$$[(AB)^T]_{ij} = (AB)_{ji} = \sum_{k} a_{jk} b_{ki} = \sum_{k} (A^T)_{kj} (B^T)_{ik} = \sum_{k} (B^T)_{ik} (A^T)_{kj} = [B^T A^T]_{ij}$$

证毕

### 10.3 $\operatorname{tr}(AB) = \operatorname{tr}(BA)$

> **定理**：迹的循环不变性。

**证明**：设 $A \in \mathbb{R}^{m \times n}$，$B \in \mathbb{R}^{n \times m}$。

$$\operatorname{tr}(AB) = \sum_{i=1}^{m} (AB)_{ii} = \sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} b_{ji}$$

$$\operatorname{tr}(BA) = \sum_{j=1}^{n} (BA)_{jj} = \sum_{j=1}^{n} \sum_{i=1}^{m} b_{ji} a_{ij}$$

双重求和交换次序，二式相等。证毕

---

## 11. 例题

### 例 1：矩阵乘法的列观点

计算 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 5 \\ 6 \end{bmatrix}$ 用列观点。

<details><summary>解</summary>

列观点：$A\mathbf{x} = 5 \begin{bmatrix} 1 \\ 3 \end{bmatrix} + 6 \begin{bmatrix} 2 \\ 4 \end{bmatrix} = \begin{bmatrix} 5 + 12 \\ 15 + 24 \end{bmatrix} = \begin{bmatrix} 17 \\ 39 \end{bmatrix}$。

</details>

### 例 2：求线性变换的矩阵

$T: \mathbb{R}^2 \to \mathbb{R}^2$ 定义为 $T([x, y]^T) = [2x + y, x - y]^T$。求矩阵表示。

<details><summary>解</summary>

$T(\mathbf{e}_1) = T([1,0]^T) = [2, 1]^T$ 是第一列。
$T(\mathbf{e}_2) = T([0,1]^T) = [1, -1]^T$ 是第二列。

$$A = \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}$$

</details>

### 例 3：判断矩阵类型

判断 $A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ 的类型。

<details><summary>解</summary>

$A^T = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} = -A$，所以 $A$ 是**反对称矩阵**。

$A^T A = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$，所以 $A$ 也是**正交矩阵**。

这就是 $\mathbb{R}^2$ 中旋转 $90^\circ$ 的矩阵。

</details>

---

## 12. 常见误区

| 误区 | 正确理解 |
|------|----------|
| 「矩阵就是数字表格」 | 矩阵是线性变换的具体表示，数字只是载体 |
| 「$AB = BA$」 | 矩阵乘法一般不交换！反例：$\begin{bmatrix}0&1\\0&0\end{bmatrix}\begin{bmatrix}0&0\\1&0\end{bmatrix} \neq \begin{bmatrix}0&0\\1&0\end{bmatrix}\begin{bmatrix}0&1\\0&0\end{bmatrix}$ |
| 「$A^2 = 0 \implies A = 0$」 | 反例：$\begin{bmatrix}0&1\\0&0\end{bmatrix}^2 = 0$，但矩阵非零（幂零矩阵） |
| 「转置就是翻一下」 | 转置的深层含义是伴随算子（对偶空间中的变换） |
| 「对称矩阵一定可对角化」 | 实对称一定可正交对角化，这里正确。但非实对称另当别论 |

---

## 本章核心概念速查

| 概念 | 定义 | 一句话 |
|------|------|--------|
| 矩阵 | $m \times n$ 数组 | 线性变换的配方 |
| 矩阵-向量乘 | $b_i = \sum_j a_{ij}x_j$ | 各列的线性组合 |
| 矩阵乘法 | $c_{ij} = \sum_k a_{ik}b_{kj}$ | 变换的复合 |
| 转置 | $(A^T)_{ij} = a_{ji}$ | 行列互换 |
| 单位矩阵 | $\operatorname{diag}(1, \ldots, 1)$ | 恒等变换 |
| 对称矩阵 | $A^T = A$ | 行列对称 |
| 反对称矩阵 | $A^T = -A$ | 行列反号 |
| 正交矩阵 | $Q^T Q = I$ | 旋转/反射 |
| 对角矩阵 | 仅对角线非零 | 坐标轴独立缩放 |
| 迹 | $\sum a_{ii}$ | 对角线之和 = 特征值之和 |
| Frobenius 范数 | $\sqrt{\sum a_{ij}^2}$ | 矩阵的「长度」 |
| Kronecker 积 | $A \otimes B$ | 逐元素块乘 |
| 线性变换 | $T(c\mathbf{u}+\mathbf{v}) = cT(\mathbf{u})+T(\mathbf{v})$ | 保线性结构 |

---

← 前置: [02 — 内积空间、范数与正交性](../02-内积空间-范数与正交性/notes.md)
→ 延伸: [04 — 线性方程组与消元法](../04-线性方程组与消元法/notes.md)
