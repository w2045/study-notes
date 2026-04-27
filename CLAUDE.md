# Study Project — 自学参考书工作流

## 会话启动协议（每次新会话必做）
1. 读取 `CLAUDE.md` 了解项目约定
2. 读取 `PROGRESS.md` 获取当前进度与上次中断点
3. 读取当前学科的 `OUTLINE.md` 获取章节清单与作业形式
4. 向用户报告当前进度，询问是否从上次中断点继续

## 会话结束协议（每轮结束前必做）
1. 内容落盘
2. 更新 `PROGRESS.md`：标记已完成章节、更新「下次从 X 开始」
3. Commit + push 到 `origin main`（远程: `https://github.com/w2045/study-notes`）

---

## 学科目录

```
Study/
├── CLAUDE.md
├── PROGRESS.md
├── Python基础/             # 参考 CS61A
├── 数据结构与算法/          # 参考 CS106B
├── 计算机视觉与深度学习/    # 参考 CS231N
├── 强化学习/
├── 大语言模型/
├── 数学基础/
│   ├── 线性代数/
│   ├── 微积分/
│   ├── 概率论/
│   ├── 凸优化/
│   └── 信息论/
├── notes/                  # 跨主题散篇笔记
└── resources/              # 论文列表、外部链接
```

## 每章结构（按学科类型：子目录分类存放）

### 数学类（线性代数 / 微积分 / 概率论 / 凸优化 / 信息论）
视章节需要，理论题与编程题可同时存在，也可仅含其一：

含编程的章节：
```
XX-章节名/
├── notes.md
├── 理论题/
│   ├── homework.md     # 理论题（LaTeX，批改用）
│   └── solutions.md    # 理论题答案
└── 编程题/
    ├── homework.md       # 题目描述
    ├── homework.py       # 代码骨架（pass 占位）
    ├── grader.py         # 自动批改
    └── solutions.md      # 参考答案
```

纯理论章节（如行列式、Jordan、矩阵微积分）：
```
XX-章节名/
├── notes.md
└── 理论题/
    ├── homework.md
    └── solutions.md
```

### 编程类（Python基础 / 数据结构与算法）
纯编程练习，自动批改：

```
XX-章节名/
├── notes.md
└── 作业/
    ├── homework.md      # 题目描述（≥10 题）
    ├── homework.py      # 代码骨架
    ├── grader.py        # 自动批改
    └── solutions.md      # 参考答案（<details> 折叠）
```

### 工具类（基础工具）
文件少，不建子目录：

```
XX-章节名/
├── notes.md
├── homework.md      # 练习题（6-8 题）
└── solutions.md     # 参考答案（<details> 折叠）
```

### notes.md 规范
1. `← 前置: [章节]` 和 `→ 延伸: [章节]` 在顶部和底部
2. 直觉引入 → 形式定义 → 推导/证明 → 代码 → 例题 → 常见误区
3. 数学用 `$$` / `$` 嵌入。代码配上逐行解释
4. 末尾附「本章核心概念速查」表

### homework.md 规范
- ≥10 题，标注难度 ⭐/⭐⭐/⭐⭐⭐
- 题型混合：代码补全、实现函数、找 bug、doctest、综合题
- 每题给出公开测试用例

### homework.py 规范
- 函数签名 + docstring（含 doctest）
- 函数体用 `pass` 占位
- 顶部注明运行方式：`python3 grader.py`

### grader.py 规范
- `import importlib` 动态导入 `homework.py`
- 每道题多组测试用例（含边界）定义在 `TEST_CASES`
- 浮点数比较用 `math.isclose`
- 输出每道题的 ✅/❌ + 错误详情 + 总分

### solutions.md 规范
- 所有答案用 `<details><summary>` 折叠
- 每题附「要点」解释关键思路和常见错误

---

## 分支策略

- `main`：完整参考书（笔记 + 题目模板 + 答案），由 AI 助手维护
- 个人分支：clone 后自行创建，用于写作业。新内容从 `main` merge

---

## 外部参考资源
- 凸优化课件：`~/Desktop/Convex Optimization/`（16 讲 PDF）
- CS106B 课件：`~/Desktop/CS106B_Slides/`（14 讲 PDF + Stanford Reader）
- Python 基础作业：`~/Desktop/Code/CS61A-Assignments/`（已完成，用作参考）
- 强化学习：西湖大学 赵世钰《强化学习的数学原理》([MathFoundationRL](https://github.com/MathFoundationRL))

---

## Python基础 大纲（12 章）

01 — 表达式、变量与函数定义
02 — 控制流：布尔、条件、while 循环
03 — 高阶函数
04 — 环境图与 Lambda
05 — 递归
06 — 树递归
07 — 序列：列表、字符串、元组
08 — 数据抽象
09 — 可变性
10 — 迭代器与生成器
11 — 对象与类
12 — 继承

---

## 数学篇章大纲（36 章）

大纲、作业形式、进度见各科目 `数学基础/<科目>/OUTLINE.md`：
- 线性代数（10 章）
- 微积分（6 章）
- 概率论（7 章）
- 凸优化（8 章）
- 信息论（5 章）

---

大纲详情见各自 `OUTLINE.md`。
