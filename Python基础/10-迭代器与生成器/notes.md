# Python基础 · 第十章 · 迭代器与生成器

← 前置: [09 — 可变性](../09-可变性/notes.md)
→ 延伸: [11 — 对象与类](../11-对象与类/notes.md)

---

## 1. 直觉引入：按需生产，而非一次制造全部

`range(10_000_000)` 不会在内存中创建一千万个整数——它只在需要时逐个产出。这就是**惰性求值**（lazy evaluation）。

迭代器和生成器让你处理比内存大得多的数据流——文件逐行读取、无限序列、管道式数据处理——而不必一次加载所有内容。

---

## 2. 可迭代对象 vs 迭代器

### 2.1 可迭代对象 (Iterable)

任何能用于 `for` 循环的对象都是**可迭代的**。它有一个 `__iter__()` 方法，返回一个迭代器。

```python
# 这些都是 iterable
lst = [1, 2, 3]       # 列表
s = "hello"           # 字符串
r = range(5)          # range
d = {"a": 1}          # 字典（迭代键）

# 本质：for 循环背后调用了 iter()
it = iter(lst)        # 获取迭代器
next(it) == 1         # True
next(it) == 2         # True
```

### 2.2 迭代器 (Iterator)

迭代器是实现了 `__next__()` 的对象。每次调用 `next()` 返回下一个值；没有值可返回时抛出 `StopIteration`。

```python
# 手动使用迭代器
it = iter([1, 2, 3])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
```

### 2.3 关键区别

| 特性 | 可迭代对象 | 迭代器 |
|------|-----------|--------|
| 可以被 for | 是 | 是 |
| 可重复遍历 | 是 | 否（消耗完为空） |
| `__iter__` | 返回迭代器 | 返回自己 |
| `__next__` | 不需要 | 必须有 |

```python
lst = [1, 2, 3]
for x in lst: ...    # 第一次，OK
for x in lst: ...    # 第二次，OK → list 是 iterable

it = iter(lst)
for x in it: ...     # 消耗迭代器
for x in it: ...     # 空！迭代器只能走一次
```

---

## 3. 生成器 (Generator)

生成器是最简单的创建迭代器的方式——用 `yield` 代替 `return`。

```python
def countdown(n):
    while n > 0:
        yield n       # ← yield，不是 return！
        n -= 1

>>> g = countdown(3)
>>> next(g)
3
>>> next(g)
2
>>> next(g)
1
>>> next(g)
StopIteration

>>> list(countdown(3))
[3, 2, 1]
```

### 3.1 生成器如何工作

- 调用生成器函数**不执行**函数体——它返回一个生成器对象
- 每次 `next()`，代码执行到下一个 `yield`，**暂停**并把 `yield` 后的值传出
- 下次 `next()`，从上次暂停的地方**恢复**执行

这是协程的基础——函数可以在中途暂停、保持状态、稍后继续。

### 3.2 生成器表达式

类似列表推导式，但用圆括号：

```python
# 列表推导式 — 一次性创建整个列表
squares_list = [x**2 for x in range(10)]

# 生成器表达式 — 惰性，逐个产出
squares_gen = (x**2 for x in range(10))

>>> sum(squares_gen)    # sum 逐个消费
285
```

### 3.3 yield from

委托给另一个生成器：

```python
def chain_generators(*gens):
    for g in gens:
        yield from g       # 等价于 for x in g: yield x

def gen1():
    yield 1; yield 2
def gen2():
    yield 3; yield 4

>>> list(chain_generators(gen1(), gen2()))
[1, 2, 3, 4]
```

### 3.4 双向通信：`send()`、`throw()`、`close()`

`yield` 不仅仅是「产出」——它也可以**接收**外部传入的值。这使生成器升级为**协程**（coroutine），可以在运行中途与外部交互：

```python
def echo():
    """每轮接收一个值，处理完后产出结果"""
    while True:
        received = yield                    # 暂停，等待 send() 传入值
        print(f"收到: {received}")
        yield f"已处理: {received}"

>>> g = echo()
>>> next(g)                   # 启动生成器，停在第一个 yield
>>> g.send("hello")           # 传入 "hello"，生成器从 yield 恢复
收到: hello
'已处理: hello'
>>> next(g)                   # 继续到下一个 yield（此时 receive = None）
收到: None
'已处理: None'
```

