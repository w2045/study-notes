# 线性代数 · 第四章 · 理论题

> 用 Markdown + LaTeX 数学公式作答。每题在 `### 解答` 下方书写推导过程。

---

## Q1 ⭐ 写出增广矩阵

将下列方程组写成增广矩阵 $[A \mid \mathbf{b}]$ 的形式：

$$\begin{cases} 2x_1 - x_2 + 3x_3 = 5 \\ x_1 + 4x_2 - x_3 = 0 \\ 3x_1 + x_2 + 2x_3 = 7 \end{cases}$$

### 解答

（在此作答）

---

## Q2 ⭐ 初等行操作

对矩阵 $\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$ 依次执行：(a) $R_2 \leftarrow R_2 - 4R_1$；(b) $R_3 \leftarrow R_3 - 7R_1$。写出结果矩阵。

### 解答

（在此作答）

---

## Q3 ⭐ 高斯消元（无选主元）

用高斯消元法（不用选主元）解方程组：

$$\begin{cases} x_1 + 2x_2 = 5 \\ 3x_1 + 4x_2 = 11 \end{cases}$$

写出增广矩阵、逐步行操作、回代过程。

### 解答

（在此作答）

---

## Q4 ⭐⭐ 回代

前向消元后得到上三角方程组：

$$\begin{cases} x_1 + 2x_2 - x_3 = 4 \\ 0x_1 + x_2 + 3x_3 = 7 \\ 0x_1 + 0x_2 + 2x_3 = 2 \end{cases}$$

用回代法求 $\mathbf{x} = [x_1, x_2, x_3]^T$。

### 解答

（在此作答）

---

## Q5 ⭐⭐ 列主元消元

对增广矩阵 $\begin{bmatrix} 0.0001 & 1 & 1 \\ 1 & 1 & 2 \end{bmatrix}$，使用列主元消元法（选取该列绝对值最大的元素作主元），写出步骤并求解。

### 解答

（在此作答）

---

## Q6 ⭐⭐ 判断解的情况

根据消元后的增广矩阵，判断以下方程组解的情况（唯一解 / 无穷多解 / 无解）：

(a) $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 0 & 0 & 0 \end{bmatrix} \mathbf{x} = \begin{bmatrix} 5 \\ 6 \\ 0 \end{bmatrix}$

(b) $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 0 & 0 & 0 \end{bmatrix} \mathbf{x} = \begin{bmatrix} 5 \\ 6 \\ 1 \end{bmatrix}$

### 解答

（在此作答）

---

## Q7 ⭐⭐ LU 分解

对 $A = \begin{bmatrix} 2 & 1 & 0 \\ 4 & 3 & 1 \\ 6 & 7 & 2 \end{bmatrix}$ 求 Doolittle LU 分解，写出 $L$ 和 $U$。

### 解答

（在此作答）

---

## Q8 ⭐⭐ 用 LU 分解求解

利用上题结果，解 $A\mathbf{x} = \mathbf{b}$，其中 $\mathbf{b} = [3, 10, 19]^T$。（先解 $L\mathbf{y} = \mathbf{b}$，再解 $U\mathbf{x} = \mathbf{y}$。）

### 解答

（在此作答）

---

## Q9 ⭐⭐⭐ 行阶梯形（REF）

将 $A = \begin{bmatrix} 1 & 2 & 1 & 3 \\ 2 & 4 & 3 & 8 \\ 3 & 6 & 4 & 11 \end{bmatrix}$ 化为行阶梯形（REF），并指出主元位置。

### 解答

（在此作答）

---

## Q10 ⭐⭐⭐ 行最简形（RREF）

将上题的 REF 进一步化为 RREF，并用 RREF 写出 $\mathbf{x} = [x_1, x_2, x_3, x_4]^T$ 的通解（$\mathbf{b} = \mathbf{0}$ 的齐次情况）。

### 解答

（在此作答）

---

## Q11 ⭐⭐⭐ 为什么需要选主元？

假设在 3 位十进制浮点精度下解方程组：

$$\begin{cases} 0.001x_1 + 1.00x_2 = 1.00 \\ 1.00x_1 + 1.00x_2 = 2.00 \end{cases}$$

(a) 不用选主元，给出消元过程和结果。
(b) 用列主元，给出消元过程和结果。
(c) 比较并说明选主元的必要性。

### 解答

（在此作答）

---

## Q12 ⭐⭐⭐ PLU 分解

对 $A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$，说明不交换行无法做 LU 分解。写出 $PA = LU$ 的 PLU 分解（$P$ 为置换矩阵），并验证。

### 解答

（在此作答）
