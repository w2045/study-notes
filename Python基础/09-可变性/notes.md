# Python基础 · 第九章 · 可变性

← 前置: [08 — 数据抽象](../08-数据抽象/notes.md)
→ 延伸: [10 — 迭代器与生成器](../10-迭代器与生成器/notes.md)

---

## 1. 直觉引入：有些东西可以「当场改变」

字符串不能变——`s.upper()` 返回新字符串，`s` 本身不变。但列表可以——`lst.append(4)` 不返回新列表，而是直接修改 `lst`。

这是 Python 最根本的区别之一：**可变对象**（list, dict, set）vs **不可变对象**（int, float, str, tuple）。掌握它，才能理解什么情况下一个操作会「意外」影响到其他变量。

---

## 2. 可变 vs 不可变

| 类型 | 可变？ | 修改方式 |
|------|--------|---------|
| int, float, bool | 不可变 | 只能创建新值 |
| str | 不可变 | 所有方法返回新字符串 |
| tuple | 不可变 | 创建后不可改内容 |
| list | 可变 | `append`, `extend`, `pop`, `insert` 等 |
| dict | 可变 | `d[key] = value` |
| set | 可变 | `add`, `remove` 等 |

---

## 3. 别名与 Mutation 的后果

```python
a = [1, 2, 3]
b = a            # b 是 a 的别名——指向同一个列表对象

b.append(4)
print(a)         # [1, 2, 3, 4] — a 也跟着变了！
```

**原因**：`a` 和 `b` 指向内存中**同一块区域**。修改 `b` 就是在修改这块内存，所以 `a` 也看到变化。

### 3.1 is vs == 回顾

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b   # True  — 值相同
a is b   # False — 不同对象
a is c   # True  — 同一个对象
```

`is` 检查**身份**（是不是同一个内存地址），`==` 检查**值**（是不是相等）。

---

## 4. 修改列表

### 4.1 原地修改方法

```python
lst = [1, 2, 3]

lst.append(4)        # [1, 2, 3, 4]      末尾追加
lst.extend([5, 6])   # [1, 2, 3, 4, 5, 6] 扩展
lst.insert(0, 0)     # [0, 1, 2, 3, 4, 5, 6] 指定位置插入
lst.pop()            # 返回 6，lst → [0,1,2,3,4,5]
lst.pop(0)           # 返回 0，lst → [1,2,3,4,5]
lst.remove(3)        # [1, 2, 4, 5]       删除第一个匹配值
lst.sort()           # [1, 2, 4, 5]       原地排序
lst.reverse()        # [5, 4, 2, 1]       原地反转

# 这些方法都返回 None！
```

> **记住**：`append`/`extend`/`sort`/`reverse`/`pop` 等**原地修改**列表，返回 `None`。`sorted()` 和 `reversed()` 返回新对象，不修改原列表。

### 4.2 切片赋值（原地修改）

```python
lst = [1, 2, 3, 4, 5]
lst[1:4] = [9, 9, 9]    # [1, 9, 9, 9, 5]
lst[1:3] = []            # [1, 9, 5]      删除切片
lst[:] = []              # []             清空列表
```

---

## 5. 字典 (dict)

### 5.1 基本操作

```python
d = {"name": "Alice", "age": 25}
d["score"] = 95         # 添加键值对
d["age"] = 26           # 修改已有键
del d["score"]          # 删除键
d.get("name")           # "Alice"   — 安全访问
d.get("missing", 0)     # 0         — 键不存在时返回默认值
```

### 5.2 迭代

```python
for key in d:             # 遍历键
for key, val in d.items(): # 遍历键值对
for val in d.values():    # 遍历值
```

### 5.3 字典推导式

```python
{x: x**2 for x in range(5)}     # {0:0, 1:1, 2:4, 3:9, 4:16}
{k: v for k, v in d.items() if v > 10}
```

---

## 6. 集合 (set)

```python
s = {1, 2, 3}          # 创建集合（注意空集合是 set()，{} 是空字典）
s.add(4)               # {1, 2, 3, 4}
s.remove(2)            # {1, 3, 4}
s.discard(99)          # 不报错（remove 会报 KeyError）

# 集合运算
a = {1, 2, 3}
b = {2, 3, 4}
a | b     # {1, 2, 3, 4}    并集
a & b     # {2, 3}          交集
a - b     # {1}             差集
a ^ b     # {1, 4}          对称差
```

---

## 7. 默认参数陷阱

```python
def add_item(item, lst=[]):       # ❌ 危险！
    lst.append(item)
    return lst

>>> add_item(1)   # [1]
>>> add_item(2)   # [1, 2]  ← 咦？不是应该 [2] 吗？
```

**原因**：默认参数在**函数定义时**求值一次，以后每次调用都共享同一个列表对象。

**正确写法**：

```python
def add_item(item, lst=None):
    if lst is None:
        lst = []          # 每次调用创建新列表
    lst.append(item)
    return lst
```

---

## 8. 可变对象作为函数参数

传入可变对象，函数内部修改会影响外部：

```python
def append_twice(x, lst):
    lst.append(x)
    lst.append(x)

nums = [1, 2]
append_twice(3, nums)
print(nums)   # [1, 2, 3, 3] — nums 被修改了！
```

这是设计特性，不是 bug——但需要清楚意识到。如果不想外部受影响，先复制：

```python
def append_twice_safe(x, lst):
    lst = lst[:]      # 浅复制
    lst.append(x)
    lst.append(x)
    return lst
```

---

## 9. 例题

### 例 1：单词计数（利用 dict 的可变性）

<details><summary>用字典统计文本词频</summary>

```python
def word_count(text):
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq
```
</details>

### 例 2：移除列表中的重复项（保持顺序）

<details><summary></summary>

```python
def dedup(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
```
</details>

### 例 3：反转字典（键值互换）

<details><summary>d = {"a":1, "b":2} → {1:"a", 2:"b"}</summary>

```python
def invert(d):
    return {v: k for k, v in d.items()}
```
</details>

---

## 10. 常见误区

| 误区 | 纠正 |
|------|------|
| `a = b` 复制了列表 | 这只是别名；用 `a = b[:]` 或 `a = list(b)` |
| `sort()` 返回排序后的列表 | `sort()` 原地修改并返回 `None`；要用 `sorted()` |
| 元组不可变所以不能包含列表 | 元组本身不可变，但**包含**的列表仍然可变 |
| 默认参数每次调用重新求值 | 只求值一次（函数定义时） |

---

## 本章核心概念速查

| 概念 | 说明 |
|------|------|
| 可变对象 | list, dict, set — 可原地修改 |
| 不可变对象 | int, float, str, tuple — 不可修改 |
| 别名 | 多个名字指向同一个对象 |
| `is` | 检查身份（同一对象） |
| `==` | 检查值相等 |
| 原地修改 | `append`, `extend`, `sort`, `reverse`, `pop` 等 |
| dict | 键值对集合，键不可变 |
| set | 无序、不重复的可变集合 |
| 默认参数陷阱 | 默认值在定义时求值一次，共享可变对象 |
