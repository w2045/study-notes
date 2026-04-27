# 基础工具 · 第二章 · LaTeX 数学公式基础

← 前置: [01 — Markdown 语法](../01-Markdown语法/notes.md)
→ 延伸: [03 — LaTeX 文档排版入门](../03-LaTeX文档排版入门/notes.md)

---

## 1. 为什么学 LaTeX 公式？

Markdown 写文字很快，但遇到数学公式就力不从心了。LaTeX 是数学排版的工业标准——从你课本上看到的每个公式，到 arXiv 上每篇 ML 论文，都是用 LaTeX 排的。

在我们的学习项目中：
- Markdown 笔记里嵌入 `$...$` 和 `$$...$$` 写公式
- 数学理论作业（`.tex` 文件）用完整的 LaTeX 语法
- 数学课的标准语言——你能读出 LaTeX 代码就能读懂任何教材的公式

---

## 2. 基础结构：行内与块级

### 2.1 两种模式

| 模式 | 语法 | 用在 |
|------|------|------|
| 行内公式 | `$...$` | 文字中间的公式 |
| 块级公式 | `$$...$$` 或 `\[...\]` | 独占一行的公式 |

```markdown
勾股定理 $a^2 + b^2 = c^2$ 是几何学的基础。

欧拉恒等式：
$$e^{i\pi} + 1 = 0$$
```

效果：勾股定理 $a^2 + b^2 = c^2$，以及：

$$e^{i\pi} + 1 = 0$$

> **注意**：Markdown Preview Enhanced 支持 `$$...$$`。在纯 `.tex` 文件中用 `\[...\]` 更标准。

---

## 3. 上标、下标与分式

| 元素 | 语法 | 效果 |
|------|------|------|
| 上标 | `x^2` | $x^2$ |
| 下标 | `x_i` | $x_i$ |
| 上下标组合 | `x_i^2` | $x_i^2$ |
| 多字符上标 | `x^{10}` | $x^{10}$ |
| 多字符下标 | `x_{i,j}` | $x_{i,j}$ |
| 分式 | `\frac{a}{b}` | $\frac{a}{b}$ |
| 大分式 | `\dfrac{a}{b}` | $\dfrac{a}{b}$ |

**常见错误**：`x^10` 显示为 $x^1 0$（只有 `1` 是上标）。必须写 `x^{10}`。

---

## 4. 希腊字母

| 小写 | 语法 | 大写 | 语法 |
|------|------|------|------|
| $\alpha$ | `\alpha` | — | — |
| $\beta$ | `\beta` | — | — |
| $\gamma$ | `\gamma` | $\Gamma$ | `\Gamma` |
| $\delta$ | `\delta` | $\Delta$ | `\Delta` |
| $\epsilon$ | `\epsilon` | — | — |
| $\theta$ | `\theta` | $\Theta$ | `\Theta` |
| $\lambda$ | `\lambda` | $\Lambda$ | `\Lambda` |
| $\mu$ | `\mu` | — | — |
| $\pi$ | `\pi` | $\Pi$ | `\Pi` |
| $\sigma$ | `\sigma` | $\Sigma$ | `\Sigma` |
| $\phi$ | `\phi` | $\Phi$ | `\Phi` |
| $\omega$ | `\omega` | $\Omega$ | `\Omega` |

---

## 5. 求和、积分、极限

```latex
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
```
$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

```latex
\int_{0}^{\infty} e^{-x} \, dx = 1
```
$$\int_{0}^{\infty} e^{-x} \, dx = 1$$

```latex
\lim_{x \to \infty} \frac{1}{x} = 0
```
$$\lim_{x \to \infty} \frac{1}{x} = 0$$

```latex
\prod_{i=1}^{n} x_i
```
$$\prod_{i=1}^{n} x_i$$

> **小技巧**：`\,` 在积分号后加一个小空格，让 $dx$ 不紧贴着被积函数。

---

## 6. 根号、括号、绝对值

```latex
\sqrt{x} \quad \sqrt[3]{x} \quad \sqrt{a^2 + b^2}
```
$$\sqrt{x} \quad \sqrt[3]{x} \quad \sqrt{a^2 + b^2}$$

括号自动缩放：用 `\left` 和 `\right`：

