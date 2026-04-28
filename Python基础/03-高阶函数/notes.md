# Python基础 · 第三章 · 高阶函数

← 前置: [02 — 控制流](../02-控制流/notes.md)
→ 延伸: [04 — 环境图与 Lambda](../04-环境图与Lambda/notes.md)

---

## 1. 直觉引入：函数也是数据

第二章我们写了很多函数——`sign`、`gcd`、`is_prime`——然后调用它们。这是函数的「动词」用法：定义好，然后执行。

但函数在 Python 中还有另一种身份：**它们是值**。和 `3`、`"hello"`、`[1,2,3]` 一样，函数可以被赋值给变量、放进列表、作为参数传递、甚至作为返回值。

```python
>>> def greet(name):
...     return f"Hello, {name}!"
...
>>> f = greet          # 把函数赋值给变量（注意：不是调用，没有括号）
>>> f("World")         # 通过新名字调用
'Hello, World!'
>>> type(f)
<class 'function'>     # 函数也是一种类型！
```

这个看似简单的特性，开启了整个**高阶函数**的世界——函数可以操作函数。

**为什么重要？** 高阶函数是抽象的核心工具。`sum_to` 把「累加」抽象成参数 n；高阶函数把**计算模式**抽象成参数 f。它让你写出更通用、更简洁的代码。

---

## 2. 函数作为参数

把函数作为参数传给另一个函数，可以抽取出通用的计算模式。

### 2.1 求和 vs 求积 vs 求立方和

```python
def sum_integers(n):
    """1 + 2 + ... + n"""
    total, k = 0, 1
    while k <= n:
        total += k
        k += 1
    return total

def sum_cubes(n):
    """1³ + 2³ + ... + n³"""
    total, k = 0, 1
    while k <= n:
        total += k ** 3
        k += 1
    return total

def sum_pi_terms(n):
    """1/(1×3) + 1/(5×7) + 1/(9×11) + ..."""
    total, k = 0, 1
    while k <= n:
        total += 1 / (k * (k + 2))
        k += 4
    return total
```

三个函数的结构完全相同——变化的只是**每一项的值**。我们可以把「每一项」抽成参数：

```python
def summation(n, term):
    """通用求和：Σ term(k) for k=1..n"""
    total, k = 0, 1
    while k <= n:
        total += term(k)    # ← 调用传入的 term 函数
        k += 1
    return total

# 重新表达上面的三个函数
def identity(x):  return x
def cube(x):      return x ** 3

sum_integers  = lambda n: summation(n, identity)
sum_cubes     = lambda n: summation(n, cube)
```

### 2.2 通用迭代模式

遍历列表做某事的模式也可以抽离：

```python
def apply_to_each(f, lst):
    """对 lst 每个元素执行 f，返回新列表"""
    result = []
    for item in lst:
        result.append(f(item))
    return result

>>> apply_to_each(abs, [-3, 5, -2, 0])
[3, 5, 2, 0]
>>> apply_to_each(str.upper, ["hello", "world"])
['HELLO', 'WORLD']
```

### 2.3 条件筛选

```python
def keep_if(predicate, lst):
    """保留使 predicate 为 True 的元素"""
    return [x for x in lst if predicate(x)]

>>> keep_if(lambda x: x > 0, [-3, 5, -2, 0, 7])
[5, 7]
```

---

## 3. 函数作为返回值

把函数作为参数，相当于告诉函数「这一步你按这个规则来」。但有时你需要的不是一次性的规则，而是一个**可复用的定制工具**——比如创建一个「加 5」函数，之后在十个地方调用它，而不是每次都写 `lambda x: x + 5`。这就是函数作为返回值：外层函数像工厂，每次调用生产一个专门化的小函数。

### 3.1 make_adder

```python
def make_adder(n):
    """返回一个函数：该函数接收 x，返回 x + n"""
    def adder(x):
        return x + n
    return adder

>>> add_5 = make_adder(5)
>>> add_5(10)
15
>>> add_5(100)
105
>>> add_3 = make_adder(3)
>>> add_3(10)
13
```

这里 `adder` 是在 `make_adder` 内部定义的函数。`make_adder` 返回后，`adder` 仍然「记得」它被创建时的环境——包括 `n = 5`。这种机制叫**闭包**（closure）。

### 3.2 闭包：函数 + 它诞生的环境

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor     # factor 来自外层函数
    return multiply

