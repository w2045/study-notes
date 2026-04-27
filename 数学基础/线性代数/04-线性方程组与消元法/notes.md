# 线性代数 · 第四章 · 线性方程组与消元法

← 前置: [03 — 矩阵与线性变换](../03-矩阵与线性变换/notes.md)
→ 延伸: [05 — 行列式、逆、秩与矩阵范数](../05-行列式-逆-秩与矩阵范数/notes.md)

---

## 1. 直觉引入：从「猜解」到「系统求解」

第三章告诉我们 $A\mathbf{x} = \mathbf{b}$ 是线性变换。但知道它是什么，不等于知道**怎么求 $\mathbf{x}$**。

初中学二元一次方程用代入消元，三元就头疼了。线性代数的答案是：**高斯消元法**——一种把任何线性方程组机械化求解的算法。

> **核心洞察**：消元 = 把矩阵变成「上三角」的阶梯形。从最后一行的「单变量方程」开始回代，逐行解出所有未知数。整个过程是确定性的、算法化的。

---

## 2. 线性方程组的形式

> **定义 1（线性方程组）**：$m$ 个方程、$n$ 个未知数的线性方程组：
>
> $$\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\ \quad \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m \end{cases}$$

**矩阵形式**：$A\mathbf{x} = \mathbf{b}$，其中 $A \in \mathbb{R}^{m \times n}$ 是系数矩阵，$\mathbf{x} \in \mathbb{R}^n$ 是未知向量，$\mathbf{b} \in \mathbb{R}^m$ 是常数向量。

**增广矩阵**：$[A \mid \mathbf{b}]$，将 $A$ 和 $\mathbf{b}$ 并排写在一起。

---

## 3. 高斯消元法 (Gaussian Elimination)

### 3.1 三种初等行操作

消元法基于三种不改变解集的**初等行操作**：

| # | 操作 | 记法 | 意义 |
|---|------|------|------|
| 1 | 交换两行 | $R_i \leftrightarrow R_j$ | 重排方程顺序 |
| 2 | 某行乘非零标量 | $R_i \leftarrow cR_i$, $c \neq 0$ | 两边同乘 |
| 3 | 某行加另一行的倍数 | $R_i \leftarrow R_i + cR_j$ | 消去变量 |

### 3.2 前向消元 (Forward Elimination)

目标：将 $A$ 化为**行阶梯形 (Row Echelon Form, REF)**。

**REF 条件**：
1. 全零行在最底部
2. 每行的第一个非零元素（主元，pivot）在其上一行主元的严格右侧

**算法**（逐列处理）：
1. 选第 $k$ 列：找 $k$ 行及以下中绝对值最大的元素作**主元**
2. 若该列全零，跳到下一列
3. 将主元交换到第 $k$ 行
4. 主元归一化（可选）：$R_k \leftarrow R_k / a_{kk}$
5. 消去下面的行：对 $i = k+1, \ldots, m$，$R_i \leftarrow R_i - a_{ik} R_k$

### 3.3 回代 (Back Substitution)

前向消元后得到上三角方程组。从最后一行开始逐行求解：

对 $i = n, n-1, \ldots, 1$：
$$x_i = \left(b_i - \sum_{j=i+1}^{n} a_{ij} x_j\right) \Big/ a_{ii}$$

**前提**：$a_{ii} \neq 0$（主元非零）。若有零主元，方程组可能无解或有无穷多解。

---

## 4. 列主元消元法 (Partial Pivoting)

### 4.1 为什么需要选主元？

经典的逐个消元可能遇到**零主元**（无法归一化）或**极小主元**（导致数值不稳定）。

**例子**：$\begin{cases} 0.0001 x_1 + x_2 = 1 \\ x_1 + x_2 = 2 \end{cases}$

若不选主元，直接用 $0.0001$ 归一化会产生巨大舍入误差。

### 4.2 列主元策略

