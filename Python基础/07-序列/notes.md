# Python基础 · 第七章 · 序列：列表、字符串、元组

← 前置: [06 — 树递归](../06-树递归/notes.md)
→ 延伸: [08 — 数据抽象](../08-数据抽象/notes.md)

---

## 1. 直觉引入：有序数据的容器

前面我们零星用过列表 `[1, 2, 3]` 和字符串 `"hello"`。它们有一个共同点——**有序**。你可以说「第 3 个元素是什么」「从第 2 个到第 5 个」。这就是**序列**——有顺序、可索引的数据类型。

Python 有 4 种内置序列类型：**列表**（可变）、**字符串**（不可变）、**元组**（不可变）、**range**（惰性整数序列）。本章系统学习它们。

---

## 2. 列表 (list)

### 2.1 创建与基本操作

```python
lst = [1, 2, 3, 4, 5]
lst[0]       # 1          — 索引（0-based）
lst[-1]      # 5          — 负索引从末尾开始
lst[1:4]     # [2, 3, 4]  — 切片 [start:stop]，不含 stop
lst[::2]     # [1, 3, 5]  — 步长 2
lst[::-1]    # [5, 4, 3, 2, 1] — 反转
```

### 2.2 可变性：列表 vs 字符串

```python
lst = [1, 2, 3]
lst[0] = 99       # ✅ 列表可变
# lst → [99, 2, 3]

s = "hello"
s[0] = "H"        # ❌ TypeError: 'str' object does not support item assignment
```

### 2.3 常用方法

```python
lst = [3, 1, 2]
lst.append(4)          # [3, 1, 2, 4]     — 末尾添加
lst.extend([5, 6])     # [3, 1, 2, 4, 5, 6] — 扩展列表
lst.insert(0, 99)      # [99, 3, 1, ...]  — 指定位置插入
lst.pop()              # 6                — 弹出末尾
lst.pop(0)             # 99               — 弹出指定位置
lst.remove(1)          # [3, 2, 4, 5]     — 移除第一个匹配值
lst.sort()             # [2, 3, 4, 5]     — 原地排序
lst.reverse()          # [5, 4, 3, 2]     — 原地反转
lst.index(3)           # 2                — 查找索引
lst.count(3)           # 1                — 计数
```

> **原地方法 vs 返回新对象**：`sort()` 原地修改返回 `None`；`sorted(lst)` 返回新列表不修改原列表。同样的模式：`reverse()` vs `reversed()`。

### 2.4 切片赋值

```python
lst = [1, 2, 3, 4, 5]
lst[1:4] = [9, 9]    # [1, 9, 9, 5]      — 替换一段
lst[2:2] = [8, 8]    # [1, 9, 8, 8, 9, 5] — 在位置 2 插入
lst[1:3] = []        # [1, 8, 8, 9, 5]   — 删除一段
```

### 2.5 is vs ==

```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b   # True   — 值相等
a is b   # False  — 不同对象

c = a
c is a   # True   — 同一个对象
c[0] = 99
a        # [99, 2, 3] — a 也变了！
```

---

## 3. 字符串 (str)

### 3.1 不可变性

字符串的任何「修改」操作都**返回新字符串**：

```python
s = "hello"
s.upper()       # "HELLO"  — s 本身不变
s               # "hello"
```

### 3.2 常用方法

```python
s = "  Hello, World!  "
s.strip()          # "Hello, World!"
s.lower()          # "  hello, world!  "
s.upper()          # "  HELLO, WORLD!  "
s.replace("Hello", "Hi")  # "  Hi, World!  "
s.split(",")       # ['  Hello', ' World!  ']
", ".join(["a", "b"])  # "a, b"
s.find("World")    # 9
s.count("l")       # 3
s.startswith("  H")  # True
s.isdigit()        # False
```

### 3.3 字符串格式化

```python
name, age = "Alice", 25

# f-string（推荐，Python 3.6+）
f"{name} is {age} years old"       # "Alice is 25 years old"
f"{age:.2f}"                        # "25.00"
f"{age:>5}"                         # "   25"（右对齐，宽度 5）

# format 方法
"{} is {} years old".format(name, age)

# % 格式化（老式）
"%s is %d years old" % (name, age)
```

---

## 4. 元组 (tuple)

```python
t = (1, 2, 3)
t = 1, 2, 3        # 等价——括号有时可省略
t[0]               # 1
t[0] = 5           # ❌ TypeError: 'tuple' object does not support item assignment
```

### 4.1 为什么需要元组？

1. **不可变**意味着安全——不会被意外修改
2. 可以作为字典键（列表不能）
3. 语义上表示「记录」：`("Alice", 25, "Engineer")` 比列表更能表达「这是一条固定的记录」
4. 略快于列表（内存和创建速度）

### 4.2 解包

