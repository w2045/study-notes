# Study — 自学参考书

一份从数学基础到深度学习的系统自学笔记，目标是产出**可随时查阅、复习的详细参考书**，而非笔记流水账。

## 项目结构

```
Study/
├── README.md                  # 本文件
├── CLAUDE.md                  # 项目约定（AI 助手自动加载）
├── PROGRESS.md                # 进度追踪
├── Python基础/                # 12 章，参考 UC Berkeley CS61A
├── 数据结构与算法/              # 13 章，参考 Stanford CS106B
├── 计算机视觉与深度学习/        # 3 工具前置 + 10 章，参考 Stanford CS231N
├── 强化学习/                   # 10 章，参考西湖大学《强化学习的数学原理》
├── 大语言模型/                 # 10 章
├── 数学基础/                   # 5 门 36 章
│   ├── 线性代数/               # 10 章
│   ├── 微积分/                 # 6 章
│   ├── 概率论/                 # 7 章
│   ├── 凸优化/                 # 8 章
│   └── 信息论/                 # 5 章
├── 基础工具/                   # Markdown、LaTeX、Git、VS Code 等
└── resources/                 # 论文列表、外部链接
```

## 每章结构

视章节需要，理论题与编程题可同时存在或仅含其一（纯理论章省略编程题）。

### 含编程的章节（数学类 + 编程类）

```
XX-章节名/
├── notes.md
├── 理论题/                    # 数学类有，编程类无
│   ├── homework.tex
│   └── solutions.tex          # .gitignore 忽略
└── 编程题/ 或 作业/
    ├── homework.md            # 题目描述
    ├── homework.py            # 代码骨架（pass 占位）
    ├── grader.py              # 自动批改
    └── solutions.md           # 参考答案（.gitignore 忽略）
```

### 纯理论章节（如行列式、Jordan、矩阵微积分）

```
XX-章节名/
├── notes.md
└── 理论题/
    ├── homework.tex
    └── solutions.tex          # .gitignore 忽略
```

## 使用方式

### 在多设备间同步

```bash
git clone https://github.com/w2045/study-notes.git
cd study-notes
code .          # 在 VS Code 中打开
```

### 预览笔记

| 文件类型 | 快捷键 (macOS) | 快捷键 (Ubuntu/Windows) |
|----------|---------------|--------------------------|
| `.md` 预览（侧边） | `Cmd + K V` | `Ctrl + K V` |
| `.md` 预览（独立标签页） | `Cmd + Shift + V` | `Ctrl + Shift + V` |
| `.tex` 编译+预览 | `Cmd + S` 保存即编译，`Cmd + Alt + V` 看 PDF | `Ctrl + S` / `Ctrl + Alt + V` |

### 做编程作业

```bash
cd Python基础/01-表达式与函数/作业
# 编辑 homework.py，填写函数体
python3 grader.py    # 自动批改
```

### 做理论作业

打开 `理论题/homework.tex`，在 `%%% 在此作答 %%%` 注释区填写答案。保存后 VS Code 自动编译为 PDF 预览。

## 当前进度

| 学科 | 进度 |
|------|------|
| Python基础 | 12/12 |
| 线性代数 | 0/10（重构中） |
| 基础工具 | 6/6 |
| 其余 | 待开始 |

详见 [`PROGRESS.md`](PROGRESS.md)。

## 协作与讨论

- **Issues**：有疑问、纠错、改进建议 → [提交 Issue](https://github.com/w2045/study-notes/issues)
- **Pull Requests**：想贡献内容（新章节、补充习题、修正错误）
  1. Fork 本仓库
  2. 创建新分支：`git checkout -b feature/你的改动`
  3. 提交并 Push
  4. 发起 Pull Request
- **讨论**：每个 Issue / PR 下方可以自由讨论

## 致谢

- CS61A: UC Berkeley, John DeNero
- CS106B: Stanford, 参考课件 `~/Desktop/CS106B_Slides/`
- CS231N: Stanford, Fei-Fei Li et al.
- 强化学习: 西湖大学 赵世钰《强化学习的数学原理》
- 凸优化课件: `~/Desktop/Convex Optimization/`