在消去第 $k$ 列时，从第 $k$ 行到第 $m$ 行中选绝对值最大的元素所在行作主元行，将该行交换到第 $k$ 行。

**效果**：数值稳定 + 避免零主元（除非整列为零）。

**全主元 (Full Pivoting)**：同时考虑行和列的交换。更稳定但通常不必需。

---

## 5. 解的三种情况

对 $A\mathbf{x} = \mathbf{b}$（$A$ 为 $m \times n$）：

| 情况 | 条件 | 解数 |
|------|------|------|
| 唯一解 | $\operatorname{rank}(A) = \operatorname{rank}([A\mid\mathbf{b}]) = n$ | 1 |
| 无穷多解 | $\operatorname{rank}(A) = \operatorname{rank}([A\mid\mathbf{b}]) < n$ | $\infty$（$n - \operatorname{rank}$ 个自由变量） |
| 无解 | $\operatorname{rank}(A) < \operatorname{rank}([A\mid\mathbf{b}])$ | 0 |

> **注**：秩的形式化定义见 Ch03 §8.2；秩-零化度定理与完整性质见 Ch05 §5。

**齐次方程组 $A\mathbf{x} = \mathbf{0}$**：必有零解。非零解存在 $\iff \operatorname{rank}(A) < n$。

---

## 6. 行阶梯形的进一步：行最简形 (RREF)

**RREF (Reduced Row Echelon Form)** 在 REF 基础上再加条件：
- 每个主元都是 1
- 每个主元所在列的其余元素都是 0

RREF 是解空间的「标准形式」。从 RREF 可以直接读出基础解系。

---

## 7. LU 分解

### 7.1 动机

如果要对多个不同的 $\mathbf{b}$ 解 $A\mathbf{x} = \mathbf{b}$，每次都做消元太低效。LU 分解将工作一分为二：
- **分解**（一次性）：$A = LU$
- **求解**（多次快速）：$L\mathbf{y} = \mathbf{b}$ → $U\mathbf{x} = \mathbf{y}$

### 7.2 定义

> **定义 2（LU 分解）**：将方阵 $A$ 分解为 $A = LU$，其中：
> - $L$ 是**下三角矩阵**（对角线全为 1，单位下三角）
> - $U$ 是**上三角矩阵**

**存在条件**：$A$ 的所有前主子式非零（即不需要行交换时）。

### 7.3 算法（Doolittle 方法）

对 $k = 1, \ldots, n$：

1. **计算 $U$ 的第 $k$ 行**：$u_{kj} = a_{kj} - \sum_{i=1}^{k-1} \ell_{ki} u_{ij}$，$j = k, \ldots, n$

2. **计算 $L$ 的第 $k$ 列**（$i = k+1, \ldots, n$）：
   $$\ell_{ik} = \left(a_{ik} - \sum_{j=1}^{k-1} \ell_{ij} u_{jk}\right) \Big/ u_{kk}$$

**与消元的关系**：消元过程中的乘数 $m_{ik} = a_{ik}^{(k)} / a_{kk}^{(k)}$ 正是 $\ell_{ik}$！

**计算复杂度**：LU 分解本身 $O(n^3)$，前代+回代各 $O(n^2)$。对单个 $\mathbf{b}$，直接消元（$O(n^3)$）和 LU + 求解（$O(n^3) + O(n^2)$）复杂度相同。LU 的优势在于：当需要对 $k$ 个不同右端项解 $A\mathbf{x} = \mathbf{b}_i$ 时，只需做一次 $O(n^3)$ 分解 + $k$ 次 $O(n^2)$ 求解 → 总复杂度 $O(n^3 + kn^2)$，vs 直接消元 $O(kn^3)$。当 $k \gg n$ 时大幅节省。

### 7.4 带行交换的 LU：PLU 分解

如果选主元时交换了行，则 $PA = LU$，其中 $P$ 是**置换矩阵**。

