# 基础工具 · 第三章 · LaTeX 文档排版 — 作业

---

## Q1 ⭐ 第一份文档

创建一个完整的 `.tex` 文件，包含：
- `ctexart` 文档类，12pt
- 标题「我的 LaTeX 练习」
- 一个 `\section{数学}` 节
- 一节内放公式 $x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$

编译验证 PDF 生成成功。

---

## Q2 ⭐ 无序与有序列表

用 LaTeX 写出你的今日待办：无序列表 3 项，有序列表 3 项。

---

## Q3 ⭐⭐ 交叉引用

写一个带编号的公式环境，给它一个 `\label`，然后在正文中用 `\eqref` 引用它。

---

## Q4 ⭐⭐ 定理环境

用 `amsthm` 定义并使用一个定理环境。写出「柯西-施瓦茨不等式」并给它一个定理编号。

---

## Q5 ⭐⭐ 对齐推导

用 `align` 环境写出「二项式平方的展开」：

$$(a+b)^2 = a^2 + 2ab + b^2$$

每一步对齐等号。

---

## Q6 ⭐ 找错误

下面这段 LaTeX 有 3 处错误，找出并修复：

```latex
\documentclass{article}
\begin{document}
\section{公式}
f(x) = \frac1x

\begin{equation)
E = mc^2
\end{equation}
\end{document}
```
