# 基础工具 · 第四章 · Git 版本控制 — 参考答案

---

## Q1

<details><summary>点击查看</summary>

- `git add` → B. 添加文件到暂存区
- `git commit` → D. 创建一次版本快照
- `git push` → C. 推送到远程仓库
- `git status` → A. 查看文件变化
</details>

---

## Q2

<details><summary>点击查看</summary>

```bash
git add 文件名
git commit -m "描述做了什么"
git push
```

例如：
```bash
git add Python基础/01-表达式与函数/notes.md
git commit -m "add: Python基础 01 笔记完成"
git push
```
</details>

---

## Q3

<details><summary>点击查看</summary>

应加入 `.gitignore` 的文件：
- `homework.aux` ✅（LaTeX 编译临时文件）
- `__pycache__/grader.pyc` ✅（Python 字节码缓存）
- `.DS_Store` ✅（macOS 系统文件）

不应加入：
- `notes.md` ❌（项目源文件）
- `README.md` ❌（项目说明文件）
</details>

---

## Q4

<details><summary>点击查看</summary>

1. ✅ 合格。描述了具体改了什么、为什么。
2. ❌ 不合格。改写：`"update: 更新 README 学习进度到 4 月"`
3. ❌ 不合格。太长了，且不具体。应拆成多个提交。例如 `"fix: grader 输出格式对齐"` + `"add: CS61A 03 递归笔记"`
4. ✅ 合格。清晰说明了新增内容。
</details>

---

## Q5

<details><summary>点击查看</summary>

在 `.gitignore` 中添加一行：
```gitignore
*.pdf
```

这会忽略所有 PDF 文件。如果你只想忽略编译产生的 PDF，保留其他 PDF（如课件），可以更精确：

```gitignore
# 忽略编译产生的 PDF（在 XX-章节名/ 下）
**/homework.pdf
**/*.pdf
```

> 注意：当前项目的 `.gitignore` 不忽略 PDF，因为作业 PDF 可以作为参考归档。
</details>

---

## Q6

<details><summary>点击查看</summary>

```bash
git clone https://github.com/w2045/study-notes.git
cd study-notes
code .
```
</details>
