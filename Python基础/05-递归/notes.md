# Python基础 · 第五章 · 递归

← 前置: [04 — 环境图与 Lambda](../04-环境图与Lambda/notes.md)
→ 延伸: [06 — 树递归](../06-树递归/notes.md)

---

## 1. 直觉引入：自己解决自己的子问题

假设你要数一个盒子里有多少颗糖。你可以把糖一颗颗拿出来数——这是迭代。另一种方式：如果盒子是空的，0 颗；否则拿出一颗，数剩下的（**同样的问题，规模更小**），再加 1。

这就是递归——函数调用自己来解决规模更小的同类问题。

```python
def count_candies(box):
    if box is_empty:
        return 0                   # 基本情况：不需要进一步递归
    else:
        box.pop()                  # 取出一颗
        return 1 + count_candies(box)  # 递归：1 + 剩下有多少颗
```

---

## 2. 递归的两要素

每个递归函数必须有两个部分：

1. **基本情况（base case）**：可以直接回答的最简情况，不需要递归。
2. **递归步骤（recursive step）**：把问题分解成「一个简单操作」+「规模更小的同类问题」。

```python
def factorial(n):
    """n! = n × (n-1) × ... × 1"""
    if n == 0:
        return 1              # 基本情况：0! = 1
    else:
        return n * factorial(n - 1)  # 递归步骤：n! = n × (n-1)!
```

**追踪 `factorial(4)`**：

```
factorial(4)
→ 4 * factorial(3)
      → 3 * factorial(2)
            → 2 * factorial(1)
                  → 1 * factorial(0)
                        → 1        ← 基本情况，开始返回
                  → 1 * 1 = 1
            → 2 * 1 = 2
      → 3 * 2 = 6
→ 4 * 6 = 24
```

---

## 3. 递归与环境图

每次函数调用创建**新的帧**。递归调用没有特殊之处——它和普通函数调用的环境图完全相同。

```python
def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)
```

调用 `factorial(3)` 创建帧序列：

```
Global: factorial → func(n)
F1 {n:3}:  return 3 * factorial(2)    → 需要等待 factorial(2) 的结果
F2 {n:2}:  return 2 * factorial(1)    → 等待 factorial(1)
F3 {n:1}:  return 1 * factorial(0)    → 等待 factorial(0)
F4 {n:0}:  return 1                   → 基本情况，开始返回
           ← 返回 1 给 F3
F3: return 1 * 1 = 1 → 返回给 F2
F2: return 2 * 1 = 2 → 返回给 F1
F1: return 3 * 2 = 6 → 最终结果
```

每个帧的 `n` 值不同，因为每次调用都有自己的参数绑定。这正是环境模型追踪递归的方式。

---

## 4. 递归 vs 迭代

```python
# 迭代版本
def factorial_iter(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# 递归版本
def factorial_rec(n):
    if n == 0: return 1
    return n * factorial_rec(n - 1)
```

| | 迭代 | 递归 |
|------|------|------|
| 实现方式 | 循环变量 + 累积器 | 函数自调用 |
| 状态管理 | 显式的变量更新 | 参数传递 + 返回值 |
| 思维模式 | 「怎么做」：步骤序列 | 「是什么」：问题的数学定义 |
| 栈空间 | O(1) | O(n)（每次调用占一帧） |
| 适合场景 | 线性处理 | 自相似结构（树、嵌套、分治） |

---

## 5. 递归的经典模式

### 5.1 整数操作

```python
def sum_digits(n):
    """各位数字之和：sum_digits(123) → 6"""
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)
    #      最后一位  + 前面所有位之和
```

分解逻辑：`n` 的最后一位是从 `n` 中分离的「一小部分」，`n // 10` 是规模更小的同类问题。

### 5.2 序列操作

```python
def length(lst):
    """递归求列表长度"""
    if lst == []:
        return 0
    return 1 + length(lst[1:])
    #  第一个元素 + 剩余列表的长度
```

### 5.3 条件累积

```python
def count_evens(lst):
    """统计列表中偶数的个数"""
    if lst == []:
        return 0
    head, rest = lst[0], lst[1:]
    return (1 if head % 2 == 0 else 0) + count_evens(rest)
```

### 5.4 递归构建列表

```python
def filter_odd(lst):
    """返回只含奇数的新列表"""
    if lst == []:
        return []
    head, rest = lst[0], lst[1:]
    if head % 2 != 0:
        return [head] + filter_odd(rest)
    else:
        return filter_odd(rest)
```

---

## 6. 相互递归

两个函数互相调用对方：

```python
def is_even(n):
    if n == 0: return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0: return False
    return is_even(n - 1)
```

相互递归将问题分解为两个交替的情况。环境图中，两个函数各自的 parent 都指向全局帧，调用对方时正常创建新帧。

