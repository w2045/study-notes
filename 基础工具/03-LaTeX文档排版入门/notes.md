# 基础工具 · 第三章 · LaTeX 文档排版入门

← 前置: [02 — LaTeX 数学公式基础](../02-LaTeX数学公式基础/notes.md)
→ 延伸: [04 — Git 版本控制基础](../04-Git版本控制基础/notes.md)

---

## 1. 从公式到完整文档

上一章学了在 Markdown 中嵌入 `$...$` 公式。但当你需要写一份完整的理论作业——带标题、章节、定理环境、交叉引用——就需要一个**完整的 `.tex` 文档**。

这就是本章的内容：从 `.tex` 源文件到 PDF。

---

## 2. 最小可编译文档

```latex
\documentclass[12pt]{ctexart}      % 文档类型：中文文章
\usepackage{amsmath, amssymb}       % 数学宏包
\usepackage{geometry}               % 页面设置
\geometry{a4paper, margin=2.5cm}

\title{我的第一份 \LaTeX{} 文档}
\author{张三}
\date{2026 年 4 月}

\begin{document}
\maketitle                          % 生成标题

\section{引言}
这是第一段。\LaTeX{} 会自动处理缩进、间距和换行。

\section{数学}
勾股定理：$a^2 + b^2 = c^2$。

\begin{equation}
    E = mc^2
    \label{eq:einstein}
\end{equation}

\end{document}
```

**编译**：`xelateh 文件名.tex` → 生成 PDF。

**VS Code 中**：保存（`Cmd+S`）→ LaTeX Workshop 自动编译 → `Cmd+Alt+V` 看 PDF。

---

## 3. 文档结构

### 3.1 documentclass

```latex
\documentclass[12pt]{ctexart}   % 中文文章
\documentclass{article}         % 英文文章
\documentclass{report}          % 报告（有 chapter）
\documentclass{book}            % 书
```

常用选项：`12pt`（字号）、`a4paper`（纸张）、`twocolumn`（双栏）。

### 3.2 章节命令

```latex
\section{节标题}
\subsection{子节标题}
\subsubsection{子子节标题}
```

LaTeX 自动编号。不想编号的话用 `\section*{...}`。

### 3.3 标题页

```latex
\title{...}
\author{...}
\date{...}        % \date{} 留空则不显示日期
\maketitle        % 在 \begin{document} 后调用
```

---

## 4. 排版基础

### 4.1 段落与换行

```latex
空行表示新段落开始，LaTeX 自动缩进首行。

\\ 或 \newline 强制换行但不新起段落。

\newpage 开始新页。
```

### 4.2 字体样式

| 命令 | 效果 |
|------|------|
| `\textbf{粗体}` | **粗体** |
| `\textit{斜体}` | *斜体* |
| `\texttt{等宽}` | 代码字体 |
| `\textsc{小大写}` | Small Caps |

### 4.3 列表

```latex
\begin{itemize}
    \item 无序列表项 1
    \item 无序列表项 2
\end{itemize}

\begin{enumerate}
    \item 有序列表项 1
    \item 有序列表项 2
\end{enumerate}
```

---

## 5. 数学环境

### 5.1 行内与块级

```latex
行内公式：$f(x) = x^2$
块级公式：
\[
    f(x) = x^2
\]
```

### 5.2 带编号公式

```latex
\begin{equation}
    \frac{\partial \mathcal{L}}{\partial w} = 0
    \label{eq:grad}
\end{equation}

如公式 \eqref{eq:grad} 所示...
```

`\label` 和 `\eqref` 实现交叉引用，编号自动管理。

### 5.3 多行对齐

```latex
\begin{align}
    f(x) &= x^2 + 2x + 1 \\
         &= (x+1)^2
\end{align}
```

---

## 6. 定理环境

用 `amsthm` 宏包定义定理样式：

```latex
\usepackage{amsthm}
\newtheorem{theorem}{定理}[section]     % 按节编号
\newtheorem{definition}{定义}
\newtheorem{example}{例}

\begin{theorem}[勾股定理]
在直角三角形中，$a^2 + b^2 = c^2$。
\end{theorem}

\begin{definition}[向量]
向量是 $\mathbb{R}^n$ 中的一个有序 $n$ 元组。
\end{definition}
```

我们的作业模板中用的 `\begin{problem}...\end{problem}` 就是这样定义的。

---

## 7. 插入代码

用 `listings` 或 `minted` 宏包：

```latex
\usepackage{listings}
\begin{lstlisting}[language=Python]
def hello():
    print("Hello, LaTeX!")
\end{lstlisting}
```

---

## 8. 注释

```latex
% 这是注释，不会出现在 PDF 中
```

我们的作业模板用 `%%% 在此作答 %%%` 作为标记——它在 PDF 中不可见，只在源码中引导你。

---

## 9. 中文支持

用了 `ctexart` 文档类就不需要额外配置。如果用 `article`，需要加：

```latex
\usepackage[UTF8]{ctex}
```

编译必须用 `xelatex`（支持 UTF-8 和系统字体）。

---

## 10. 常见错误

| 错误 | 原因 | 解决 |
|------|------|------|
| `Undefined control sequence` | 命令名写错了 | 检查拼写，注意大小写 |
| `Missing $ inserted` | 在普通文字中用了数学命令 | 加 `$...$` 包裹 |
| `Runaway argument` | 缺 `}` 关闭括号 | 检查 `{` 和 `}` 配对 |
| 中文不显示 | 用了 `pdflatex` 编译 | 改用 `xelatex` |

---

## 本章核心概念速查

| 概念 | 命令 |
|------|------|
| 文档类型 | `\documentclass{ctexart}` |
| 标题 | `\title{} \maketitle` |
| 章节 | `\section{} \subsection{}` |
| 块级公式 | `\[...\]` 或 `equation` 环境 |
| 交叉引用 | `\label{}` + `\eqref{}` |
| 列表 | `itemize` / `enumerate` |
| 定理 | `\newtheorem{}{}` |
| 编译 | `xelatex file.tex` |
