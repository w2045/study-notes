# Python基础 · 第三章 · 高阶函数 — 参考答案

<details><summary>Q1 — apply_func</summary>

```python
def apply_func(f, x):
    return f(x)
```
**要点**：高阶函数的最简形式——函数作为参数传入并调用。
</details>

<details><summary>Q2 — make_adder</summary>

```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder
```
**要点**：函数作为返回值的经典例子。`adder` 是闭包——它记住了创建时的 `n`。
</details>

<details><summary>Q3 — keep_if</summary>

```python
def keep_if(predicate, lst):
    result = []
    for x in lst:
        if predicate(x):
            result.append(x)
    return result
```
**要点**：手动实现 filter 的逻辑。用 for 循环 + if 判断，保持原顺序。
</details>

<details><summary>Q4 — transform_list</summary>

```python
def transform_list(f, lst):
    result = []
    for x in lst:
        result.append(f(x))
    return result
```
**要点**：手动实现 map 的逻辑。和 keep_if 结构相同，区别在于每项都保留（不筛选），但经过了 f 变换。
</details>

<details><summary>Q5 — compose</summary>

```python
def compose(f, g):
    def h(x):
        return f(g(x))
    return h
```
**要点**：`compose(f, g)(x)` = `f(g(x))`。注意顺序——先执行 g，结果再传给 f。
</details>

<details><summary>Q6 — curry2</summary>

```python
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
```
**要点**：两层嵌套——外层接收 x 返回函数，内层接收 y 才真正计算 f(x, y)。`curry2(f)(x)(y)` 等价于 `f(x, y)`。
</details>

<details><summary>Q7 — make_power</summary>

```python
def make_power(n):
    def power(x):
        return x ** n
    return power
```
**要点**：和 make_adder 同模式——用闭包「记住」指数 n。
</details>

<details><summary>Q8 — make_repeater</summary>

```python
def make_repeater(f, n):
    def repeater(x):
        result = x
        for _ in range(n):
            result = f(result)
        return result
    return repeater
```
**要点**：将 f 在 x 上重复应用 n 次。n=0 时循环不执行，直接返回原值。
</details>

<details><summary>Q9 — accumulate</summary>

```python
def accumulate(combiner, base, n, term):
    result = base
    k = 1
    while k <= n:
        result = combiner(result, term(k))
        k += 1
    return result
```
**要点**：summation 和 product 的统一抽象。`base` 是单位元（加法为 0，乘法为 1），`combiner` 是二元运算。
</details>

<details><summary>Q10 — make_and</summary>

```python
def make_and(pred1, pred2):
    def combined(x):
        if not pred1(x):
            return False
        return pred2(x)
    return combined
```
**要点**：短路求值——先 `pred1(x)`，为 False 则直接返回 False，不调用 `pred2(x)`。等价写法：`return pred1(x) and pred2(x)`（Python 的 `and` 本身短路）。

```python
def make_and(pred1, pred2):
    def combined(x):
        return pred1(x) and pred2(x)
    return combined
```
</details>

<details><summary>Q11 — square_list</summary>

```python
def square_list(lst):
    return transform_list(lambda x: x * x, lst)
```
**要点**：利用已实现的 `transform_list` 搭配匿名函数。一行代码完成。
</details>

<details><summary>Q12 — make_alternator</summary>

```python
def make_alternator(f, g):
    use_f = [True]     # 用列表包装，让内层函数可以修改
    def alternator(x):
        if use_f[0]:
            use_f[0] = False
            return f(x)
        else:
            use_f[0] = True
            return g(x)
    return alternator
```
**要点**：闭包 + 可变状态。用列表包装布尔标志，因为内层函数赋值 `use_f = False` 会创建新的局部变量。也可以用 `nonlocal`：

```python
def make_alternator(f, g):
    toggle = True
    def alternator(x):
        nonlocal toggle
        if toggle:
            toggle = False
            return f(x)
        else:
            toggle = True
            return g(x)
    return alternator
```
</details>