>>> double = make_multiplier(2)
>>> triple = make_multiplier(3)
>>> double(7), triple(7)
(14, 21)
```

关键洞察：每次调用 `make_multiplier` 都创建一个**新的局部帧**，`factor` 在那个帧里被绑定到不同的值。`multiply` 函数携带了对创建时那个帧的引用——所以 `double` 里的 `factor=2`，`triple` 里的 `factor=3`。

> 闭包 = 函数体 + 定义时所在的环境（而不是调用时的环境）。第四章会用环境图详细可视化这个过程。

`make_adder(n)` 把「加 n」这个双参数操作变成了一个单参数函数的工厂。这个模式可以推广：**任何多参数函数都可以改写成一系列单参数函数**——传一个参数，返回一个等下一个参数的函数。这就是柯里化。

---

## 4. 柯里化（Currying）

柯里化：把「接受多个参数的函数」转化为「一系列只接受一个参数的函数」的嵌套。

```python
# 普通写法：两个参数
def add(x, y):
    return x + y

# 柯里化写法：返回函数的函数
def curried_add(x):
    def inner(y):
        return x + y
    return inner

>>> curried_add(3)(5)    # 注意调用方式
8

>>> add_3 = curried_add(3)   # 先「部分应用」一个参数
>>> add_3(5), add_3(10)
(8, 13)
```

柯里化的价值：**部分应用**——先传一部分参数，得到一个更具体的新函数，再传给其他函数。

```python
# 通用柯里化（双参数）
def curry2(f):
    """将 f(x, y) 转化为 g(x)(y)"""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

# 反柯里化
def uncurry2(g):
    """将 g(x)(y) 转化回 f(x, y)"""
    def f(x, y):
        return g(x)(y)
    return f
```

```python
# 实际应用：用 curried_add 配合 map
>>> from operator import add
>>> list(map(curried_add(3), [1, 2, 3]))
[4, 5, 6]
```

---

## 5. 函数组合

柯里化把**一个**多参函数拆成单参链。另一个方向同样重要：把**多个**不同的函数串成一条流水线——第一个函数的输出变成第二个函数的输入。这就是函数组合，数学里写成 $f \circ g$。

```python
def compose(f, g):
    """返回复合函数 h(x) = f(g(x))"""
    def h(x):
        return f(g(x))
    return h

>>> square = lambda x: x * x
>>> add_one = lambda x: x + 1
>>> add_one_then_square = compose(square, add_one)
>>> add_one_then_square(3)     # square(add_one(3)) = (3+1)² = 16
16
>>> square_then_add_one = compose(add_one, square)
>>> square_then_add_one(3)     # add_one(square(3)) = 9+1 = 10
10
```

注意顺序！`compose(f, g)` 是先 `g` 后 `f`（从右向左），和数学记号 $f \circ g$ 一致。

组合是把**不同**函数串起来。有一个特殊情况：把**同一个**函数重复应用多次——$f(f(f(x)))$，也就是函数幂。

---

## 6. 多次应用

```python
def make_repeater(f, n):
    """返回一个函数：将 f 重复应用 n 次"""
    def repeater(x):
        result = x
        for _ in range(n):
            result = f(result)
        return result
    return repeater

>>> triple = lambda x: 3 * x
>>> thrice = make_repeater(triple, 3)
>>> thrice(1)     # 3 * (3 * (3 * 1)) = 27
27
```

这其实是一种**函数幂**：`repeater(x) = f(f(...f(x)...))`（共 n 次）。

从 `summation` 到 `make_repeater`，我们一直在做同一件事：写一个函数，接收一个函数，返回一个增强版的函数。Python 为这个模式提供了专门的语法糖——装饰器。它让你不用在调用处手动包装函数，而是直接在定义处声明「这个函数要用这个包装器」。

---

## 7. 装饰器（入门）

```python
def trace(f):
    """每次调用 f 时打印参数和返回值"""
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print(f"{f.__name__}({args}) -> {result}")
        return result
    return wrapper

@trace                     # 等价于 factorial = trace(factorial)
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

