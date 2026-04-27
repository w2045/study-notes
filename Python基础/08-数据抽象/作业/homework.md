# Python基础 · 第八章 · 数据抽象 — 作业

> 完成 `homework.py`。运行 `python3 grader.py` 自动批改。

---

## Q1 ⭐ 有理数构造器
实现 `make_rational(numer, denom)` 返回一个有理数（用列表 `[numer, denom]` 表示）。

## Q2 ⭐ 有理数选择器
实现 `numer(r)` 和 `denom(r)`。例如 `r = make_rational(3, 4)`，`numer(r) == 3, denom(r) == 4`。

## Q3 ⭐⭐ 有理数化简
重新实现 `make_rational_simplified(numer, denom)`：构造时用 `math.gcd` 自动约分到最简。

## Q4 ⭐⭐ 有理数乘法
实现 `mul_rational(r1, r2)` 返回两个有理数的乘积（新有理数）。**必须用 numer/denom 接口，不能直接取列表元素**。

## Q5 ⭐⭐⭐ 树构造器与选择器
实现 `tree(label, branches)`（构造器）、`label(t)`、`branches(t)`、`is_leaf(t)`。树用列表 `[label, [branch...]]` 表示。

## Q6 ⭐⭐ 统计叶子
实现 `count_leaves(t)`：返回树的叶子节点数。叶子是没有分支的节点。**必须用树接口函数**。

## Q7 ⭐⭐⭐ 树总和
实现 `tree_sum(t)`：返回树所有标签的**总和**（所有节点）。**必须用树接口函数**。

## Q8 ⭐⭐⭐ 树映射
实现 `tree_map(f, t)`：对 t 的每个标签应用 `f`，返回新树（结构相同，标签变换）。

## Q9 ⭐⭐ 闭包有理数
实现 `make_rational_closure(numer, denom)`：用**闭包**（返回函数）而非列表实现有理数。同时实现对应的 `numer_closure(r)` 和 `denom_closure(r)` 选择器。

## Q10 ⭐⭐⭐ cons/car/cdr
实现 `cons(a, b)`（返回闭包）、`car(p)`、`cdr(p)`。例如 `car(cons(1, 2)) == 1`，`cdr(cons(1, 2)) == 2`。

## Q11 ⭐⭐ 有理数加法
实现 `add_rational(r1, r2)` 返回两个有理数的和。**用接口函数**。

## Q12 ⭐⭐⭐ 最大标签路径
实现 `max_label_path(t)`：返回从根到叶子路径上标签之和的最大值。例如树 `[3, [[1], [5]]]` → 根到 1 的路径和为 3+1=4，根到 5 的为 3+5=8，返回 8。