**求解 $A\mathbf{x} = \mathbf{b}$**：
1. 置换：$\mathbf{b}' = P\mathbf{b}$
2. 前代：解 $L\mathbf{y} = \mathbf{b}'$
3. 回代：解 $U\mathbf{x} = \mathbf{y}$

---

## 8. LU 分解的几何直觉

$A = LU$ 可理解为把复杂变换 $A$ 拆成两步：

1. $U$：先做消元（把原来的空间变成上三角结构）
2. $L$：再逆向恢复消元过程的「记录」

消元过程本身是可逆的（只要不做除以零的操作）——这意味着 $A$ 蕴含的信息可以无损分解。

---

## 9. 概念演示：消元过程追踪

> 本章的编程练习在 `编程题/` 目录下。运行 `python3 grader.py` 自动批改。

```python
import numpy as np

A = np.array([[1., 2., 1.],
              [2., 6., 1.],
              [1., 1., 4.]])
b = np.array([2., 7., 3.])

# NumPy 直接求解（内部用 LU 分解）
x = np.linalg.solve(A, b)
print(f"解: {x}")  # [-3.  2.  1.]

# 验证：残差应接近零
print(f"残差: {A @ x - b}")  # [0. 0. 0.]
```

**要点**：`np.linalg.solve` 在后台自动选择最优算法（含列主元 LU 分解）。理解其内部机理（消元→上三角→回代）能帮助你判断何时解不稳定（条件数大，见 Ch05）。

---

## 10. 例题

### 例 1：高斯消元完整过程

解方程组：
$$\begin{cases} x_1 + 2x_2 + x_3 = 2 \\ 2x_1 + 6x_2 + x_3 = 7 \\ x_1 + x_2 + 4x_3 = 3 \end{cases}$$

<details><summary>解</summary>

增广矩阵：
$$\begin{bmatrix} 1 & 2 & 1 & 2 \\ 2 & 6 & 1 & 7 \\ 1 & 1 & 4 & 3 \end{bmatrix}$$

$R_2 \leftarrow R_2 - 2R_1$：$\begin{bmatrix} 1 & 2 & 1 & 2 \\ 0 & 2 & -1 & 3 \\ 1 & 1 & 4 & 3 \end{bmatrix}$

$R_3 \leftarrow R_3 - R_1$：$\begin{bmatrix} 1 & 2 & 1 & 2 \\ 0 & 2 & -1 & 3 \\ 0 & -1 & 3 & 1 \end{bmatrix}$

$R_3 \leftarrow R_3 + \frac{1}{2}R_2$：$\begin{bmatrix} 1 & 2 & 1 & 2 \\ 0 & 2 & -1 & 3 \\ 0 & 0 & \frac{5}{2} & \frac{5}{2} \end{bmatrix}$

回代：
- $x_3 = \frac{5/2}{5/2} = 1$
- $2x_2 - 1 = 3 \implies x_2 = 2$
- $x_1 + 4 + 1 = 2 \implies x_1 = -3$

解：$[-3, 2, 1]^T$。

</details>

### 例 2：LU 分解

对 $A = \begin{bmatrix} 2 & 1 \\ 6 & 8 \end{bmatrix}$ 做 LU 分解。

<details><summary>解</summary>

消元步：$R_2 \leftarrow R_2 - 3R_1$，其中乘数 $3$ 存入 $L$。

$$L = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 2 & 1 \\ 0 & 5 \end{bmatrix}$$

验证：$LU = \begin{bmatrix} 2 & 1 \\ 6 & 8 \end{bmatrix} = A$。✓

</details>

---

## 11. 四个基本子空间 (Four Fundamental Subspaces)

矩阵 $A \in \mathbb{R}^{m \times n}$ 不仅定义了一个线性变换 $\mathbf{x} \mapsto A\mathbf{x}$，还诱导出 $\mathbb{R}^n$ 和 $\mathbb{R}^m$ 中各**两个**子空间。这四个子空间完整刻画了 $A\mathbf{x} = \mathbf{b}$ 的解的结构——这是线性代数**基本定理**的核心内容（Strang, 1993）。

