# Python基础 · 第四章 · 环境图与 Lambda — 参考答案

<details><summary>Q1 — Lambda 基础</summary>

```python
square = lambda x: x * x
is_even = lambda x: x % 2 == 0
add = lambda x, y: x + y
```
**要点**：lambda 表达式直接赋值给变量名，等价于 `def square(x): return x*x`。
</details>

<details><summary>Q2 — make_multiplier</summary>

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

# 或一行的 lambda 写法
def make_multiplier(n):
    return lambda x: x * n
```
**要点**：和 make_adder 相同模式——闭包记住 `n`。
</details>

<details><summary>Q3 — sort_by_last_letter</summary>

```python
def sort_by_last_letter(words):
    return sorted(words, key=lambda w: w[-1])
```
**要点**：`key` 参数接收一个函数，提取比较用的键值。`w[-1]` 取最后一个字符。
</details>

<details><summary>Q4 — make_averager</summary>

```python
def make_averager():
    total = [0]
    count = [0]
    def averager(x):
        total[0] += x
        count[0] += 1
        return total[0] / count[0]
    return averager

# 或用 nonlocal
def make_averager():
    total = 0
    count = 0
    def averager(x):
        nonlocal total, count
        total += x
        count += 1
        return total / count
    return averager
```
**要点**：闭包维护状态。用列表包装避免了 `nonlocal`（在较旧的 Python 中也可以工作）。
</details>

<details><summary>Q5 — make_bank_account</summary>

```python
def make_bank_account(initial):
    balance = [initial]
    def action(amount):
        if amount > 0:
            balance[0] += amount
            return balance[0]
        elif amount < 0:
            if balance[0] >= -amount:
                balance[0] += amount
                return balance[0]
            else:
                return "余额不足"
        else:
            return balance[0]
    return action
```
**要点**：闭包 + 条件判断。余额用可变列表包装，在闭包中修改。
</details>

<details><summary>Q6 — curry_power</summary>

```python
def curry_power(x):
    return lambda n: x ** n
```
**要点**：柯里化（部分应用）的最简实现。先提供底数 `x`，返回的函数负责接收指数 `n` 并计算。
</details>

<details><summary>Q7 — apply_to_two</summary>

```python
apply_to_two = lambda f, a, b: f(a, b)

# 或
def apply_to_two(f, a, b):
    return f(a, b)
```
**要点**：最基础的高阶函数——函数作为参数。
</details>

<details><summary>Q8 — make_counter</summary>

```python
def make_counter(step=1):
    count = 0
    def counter():
        nonlocal count
        result = count
        count += step
        return result
    return counter
```
**要点**：用 `nonlocal` 声明 `count` 是可修改的闭包变量。返回的是**当前值**，然后累加。
</details>

<details><summary>Q9 — filter_map</summary>

```python
def filter_map(predicate, mapper, lst):
    return list(map(mapper, filter(predicate, lst)))
```
**要点**：先 `filter` 再 `map`。`filter(pred, lst)` 是惰性的（iterator），`map` 也是，所以需要 `list()` 强制求值。
</details>

<details><summary>Q10 — decode_lambda</summary>

```python
def decode_lambda():
    return 8
```
**要点**：`f = lambda x: (lambda y: x + y)`，`f(3)` 返回 `lambda y: 3 + y`，再 `(5)` → `3 + 5 = 8`。嵌套 lambda 等价于嵌套 def。
</details>

<details><summary>Q11 — make_greeting</summary>

```python
def make_greeting(greeting):
    return lambda name: f"{greeting}, {name}!"
```
**要点**：lambda 作为返回值，「记住」greeting，运行时接收 name 拼接。
</details>

<details><summary>Q12 — make_timer</summary>

```python
import time

def make_timer():
    start = [time.time()]
    def elapsed():
        return time.time() - start[0]
    return elapsed
```
**要点**：闭包捕获起始时间。用列表包装避免 `nonlocal`。每次调用用当前时间减起始时间得到经过的秒数。
</details>
