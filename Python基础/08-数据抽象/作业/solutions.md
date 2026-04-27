# Python基础 · 第八章 · 数据抽象 — 参考答案

<details><summary>Q1 — make_rational</summary>

```python
def make_rational(numer, denom):
    return [numer, denom]
```
</details>

<details><summary>Q2 — numer / denom</summary>

```python
def numer(r):
    return r[0]

def denom(r):
    return r[1]
```
**要点**：初学者常把接口函数和底层实现等价。这里看起来「无聊」的选择器正是抽象屏障——上层通过它们访问，而非直接 `r[0]`。
</details>

<details><summary>Q3 — make_rational_simplified</summary>

```python
from math import gcd

def make_rational_simplified(numer, denom):
    g = gcd(numer, denom)
    return [numer // g, denom // g]
```
**要点**：构造时自动约分。改变底层实现了，但 `numer`/`denom` 接口不变 → 上层代码全都不用改。这就是抽象的威力。
</details>

<details><summary>Q4 — mul_rational</summary>

```python
def mul_rational(r1, r2):
    return make_rational(numer(r1) * numer(r2),
                         denom(r1) * denom(r2))
```
**要点**：只用 `numer`/`denom`/`make_rational` 接口。不能写 `r1[0] * r2[0]`。
</details>

<details><summary>Q5 — tree / label / branches / is_leaf</summary>

```python
def tree(label, branches=None):
    if branches is None:
        branches = []
    return [label, list(branches)]

def label(t):
    return t[0]

def branches(t):
    return t[1]

def is_leaf(t):
    return len(branches(t)) == 0
```
**要点**：标准的树抽象。用列表 `[label, branches]` 表示。所有使用树的代码都应通过这四个函数访问。
</details>

<details><summary>Q6 — count_leaves</summary>

```python
def count_leaves(t):
    if is_leaf(t):
        return 1
    return sum(count_leaves(b) for b in branches(t))
```
**要点**：叶子是 branches 为空的节点。非叶子递归到各子树计数。
</details>

<details><summary>Q7 — tree_sum</summary>

```python
def tree_sum(t):
    return label(t) + sum(tree_sum(b) for b in branches(t))
```
**要点**：当前标签 + 各子树标签和的累加。叶子递归时 `sum([])` = 0。
</details>

<details><summary>Q8 — tree_map</summary>

```python
def tree_map(f, t):
    return tree(f(label(t)),
                [tree_map(f, b) for b in branches(t)])
```
**要点**：保持树的形状，只替换标签值。递归对每个 subtree 做 map。
</details>

<details><summary>Q9 — make_rational_closure</summary>

```python
def make_rational_closure(numer, denom):
    def dispatch(which):
        if which == 'n': return numer
        if which == 'd': return denom
    return dispatch

def numer_closure(r):
    return r('n')

def denom_closure(r):
    return r('d')
```
**要点**：用闭包而非列表存储分子分母。「函数即数据」。
</details>

<details><summary>Q10 — cons / car / cdr</summary>

```python
def cons(a, b):
    def pair(which):
        if which == 1: return a
        if which == 2: return b
    return pair

def car(p):
    return p(1)

def cdr(p):
    return p(2)
```
**要点**：纯函数实现的 pair 数据结构。`car(cons(1,2)) → 1`。
</details>

<details><summary>Q11 — add_rational</summary>

```python
def add_rational(r1, r2):
    n1, d1 = numer(r1), denom(r1)
    n2, d2 = numer(r2), denom(r2)
    return make_rational(n1 * d2 + n2 * d1, d1 * d2)
```
**要点**：通分后相加，仅用接口函数。`a/b + c/d = (ad + bc) / bd`。
</details>

<details><summary>Q12 — max_label_path</summary>

```python
def max_label_path(t):
    if is_leaf(t):
        return label(t)
    return label(t) + max(max_label_path(b) for b in branches(t))
```
**要点**：对每个分支计算到叶子的最大路径和，取最大值加当前标签。和 `tree_sum` 的区别是取 `max` 而非 `sum`。
</details>