```python
point = (3, 5)
x, y = point         # x=3, y=5

a, b = b, a          # 交换——右侧先创建元组 (b, a)，然后解包

# 多值返回实际上返回元组
def min_max(lst):
    return min(lst), max(lst)    # 返回 tuple (a, b)

lo, hi = min_max([3, 1, 4, 1, 5])  # 解包
```

### 4.3 星号解包

```python
first, *rest = [1, 2, 3, 4]
# first=1, rest=[2, 3, 4]

a, *mid, b = "hello"
# a='h', mid=['e','l','l'], b='o'
```

---

## 5. Range

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 6)       # 2, 3, 4, 5
range(0, 10, 3)   # 0, 3, 6, 9
range(5, 0, -1)   # 5, 4, 3, 2, 1
```

Range 是惰性的——`range(1000000)` 不创建 100 万个整数，只在迭代时逐个产生。

---

## 6. 序列操作

### 6.1 通用操作

适用所有序列类型（str, list, tuple, range）：
```python
len(s) / s[i] / s[i:j] / x in s / x not in s
s + t                          # 拼接
s * n                          # 重复 n 次
for item in s:                 # 迭代
min(s) / max(s) / sum(s)
```

### 6.2 zip — 并行迭代

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

list(zip(names, scores))  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
```

### 6.3 enumerate — 索引 + 值

```python
for i, item in enumerate(["a", "b", "c"]):
    print(i, item)
# 0 a / 1 b / 2 c
```

### 6.4 序列解包嵌套

```python
pairs = [(1, 2), (3, 4), (5, 6)]
for a, b in pairs:         # 直接解包
    print(a + b)

# 嵌套结构也支持
data = [("Alice", (85, 92)), ("Bob", (78, 88))]
for name, (math, english) in data:
    print(f"{name}: math={math}, english={english}")
```

---

## 7. 列表推导式（Comprehensions）

```python
# 基本形式
[x * 2 for x in range(5)]          # [0, 2, 4, 6, 8]

# 带条件
[x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# 嵌套
[(x, y) for x in [1,2] for y in [3,4]]  # [(1,3),(1,4),(2,3),(2,4)]

# 带变换 + 条件
[x**2 for x in range(10) if x % 3 == 0]  # [0, 9, 36, 81]
```

> 列表推导式通常比等效的 `for` 循环更快、更可读——但嵌套超过两层就该拆成普通循环。

---

## 8. 复制：浅复制 vs 深复制

```python
import copy

original = [[1, 2], [3, 4]]

shallow = original[:]        # 浅复制
shallow = list(original)     # 同上
shallow = copy.copy(original)

deep = copy.deepcopy(original)   # 深复制

# 浅复制：外层新列表，内层共享
shallow[0][0] = 99
original[0][0]   # 99 — 内层列表还是同一个！

# 深复制：递归复制所有层
deep[0][0] = 99
original[0][0]   # 1 — 完全独立
```

---

## 9. 例题

### 例 1：字符频率统计

<details><summary>统计字符串中每个字符出现次数</summary>

```python
def char_freq(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

>>> char_freq("hello")
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```
</details>

### 例 2：滑动窗口求和

<details><summary>每 k 个连续元素求和</summary>

```python
def sliding_sum(lst, k):
    return [sum(lst[i:i+k]) for i in range(len(lst) - k + 1)]

>>> sliding_sum([1, 2, 3, 4, 5], 3)
[6, 9, 12]
```
</details>

### 例 3：压缩连续重复字符

<details><summary>"aaabbbcc" → "a3b3c2"</summary>

```python
def compress(s):
    if not s: return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(f"{s[i-1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return "".join(result)

>>> compress("aaabbbcc")
'a3b3c2'
```
</details>

---

## 10. 常见误区

| 误区 | 纠正 |
|------|------|
| `list.append(lst2)` 加的是整个列表 | 用 `extend` 或 `+=` 来合并列表 |
| 切片返回新列表，很「便宜」 | 创建新列表需要 O(k) 空间 |
| `a = b` 复制列表 | 这只是别名；用 `a = b[:]` 或 `list(b)` |
| 元组不可变 = 不能包含可变元素 | 元组本身不可变，但可以包含可变元素如列表 |

---

## 本章核心概念速查

| 概念 | 语法 | 说明 |
|------|------|------|
| 索引 | `lst[i]` | 0-based, 负索引从末尾开始 |
| 切片 | `lst[i:j:k]` | 包含 i，不包含 j，步长 k |
| 列表推导 | `[f(x) for x in seq if cond]` | 创建新列表的简洁语法 |
| 解包 | `a, *b = seq` | 将序列展开赋值给多个变量 |
| zip | `zip(seq1, seq2)` | 并行迭代 |
| enumerate | `enumerate(seq)` | 索引 + 值 |
| sorted | `sorted(seq, key=f)` | 返回排序的新列表 |
| is vs == | `a is b` / `a == b` | 身份比较 / 值比较 |
| f-string | `f"{expr}"` | 字符格式化 |
| join | `sep.join(seq)` | 用分隔符连接字符串序列 |
