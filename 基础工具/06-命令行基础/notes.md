# 基础工具 · 第六章 · 命令行基础 (Shell)

← 前置: [05 — VS Code 高效技巧](../05-VSCode高效技巧/notes.md)
→ 延伸: [Python基础 — 01 表达式与函数](../../Python基础/01-表达式与函数/notes.md)

---

## 1. 什么是命令行？

命令行（终端/Terminal）是一个**纯文本界面**，你输入命令，系统执行并输出结果。它看起来没有图形界面友好，但比图形界面**快得多**、**更精确**、**可自动化**。

在你的学习过程中，命令行用于：
- 运行 Python 脚本：`python3 grader.py`
- 编译 LaTeX：`xelatex homework.tex`
- Git 操作：`git add`, `git commit`, `git push`
- 文件管理、搜索、批量操作

**Shell** 是解读命令的程序。macOS 用 zsh，Ubuntu 用 bash，Windows PowerShell / WSL 用 bash。

---

## 2. 基础导航

```bash
pwd                     # 打印当前所在目录 (Print Working Directory)
ls                      # 列出当前目录下的文件
ls -la                  # 列出所有文件（含隐藏文件），详细信息
cd 目录名               # 进入目录 (Change Directory)
cd ..                   # 返回上一级目录
cd ~                    # 返回 home 目录
cd -                    # 返回刚才所在的目录
```

**路径表示法**：
- **绝对路径**：从根目录 `/` 开始，如 `/Users/w2045/Desktop/Study`
- **相对路径**：从当前目录开始，如 `Study/Python基础`
- `.` 当前目录，`..` 上一级目录，`~` home 目录

---

## 3. 文件操作

```bash
touch 文件名            # 创建空文件
mkdir 目录名            # 创建目录 (Make Directory)
mkdir -p a/b/c          # 递归创建多层目录
cp 源文件 目标           # 复制文件 (Copy)
cp -r 源目录 目标        # 复制目录
mv 源 目标              # 移动/重命名 (Move)
rm 文件名               # 删除文件 (Remove) ⚠️ 没有回收站！
rm -r 目录名            # 删除目录 ⚠️ 谨慎使用！
```

> **警告**：`rm` 是永久删除，不会进回收站。删除前确认路径正确。

---

## 4. 查看文件内容

```bash
cat 文件名              # 显示全部内容（短文件用）
less 文件名             # 分页浏览（q 退出，/ 搜索）
head -20 文件名         # 显示前 20 行
tail -20 文件名         # 显示后 20 行
```

---

## 5. 运行程序

```bash
python3 脚本.py                  # 运行 Python
python3 -c "print(2+3)"          # 运行一行 Python 代码
xelatex 文件.tex                  # 编译 LaTeX
code .                            # 在当前目录打开 VS Code
```

---

## 6. 管道与重定向

这是命令行的灵魂——将多个简单命令组合成复杂操作。

```bash
# 管道 |  把左边命令的输出传给右边命令
ls -la | grep ".md"              # 找出所有 .md 文件
cat notes.md | head -5           # 看笔记的前 5 行

# 重定向 >  把输出写入文件（覆盖）
ls > 文件列表.txt

# 重定向 >>  把输出追加到文件末尾
echo "新的一行" >> homework.log
```

---

## 7. 常用实用命令

```bash
grep "关键词" 文件名     # 在文件中搜索关键词
grep -r "def" .          # 递归搜索当前目录下所有文件
find . -name "*.py"      # 查找所有 .py 文件
wc -l 文件名             # 统计文件行数 (Word Count)
du -sh 目录              # 查看目录占用空间
history                  # 查看命令历史
```

---

## 8. Tab 补全 — 最好的功能

输入前几个字母 → 按 `Tab` → Shell 自动补全文件名/命令名。如果有多个匹配，快速按两下 `Tab` 显示所有选项。

```
cd Pyth<Tab>           → cd Python基础/
xela<Tab>              → xelatex
```

这是命令行能比 GUI 快的重要原因之一。

---

## 9. 终端中的快捷键

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + C` | 终止当前运行的命令 |
| `Ctrl + D` | 发送 EOF（退出 Python REPL） |
| `Ctrl + A` | 跳到行首 |
| `Ctrl + E` | 跳到行尾 |
| `Ctrl + U` | 删除光标前所有内容 |
| `Ctrl + R` | 搜索历史命令 |
| `↑ / ↓` | 上一条/下一条命令 |

> macOS Terminal 中 `Ctrl` 就是 Control 键，不是 Cmd。

---

## 10. 你的日常命令清单

学习中最常用的命令：

```bash
# 打开学习项目
cd ~/Desktop/Study
code .

# 运行 Python 作业批改
cd Python基础/01-表达式与函数/作业
python3 grader.py

# 编译 LaTeX
cd 数学基础/线性代数/01-向量与向量空间/理论题
xelatex homework.tex

# 保存到 Git
git add -A
git commit -m "描述"
git push

# 查看状态
git status
git log --oneline

# 环境检查
python3 --version
latex --version
```

---

## 本章核心概念速查

| 命令 | 作用 |
|------|------|
| `pwd` | 我在哪 |
| `ls` | 这里有什么 |
| `cd` | 去那里 |
| `mkdir` | 创建目录 |
| `touch` | 创建文件 |
| `cp / mv / rm` | 复制 / 移动 / 删除 |
| `cat / less` | 查看文件 |
| `grep` | 搜索内容 |
| `find` | 查找文件 |
| `\|` 管道 | 组合命令 |
| `Tab` 补全 | 省去手动输入 |