### 11.1 列空间 $\operatorname{Col}(A)$

> **定义 3（列空间）**：$\operatorname{Col}(A) = \{A\mathbf{x} \mid \mathbf{x} \in \mathbb{R}^n\} \subseteq \mathbb{R}^m$。即 $A$ 各列的所有线性组合。

$\operatorname{Col}(A)$ 就是线性变换的**像** $\operatorname{im}(A)$（见 Ch03 §4.2）——只有 $\mathbf{b} \in \operatorname{Col}(A)$ 时，$A\mathbf{x} = \mathbf{b}$ 才有解。

**如何求基**：
1. 将 $A$ 化为 RREF，找到**主元列**（pivot column）的位置
2. 返回**原始 $A$** 中对应位置的列——这些列就是 $\operatorname{Col}(A)$ 的一组基

> **警惕**：RREF 的列本身不是列空间的基！行变换会改变列空间。必须回原矩阵取列。

维数：$\dim(\operatorname{Col}(A)) = \operatorname{rank}(A) = r$。

### 11.2 零空间 $\operatorname{Null}(A)$（= 核空间）

> **定义 4（零空间 / 核空间）**：$\operatorname{Null}(A) = \{\mathbf{x} \in \mathbb{R}^n \mid A\mathbf{x} = \mathbf{0}\} = \ker(A) \subseteq \mathbb{R}^n$。

这就是齐次方程组的解空间。它告诉你「多少输入被 $A$ 压扁到零」。

**关键术语**：
- **主元变量 (pivot variable)**：RREF 中主元列对应的 $x_i$
- **自由变量 (free variable)**：非主元列对应的 $x_j$，可取任意值
- 自由变量的个数 = $n - r$

**如何求基**（从 RREF 读零空间基）：
1. 化 $A$ 为 RREF，标出主元列和自由列
2. 对每个自由变量，置其为 1、其余自由变量为 0，解出各主元变量的值 → 得到一个基向量
3. 所有基向量构成 $\operatorname{Null}(A)$ 的一组基

维数：$\dim(\operatorname{Null}(A)) = n - r$（自由变量的个数）。

**通解结构定理**：若 $A\mathbf{x} = \mathbf{b}$ 有解（即 $\mathbf{b} \in \operatorname{Col}(A)$），则：
$$\mathbf{x}_{\text{general}} = \mathbf{x}_{\text{particular}} + \operatorname{Null}(A)$$
即：通解 = 一个特解 + 零空间中任意向量。零空间「参数化」了解的自由度。

### 11.3 行空间 $\operatorname{Row}(A)$

> **定义 5（行空间）**：$\operatorname{Row}(A) = \operatorname{Col}(A^T) \subseteq \mathbb{R}^n$。即 $A$ 各行的所有线性组合。

**关键事实**：初等行变换**不改变**行空间！$\operatorname{Row}(A) = \operatorname{Row}(\text{RREF}(A))$。

**如何求基**：RREF 的**非零行**直接构成 $\operatorname{Row}(A)$ 的一组基（比列空间简单——不需要回原矩阵）。

维数：$\dim(\operatorname{Row}(A)) = \operatorname{rank}(A) = r$。行列秩相等：$\operatorname{rank}(A) = \operatorname{rank}(A^T)$。

### 11.4 左零空间 $\operatorname{Null}(A^T)$

> **定义 6（左零空间）**：$\operatorname{Null}(A^T) = \{\mathbf{y} \in \mathbb{R}^m \mid \mathbf{y}^T A = \mathbf{0}\} = \{\mathbf{y} \in \mathbb{R}^m \mid A^T \mathbf{y} = \mathbf{0}\} \subseteq \mathbb{R}^m$。

