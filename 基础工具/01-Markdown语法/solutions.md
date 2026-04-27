# 基础工具 · 第一章 · Markdown — 参考答案

---

## Q1

<details><summary>点击查看</summary>

```markdown
# 我的笔记

## 今天学到的

Markdown 是一种轻量级标记语言，用简单的符号就能控制排版。

- 标题用 `#`
- 代码用反引号
- 公式用 `$$`
```
</details>

---

## Q2

<details><summary>点击查看</summary>

````markdown
```python
print("Hello, Markdown!")
```

勾股定理：$a^2 + b^2 = c^2$

高斯求和公式：
$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$
````
</details>

---

## Q3

<details><summary>点击查看</summary>

```markdown
| 日期 | 科目 | 内容 | 完成 |
|------|------|------|------|
| 周一 | Python 基础 | 表达式与变量 | ✅ |
| 周三 | 线性代数 | 向量基础 | ✅ |
| 周五 | 基础工具 | Markdown 语法 | ⬜ |
```
</details>

---

## Q4

<details><summary>点击查看</summary>

四处错误：
1. `#标题` → `# 标题`（`#` 后面需要空格）
2. `-第一项` → `- 第一项`（`-` 后面需要空格）
3. 子项缩进：需要至少 2 格（通常 2 或 4 格缩进）
4. `'''` → ` ``` `（三个反引号，不是单引号）+ 加语言标注 `python`

修正后：
````markdown
# 标题

列表项:

- 第一项
- 第二项
  - 子项

代码:

```python
print("no highlight")
```
````
</details>

---

## Q5

<details><summary>点击查看</summary>

```markdown
<details>
<summary>参考答案</summary>

1. 第一步
2. 第二步
3. 第三步

</details>
```
</details>

---

## Q6

<details><summary>点击查看</summary>

```markdown
← 前置: [Python基础 — 表达式与函数](../../Python基础/01-表达式与函数/notes.md)
→ 延伸: [基础工具 — LaTeX 公式](../02-LaTeX数学公式/notes.md)
```
</details>
