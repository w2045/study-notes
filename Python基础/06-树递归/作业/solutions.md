# Python基础 · 第六章 · 树递归 — 参考答案

<details><summary>Q1 — fib</summary>

```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
```
**要点**：树递归最经典例子。两个基本情况 n=0 和 n=1。
</details>

<details><summary>Q2 — C(n, k)</summary>

```python
def C(n, k):
    if k == 0 or k == n:
        return 1
    return C(n - 1, k - 1) + C(n - 1, k)
```
**要点**：帕斯卡恒等式。分支：「选当前元素」（从 n-1 选 k-1）+「不选当前元素」（从 n-1 选 k）。
</details>

<details><summary>Q3 — grid_paths</summary>

```python
def grid_paths(m, n):
    if m == 0 or n == 0:
        return 1
    return grid_paths(m - 1, n) + grid_paths(m, n - 1)
```
**要点**：走到 (m,n) 的最后一步要么从上面来（m-1,n），要么从左边来（m,n-1）。
</details>

<details><summary>Q4 — coin_change</summary>

```python
def coin_change(amount, coins):
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    return coin_change(amount - coins[0], coins) + coin_change(amount, coins[1:])
```
**要点**：「用至少一个第一种硬币」+「完全不用第一种硬币」，互斥完备的分支。
</details>

<details><summary>Q5 — count_partitions</summary>

```python
def count_partitions(n, m):
    if n == 0:
        return 1
    if n < 0 or m == 0:
        return 0
    return count_partitions(n - m, m) + count_partitions(n, m - 1)
```
**要点**：与硬币找零同构——m 相当于最大面额。
</details>

<details><summary>Q6 — subsets</summary>

```python
def subsets(lst):
    if not lst:
        return [[]]
    head, rest = lst[0], lst[1:]
    rest_subs = subsets(rest)
    return rest_subs + [[head] + s for s in rest_subs]
```
**要点**：经典「含 / 不含」分支。不含 head 的 + 含 head 的（每个子集前面加上 head）。
</details>

<details><summary>Q7 — hanoi</summary>

```python
def hanoi(n, source, target, auxiliary):
    if n == 0:
        return []
    moves = []
    moves += hanoi(n - 1, source, auxiliary, target)
    moves.append(f"{source}→{target}")
    moves += hanoi(n - 1, auxiliary, target, source)
    return moves
```
**要点**：n-1 移到辅助柱 → 最大的移到目标 → n-1 从辅助柱移到目标。返回列表而非打印。
</details>

<details><summary>Q8 — triple_steps</summary>

```python
def triple_steps(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return triple_steps(n - 1) + triple_steps(n - 2) + triple_steps(n - 3)
```
**要点**：斐波那契的推广。三个分支对应最后一步走 1/2/3 级。
</details>

<details><summary>Q9 — pascal_row</summary>

```python
def pascal_row(k):
    if k == 0:
        return [1]
    prev = pascal_row(k - 1)
    row = [1]
    for i in range(len(prev) - 1):
        row.append(prev[i] + prev[i + 1])
    row.append(1)
    return row
```
**要点**：树递归求前一行，再构造当前行。也是一种混合——递归在行间，迭代在行内。
</details>

<details><summary>Q10 — permutations</summary>

```python
def permutations(lst):
    if not lst:
        return [[]]
    result = []
    for i, elem in enumerate(lst):
        rest = lst[:i] + lst[i+1:]          # 去掉当前元素的剩余列表
        for perm in permutations(rest):      # 递归生成剩余元素的排列
            result.append([elem] + perm)     # 当前元素放在最前面
    return result
```
**要点**：依次选每个元素作为「第一个」，递归排列剩余部分。`lst[:i] + lst[i+1:]` 构建不包含当前位置的列表。
</details>

<details><summary>Q11 — max_subset_sum</summary>

```python
def max_subset_sum(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return max(0, lst[0])
    # 包含第一个 → 不能包含第二个，从第三个开始
    include = lst[0] + max_subset_sum(lst[2:])
    # 不包含第一个 → 从第二个开始
    exclude = max_subset_sum(lst[1:])
    return max(include, exclude)
```
**要点**：含 / 不含分支，但「含」时跳过下一个以遵守相邻约束。
</details>

<details><summary>Q12 — coin_change_ways</summary>

```python
def coin_change_ways(amount, coins):
    if amount == 0:
        return [[]]                  # 空方案
    if amount < 0 or not coins:
        return []                    # 无方案
    # 用第一个硬币的方案
    use = coin_change_ways(amount - coins[0], coins)
    use = [[coins[0]] + way for way in use]
    # 不用第一个硬币的方案
    skip = coin_change_ways(amount, coins[1:])
    return use + skip
```
**要点**：和 `coin_change` 计数版本同结构，但返回方案列表而非计数。合并「用」和「不用」两个分支的方案。
</details>