名字中的「左」来自 $\mathbf{y}^T A = \mathbf{0}^T$ 中 $\mathbf{y}$ 在 $A$ 的**左侧**。维数：$\dim(\operatorname{Null}(A^T)) = m - r$。

**如何求基**：对 $[A \mid I_m]$ 做 Gauss-Jordan 消元得 $[R \mid E]$，$E$ 中对应 $R$ 零行的行向量构成基。

### 11.5 四个子空间的关系（线性代数基本定理）

**正交直和分解**：
$$\mathbb{R}^n = \operatorname{Row}(A) \oplus \operatorname{Null}(A), \qquad \mathbb{R}^m = \operatorname{Col}(A) \oplus \operatorname{Null}(A^T)$$

其中 $\oplus$ 表示**正交直和**（两个子空间不仅张成全空间，而且彼此**正交**）：
- $\operatorname{Row}(A) \perp \operatorname{Null}(A)$
- $\operatorname{Col}(A) \perp \operatorname{Null}(A^T)$

**$A$ 作为双射**：$A$ 将 $\operatorname{Row}(A)$ **一一映射**到 $\operatorname{Col}(A)$，将 $\operatorname{Null}(A)$ 映射到 $\mathbf{0}$。这意味着每个 $\mathbf{b} \in \operatorname{Col}(A)$ 恰好对应 $\operatorname{Row}(A)$ 中的一个原像——加上 $\operatorname{Null}(A)$ 中任意向量就是全部原像。

### 11.6 完整示例：一个 $3 \times 3$ 秩-2 矩阵

$$A = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 3 \\ 3 & 6 & 4 \end{bmatrix}$$

**化 RREF**：
- $R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 3R_1$：$\begin{bmatrix} 1 & 2 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{bmatrix}$
- $R_3 \leftarrow R_3 - R_2$, $R_1 \leftarrow R_1 - R_2$：$\text{RREF} = \begin{bmatrix} \mathbf{1} & 2 & 0 \\ 0 & 0 & \mathbf{1} \\ 0 & 0 & 0 \end{bmatrix}$

主元在列 1 和列 3。秩 $r = 2$。**主元变量**：$x_1, x_3$；**自由变量**：$x_2$。

**(1) $\operatorname{Col}(A)$**：基 = 原矩阵第 1、3 列 = $\{[1,2,3]^T, [1,3,4]^T\}$。维数 = 2。

**(2) $\operatorname{Null}(A)$**：自由变量 $x_2 = t$。从 RREF 回代：
$x_3 = 0$，$x_1 + 2x_2 = 0 \implies x_1 = -2t$。故 $\mathbf{x} = t[-2, 1, 0]^T$。
基 = $\{[-2,1,0]^T\}$。维数 = $n - r = 3 - 2 = 1$。

**(3) $\operatorname{Row}(A)$**：基 = RREF 的非零行 = $\{[1,2,0]^T, [0,0,1]^T\}$。维数 = 2。

**(4) $\operatorname{Null}(A^T)$**：对 $[A \mid I_3]$ 做 Gauss-Jordan：
$$\begin{bmatrix} 1 & 2 & 1 & | & 1 & 0 & 0 \\ 2 & 4 & 3 & | & 0 & 1 & 0 \\ 3 & 6 & 4 & | & 0 & 0 & 1 \end{bmatrix} \to \cdots \to \begin{bmatrix} 1 & 2 & 0 & | & 3 & -1 & 0 \\ 0 & 0 & 1 & | & -2 & 1 & 0 \\ 0 & 0 & 0 & | & -1 & -1 & 1 \end{bmatrix}$$

RREF 第 3 行为零 → 取 $E$ 的第 3 行。基 = $\{[-1,-1,1]^T\}$。维数 = $m - r = 3 - 2 = 1$。
验证：$[-1,-1,1]\,A = [-1-2+3,\;-2-4+6,\;-1-3+4] = [0,0,0]$ ✓。

