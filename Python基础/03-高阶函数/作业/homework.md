# Python基础 · 第三章 · 高阶函数 — 作业

> 完成 `homework.py`。运行 `python3 grader.py` 自动批改。

---

## Q1 ⭐ 应用函数
实现 `apply_func(f, x)`：将函数 `f` 应用到 `x`，返回 `f(x)`。

## Q2 ⭐ 创建加法器
实现 `make_adder(n)`：返回一个函数，该函数接收一个参数 `x`，返回 `x + n`。

## Q3 ⭐⭐ 条件筛选
实现 `keep_if(predicate, lst)`：返回一个新列表，只保留使 `predicate(x)` 为 `True` 的元素。保持原顺序。不允许用内置 `filter`。

## Q4 ⭐⭐ 列表变换
实现 `transform_list(f, lst)`：返回新列表，每项为 `f(x)`。不允许用内置 `map`。

## Q5 ⭐⭐ 函数组合
实现 `compose(f, g)`：返回新函数 `h`，满足 `h(x) = f(g(x))`（先 `g` 后 `f`）。

## Q6 ⭐⭐⭐ 柯里化
实现 `curry2(f)`：将双参数函数 `f(x, y)` 转化为柯里化版本。返回一个函数 `g`，使得 `g(x)(y) = f(x, y)`。

## Q7 ⭐⭐ 创建幂函数
实现 `make_power(n)`：返回一个函数，接收 `x` 返回 `x ** n`。

## Q8 ⭐⭐⭐ 重复应用
实现 `make_repeater(f, n)`：返回一个函数，将 `f` 重复应用到输入值上 `n` 次。即 n=0 返回原值，n=1 返回 f(x)，n=2 返回 f(f(x))...

## Q9 ⭐⭐ 通用累积
实现 `accumulate(combiner, base, n, term)`：通用累积函数。combiner 是二元函数，base 是初始值，n 是迭代次数，term 计算第 k 项（k=1..n）。

## Q10 ⭐⭐⭐ 合取谓词
实现 `make_and(pred1, pred2)`：返回一个新谓词函数。接收参数 `x`，当 `pred1(x)` 和 `pred2(x)` 都为 `True` 时才返回 `True`。必须短路求值（pred1 为 False 时不调用 pred2）。

## Q11 ⭐⭐ 平方映射
实现 `square_list(lst)`：返回新列表，每项为原项的平方。要求用 `transform_list` 和 `lambda` 一行代码实现。

## Q12 ⭐⭐⭐ 交替函数
实现 `make_alternator(f, g)`：返回一个函数，第一次调用执行 `f`，第二次执行 `g`，第三次又执行 `f`，依此类推。两个函数都只接收一个参数。
