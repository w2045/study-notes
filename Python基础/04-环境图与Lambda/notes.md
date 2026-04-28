# Python基础 · 第四章 · 环境图与 Lambda

← 前置: [03 — 高阶函数](../03-高阶函数/notes.md)
→ 延伸: [05 — 递归](../05-递归/notes.md)

---

## 1. 直觉引入：函数「记住」了什么？

第三章的 `make_adder(5)` 返回一个函数，它在 `make_adder` 结束之后仍然「记得」`n=5`。这是怎么实现的？

```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
add5(10)   # 15 —— n 已经不存在了，add5 怎么还记得 n=5？
```

答案在**环境模型**中。函数不仅仅是一段代码——它是代码 + 指向创建时环境的指针。这一章我们深入理解这个机制，同时系统学习 `lambda`（匿名函数）。

---

## 2. 环境模型回顾

### 2.1 帧与环境

程序运行时，解释器维护着一系列**帧**（frame）。每个帧是一个「名字 → 值」的映射表。**环境**是一系列帧的链。

- **全局帧**：程序启动时创建，存模块顶层定义的变量/函数
- **局部帧**：每次函数调用时创建，存参数和函数内定义的变量
- 当前环境 = 当前局部帧 → 外层帧 → ... → 全局帧

### 2.2 名字求值规则

当 Python 遇到一个名字（如 `x`），它按以下顺序查找：

1. 当前局部帧
2. 外层函数的局部帧（如果有）
3. 再外层……
4. 全局帧
5. 内置名字空间（`print`, `len`, `range` 等）

**关键**：查找沿着**定义时的环境链**向上，而不是调用时的环境链！这就是闭包能工作的原因。

---

## 3. 环境图：可视化闭包

### 3.1 make_adder 的环境图

```
全局帧:
  make_adder ───→ func make_adder(n) [parent=Global]

调用 make_adder(5) 创建帧 F1:
  n: 5
  adder ───→ func adder(x) [parent=F1]    ← 函数的 parent 指向定义时的帧
  return adder

调用 add5(10) = adder(10) 创建帧 F2:
  x: 10
  parent=F1                               ← 找 n: 在 F1 找到 n=5
  return 10 + 5 = 15
```

**核心规则**：每个函数对象有一个 `parent` 指针，指向它被**定义**时所在的环境。不是调用时！

### 3.2 不同的闭包，不同的环境

```python
add5 = make_adder(5)    # adder 的 parent → {n: 5}
add3 = make_adder(3)    # adder 的 parent → {n: 3}
```

每次调用 `make_adder` 创建**新的帧**，所以每个 `adder` 的 parent 指向不同的环境，`n` 的值不同。

```python
>>> add5(10), add3(10)
(15, 13)
```

### 3.3 多层嵌套

```python
def make_multiplier(a):
    def multiplier(b):
        def multiply(c):
            return a * b * c
        return multiply
    return multiplier

>>> double = make_multiplier(2)       # multiplier parent→{a:2}
>>> double3 = double(3)               # multiply parent→{b:3}→{a:2}
>>> double3(4)                        # 在父帧链上找到 a=2, b=3
24
```

名字查找沿 parent 链从内向外：`multiply` 帧 → 帧 `{b=3, parent→F1}` → 帧 `F1 {a=2, parent→Global}`。

环境图让我们看清了闭包的内部机制。到目前为止，创建函数一直用 `def`。但还有一种等价写法——`lambda`，它创建一个没有名字的函数，可以作为**表达式**嵌在任何需要值的地方。

---

## 4. Lambda：匿名函数

### 4.1 语法

```python
lambda 参数1, 参数2, ...: 表达式
```

`lambda` 是一个**表达式**（不是语句），它求值的结果是一个函数对象。不同于 `def`：

```python
# lambda —— 表达式，可以嵌在任何需要值的地方
square = lambda x: x * x

# def —— 语句，建立名字绑定
def square(x):
    return x * x
```

两者编译后生成的对象完全相同——语义上等价。区别仅在于语法形式和使用场景。

### 4.2 使用场景

**场景 1：高阶函数参数（最常用）**

```python
>>> sorted(["apple", "banana", "kiwi"], key=lambda word: len(word))
['kiwi', 'apple', 'banana']

>>> list(filter(lambda x: x > 0, [-3, 5, -2, 7]))
[5, 7]

>>> list(map(lambda x: x ** 2, [1, 2, 3, 4]))
[1, 4, 9, 16]
```

