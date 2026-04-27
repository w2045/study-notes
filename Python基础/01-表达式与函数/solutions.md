# 第一章 · 表达式与函数 — 参考答案

> ⚠️ 先自己尝试完成，实在做不出来再看答案。

---

## Q1 — 华氏度转摄氏

<details><summary>点击查看答案</summary>

```python
def f_to_c(f: float) -> float:
    return round((f - 32) * 5 / 9, 1)
```

**要点**: 公式不要写反。常见错误是写成了 `f * 9/5 + 32`（那是 C→F）。
</details>

---

## Q2 — 判断偶数

<details><summary>点击查看答案</summary>

```python
def is_even(n: int) -> bool:
    return n % 2 == 0
```

**要点**: 负数也能用 `%`。`-2 % 2 == 0` 也是 `True`。
</details>

---

## Q3 — 球体积

<details><summary>点击查看答案</summary>

```python
def sphere_volume(r: float) -> float:
    return (4 / 3) * math.pi * (r ** 3)
```

**要点**: 注意 `4/3` 会得到 `1.333...`（浮点），如果是 `4//3` 会得到 `1`（错误）。
</details>

---

## Q4 — 三个数的中间值

<details><summary>点击查看答案</summary>

一种解：利用「中间值 = 总和 - 最大值 - 最小值」：

```python
def middle(a: float, b: float, c: float) -> float:
    return a + b + c - max(a, b, c) - min(a, b, c)
```

纯比较写法：

```python
def middle(a: float, b: float, c: float) -> float:
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c
```
</details>

---

## Q5 — 编写 doctest

<details><summary>点击查看答案</summary>

```python
def add_and_double(a: float, b: float) -> float:
    """返回 a + b 的两倍。

    >>> add_and_double(2, 3)
    10
    >>> add_and_double(0, 5)
    10
    >>> add_and_double(-1, 1)
    0
    >>> add_and_double(-2, -3)
    -10
    """
    return 2 * (a + b)
```

**要点**: 正常值、零、负数、负数+负数都要覆盖。
</details>

---

## Q6 — 自由落体时间

<details><summary>点击查看答案</summary>

```python
def fall_time(h: float) -> float:
    g = 9.8
    t = math.sqrt(2 * h / g)
    return round(t, 2)
```

**推导**: $h = \frac{1}{2}gt^2$ → $t^2 = \frac{2h}{g}$ → $t = \sqrt{\frac{2h}{g}}$
</details>

---

## Q7 — 判断三角形

<details><summary>点击查看答案</summary>

```python
def is_triangle(a: float, b: float, c: float) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)
```

**要点**: 三条都要检查。别忘记边长必须为正——如果边长为 0 或负，`a + b > c` 不成立。
</details>

---

## Q8 — 数字反转

<details><summary>点击查看答案</summary>

```python
def reverse_digits(n: int) -> int:
    tens = n // 10
    ones = n % 10
    return ones * 10 + tens
```

**要点**: `37 // 10 = 3`, `37 % 10 = 7`。交换后是 `7 * 10 + 3 = 73`。对于 `90`，结果是 `0 * 10 + 9 = 9`（自动去掉了前导零）。
</details>

---

## Q9 — 距离公式

<details><summary>点击查看答案</summary>

```python
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
```
</details>

---

## Q10 — 找 bug

<details><summary>点击查看答案</summary>

原代码：
```python
def square_of_sum(a, b):
    return a + b ** 2   # 实际上在算 a + b²
```

修复后：
```python
def square_of_sum(a: float, b: float) -> float:
    return (a + b) ** 2
```

**根源**: `**` 的优先级高于 `+`，所以 `a + b ** 2` 被解析为 `a + (b ** 2)`。加括号强制先算加法。
</details>

---

## Q11 — 四舍五入

<details><summary>点击查看答案</summary>

```python
def round_to(n: float, decimals: int) -> float:
    shift = 10 ** decimals
    return int(n * shift + 0.5) / shift
```

**原理**: 以 `3.14159` 到 2 位小数为例：
1. `3.14159 * 100 = 314.159`
2. `314.159 + 0.5 = 314.659`
3. `int(314.659) = 314`
4. `314 / 100 = 3.14`

> **注意**: 这种实现对负数处理有瑕疵（`int(-2.5)` → `-2`）。如需正确处理负数，用 `math.floor` 或直接调内置 `round`。本题主要帮助理解原理。
</details>

---

## Q12 — 二次方程求根

<details><summary>点击查看答案</summary>

```python
def solve_quadratic(a: float, b: float, c: float):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return None
    elif delta == 0:
        root = -b / (2 * a)
        return (root, root)
    else:
        sqrt_delta = math.sqrt(delta)
        root1 = (-b - sqrt_delta) / (2 * a)
        root2 = (-b + sqrt_delta) / (2 * a)
        # 从小到大排序
        return (min(root1, root2), max(root1, root2))
```

**要点**:
- `delta == 0` 用浮点数直接比较不安全。更好的写法是 `abs(delta) < 1e-9`
- 返回的是 `tuple`，不是 `list`
- 两个根需要排序（从小到大）
- 无解时返回 `None`（注意不是字符串 `"None"`）
</details>
