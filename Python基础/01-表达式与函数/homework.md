# 第一章 · 表达式与函数 — 作业

> 完成 `homework.py` 中对应的函数。完成后运行 `python3 grader.py` 自动批改。
> 题目前面的 ⭐ 代表难度：⭐ 基础 | ⭐⭐ 中等 | ⭐⭐⭐ 挑战

---

## Q1 ⭐ 华氏度转摄氏度

实现函数 `f_to_c(f)`，将华氏温度转为摄氏温度，四舍五入到 1 位小数。

$$C = \frac{5}{9}(F - 32)$$

```python
f_to_c(32)   → 0.0
f_to_c(212)  → 100.0
f_to_c(98.6) → 37.0
```

**文件位置**: `homework.py` → `f_to_c`

---

## Q2 ⭐ 判断偶数

实现函数 `is_even(n)`，判断整数 `n` 是否为偶数。提示：使用取余运算 `%`。

```python
is_even(4)  → True
is_even(7)  → False
is_even(0)  → True
is_even(-2) → True
```

---

## Q3 ⭐ 计算球体积

实现函数 `sphere_volume(r)`，返回半径为 `r` 的球的体积。

$$V = \frac{4}{3}\pi r^3$$

`math.pi` 已导入，直接用。

```python
sphere_volume(1)  → 4.1887...  (约)
sphere_volume(3)  → 113.097...
```

---

## Q4 ⭐⭐ 三个数的中间值

实现函数 `middle(a, b, c)`，返回三个数中大小居中的那个（不是平均数，不是中位数 index）。

```python
middle(1, 2, 3)    → 2
middle(5, 1, 9)    → 5
middle(3, 3, 1)    → 3
middle(7, 7, 7)    → 7
```

**限制**: 不允许使用 `list.sort()` 或 `sorted()`。用比较运算和条件表达式。

---

## Q5 ⭐⭐ 编写 doctest

在 `homework.py` 的 `add_and_double` 函数中，它已有实现但**缺少 doctest**。添加至少 3 个 doctest（包括边界情况），确保覆盖正常情况和边界 `0`。

---

## Q6 ⭐⭐ 自由落体时间

自由落体从静止开始，下落距离 $h$（米）与时间 $t$（秒）的关系：

$$h = \frac{1}{2}gt^2$$

其中 $g = 9.8 \text{ m/s}^2$。实现函数 `fall_time(h)`，给定下落距离 `h`，计算下落时间 `t`。四舍五入到 2 位小数。假设 $h \geq 0$。

```python
fall_time(0)     → 0.0
fall_time(4.9)   → 1.0
fall_time(19.6)  → 2.0
```

---

## Q7 ⭐⭐ 判断三角形

三边长 `a, b, c` 能构成三角形当且仅当任意两边之和大于第三边。实现 `is_triangle(a, b, c)`。

```python
is_triangle(3, 4, 5)  → True
is_triangle(1, 1, 3)  → False
is_triangle(5, 5, 5)  → True
is_triangle(0, 4, 5)  → False
```

---

## Q8 ⭐⭐ 数字反转

实现函数 `reverse_digits(n)`，反转一个**两位正整数**的数字顺序。

```python
reverse_digits(37)  → 73
reverse_digits(90)  → 9    # 注意：不是 "09"
reverse_digits(10)  → 1
```

提示：`//` 取十位，`%` 取个位。

---

## Q9 ⭐⭐ 距离公式

实现函数 `distance(x1, y1, x2, y2)`，返回两点 $(x_1, y_1)$ 和 $(x_2, y_2)$ 之间的欧氏距离。

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

```python
distance(0, 0, 3, 4)  → 5.0
distance(1, 2, 4, 6)  → 5.0
distance(0, 0, 0, 0)  → 0.0
```

---

## Q10 ⭐⭐ 调试：找 bug

下面的函数本意是计算 $(a+b)^2$，但有 bug。在 `homework.py` 中修复它。

```python
def square_of_sum(a, b):
    return a + b ** 2   # BUG: 平方只作用在 b 上
```

预期：

```python
square_of_sum(2, 3)  → 25   # (2+3)^2 = 25
square_of_sum(1, 4)  → 25   # (1+4)^2 = 25
square_of_sum(0, 5)  → 25   # (0+5)^2 = 25
```

---

## Q11 ⭐⭐ 四舍五入到指定小数位

实现函数 `round_to(n, decimals)`，将浮点数 `n` 四舍五入到 `decimals` 位小数。**不允许使用内置 `round` 函数**。

提示：乘以 $10^d$ → `int()` 截断 → 加 0.5 做四舍五入 → 除回 $10^d$。

```python
round_to(3.14159, 2)  → 3.14
round_to(3.14159, 4)  → 3.1416
round_to(2.5, 0)      → 3.0     # 0 位小数 = 四舍五入到整数
```

---

## Q12 ⭐⭐⭐ 综合：二次方程求根

对于二次方程 $ax^2 + bx + c = 0$（$a \neq 0$），判别式 $\Delta = b^2 - 4ac$。

- 如果 $\Delta > 0$：有两个不同实根 $x = \frac{-b \pm \sqrt{\Delta}}{2a}$
- 如果 $\Delta = 0$：有一个重根 $x = \frac{-b}{2a}$
- 如果 $\Delta < 0$：无实根，返回 `None`

实现函数 `solve_quadratic(a, b, c)`。返回格式为 `(root1, root2)`，两个根**从小到大排序**。重根时返回 `(root, root)`。

```python
solve_quadratic(1, -3, 2)   → (1.0, 2.0)      # x²-3x+2=0
solve_quadratic(1, -2, 1)   → (1.0, 1.0)      # x²-2x+1=0 重根
solve_quadratic(1, 0, 1)    → None             # x²+1=0 无实根
solve_quadratic(2, 5, -3)   → (-3.0, 0.5)     # 从小到大排序
```

---

## 提交检查清单

- [ ] 所有函数已实现
- [ ] `python3 grader.py` 全部通过
- [ ] `python3 -m doctest homework.py -v` 无失败（Q5 检验）