**场景 2：立即调用（不常用但合法）**

```python
>>> (lambda x, y: x + y)(3, 5)
8
```

**场景 3：作为返回值**

```python
def make_power(n):
    return lambda x: x ** n    # 比 def + return 更简洁

>>> cube = make_power(3)
>>> cube(4)
64
```

### 4.3 Lambda 的限制

| Lambda | Def |
|--------|-----|
| 只能一个表达式 | 可以多条语句 |
| 不能有 `if`/`for`/`while` 语句 | 可以有任意控制流 |
| 不能有 docstring | 可以有 docstring |
| 不能有 `return`（隐式返回表达式值） | 需要 `return` |
| 不能有赋值语句（`x = ...`） | 可以 |

```python
# ❌ 语法错误：lambda 中不能用赋值语句
# lambda x: y = x + 1; return y

# ❌ 语法错误：不能写 if 语句
# lambda x: if x > 0: return 1 else: return 0

# ✅ 但可以用条件表达式
safe_sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)
```

`lambda` 简短但有一处出名容易踩的坑——当它与循环和闭包结合时。上一节讲了闭包捕获的是名字绑定而非值的快照，这在循环中创建多个 lambda 时会产生违反直觉的结果。

---

## 5. Lambda 与闭包陷阱

### 5.1 经典陷阱：循环中的 lambda

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

>>> [f() for f in funcs]
[2, 2, 2]         # 不是 [0, 1, 2]！
```

**环境图解释**：三个 lambda 的 parent 都指向**同一个帧**（全局帧），而循环结束后 `i = 2`。当调用 `f()` 时，沿 parent 链找到的 `i` 都是 2。

**修复方法 1**：用默认参数捕获当前值（默认参数在定义时求值）：

```python
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)    # 默认参数在定义时绑定

>>> [f() for f in funcs]
[0, 1, 2]
```

**修复方法 2**：用工厂函数隔离环境：

```python
def make_printer(val):
    return lambda: val

funcs = [make_printer(i) for i in range(3)]
>>> [f() for f in funcs]
[0, 1, 2]
```

### 5.2 闭包修改外部变量

```python
def make_counter():
    count = 0
    def counter():
        count += 1       # ❌ UnboundLocalError!
        return count
    return counter
```

`count += 1` 被 Python 解析为 `count = count + 1`，赋值使 `count` 被视为局部变量。但右侧 `count + 1` 又试图读取还没有值的局部变量 → 错误。

**修复**：用 `nonlocal` 声明：

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count    # 告诉 Python: count 不是局部变量
        count += 1
        return count
    return counter

>>> c = make_counter()
>>> c(), c(), c()
(1, 2, 3)
```

或者用可变对象包装（无需 nonlocal）：

```python
def make_counter():
    count = [0]
    def counter():
        count[0] += 1     # 修改列表内容，不是重新赋值 count
        return count[0]
    return counter
```

搞清楚了陷阱和修复方法，现在看 Lambda 在实际代码中最高频的用法——配合 `sorted`、`map`、`filter` 等内置高阶函数，用一行表达式完成常见的数据处理任务。

---

## 6. Lambda 常见模式

### 6.1 排序 key

```python
# 按长度
sorted(words, key=lambda w: len(w))

# 按元组第二个元素
sorted(pairs, key=lambda p: p[1])

# 先按年级再按姓名
students = [("张三", 3, 85), ("李四", 2, 90)]
sorted(students, key=lambda s: (s[1], s[0]))
```

### 6.2 条件筛选 + 变换

```python
# 筛选偶数并平方
list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, range(10))))
# → [0, 4, 16, 36, 64]

# 等价列表推导（更 Pythonic）
[x*x for x in range(10) if x % 2 == 0]
```

### 6.3 Partial 函数

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube   = partial(power, exp=3)