`send(value)` 做了两件事：把 `value` 传给当前暂停的 `yield` 表达式 → 恢复执行直到下一个 `yield`。注意第一次调用必须用 `next()` 或 `send(None)` 启动，因为此时还没有 `yield` 可以接收值。

**`throw()` — 向生成器注入异常**：

```python
def resilient():
    try:
        while True:
            yield "运行中"
    except ValueError:
        yield "捕获了 ValueError"

>>> g = resilient()
>>> next(g)
'运行中'
>>> g.throw(ValueError)      # 在生成器内部抛出异常
'捕获了 ValueError'
```

**`close()` — 优雅关闭生成器**：向生成器内部抛出 `GeneratorExit`，常用于清理资源（关闭文件、释放锁等）：

```python
def read_lines(path):
    f = open(path)
    try:
        for line in f:
            yield line.strip()
    finally:
        f.close()             # 无论正常结束还是 close() 都会执行
```

这三个方法让生成器从「单向数据流」（只产出）变成「双向对话」——这是 `asyncio` 中 `async`/`await` 协程的底层基础。

---

## 4. 迭代器协议：手动实现

```python
class Countdown:
    """倒计数迭代器（实现迭代器协议）"""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self              # 迭代器的 __iter__ 返回自己

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        x = self.current
        self.current -= 1
        return x

>>> list(Countdown(3))
[3, 2, 1]
```

---

## 5. 内置迭代工具

```python
# enumerate — 返回 (索引, 值) 的迭代器
list(enumerate(['a', 'b', 'c']))  # [(0,'a'),(1,'b'),(2,'c')]

# zip — 并行迭代
list(zip([1, 2], ['a', 'b']))     # [(1,'a'),(2,'b')]

# map / filter — 返回迭代器（非列表！）
map(str, [1, 2, 3])               # <map object>，惰性
list(map(str, [1, 2, 3]))         # ['1', '2', '3']

# itertools 模块
import itertools
itertools.count(10, 2)            # 10, 12, 14, ... 无限
itertools.cycle(['a', 'b'])       # 'a', 'b', 'a', 'b', ... 无限
itertools.repeat('x', 3)          # 'x', 'x', 'x'
itertools.islice(gen, 5)          # 取前 5 个
```

---

## 6. 惰性管道的威力

```python
# 读大文件：逐行处理，内存只存当前行
def read_large_file(path):
    with open(path) as f:
        for line in f:           # 文件对象是迭代器
            yield line.strip()

# 管道式处理
lines = read_large_file("data.txt")
filtered = (line for line in lines if "ERROR" in line)  # 筛选
parsed = (line.split(":")[-1] for line in filtered)     # 提取
first_5 = list(itertools.islice(parsed, 5))              # 前 5 个
# 整个过程没有一次性加载全部数据到内存
```

---

## 7. 例题

### 例 1：斐波那契生成器

<details><summary>无限斐波那契数列</summary>

```python
def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

>>> from itertools import islice
>>> list(islice(fib_gen(), 10))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
</details>

### 例 2：自定义 Range

<details><summary>实现 iterable 的 MyRange</summary>

```python
class MyRange:
    def __init__(self, start, stop, step=1):
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        curr = self.start
        while curr < self.stop:
            yield curr
            curr += self.step

>>> list(MyRange(2, 8, 2))
[2, 4, 6]
```
</details>

---

## 本章核心概念速查

| 概念 | 说明 |
|------|------|
| Iterable | 有 `__iter__`，可被 `for` 遍历 |
| Iterator | 有 `__next__`，惰性产出值 |
| 生成器函数 | 用 `yield` 的函数，返回生成器对象 |
| 生成器表达式 | `(x for x in seq if cond)` |
| `yield from` | 委托给子生成器 |
| `StopIteration` | 迭代结束的信号 |
| `itertools` | 标准库迭代工具集 |
