# 基础工具 · 第二章 · LaTeX 数学公式 — 作业

> 在 Markdown 文件中写出对应的 LaTeX 代码，用 `Cmd+K V` 预览效果。

---

## Q1 ⭐ 基础公式

写出以下公式的 LaTeX 代码：

- $a^2 + b^2 = c^2$
- $x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

---

## Q2 ⭐ 求和与积分

写出高斯积分公式：

$$\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}$$

---

## Q3 ⭐ 矩阵

写出 $2 \times 2$ 旋转矩阵：

$$R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$

---

## Q4 ⭐⭐ 分段函数

写出 ReLU 激活函数的分段定义：

$$\text{ReLU}(x) = \max(0, x) = \begin{cases} 0, & x \leq 0 \\ x, & x > 0 \end{cases}$$

---

## Q5 ⭐⭐ 多行对齐推导

写出交叉熵损失的偏导推导（至少 2 行，用 `aligned`）：

$$\frac{\partial \mathcal{L}}{\partial \hat{y}} = \cdots$$

---

## Q6 ⭐⭐ 修复语法错误

下面的 LaTeX 代码有 3 处错误，找出并修复：

```latex
$$ x^10 + y^10 = z^10 $$
$$ \frac12 + \frac13 = \frac56 $$
$$ \sum_i=1^n x_i $$
```

---

## Q7 ⭐⭐ 写出正态分布 PDF

写出正态分布的概率密度函数：

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right)$$