**实际应用**：语法分析（表达式递归调用语句，语句递归调用表达式）、状态机、游戏中的回合交替。

---

## 7. 尾递归（简介）

**尾递归**：递归调用是函数体中执行的**最后一步**（没有额外的「等待计算」）。

```python
# 普通递归（非尾递归）：factorial(4) 调用 factorial(3) 后还要乘以 4
def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)      # ← 还要乘以 n，不是最后一步

# 尾递归：累积器参数，递归调用是最后一步
def factorial_tail(n, acc=1):
    if n == 0: return acc
    return factorial_tail(n - 1, acc * n)   # ← 真正最后一步
```

**为什么关心？** 尾递归可以被编译器优化为迭代——复用同一个帧，不消耗额外栈空间。Python 官方实现**不做尾递归优化**（Guido 认为它会破坏调试信息），但理解这个概念有助于学习 Scheme 等语言（第 13 章），那些语言依赖尾递归代替循环。

---

## 8. 常见错误与调试

### 8.1 没有基本情况

```python
def forever(n):
    return forever(n - 1)    # 永远不会停！
# RecursionError: maximum recursion depth exceeded
```

Python 默认递归深度限制 ~1000 层。超过则抛 `RecursionError`。

### 8.2 基本情况不对

```python
def factorial_bug(n):
    if n == 1:               # ❌ factorial(0) 会无限递归
        return 1
    return n * factorial_bug(n - 1)
```

### 8.3 「信任递归」原则

写递归函数时最难的是相信递归能正确解决子问题。步骤：
1. 明确基本情况，直接给出答案
2. **相信** `func(smaller_input)` 是正确的（不要追踪所有调用！）
3. 用子结果组合出当前答案

### 8.4 调试技巧

```python
def factorial_debug(n, depth=0):
    """带缩进追踪的递归"""
    print(f"{'  ' * depth}factorial({n})")
    if n == 0:
        print(f"{'  ' * depth}→ 1")
        return 1
    result = n * factorial_debug(n - 1, depth + 1)
    print(f"{'  ' * depth}→ {result}")
    return result

>>> factorial_debug(3)
factorial(3)
  factorial(2)
    factorial(1)
      factorial(0)
      → 1
    → 1
  → 2
→ 6
```

---

## 9. 例题

### 例 1：递归求幂

<details><summary>x 的 n 次方，不使用 **</summary>

```python
def power(x, n):
    """x^n, n ≥ 0"""
    if n == 0:
        return 1
    return x * power(x, n - 1)

assert power(2, 3) == 8
assert power(5, 0) == 1
```
</details>

### 例 2：判断回文

<details><summary>字符串是否正反读相同</summary>

```python
def is_palindrome(s):
    """'racecar' → True, 'hello' → False"""
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

assert is_palindrome("racecar") == True
assert is_palindrome("hello") == False
```
</details>

### 例 3：二分查找

<details><summary>在有序列表中递归查找目标值</summary>

```python
def binary_search(lst, target, lo=0, hi=None):
    if hi is None:
        hi = len(lst) - 1
    if lo > hi:
        return -1                     # 没找到
    mid = (lo + hi) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, hi)
    else:
        return binary_search(lst, target, lo, mid - 1)

>>> binary_search([1, 3, 5, 7, 9], 5)
2
>>> binary_search([1, 3, 5, 7, 9], 6)
-1
```

每次递归将搜索范围减半，时间复杂度 O(log n)。
</details>

---

## 10. 常见误区

| 误区 | 纠正 |
|------|------|
| 递归比迭代慢所以不应该用 | 对某些问题（树遍历、分治）递归更自然、更可读；性能差异通常无关紧要 |
| 递归一定比迭代短 | 不总是——但递归更贴近数学定义 |
| 尾递归在 Python 中有优化 | Python 不做尾递归优化 |
| 基本情况总是 `n==0` | 基本情况取决于问题：空列表、空字符串、`n==1`、`lo>hi` 等 |

---

## 本章核心概念速查

| 概念 | 说明 | 示例 |
|------|------|------|
| 基本情况 | 可直接回答的最简情况 | `if n == 0: return 1` |
| 递归步骤 | 分解问题 + 自调用 | `return n * f(n-1)` |
| 递归环境图 | 每次调用创建新帧，参数独立 | n=3→n=2→n=1→n=0 |
| 相互递归 | 两个函数互相调用 | `is_even` / `is_odd` |
| 尾递归 | 递归调用是最后一步 | `return f(n-1, acc*n)` |
| `RecursionError` | 超过递归深度限制 | 缺基本情况或输入太大 |
| 信任递归 | 先假设子问题已被正确解决 | 写递归的核心心态 |
