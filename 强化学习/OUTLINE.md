# 强化学习 · 课程大纲

参考：西湖大学 赵世钰《强化学习的数学原理》（[MathFoundationRL](https://github.com/MathFoundationRL)）

## 章节

| # | 章 | 核心内容 |
|---|-----|----------|
| 01 | 基本概念：MDP 框架 | State, Action, Policy, Reward, Return, Episode, Markov 性质 |
| 02 | 贝尔曼公式 | State value、贝尔曼方程推导、向量形式与求解、Action value |
| 03 | 贝尔曼最优公式 | 最优策略定义、不动点原理、最优策略的存在性与唯一性 |
| 04 | 值迭代与策略迭代 | Value Iteration, Policy Iteration, Truncated Policy Iteration |
| 05 | 蒙特卡洛方法 | MC Basic, MC Exploring Starts, MC ε-Greedy |
| 06 | 随机近似与随机梯度下降 | Robbins-Monro 算法、SGD、BGD/MBGD/SGD 对比 |
| 07 | 时序差分方法 | TD 算法、SARSA、Expected Sarsa、n-step Sarsa、Q-learning、On-policy vs Off-policy |
| 08 | 值函数近似 | 函数逼近、Sarsa/Q-learning with VFA、DQN、Experience Replay |
| 09 | 策略梯度方法 | Average value/Average reward 目标函数、梯度计算、REINFORCE 算法 |
| 10 | Actor-Critic 方法 | QAC、Advantage A2C、重要性采样、Off-policy AC、DPG |
