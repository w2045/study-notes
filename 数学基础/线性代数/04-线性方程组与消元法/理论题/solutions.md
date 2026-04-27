# 线性代数 · 第四章 · 理论题 — 参考答案

---

## Q1 写出增广矩阵

<details><summary>解</summary>

$$[A \mid \mathbf{b}] = \begin{bmatrix} 2 & -1 & 3 & | & 5 \\ 1 & 4 & -1 & | & 0 \\ 3 & 1 & 2 & | & 7 \end{bmatrix}$$

</details>

---

## Q2 初等行操作

<details><summary>解</summary>

(a) $R_2 \leftarrow R_2 - 4R_1$：$\begin{bmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ 7 & 8 & 9 \end{bmatrix}$

(b) $R_3 \leftarrow R_3 - 7R_1$：$\begin{bmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ 0 & -6 & -12 \end{bmatrix}$

</details>

---

## Q3 高斯消元（无选主元）

<details><summary>解</summary>

增广矩阵：$\begin{bmatrix} 1 & 2 & 5 \\ 3 & 4 & 11 \end{bmatrix}$

$R_2 \leftarrow R_2 - 3R_1$：$\begin{bmatrix} 1 & 2 & 5 \\ 0 & -2 & -4 \end{bmatrix}$

回代：
- 第 2 行：$-2x_2 = -4 \implies x_2 = 2$
- 第 1 行：$x_1 + 2(2) = 5 \implies x_1 = 1$

解：$[1, 2]^T$。

</details>

---

## Q4 回代

<details><summary>解</summary>

- 第 3 行：$2x_3 = 2 \implies x_3 = 1$
- 第 2 行：$x_2 + 3(1) = 7 \implies x_2 = 4$
- 第 1 行：$x_1 + 2(4) - 1 = 4 \implies x_1 + 7 = 4 \implies x_1 = -3$

解：$[-3, 4, 1]^T$。

</details>

---

## Q5 列主元消元

<details><summary>解</summary>

增广矩阵：$\begin{bmatrix} 0.0001 & 1 & 1 \\ 1 & 1 & 2 \end{bmatrix}$

第 1 列中，$\max(|0.0001|, |1|) = 1$ 在第 2 行。

交换 $R_1 \leftrightarrow R_2$：$\begin{bmatrix} 1 & 1 & 2 \\ 0.0001 & 1 & 1 \end{bmatrix}$

$R_2 \leftarrow R_2 - 0.0001R_1$：$\begin{bmatrix} 1 & 1 & 2 \\ 0 & 0.9999 & 0.9998 \end{bmatrix}$

回代：
- $0.9999x_2 = 0.9998 \implies x_2 \approx 1.0$
- $x_1 + 1 = 2 \implies x_1 = 1$

解：$[1, 1]^T$。（用精确分数：$x_2 = \frac{1 - 0.0001 \times 2}{1 - 0.0001} = \frac{0.9998}{0.9999} \approx 1$）

</details>

---

## Q6 判断解的情况

<details><summary>解</summary>

**(a)** 最后一行 $0 = 0$，第三变量 $x_3$ 是自由变量，$\operatorname{rank} = 2 < n = 3$。**无穷多解**。

**(b)** 最后一行 $0 = 1$，矛盾。**无解**。

</details>

---

## Q7 LU 分解

<details><summary>解</summary>

Doolittle 算法：

**$k = 1$**：
- $U_{1,:} = [2, 1, 0]$
- $L_{2,1} = 4/2 = 2$, $L_{3,1} = 6/2 = 3$

**$k = 2$**：
- $u_{22} = 3 - 2 \cdot 1 = 1$, $u_{23} = 1 - 2 \cdot 0 = 1$
- $L_{3,2} = (7 - 3 \cdot 1) / 1 = 4$

**$k = 3$**：
- $u_{33} = 2 - 3 \cdot 0 - 4 \cdot 1 = -2$

$$L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 3 & 4 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & -2 \end{bmatrix}$$

验证：$LU = \begin{bmatrix} 2 & 1 & 0 \\ 4 & 3 & 1 \\ 6 & 7 & -2 \end{bmatrix}$ 不对，让我重新算。

仔细做：$A = \begin{bmatrix} 2 & 1 & 0 \\ 4 & 3 & 1 \\ 6 & 7 & 2 \end{bmatrix}$

$L_{21} = 4/2 = 2$，$L_{31} = 6/2 = 3$

消元后 $A^{(1)}$：
- 第 2 行：$4 - 2\cdot2 = 0$, $3 - 2\cdot1 = 1$, $1 - 2\cdot0 = 1$
- 第 3 行：$6 - 3\cdot2 = 0$, $7 - 3\cdot1 = 4$, $2 - 3\cdot0 = 2$

$L_{32} = 4/1 = 4$

消元后第 3 行：$0$, $4 - 4\cdot1 = 0$, $2 - 4\cdot1 = -2$

$$L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 3 & 4 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & -2 \end{bmatrix}$$

验证：$LU = \begin{bmatrix} 2 & 1 & 0 \\ 4 & 2+1=3 & 0+1=1 \\ 6 & 3+4=7 & 0+4-2=2 \end{bmatrix} = A$ ✓

</details>

---

## Q8 用 LU 分解求解

<details><summary>解</summary>

**前代 $L\mathbf{y} = \mathbf{b}$**：

$$\begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 3 & 4 & 1 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix} = \begin{bmatrix} 3 \\ 10 \\ 19 \end{bmatrix}$$

- $y_1 = 3$
- $2y_1 + y_2 = 10 \implies 6 + y_2 = 10 \implies y_2 = 4$
- $3y_1 + 4y_2 + y_3 = 19 \implies 9 + 16 + y_3 = 19 \implies y_3 = -6$

**回代 $U\mathbf{x} = \mathbf{y}$**：

$$\begin{bmatrix} 2 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & -2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 3 \\ 4 \\ -6 \end{bmatrix}$$

- $-2x_3 = -6 \implies x_3 = 3$
- $x_2 + 3 = 4 \implies x_2 = 1$
- $2x_1 + 1 = 3 \implies x_1 = 1$

解：$[1, 1, 3]^T$。

</details>

---

## Q9 行阶梯形（REF）

<details><summary>解</summary>

$$\begin{bmatrix} 1 & 2 & 1 & 3 \\ 2 & 4 & 3 & 8 \\ 3 & 6 & 4 & 11 \end{bmatrix}$$

$R_2 \leftarrow R_2 - 2R_1$：$\begin{bmatrix} 1 & 2 & 1 & 3 \\ 0 & 0 & 1 & 2 \\ 3 & 6 & 4 & 11 \end{bmatrix}$

$R_3 \leftarrow R_3 - 3R_1$：$\begin{bmatrix} 1 & 2 & 1 & 3 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 1 & 2 \end{bmatrix}$

$R_3 \leftarrow R_3 - R_2$：$\begin{bmatrix} 1 & 2 & 1 & 3 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}$

