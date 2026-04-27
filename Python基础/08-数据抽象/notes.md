# Python基础 · 第八章 · 数据抽象

← 前置: [07 — 序列](../07-序列/notes.md)
→ 延伸: [09 — 可变性](../09-可变性/notes.md)

---

## 1. 直觉引入：隐藏实现，暴露接口

你用 `list` 时，不关心它内部如何分配内存。你用 `dict` 时，不关心里面如何做哈希。你只需要知道 `append` 在末尾接一个元素、`d[key]` 返回对应的值。

这就是**数据抽象**——把数据的实现细节隐藏在接口（一组操作函数）后面。使用数据的人只需知道能做什么，不需知道怎么做。

---

## 2. 抽象屏障

```
使用数据的程序（最高层）
        ↑
    add_rational, mul_rational, print_rational ...
        ↑
    numer, denom   ← 构造函数和选择器（接口层）
        ↑
    [num, den] 或 (num, den) 或 自定义类  ← 具体表示（实现层）
```

**规则**：高层代码只能通过接口函数访问数据，不能直接访问底层表示。这样改变底层实现时，高层代码无需修改。

---

## 3. 有理数示例

### 3.1 基本实现（用列表）

```python
# 构造函数
def make_rational(numer, denom):
    """创建有理数 numer/denom"""
    return [numer, denom]

# 选择器
def numer(r):
    return r[0]

def denom(r):
    return r[1]

# 使用接口的函数（不接触 r[0]/r[1]）
def add_rational(r1, r2):
    n1, d1 = numer(r1), denom(r1)
    n2, d2 = numer(r2), denom(r2)
    return make_rational(n1 * d2 + n2 * d1, d1 * d2)

def mul_rational(r1, r2):
    return make_rational(numer(r1) * numer(r2),
                         denom(r1) * denom(r2))

def rational_to_string(r):
    return f"{numer(r)}/{denom(r)}"
```

### 3.2 改进：自动约分

现在改变底层实现——在构造时自动约分，所有上层代码不变：

```python
from math import gcd

def make_rational(numer, denom):
    g = gcd(numer, denom)
    return [numer // g, denom // g]    # 只有这行变了

# numer, denom, add_rational, mul_rational — 全都不需要改！
```

### 3.3 改用闭包实现

即使完全不用列表，改用闭包作为底层表示，接口不变：

```python
def make_rational(numer, denom):
    g = gcd(numer, denom)
    n, d = numer // g, denom // g
    def dispatch(which):
        if which == 'n': return n
        if which == 'd': return d
    return dispatch

def numer(r):    return r('n')
def denom(r):    return r('d')

# add_rational, mul_rational, rational_to_string — 一行不变！
```

这是数据抽象的力量——改底层实现不影响任何使用方。

---

## 4. 抽象数据类型（ADT）的构成

每个 ADT 由三类操作组成：

| 类别 | 作用 | 示例（有理数） |
|------|------|--------------|
| 构造器 | 创建该类型的值 | `make_rational(n, d)` |
| 选择器 | 取出内部信息 | `numer(r)`, `denom(r)` |
| 谓词/转换器 | 判断类型、转换输出 | `rational_to_string(r)` |

---

## 5. 树抽象

树是一种递归数据结构——每个节点包含一个标签和 0 个或多个子树。

```python
# 构造器
def tree(label, branches=None):
    if branches is None:
        branches = []
    return [label, list(branches)]

# 选择器
def label(t):
    return t[0]

def branches(t):
    return t[1]

def is_leaf(t):
    return len(branches(t)) == 0
```

**关键**：使用树的代码**只通过这四个函数**访问树，绝不直接写 `t[0]` 或 `t[1]`。

```python
# 示例树
t = tree(1, [
    tree(2, [tree(4), tree(5)]),
    tree(3, [tree(6)])
])

#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
```

### 5.1 递归树操作

```python
def count_nodes(t):
    """统计树中节点数"""
    return 1 + sum(count_nodes(b) for b in branches(t))

def tree_sum(t):
    """所有标签之和"""
    return label(t) + sum(tree_sum(b) for b in branches(t))

def tree_max(t):
    """最大标签"""
    return max([label(t)] + [tree_max(b) for b in branches(t)])
```

### 5.2 树的映射

```python
def tree_map(f, t):
    """对每个标签应用 f，返回新树"""
    return tree(f(label(t)),
                [tree_map(f, b) for b in branches(t)])
# 注意：这也是一种树递归！
```

---

## 6. 用闭包实现 Pair

Lisp/Scheme 的传统：用函数实现 cons cell：

```python
def cons(a, b):
    """构造有序对"""
    def pair(which):
        if which == 1: return a
        if which == 2: return b
    return pair

def car(pair):
    return pair(1)

def cdr(pair):
    return pair(2)
```

所有数据结构（列表、树、字典）都可以用 `cons`/`car`/`cdr` 构建——虽然 Python 通常不这样写，但这是理解「函数即数据」的重要练习。

---

## 7. 例题

### 例 1：用有理数接口做运算

<details><summary>1/2 + 1/3, 且化简</summary>

```python
r1 = make_rational(1, 2)
r2 = make_rational(1, 3)
result = add_rational(r1, r2)
rational_to_string(result)  # "5/6"
```
</details>

### 例 2：过滤树中满足条件的标签

<details><summary>返回所有 >5 的标签</summary>

```python
def filter_tree(pred, t):
    """返回树中所有满足 pred 的标签列表"""
    labels = [label(t)] if pred(label(t)) else []
    for b in branches(t):
        labels.extend(filter_tree(pred, b))
    return labels

>>> filter_tree(lambda x: x > 3, t)
[4, 5, 6]
```
</details>

### 例 3：树的深度

<details><summary>递归计算树的最大深度</summary>

```python
def depth(t):
    if is_leaf(t):
        return 0
    return 1 + max(depth(b) for b in branches(t))
```
</details>

---

## 8. 常见误区

| 误区 | 纠正 |
|------|------|
| 抽象 = 复杂 | 抽象的目的是简化——把复杂细节关在接口后面 |
| 直接用底层访问更快 | 损失了可维护性。`numer(r)` 的调用开销可以忽略不计 |
| 数据抽象只有类才能实现 | 列表、闭包、类都可以——接口是关键，具体实现是细节 |

---

## 本章核心概念速查

| 概念 | 说明 | 示例 |
|------|------|------|
| 抽象屏障 | 接口与实现之间的边界 | 上层不碰 `r[0]` |
| 构造器 | 创建该类型值的函数 | `make_rational`, `tree` |
| 选择器 | 取出内部信息的函数 | `numer`, `label`, `branches` |
| 树 | 递归的层次数据结构 | `[label, [branch...]]` |
| 闭包表示 | 用函数表示数据 | `cons`/`car`/`cdr` |
| ADT | Abstract Data Type | 由接口定义，实现可换 |
