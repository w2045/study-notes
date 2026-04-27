# 基础工具 · 第六章 · 命令行基础 — 参考答案

---

## Q1

<details><summary>点击查看</summary>

```bash
pwd                     # → /Users/w2045（或你的 home 目录）
cd ~/Desktop/Study
ls                      # → 列出 Python基础/ 数学基础/ 基础工具/ 等
cd ~
```
</details>

---

## Q2

<details><summary>点击查看</summary>

```bash
cd ~/Desktop/Study
mkdir test_dir
cd test_dir
touch test.txt
cd ..
rm -r test_dir          # 删除目录及内容
```

> `rm -r` 是永久删除，确认路径正确再回车。
</details>

---

## Q3

<details><summary>点击查看</summary>

```bash
cd ~/Desktop/Study
head -3 PROGRESS.md
```

输出前 3 行（标题和元数据）。
</details>

---

## Q4

<details><summary>点击查看</summary>

```bash
ls ~/Desktop/Study | grep "基础"
```

输出：
```
Python基础
基础工具
数学基础
```
</details>

---

## Q5

<details><summary>点击查看</summary>

```bash
cd ~/Desktop/Study
grep -r "def normalize" .
```

输出类似：
```
./数学基础/线性代数/01-向量与向量空间/编程题/homework.py:def normalize(v):
```
</details>

---

## Q6

<details><summary>点击查看</summary>

```bash
cd ~/Desktop/Study
find . -name "*.py"
```

输出所有 `.py` 文件的路径列表。
</details>

---

## Q7

<details><summary>点击查看</summary>

实操题，无需答案。记住：
- `Ctrl + A` 到行首，`Ctrl + E` 到行尾
- `Ctrl + U` 清空当前行
- `Ctrl + R` 搜索历史命令
</details>