这是 REF。主元位置：$(1,1)$ 的 1 和 $(2,3)$ 的 1。第 2 列和第 4 列无主元。

</details>

---

## Q10 行最简形（RREF）

<details><summary>解</summary>

从 REF：$\begin{bmatrix} 1 & 2 & 1 & 3 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}$

$R_1 \leftarrow R_1 - R_2$：$\begin{bmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}$

这是 RREF。对于齐次方程 $A\mathbf{x} = \mathbf{0}$：

$$\begin{cases} x_1 + 2x_2 + x_4 = 0 \\ x_3 + 2x_4 = 0 \end{cases}$$

主元变量：$x_1, x_3$；自由变量：$x_2, x_4$。

通解：
$$\mathbf{x} = x_2\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + x_4\begin{bmatrix} -1 \\ 0 \\ -2 \\ 1 \end{bmatrix}$$

</details>

---

## Q11 为什么需要选主元？

<details><summary>解</summary>

**(a) 不选主元**：系统 $\begin{cases} 0.001x_1 + 1.00x_2 = 1.00 \\ 1.00x_1 + 1.00x_2 = 2.00 \end{cases}$

乘数 $m = 1.00 / 0.001 = 1000$。$R_2 \leftarrow R_2 - 1000R_1$：

新 $R_2$ 常数：$2.00 - 1000 \cdot 1.00 = -998$（三位精度下），$x_2$ 系数：$1.00 - 1000 \cdot 1.00 = -999$。

- $-999x_2 \approx -998 \implies x_2 \approx 0.999$（有很大的舍入误差风险）

回代：$0.001x_1 + 1.00(0.999) = 1.00 \implies 0.001x_1 \approx 0.001 \implies x_1 \approx 1$。

若精确算，$x_1 = x_2 = 1$。但浮点误差可能偏离。

**(b) 列主元**：交换 $R_1 \leftrightarrow R_2$：

$\begin{cases} 1.00x_1 + 1.00x_2 = 2.00 \\ 0.001x_1 + 1.00x_2 = 1.00 \end{cases}$

乘数 $m = 0.001 / 1.00 = 0.001$。$R_2 \leftarrow R_2 - 0.001R_1$：$x_2$ 系数 $= 1.00 - 0.001 \times 1.00 = 0.999$，常数 $= 1.00 - 0.001 \times 2.00 = 0.998$。

$x_2 = 0.998/0.999 \approx 0.999$，$x_1 = 2 - x_2 \approx 1.001$。误差小得多！

**(c)** 不选主元时乘数 $m = 1000$ 放大了舍入误差。列主元确保 $|m| \leq 1$，抑制误差传播。

</details>

---

## Q12 PLU 分解

<details><summary>解</summary>

$A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$，第一个主元位置 $a_{11} = 0$，无法做标准 LU。

交换两行：**$P = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$**，$PA = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$

$I = LU$ 显然取 $L = I$, $U = I$。

所以 $PA = LU$：
$$P = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad L = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$

验证：$PA = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I = LU$ ✓

</details>