>>> square(5), cube(5)
(25, 125)
```

`partial` 本质上就是帮你写 `lambda base: power(base, 2)`。

Lambda 在 `sorted(key=...)` 和 `map(...)` 里用起来很方便。但在环境图里，它和 `def` 有什么区别？答案是：**没有区别**。Lambda 创建的函数对象和 `def` 创建的函数对象内部结构完全相同——都有一个 parent 指针指向定义时的环境。唯一的区别是 `lambda` 没有名字。

---

## 7. 环境模型中的 Lambda

```python
# 这两个在环境图中产生的结构完全相同
f = lambda x: x + n          # 函数对象没名字，f 指向它
def f(x): return x + n       # 函数对象有名字 "f"，f 指向它
```

匿名函数在环境图中显示为 `λ(x) <line N>` 而非 `func_name(x)`。

环境模型展示了函数对象的运行时行为。在 Python 中，函数对象还携带丰富的元信息——名字、参数个数、字节码——可以在运行时检查。`def` 和 `lambda` 创建的函数的区别在这些元信息里也能看到。

---

## 8. 函数内省

函数对象携带元信息：

```python
>>> def add(x, y): return x + y
...
>>> add.__name__           # 名字
'add'
>>> add.__code__.co_varnames   # 参数名
('x', 'y')
>>> add.__code__.co_argcount   # 参数数量
2
>>> add.__code__.co_code       # 字节码（不常用）
b'|\x00|\x01\x17\x00S\x00'
```

Lambda 也有这些属性：

```python
>>> f = lambda x, y: x + y
>>> f.__name__
'<lambda>'            # lambda 没有自定义名字
>>> f.__code__.co_varnames
('x', 'y')
```

---

## 9. 例题

### 例 1：环境图追踪

<details><summary>画出下面代码的环境图</summary>

```python
y = 10
def make_f(z):
    def f(x):
        return x + y + z
    return f

f = make_f(5)
print(f(3))
```

**追踪**：
1. 全局帧：`y=10`, `make_f → func(z)`
2. `make_f(5)`：帧 F1 = `{z:5}`, 定义 `f(x)` [parent=F1]，返回 f
3. 全局帧添加：`f → func f(x) [parent=F1]`
4. `f(3)`：帧 F2 = `{x:3}`, parent→F1
5. 查找 `x`→F2, `y`→F2没有→F1没有→Global `y=10`, `z`→F2没有→F1 `z=5`
6. 返回 `3 + 10 + 5 = 18`
</details>

### 例 2：重绑定对闭包的影响

<details><summary>如果闭包创建后修改了外层变量？</summary>

```python
def make_func():
    x = 10
    def f():
        return x
    x = 20          # ← 修改了 x！
    return f

>>> g = make_func()
>>> g()
20
```

闭包捕获的是**名字绑定**，不是值的快照。`f` 的 parent 总是指向 `make_func` 的那个帧，不管 `x` 后来被改成什么。
</details>

### 例 3：sorted 多级排序

<details><summary>lambda key 实现先按分数降序、再按姓名升序</summary>

```python
students = [("张三", 85), ("李四", 90), ("王五", 85)]
sorted(students, key=lambda s: (-s[1], s[0]))
# [('李四', 90), ('张三', 85), ('王五', 85)]
```

小技巧：取负数实现降序（适用于数值）。或者 `reverse=True` + 合适的 key。
</details>

---

## 10. 常见误区

| 误区 | 纠正 |
|------|------|
| lambda 比 def 快 | 语义完全相同，执行速度一样 |
| 闭包捕获的是值的快照 | 捕获的是**名字的绑定**，指向当前值 |
| 循环中 lambda 各自独立 | 它们共享同一个 parent 帧，引用同一个变量 |
| `x = lambda ...` 不如 `def` | 当函数体是简单表达式时 lambda 更紧凑；长逻辑用 def |
| nonlocal 能跨越多层 | nonlocal 只能绑定到最近一层的非全局、非局部名字 |

---

## 本章核心概念速查

| 概念 | 说明 | 示例 |
|------|------|------|
| 帧 | 名字→值的映射 | 每个函数调用创建新帧 |
| 环境 | 帧的链表 | 局部帧 → 外层 → ... → 全局 |
| 函数 parent | 指向定义时环境的指针 | 闭包的关键 |
| `lambda` | 匿名函数表达式 | `lambda x: x + 1` |
| 闭包 | 函数 + 定义时的环境 | `make_adder(5)` 中的 `adder` |
| `nonlocal` | 声明使用外层局部变量 | `nonlocal count` |
| 默认参数求值时点 | 在定义时求值 | `lambda i=i: i` 修复循环捕获问题 |
| `functools.partial` | 部分应用 | `partial(pow, exp=2)` |
| 函数内省 | `__name__`, `__code__` | 运行时检查函数信息 |
