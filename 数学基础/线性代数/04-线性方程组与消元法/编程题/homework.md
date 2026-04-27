# 线性代数 · 第四章 · 线性方程组与消元法 — 编程作业

> 完成 `homework.py` 中的函数。运行 `python3 grader.py` 自动批改。
> 难度: ⭐ 基础 | ⭐⭐ 中等 | ⭐⭐⭐ 挑战

---

## Q1 ⭐ 增广矩阵构造

实现 `make_augmented(A, b)`，将系数矩阵 $A$ 和右端项 $\mathbf{b}$ 合并为增广矩阵 $[A \mid \mathbf{b}]$。

```python
make_augmented([[1, 2], [3, 4]], [5, 6])  → [[1, 2, 5], [3, 4, 6]]
```

---

## Q2 ⭐ 初等行操作：交换

实现 `row_swap(M, i, j)`，返回交换第 $i$ 行和第 $j$ 行后的新矩阵（不改原矩阵）。

```python
row_swap([[1, 2], [3, 4]], 0, 1)  → [[3, 4], [1, 2]]
```

---

## Q3 ⭐ 初等行操作：缩放

实现 `row_scale(M, i, c)`，返回第 $i$ 行乘以 $c$ 后的新矩阵。

```python
row_scale([[1, 2], [3, 4]], 0, 2.0)  → [[2.0, 4.0], [3, 4]]
```

---

## Q4 ⭐ 初等行操作：加减

实现 `row_add(M, target, source, c)`。$R_{\text{target}} \leftarrow R_{\text{target}} + c \cdot R_{\text{source}}$。

```python
row_add([[1, 2], [3, 4]], 1, 0, -3.0)  → [[1, 2], [0.0, -2.0]]
```

---

## Q5 ⭐⭐ 前向消元（无选主元）

实现 `forward_elimination(A, b)`。对增广矩阵执行高斯消元（不选主元），返回 `(A_upper, b_upper)`。

```python
A, b = forward_elimination([[1, 2], [3, 4]], [5, 11])
# A → [[1.0, 2.0], [0.0, -2.0]]
# b → [5.0, -4.0]
```

---

## Q6 ⭐⭐ 回代

实现 `back_substitution(A, b)`。对已经化为上三角的方程组回代求解。无解或无穷多解返回 `None`。

```python
back_substitution([[1, 2], [0, -2]], [5, -4])  → [1.0, 2.0]
back_substitution([[1, 2], [0, 0]], [3, 1])    → None
```

---

## Q7 ⭐⭐ 列主元前向消元

实现 `forward_elimination_pivot(A, b)`。与 Q5 相同，但每步消元前先做列主元选择（换到绝对值最大的行）。

```python
A, b = forward_elimination_pivot([[0.0001, 1], [1, 1]], [1, 2])
# 原来第二行（主元 1.0）会被换到第一行
```

**为什么重要**：小主元会放大浮点舍入误差，列主元确保乘数 $|m| \leq 1$，抑制误差传播。

---

## Q8 ⭐⭐ LU 分解

实现 `lu_decomposition(A)`。Doolittle 算法（$L$ 对角线全 1），假设不需要行交换，返回 `(L, U)`。

```python
L, U = lu_decomposition([[2, 1], [6, 8]])
# L → [[1, 0], [3, 1]]
# U → [[2, 1], [0, 5]]
```

---

## Q9 ⭐⭐ 前代（解 Ly = b）

实现 `forward_substitution(L, b)`。$L$ 是单位下三角矩阵（对角线全 1）。

```python
forward_substitution([[1, 0], [3, 1]], [3, 10])  → [3.0, 1.0]
```

---

## Q10 ⭐⭐⭐ 高斯消元完整求解

实现 `gaussian_solve(A, b, use_pivoting=True)`。整合前向消元 + 回代，返回解 $\mathbf{x}$ 或 `None`。

```python
gaussian_solve([[1, 2, 1], [2, 6, 1], [1, 1, 4]], [2, 7, 3])  → [-3.0, 2.0, 1.0]
```

---

## Q11 ⭐⭐⭐ 判断解的情况

实现 `classify_solution(A, b)`。对已化为行阶梯形的增广矩阵，返回 `'unique'`、`'infinite'` 或 `'none'`。

判断依据：比较 $\operatorname{rank}(A)$、$\operatorname{rank}([A \mid \mathbf{b}])$ 与 $n$。

```python
classify_solution([[1, 0], [0, 1]], [3, 4])    → 'unique'
classify_solution([[1, 2], [0, 0]], [3, 0])    → 'infinite'
classify_solution([[1, 2], [0, 0]], [3, 1])    → 'none'
```

---

## Q12 ⭐⭐⭐ 用 LU 分解求解

实现 `lu_solve(L, U, b)`。给定 $A = LU$，解 $A\mathbf{x} = \mathbf{b}$（先 $L\mathbf{y} = \mathbf{b}$，再 $U\mathbf{x} = \mathbf{y}$）。

```python
L = [[1, 0], [3, 1]]
U = [[2, 1], [0, 5]]
lu_solve(L, U, [3, 10])  → [1.0, 1.0]
```
