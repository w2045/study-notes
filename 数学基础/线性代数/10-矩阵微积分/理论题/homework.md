# 线性代数 · 第十章 · 理论题

> 用 Markdown + LaTeX 数学公式作答。每题在 `### 解答` 下方书写推导过程。

---

## Q1 ⭐ 标量对向量求导

求 $\nabla_\mathbf{x} f$，其中 $f(\mathbf{x}) = \mathbf{a}^T \mathbf{x}$，$\mathbf{a} = [2, -1, 3]^T$。

### 解答

（在此作答）

---

## Q2 ⭐ 范数平方的梯度

求 $\nabla_\mathbf{x} \|\mathbf{x}\|^2$，并给出 $\mathbf{x} = [3, 4]^T$ 处的值。

### 解答

（在此作答）

---

## Q3 ⭐ 线性回归梯度

对 $f(\mathbf{w}) = \|X\mathbf{w} - \mathbf{y}\|^2$，求 $\nabla_\mathbf{w} f$。结果用 $X$ 和 $\mathbf{y}$ 表示。

### 解答

（在此作答）

---

## Q4 ⭐ Jacobian 基础

求 $\mathbf{f}(\mathbf{x}) = A\mathbf{x}$ 的 Jacobian 矩阵，其中 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$。

### 解答

（在此作答）

---

## Q5 ⭐⭐ 二次型的梯度

设 $A = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$（对称）。求 $\nabla_\mathbf{x} (\mathbf{x}^T A \mathbf{x})$，并计算 $\mathbf{x} = [1, 1]^T$ 处的梯度值。

### 解答

（在此作答）

---

## Q6 ⭐⭐ Hessian 计算

求 $f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$（$A$ 对称）的 Hessian 矩阵。

### 解答

（在此作答）

---

## Q7 ⭐⭐ 标量对矩阵的导数

求 $\nabla_X f$，其中 $f(X) = \operatorname{tr}(A X)$，$A, X \in \mathbb{R}^{n \times n}$。

### 解答

（在此作答）

---

## Q8 ⭐⭐ 链式法则应用

设 $f(\mathbf{x}) = \|\mathbf{x}\|$，$g(\mathbf{w}) = \mathbf{x}_0 + B\mathbf{w}$。求 $\nabla_\mathbf{w} f(g(\mathbf{w}))$（复合函数的梯度）。

### 解答

（在此作答）

---

## Q9 ⭐⭐⭐ $\log\det$ 的梯度

求 $\nabla_X \log \det X$（$X$ 可逆）。提示：用 $d(\log \det X) = \operatorname{tr}(X^{-1} dX)$。

### 解答

（在此作答）

---

## Q10 ⭐⭐⭐ 矩阵二次型的梯度

设 $f(X) = \operatorname{tr}(X^T A X)$，其中 $A$ 是常矩阵，$X \in \mathbb{R}^{m \times n}$。求 $\nabla_X f$（用 $A$ 和 $X$ 表示）。

### 解答

（在此作答）

---

## Q11 ⭐⭐⭐ Logistic 回归梯度推导

设 $L(\mathbf{w}) = \sum_{i=1}^{n} \log(1 + e^{\mathbf{x}_i^T \mathbf{w}}) - y_i \mathbf{x}_i^T \mathbf{w}$。将 $\nabla_\mathbf{w} L$ 表示为矩阵形式 $X^T(\sigma - \mathbf{y})$，其中 $\sigma_i = 1/(1+e^{-\mathbf{x}_i^T \mathbf{w}})$ 是 sigmoid。

### 解答

（在此作答）

---

## Q12 ⭐⭐⭐ Frobenius 范数的梯度

对 $f(X) = \frac{1}{2}\|AX - B\|_F^2$，求 $\nabla_X f$，并导出使 $f$ 最小化的一阶条件（正规方程）。

### 解答

（在此作答）
