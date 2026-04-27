# 基础工具 · 第三章 · LaTeX 文档排版 — 参考答案

---

## Q1

<details><summary>点击查看</summary>

```latex
\documentclass[12pt]{ctexart}
\usepackage{amsmath}
\usepackage{geometry}
\geometry{a4paper, margin=2.5cm}

\title{我的 \LaTeX{} 练习}
\author{}
\date{}

\begin{document}
\maketitle

\section{数学}

一元二次方程的求根公式：
\[
x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

\end{document}
```
</details>

---

## Q2

<details><summary>点击查看</summary>

```latex
\section{今日待办}

\subsection*{无序列表}
\begin{itemize}
    \item 学习 LaTeX 语法
    \item 完成数学题
    \item 整理笔记
\end{itemize}

\subsection*{有序列表}
\begin{enumerate}
    \item 打开 VS Code
    \item 写 .tex 文件
    \item 保存编译看 PDF
\end{enumerate}
```
</details>

---

## Q3

<details><summary>点击查看</summary>

```latex
\section{交叉引用练习}

\begin{equation}
    \sum_{i=1}^{n} i = \frac{n(n+1)}{2}
    \label{eq:gauss}
\end{equation}

如公式 \eqref{eq:gauss} 所示，这是高斯求和公式。
```

编译两次以更新引用编号（LaTeX 需要两次编译来解析交叉引用）。
</details>

---

## Q4

<details><summary>点击查看</summary>

```latex
\usepackage{amsthm}
\newtheorem{theorem}{定理}

\begin{theorem}[柯西-施瓦茨不等式]
对任意 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$，
\[
|\mathbf{u} \cdot \mathbf{v}| \leq \|\mathbf{u}\| \|\mathbf{v}\|
\]
当且仅当 $\mathbf{u}$ 和 $\mathbf{v}$ 共线时取等号。
\end{theorem}
```
</details>

---

## Q5

<details><summary>点击查看</summary>

```latex
\begin{align}
    (a + b)^2 &= (a + b)(a + b) \\
              &= a^2 + ab + ba + b^2 \\
              &= a^2 + 2ab + b^2
\end{align}
```
</details>

---

## Q6

<details><summary>点击查看</summary>

三处错误：
1. `\frac1x` → `\frac{1}{x}`（分式需要花括号）
2. `\begin{equation)` → `\begin{equation}`（圆括号应该是花括号）
3. 缺少中文支持（如果含中文）→ 改用 `ctexart` 或加 `\usepackage[UTF8]{ctex}`

修正后：
```latex
\documentclass{article}
\usepackage{amsmath}
\begin{document}
\section{公式}
\[ f(x) = \frac{1}{x} \]

\begin{equation}
E = mc^2
\end{equation}
\end{document}
```
</details>