>>> factorial(5)
factorial((1,)) -> 1
factorial((2,)) -> 2
factorial((3,)) -> 6
factorial((4,)) -> 24
factorial((5,)) -> 120
120
```

`@trace` 语法只是语法糖——上面等价于 `factorial = trace(factorial)`。

更多装饰器的高级用法（带参数的装饰器、类装饰器）将在后续章节展开。

本章大量使用了 `lambda` 作为高阶函数的参数。`lambda` 只能包含一个表达式，不能包含 `if` 语句——这时第一章 §6 和第二章 §8 的条件表达式就成了必需品。这里快速回顾并展示它在高阶函数中的典型用法。

---

## 8. 条件表达式回顾

高阶函数常配合条件表达式使用——简洁的函数体中可以一行写完逻辑：

```python
# 条件表达式写法
is_even = lambda x: True if x % 2 == 0 else False
# 更简洁的等效写法
is_even = lambda x: x % 2 == 0

# 在高阶函数中使用
>>> list(filter(lambda x: x % 2 == 0, range(10)))
[0, 2, 4, 6, 8]
```

---

## 9. 例题

### 例 1：通用累乘

<details><summary>用高阶函数抽象累乘模式</summary>

```python
def product(n, term):
    """Π term(k) for k=1..n"""
    result, k = 1, 1
    while k <= n:
        result *= term(k)
        k += 1
    return result

def factorial(n):
    return product(n, lambda x: x)

assert factorial(5) == 120
assert product(3, lambda x: x**2) == 1 * 4 * 9  # = 36
```
</details>

### 例 2：accumulate — 终极抽象

<details><summary>进一步抽象：只需要初始值、组合方式、序列</summary>

```python
def accumulate(combiner, base, n, term):
    """通用累积：从 base 开始，对 term(1)..term(n) 依次用 combiner 合并"""
    result, k = base, 1
    while k <= n:
        result = combiner(result, term(k))
        k += 1
    return result

def sum_to(n):
    return accumulate(lambda x, y: x + y, 0, n, lambda x: x)

def factorial(n):
    return accumulate(lambda x, y: x * y, 1, n, lambda x: x)

assert sum_to(5) == 15
assert factorial(5) == 120
```

`accumulate` 是求和、求积、求阶乘等无数操作的统一抽象。这正是高阶函数的力量——用一个函数表达一整类计算。
</details>

### 例 3：部分柯里化实战

<details><summary>用柯里化简化 map 调用</summary>

```python
def curried_pow(n):
    def f(x):
        return x ** n
    return f

# 对列表每个元素求平方、立方
>>> list(map(curried_pow(2), [1, 2, 3, 4]))
[1, 4, 9, 16]
>>> list(map(curried_pow(3), [1, 2, 3, 4]))
[1, 8, 27, 64]
```
</details>

---

## 10. 常见误区

| 误区 | 纠正 |
|------|------|
| `f` 和 `f()` 混淆 | `f` 是函数本身（值）；`f()` 是调用函数（求值） |
| 闭包捕获的是引用还是值？ | 捕获的是**名字绑定**，指向同一个对象。如果闭包内修改可变对象，外部也受影响 |
| 认为 `lambda` 比 `def` 更高效 | 语法不同，语义完全等价——编译后是同一种对象 |
| 递归 + 高阶函数 = 无穷抽象 | 过度抽象会降低可读性。如果一个模式只用两次，不一定需要抽成高阶函数 |

### 闭包陷阱

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)    # 所有 lambda 引用的是同一个 i！

>>> [f() for f in funcs]
[2, 2, 2]    # 不是 [0, 1, 2]！

# 修复：捕获当前值
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)   # 默认参数在定义时求值

>>> [f() for f in funcs]
[0, 1, 2]
```

---

## 本章核心概念速查

| 概念 | 说明 | 示例 |
|------|------|------|
| 函数是一等对象 | 可赋值、传参、返回 | `f = abs; f(-3)` |
| 高阶函数 | 接收/返回函数的函数 | `apply_to_each(abs, lst)` |
| 闭包 | 函数 + 定义时所在的环境 | `make_adder(5)` 中的 `adder` |
| 柯里化 | 多参→单参链 | `curried_add(3)(5)` |
| 函数组合 | $f \circ g$ | `compose(f, g)(x) = f(g(x))` |
| 装饰器 | 包装函数的函数 | `@trace` |
| `lambda` | 匿名函数表达式 | `lambda x: x + 1` |
| 部分应用 | 先固定部分参数 | `add_5 = curried_add(5)` |
| `map` | 对序列每项应用函数 | `map(f, iterable)` |
| `filter` | 用谓词筛选序列 | `filter(pred, iterable)` |