```latex
\left( \frac{x}{y} \right)^2
\quad
\left[ \int_0^1 f(x) dx \right]
\quad
\left\{ \frac{a}{b} \right\}
```
$$\left( \frac{x}{y} \right)^2
\quad
\left[ \int_0^1 f(x) dx \right]
\quad
\left\{ \frac{a}{b} \right\}$$

绝对值与范数：

```latex
|x| \quad \|x\| \quad \left\| \frac{a}{b} \right\|
```
$$|x| \quad \|x\| \quad \left\| \frac{a}{b} \right\|$$

---

## 7. 矩阵

```latex
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
```
$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}$$

不同括号的矩阵环境：

| 环境 | 括号 |
|------|------|
| `bmatrix` | `[ ]` |
| `pmatrix` | `( )` |
| `vmatrix` | `| |` |
| `matrix` | 无括号 |

---

## 8. 常用符号速查

| 符号 | 语法 | 符号 | 语法 |
|------|------|------|------|
| $\times$ | `\times` | $\cdot$ | `\cdot` |
| $\pm$ | `\pm` | $\mp$ | `\mp` |
| $\leq$ | `\leq` | $\geq$ | `\geq` |
| $\neq$ | `\neq` | $\approx$ | `\approx` |
| $\equiv$ | `\equiv` | $\sim$ | `\sim` |
| $\infty$ | `\infty` | $\partial$ | `\partial` |
| $\nabla$ | `\nabla` | $\forall$ | `\forall` |
| $\exists$ | `\exists` | $\in$ | `\in` |
| $\subset$ | `\subset` | $\subseteq$ | `\subseteq` |
| $\to$ | `\to` | $\mapsto$ | `\mapsto` |
| $\implies$ | `\implies` | $\iff$ | `\iff` |
| $\cdot$ | `\cdot` | $\cdots$ | `\cdots` |
| $\ldots$ | `\ldots` | $\vdots$ | `\vdots` |

---

## 9. 对齐公式

用 `\begin{aligned}` 实现多行公式对齐，`&` 标记对齐点：

```latex
\begin{aligned}
f(x) &= x^2 + 2x + 1 \\
     &= (x + 1)^2 \\
     &\geq 0
\end{aligned}
```

$$\begin{aligned}
f(x) &= x^2 + 2x + 1 \\
     &= (x + 1)^2 \\
     &\geq 0
\end{aligned}$$

多行条件用 `\begin{cases}`：

```latex
f(x) = \begin{cases}
x,  & x \geq 0 \\
-x, & x < 0
\end{cases}
```

$$f(x) = \begin{cases} x, & x \geq 0 \\ -x, & x < 0 \end{cases}$$

---

## 10. 在 Markdown 中使用 LaTeX

在你的 `.md` 笔记中，VS Code + Markdown Preview Enhanced 已配置好：

```markdown
行内: 损失函数 $\mathcal{L}(\theta) = \frac{1}{N}\sum_i \ell(y_i, \hat{y}_i)$

块级:
$$\frac{\partial \mathcal{L}}{\partial \theta} = 0$$
```

即可渲染出公式。不需要任何额外配置。

---

## 11. 常见错误

| 错误 | 正确 | 说明 |
|------|------|------|
| `x^10` | `x^{10}` | 多字符上标要加 `{}` |
| `\frac12` | `\frac{1}{2}` | 分式参数用 `{}` |
| `( \frac{a}{b} )` | `\left( \frac{a}{b} \right)` | 括号不会自动缩放 |
| `$...$` 和 `$$...$$` 混用 | 行内用 `$`，块级用 `$$` | |
| 忘记 `\` | `alpha` → `\alpha` | 所有命令以 `\` 开头 |

---

## 本章核心概念速查

| 概念 | 语法 |
|------|------|
| 行内公式 | `$E = mc^2$` |
| 分式 | `\frac{分子}{分母}` |
| 上下标 | `x^{10}` `x_i` |
| 求和 | `\sum_{i=1}^{n}` |
| 积分 | `\int_{a}^{b}` |
| 矩阵 | `\begin{bmatrix}...\end{bmatrix}` |
| 希腊字母 | `\alpha \beta \gamma \pi \sigma \theta` |
| 对齐 | `\begin{aligned}...\end{aligned}` |
