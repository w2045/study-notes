# 基础工具 · 第四章 · Git 版本控制基础

← 前置: [03 — LaTeX 文档排版入门](../03-LaTeX文档排版入门/notes.md)
→ 延伸: [05 — VS Code 高效技巧](../05-VSCode高效技巧/notes.md)

---

## 1. 为什么需要 Git？

想象你在写一份重要笔记。第一天写了初版，第二天大改，第三天发现第一版的思路更好——但文件已经被覆盖了。于是你开始手动复制：

```
笔记_v1.md
笔记_v2_修改版.md
笔记_v3_最终版.md
笔记_v3_最终版_真的最终.md
```

Git 解决的就是这个问题。它像一个**时间机器**——记录每次修改的快照，你可以随时回到任意历史版本、对比差异、合并改动。

在我们的 Study 项目中，Git 还承担了**多设备同步** + **远程备份**的角色。

---

## 2. 核心概念

| 概念 | 一句话解释 |
|------|-----------|
| **仓库 (repo)** | 一个被 Git 跟踪的目录 |
| **工作区** | 你正在编辑的文件（还没存进 Git） |
| **暂存区 (stage)** | 准备存进 Git 的文件列表 |
| **提交 (commit)** | 一次版本快照，有唯一 ID |
| **远程 (remote)** | 托管在 GitHub 等服务器上的副本 |
| **分支 (branch)** | 一条独立的开发线 |

```
工作区        暂存区          本地仓库        远程仓库
(编辑文件) → git add → (暂存) → git commit → (提交) → git push → GitHub
```

---

## 3. 基本操作

### 3.1 初始化仓库

```bash
git init                    # 把当前目录变成 Git 仓库
```

这会创建隐藏的 `.git/` 文件夹，里面存着所有版本历史。

### 3.2 查看状态

```bash
git status                  # 看哪些文件改了、哪些已暂存
```

这是你最常用的 Git 命令。每次操作前后跑一下，清楚看到当前状态。

### 3.3 添加文件到暂存区

```bash
git add 文件名              # 添加指定文件
git add 文件名1 文件名2      # 添加多个
git add -A                  # 添加所有变更（谨慎使用）
```

### 3.4 提交

```bash
git commit -m "描述做了什么"
```

提交 = 拍一张快照。`-m` 后面写描述，要简短但有意义。

**良好的提交信息**：
```
✅ "add: 线性代数第一章向量空间笔记"
✅ "fix: 修正 grader.py 浮点数比较精度"
❌ "更新"
❌ "bug"（什么 bug？）
```

### 3.5 查看历史

```bash
git log                     # 查看提交历史（按 q 退出）
git log --oneline           # 简洁版：一行一个提交
git diff                    # 查看未暂存的修改
git diff 文件名              # 只看某文件的修改
```

---

## 4. 远程仓库（GitHub）

### 4.1 关联远程

```bash
git remote add origin https://github.com/用户名/仓库名.git
git push -u origin main     # 首次推送 + 设置默认上游
```

### 4.2 日常推送

```bash
git push                    # 把本地提交推送到 GitHub
```

### 4.3 从远程拉取

```bash
git pull                    # 拉取远程更新 + 合并到本地
```

### 4.4 克隆（新设备）

```bash
git clone https://github.com/用户名/仓库名.git
cd 仓库名
```

这就是你在新设备上恢复 Study 项目的方式。

---

## 5. 常用工作流

### 5.1 日常学习流程

```bash
# 写完笔记后
git add Python基础/01-表达式与函数/notes.md
git commit -m "add: Python基础 01 笔记完成"
git push

# 做完作业后
git add Python基础/01-表达式与函数/作业/homework.py
git commit -m "complete: Python基础 01 作业"
git push
```

### 5.2 新章节流程

```bash
# 写完了新的一章
git add -A
git status                  # 检查一遍
git commit -m "add: 线性代数 02 矩阵与线性变换"
git push
```

---

## 6. 让我们这个项目自动执行

Claude Code 在每次会话结束时会自动帮你：
1. Commit 所有新内容
2. Push 到 GitHub

你只需要在新设备上 `git clone` 或日常 `git pull` 即可同步。

---

## 7. .gitignore

有些文件不需要版本控制（编译产物、临时文件）：

```gitignore
# LaTeX 辅助文件
*.aux
*.log
*.out
*.pdf           # 如果只想存源码不存编译结果

# macOS
.DS_Store

# Python
__pycache__/
```

Study 项目已有 `.gitignore`，自动忽略 LaTeX 临时文件和 `__pycache__`。

---

## 8. 常见错误与恢复

| 情况 | 命令 |
|------|------|
| 提交信息写错了 | `git commit --amend -m "新信息"` |
| 加了不该加的文件 | `git reset HEAD 文件名` |
| 想回到某次提交看看 | `git checkout 提交ID` |
| 放弃了，回到最新 | `git checkout main` |
| 想看某个文件的旧版本 | `git show 提交ID:文件路径` |

> **黄金法则**：不确定时先 `git status` 和 `git log` 看看当前状态，再决定下一步。

---

## 9. GitHub 私密仓库

我们的 Study 仓库是 **private**——只有你能看到。GitHub 免费提供无限私有仓库。

别人访问 `https://github.com/w2045/study-notes` 会看到 404，保证学习笔记的私密性。

---

## 本章核心概念速查

| 命令 | 作用 |
|------|------|
| `git status` | 查看当前状态 |
| `git add` | 暂存文件 |
| `git commit -m ""` | 创建提交 |
| `git push` | 推送到远程 |
| `git pull` | 拉取远程更新 |
| `git clone url` | 克隆仓库 |
| `git log` | 查看历史 |
| `git diff` | 查看差异 |
