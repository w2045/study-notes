# Study Project — 自学参考书工作流

## 会话启动协议（每次新会话必做）
1. 读取 `CLAUDE.md`（本文件）了解项目约定
2. 读取 `PROGRESS.md` 获取当前进度与上次中断点
3. 向用户报告当前进度，询问是继续上次中断点还是切换主题

## 会话结束协议（每轮结束前必做）
1. 将本次完成的内容落盘
2. 更新 `PROGRESS.md`：标记已完成的章节、记录「下次从 X 开始」
3. 确保所有交叉引用链接正确

## 产出格式：参考书风格
每个章节文件为 Markdown（数学用 `$$` / `$` LaTeX 嵌入），必须包含：
1. **前置与延伸** — 文档顶部注明 `← 前置: [章节]` 和 `→ 延伸: [章节]`
2. **直觉引入** — 用日常场景解释「为什么需要这个东西」
3. **形式化定义** — 精确定义、符号约定、前提假设
4. **推导与证明** — 手把手推导，不留「显然可得」
5. **代码实现** — Python 从零实现核心算法，逐行解释
6. **例题（≥3 个）** — 全解，展示典型错误
7. **练习题（≥5 个）** — 答案用 `<details>` 折叠

## 编译
- Markdown 中嵌入 LaTeX 公式，VS Code 直接预览
- 若某章公式极度密集，写成纯 `.tex` 文件，用 `xelatex` 编译（中文支持）

## 目录结构
```
Study/
├── CLAUDE.md              # 本文件（项目约定）
├── PROGRESS.md            # 进度追踪（每次会话更新）
├── math/
│   ├── linear-algebra/    # 7 章
│   ├── calculus/          # 6 章
│   ├── probability/       # 7 章
│   ├── convex-optimization/  # 8 章
│   └── information-theory/   # 5 章
├── CS61A/                 # 后续
├── CS106B/                # 后续
├── CS231N/                # 后续
├── RL/                    # 后续
├── LLM/                   # 后续
├── notes/                 # 交叉主题笔记
└── resources/             # 论文列表、外部链接
```

## 使用的外部资源
- 凸优化课件：`~/Desktop/Convex Optimization/`（16 讲 PDF）
- CS106B 课件：`~/Desktop/CS106B_Slides/`（14 讲 PDF + Stanford Reader）
- CS61A 作业：`~/Desktop/Code/CS61A-Assignments/`（已完成，用作参考）

## 数学篇章大纲（33 章）

### 线性代数 (math/linear-algebra/) — 7 章
01-vectors-spaces.md — 向量、线性组合、向量空间
02-matrices-transforms.md — 矩阵与线性变换
03-linear-systems.md — 线性方程组与消元法
04-determinant-inverse-rank.md — 行列式、逆、秩
05-eigenvalues-eigenvectors.md — 特征值与特征向量
06-svd.md — 奇异值分解
07-matrix-calculus.md — 矩阵微积分

### 微积分 (math/calculus/) — 6 章
01-limits-derivatives.md — 极限、导数与微分
02-differentiation-chainrule.md — 求导法则与链式法则
03-partial-gradients.md — 偏导数与梯度
04-jacobian-hessian.md — 方向导数、Jacobian、Hessian
05-taylor-series.md — 泰勒展开与近似
06-optimization-calc.md — 优化中的微积分（驻点、鞍点）

### 概率论 (math/probability/) — 7 章
01-axioms-conditional.md — 概率公理与条件概率
02-random-variables.md — 随机变量与分布函数
03-expectation-moments.md — 期望、方差、矩
04-discrete-distributions.md — 常见离散分布
05-continuous-distributions.md — 常见连续分布
06-bayes-inference.md — 贝叶斯定理与贝叶斯推断
07-mle.md — 最大似然估计

### 凸优化 (math/convex-optimization/) — 8 章
01-intro-math-review.md — 引言与数学回顾
02-convex-sets.md — 凸集
03-convex-functions-1.md — 凸函数 (上)
04-convex-functions-2.md — 凸函数 (下)
05-convex-optimization-problems.md — 凸优化问题
06-gradient-descent.md — 梯度下降法
07-newton-proximal.md — 牛顿法与近端梯度
08-duality-kkt.md — 对偶理论与 KKT 条件

### 信息论 (math/information-theory/) — 5 章
01-entropy.md — 熵与信息量
02-cross-entropy-kl.md — 交叉熵与 KL 散度
03-mutual-information.md — 互信息
04-source-coding.md — 信源编码
05-channel-capacity.md — 信道容量