**(5) 正交关系验证**：
- $\operatorname{Row}(A) \perp \operatorname{Null}(A)$：$[1,2,0]\cdot[-2,1,0] = -2+2+0 = 0$ ✓
- $\operatorname{Col}(A) \perp \operatorname{Null}(A^T)$：$[1,2,3]\cdot[-1,-1,1] = -1-2+3 = 0$ ✓, $[1,3,4]\cdot[-1,-1,1] = -1-3+4 = 0$ ✓

### 11.7 SVD 视角（预告）

四个子空间在 SVD $A = U\Sigma V^T$ 下有极简洁的表达式（见 Ch09 §）：
- $\operatorname{Col}(A) = \operatorname{span}\{\mathbf{u}_1, \ldots, \mathbf{u}_r\}$
- $\operatorname{Null}(A^T) = \operatorname{span}\{\mathbf{u}_{r+1}, \ldots, \mathbf{u}_m\}$
- $\operatorname{Row}(A) = \operatorname{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$
- $\operatorname{Null}(A) = \operatorname{span}\{\mathbf{v}_{r+1}, \ldots, \mathbf{v}_n\}$

奇异向量给出了四个子空间的标准正交基——比从 RREF 提取的基更「干净」。

---

## 12. 常见误区

| 误区 | 正确理解 |
|------|----------|
| 「消元可以任意顺序做」 | 必须逐列从左上到右下，否则前功尽弃 |
| 「有零主元就是无解」 | 可能有无穷多解（该列为自由变量） |
| 「LU 分解总是存在」 | 需要所有前主子式非零。否则需 $PA = LU$ |
| 「回代永远能得到解」 | 若消元后出现 $0 = c$（$c \neq 0$），则无解 |
| 「RREF 的列就是列空间的基」 | 行变换改变列空间——必须回**原始矩阵**取主元列 |
| 「零空间和核空间是不同概念」 | 同一概念：$\operatorname{Null}(A) = \ker(A)$，前者矩阵语境，后者变换语境 |
| 「行空间和列空间维数不同」 | 永远相同：$\dim(\operatorname{Row}(A)) = \dim(\operatorname{Col}(A)) = \operatorname{rank}(A)$ |

---

## 本章核心概念速查

| 概念 | 定义 | 一句话 |
|------|------|--------|
| 增广矩阵 | $[A \mid \mathbf{b}]$ | 把方程组写成矩阵 |
| 初等行操作 | 交换/缩放/加倍数 | 不改变解集的三种操作 |
| 前向消元 | 化为行阶梯形 | 自顶向下消去变量 |
| 主元/自由变量 | 主元列 vs 非主元列的变量 | 自由变量参数化解的自由度 |
| 列主元 | 选该列绝对值最大者 | 数值稳定的关键 |
| 回代 | 从下往上求解 | 上三角矩阵的「自然解法」 |
| REF | 行阶梯形 | 每行主元在上一行主元右侧 |
| RREF | 行最简形 | 主元 = 1，该列其余 = 0 |
| LU 分解 | $A = LU$ | 一次分解，多次求解 |
| PLU 分解 | $PA = LU$ | 带行交换的 LU |
| $\operatorname{Col}(A)$ | 列空间 | $\mathbf{b}$ 必须属于它才有解 |
| $\operatorname{Null}(A)$ | 零空间 / 核空间 | 齐次解空间，参数化通解的自由度 |
| $\operatorname{Row}(A)$ | 行空间 | RREF 的非零行，与零空间正交 |
| $\operatorname{Null}(A^T)$ | 左零空间 | $\mathbf{y}^T A = \mathbf{0}$，与列空间正交 |
| 通解结构 | $\mathbf{x}_p + \operatorname{Null}(A)$ | 特解 + 任意零空间向量 |

---

← 前置: [03 — 矩阵与线性变换](../03-矩阵与线性变换/notes.md)
→ 延伸: [05 — 行列式、逆、秩与矩阵范数](../05-行列式-逆-秩与矩阵范数/notes.md)
