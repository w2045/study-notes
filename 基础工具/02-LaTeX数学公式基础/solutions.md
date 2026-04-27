# 基础工具 · 第二章 · LaTeX 数学公式 — 参考答案

---

## Q1

<details><summary>点击查看</summary>

```latex
$$a^2 + b^2 = c^2$$

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
```
</details>

---

## Q2

<details><summary>点击查看</summary>

```latex
$$\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}$$
```

要点：`\infty` 无穷大符号，`\,` 在 dx 前加小空格。
</details>

---

## Q3

<details><summary>点击查看</summary>

```latex
$$R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
```
</details>

---

## Q4

<details><summary>点击查看</summary>

```latex
$$\text{ReLU}(x) = \max(0, x) = \begin{cases} 0, & x \leq 0 \\ x, & x > 0 \end{cases}$$
```

要点：`\text{}` 在数学环境中插入普通文字。
</details>

---

## Q5

<details><summary>点击查看</summary>

以二元交叉熵 $\mathcal{L} = -y\log\hat{y} - (1-y)\log(1-\hat{y})$ 为例：

```latex
$$\begin{aligned}
\frac{\partial \mathcal{L}}{\partial \hat{y}}
&= -\frac{y}{\hat{y}} + \frac{1-y}{1-\hat{y}} \\
&= \frac{\hat{y} - y}{\hat{y}(1-\hat{y})}
\end{aligned}$$
```
</details>

---

## Q6

<details><summary>点击查看</summary>

三处错误：
1. `x^10` → `x^{10}`（多字符上标要 `{}`）
2. `\frac12` → `\frac{1}{2}`（分式参数用 `{}`）
3. `\sum_i=1^n` → `\sum_{i=1}^{n}`（上下限用 `_{}^{}`）

修正后：

```latex
$$ x^{10} + y^{10} = z^{10} $$
$$ \frac{1}{2} + \frac{1}{3} = \frac{5}{6} $$
$$ \sum_{i=1}^{n} x_i $$
```
</details>

---

## Q7

<details><summary>点击查看</summary>

```latex
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right)$$
```

要点：`\exp` 指数函数，`\left(` `\right)` 自动缩放括号，`\sigma` 和 `\mu` 希腊字母。
</details>
