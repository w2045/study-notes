# Python基础 · 第四章 · 环境图与 Lambda — 作业

> 完成 `homework.py`。运行 `python3 grader.py` 自动批改。

---

## Q1 ⭐ Lambda 基础
用 `lambda` 实现 `square`、`is_even`、`add`（两个数相加），每条一句 lambda 赋值。

## Q2 ⭐ 创建乘法器
实现 `make_multiplier(n)`：返回一个函数，接收 `x` 返回 `x * n`。

## Q3 ⭐⭐ Lambda 排序
实现 `sort_by_last_letter(words)`：接收字符串列表，按每个单词的**最后一个字母**排序后返回新列表。用 `sorted` + `lambda`。

## Q4 ⭐⭐ 创建平均值器
实现 `make_averager()`：返回一个函数。每次调用传入一个新数字，返回**到目前为止所有传入数字的平均值**。提示：需要闭包维护 count 和 total（用可变对象或 nonlocal）。

## Q5 ⭐⭐⭐ 银行账户
实现 `make_bank_account(initial)`：返回一个函数 `action(amount)`。
- `amount > 0`：存款（余额增加），返回新余额
- `amount < 0`：取款，如果余额足够则扣除并返回新余额；如果余额不足，不扣款并返回字符串 `"余额不足"`
- `amount == 0`：返回当前余额

## Q6 ⭐⭐ 柯里化幂函数
实现 `curry_power(x)`：返回一个函数 `f(n)` 使得 `f(n) = x ** n`（一行的 lambda 写法）。

## Q7 ⭐⭐ 两数应用
实现 `apply_to_two(f, a, b)`：将双参数函数 `f` 应用到 `(a, b)` 返回 `f(a, b)`。只用一行 lambda 实现（即使它是 trivial）。

## Q8 ⭐⭐⭐ 计数器工厂
实现 `make_counter(step=1)`：返回一个计数器函数。每次调用返回计数（从 0 开始，每次 +step）。例如 `step=2` 输出 `0, 2, 4, 6...`。用 nonlocal 实现。

## Q9 ⭐⭐ 筛选后变换
实现 `filter_map(predicate, mapper, lst)`：先筛选（保留 predicate 为 True 的），再对筛选结果应用 mapper。一行，用 `map`、`filter` 和 `lambda` 组合。

## Q10 ⭐⭐⭐ 嵌套 Lambda 解码
写出下面表达式对应的普通函数定义：
```python
f = lambda x: (lambda y: x + y)
```
实现 `decode_lambda()`：返回 `f(3)(5)` 的值（即 8）。

## Q11 ⭐⭐ Lambda 问候语
实现 `make_greeting(greeting)`：返回一个 lambda，接收 `name` 返回 `f"{greeting}, {name}!"`。

## Q12 ⭐⭐⭐ 闭包计时器
实现 `make_timer()`：返回一个函数。第一次调用开始计时（记录当前时间），之后每次调用返回**自开始以来经过的秒数**（浮点数）。用 `time.time()`。
