# Python基础 · 第二章 · 控制流

← 前置: [01 — 表达式与函数](../01-表达式与函数/notes.md)
→ 延伸: [03 — 高阶函数](../03-高阶函数/notes.md)

---

## 1. 直觉引入：程序需要「判断」

上一章的函数是一条直线——输入进来，计算，输出出去。但真实的程序需要分叉：如果用户登录了就显示主页，否则跳转登录页；如果梯度足够小就停止训练，否则继续迭代。

控制流就是程序的「决策机制」。Python 有三种基本控制结构：**条件判断**、**循环**、**函数调用**。本章重点讲前两种。

---

## 2. 布尔值与比较

### 2.1 布尔值

`bool` 类型只有两个值：`True` 和 `False`。它们来自比较运算：

```python
>>> 3 > 2
True
>>> 5 == 6
False
>>> "hello" == "hello"
True
>>> 1 + 1 == 2
True
```

比较运算符：`==` `!=` `>` `<` `>=` `<=`

> **常见错误**：`=` 是赋值，`==` 是判断相等。`if x = 5:` 是语法错误。

### 2.2 逻辑运算符

```python
# and: 两边都 True 才 True
>>> (3 > 2) and (5 > 4)    # True and True
True
>>> (3 > 2) and (5 < 4)    # True and False
False

# or: 至少一边 True 就是 True
>>> (3 < 2) or (5 > 4)     # False or True
True

# not: 取反
>>> not True
False
>>> not (3 > 5)
True
```

**短路求值**：Python 从左到右求值逻辑表达式，一旦能确定结果就停止。

```python
>>> False and (1/0)   # 不会执行 1/0，因为 False and ... 必定 False
False
>>> True or (1/0)     # 不会执行 1/0，因为 True or ... 必定 True
True
```

这很实用——你可以在 `and` 右边放「仅当左边为 True 时才安全」的操作。

**`and`/`or` 的返回值**：Python 的 `and`/`or` 不是简单地返回 `True`/`False`——它们返回**实际参与判断的操作数值**：

```python
>>> 3 and 5          # 两边都真 → 返回最后一个
5
>>> 0 and 5          # 左边假 → 短路，直接返回左边
0
>>> "" or "hello"    # 左边假 → 返回右边
'hello'
>>> "hi" or "hello"  # 左边真 → 短路，直接返回左边
'hi'
```

规则是：`and` — 左边为假返回左边，否则返回右边；`or` — 左边为真返回左边，否则返回右边。基于这个特性，可以写出简洁的默认值模式：

```python
name = user_input or "匿名用户"    # 如果 user_input 为空，用默认值
```

### 2.3 真值测试

在 `if` 和 `while` 条件中，非布尔值会自动转为布尔：

| 值 | 被视为 |
|----|--------|
| `0`, `0.0` | `False` |
| `""`, `[]`, `{}` （空容器） | `False` |
| `None` | `False` |
| 其他值 | `True` |

```python
if []:          # 空列表 → False → 不执行
    print("不会执行")
if [1, 2]:      # 非空列表 → True → 执行
    print("会执行")
```

---

## 3. if / elif / else

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"            # ← 走这条
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)  # B
```

**执行逻辑**：从上到下检查每个条件，遇到第一个 `True` 就执行对应块，然后**跳过所有后续分支**。

**关键规则**：
- 必须从 `if` 开始
- `elif` 可以有 0 个或多个
- `else` 可有可无（最多一个）
- 缩进必须一致（4 空格）

---

## 4. while 循环

```python
i = 1
while i <= 5:
    print(i)
    i = i + 1
# 输出: 1 2 3 4 5
```

**执行逻辑**：
1. 检查条件
2. 如果为 True：执行循环体 → 回到第 1 步
3. 如果为 False：跳出循环

> **无限循环陷阱**：如果条件永远为 True，程序不会停止。按 `Ctrl+C` 强制终止。

```python
# 错误示例——别运行！
while True:
    print("停不下来...")
```

**常用模式——累加**：

```python
def sum_to(n):
    """返回 1+2+...+n。"""
    total = 0
    i = 1
    while i <= n:
        total += i     # 等价于 total = total + i
        i += 1
    return total

assert sum_to(5) == 15   # 1+2+3+4+5
assert sum_to(0) == 0    # 空范围→0
```

---

## 5. for 循环

`while` 需要手动维护计数器，容易出错。遍历序列时 `for` 更简洁：

```python
for name in ["张三", "李四", "王五"]:
    print(f"Hello, {name}!")
# Hello, 张三!
# Hello, 李四!
# Hello, 王五!

for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i)
```

`range(start, stop, step)`：
- `range(5)` → 0, 1, 2, 3, 4
- `range(2, 6)` → 2, 3, 4, 5
- `range(1, 10, 2)` → 1, 3, 5, 7, 9
- `range(10, 0, -1)` → 10, 9, 8, ..., 1

---

## 6. break 与 continue

```python
# break: 立即跳出循环
for i in range(10):
    if i == 5:
        break
    print(i)
# 输出: 0 1 2 3 4

# continue: 跳过本次迭代，继续下一次
for i in range(5):
    if i == 2:
        continue
    print(i)
# 输出: 0 1 3 4
```

---

## 7. 循环的 `else` 子句

Python 的 `while`/`for` 可以带 `else`——当循环**正常结束**（没有被 `break` 中断）时执行：

```python
# 查找元素，没找到时执行 else
def find_index(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            print(f"找到了，索引 {i}")
            break
    else:                               # 只有 break 没执行才到这里
        print(f"{target} 不在列表中")

>>> find_index([1, 3, 5], 3)
找到了，索引 1
>>> find_index([1, 3, 5], 7)
7 不在列表中
```

这是一个很好的语法糖——替代了「加一个 `found` 标志位再最后检查」的笨拙写法。注意：如果循环体一次都没执行（如 `for x in []`），`else` 仍会执行（因为没有 `break` 中断）。

---

## 8. 条件表达式（三元运算符）

```python
x = "偶数" if n % 2 == 0 else "奇数"
```

这是**表达式**（返回值），不同于 `if` **语句**（只执行动作）。

---

## 9. 环境模型中的控制流

前章讲了环境模型。`if/while` 在环境模型中不创建新帧——它们只是在当前帧中按条件选择执行路径。

`while` 循环的每次迭代都在同一个局部帧中进行，变量在迭代之间保持。

---

## 10. 例题

### 例 1：FizzBuzz
打印 1 到 20，3 的倍数输出 "Fizz"，5 的倍数输出 "Buzz"，同时是 3 和 5 的倍数输出 "FizzBuzz"。

<details><summary>解</summary>

```python
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

关键：`%15` 判断要放在 `%3` 和 `%5` 之前——否则 15 会先匹配 `%3` 输出 "Fizz"。
</details>

### 例 2：最大公约数（欧几里得算法）

<details><summary>解</summary>

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

assert gcd(48, 18) == 6
assert gcd(17, 5) == 1
```
</details>

---

## 本章核心概念速查

| 概念 | 语法 |
|------|------|
| 布尔 | `True`, `False`, `and`, `or`, `not` |
| 条件 | `if ... elif ... else` |
| while | `while 条件: 循环体` |
| for | `for x in 序列:` |
| range | `range(start, stop, step)` |
| break | 跳出循环 |
| continue | 跳过本次迭代 |
