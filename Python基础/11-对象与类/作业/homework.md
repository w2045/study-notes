# Python基础 · 第十一章 · 对象与类 — 作业

> 完成 `homework.py`。运行 `python3 grader.py` 自动批改。

---

## Q1 ⭐ 创建类
实现 `Rectangle` 类。`__init__(self, width, height)`，方法 `area` 返回面积，`perimeter` 返回周长。

## Q2 ⭐ Counter 类
实现 `Counter` 类。`__init__(self)` → count=0，`inc()` 自增返回新值，`reset()` 归零，`get()` 返回当前值。

## Q3 ⭐⭐ 向量类
实现 `Vector` 类。`__init__(self, x, y)`，`__add__` 向量加法，`__eq__` 相等判断，`__repr__` 返回 `"Vector(x, y)"`。

## Q4 ⭐⭐ Student 类
实现 `Student` 类。`__init__(self, name, scores)` — scores 是分数列表。方法 `average()` 返回平均分，`grade()` 返回等级：≥90→A，≥80→B，≥70→C，≥60→D，<60→F。`__str__` 返回 `"name (avg)"`（保留一位小数）。

## Q5 ⭐⭐ 银行账户
实现 `BankAccount` 类。`__init__(self, owner, balance=0)`。`deposit(amount)` 存款，`withdraw(amount)` 取款（超额抛 `ValueError("余额不足")`），`__str__` 返回 `"owner: balance"`。

## Q6 ⭐⭐⭐ Fraction 类
实现 `Fraction` 类。`__init__(self, num, den=1)` 自动约分化简。`__add__`、`__mul__`、`__eq__`、`__repr__`（返回 `"Fraction(num, den)"`）。

## Q7 ⭐⭐ 温度类
实现 `Temperature` 类。`__init__(self, celsius)`，`@property fahrenheit`（华氏度 = celsius*9/5+32），`@fahrenheit.setter`。

## Q8 ⭐⭐⭐ 复数类
实现 `Complex` 类。`__init__(self, real, imag)`，`__add__`，`__sub__`，`__mul__`，`__eq__`，`__repr__`（返回 `"Complex(real, imag)"`）。

## Q9 ⭐⭐ 计时器
实现 `Timer` 类。`__init__` 记录起始时间（`time.time()`），`elapsed()` 返回从起始到现在经过的秒数，`reset()` 重置起始时间为现在。

## Q10 ⭐⭐⭐ TodoList 类
实现 `TodoList` 类。`add(task)` 添加任务，`remove(task)` 删除（不存在直接忽略），`list_all()` 返回所有任务列表，`clear()` 清空，`__len__` 返回任务数。

## Q11 ⭐⭐ @classmethod
实现 `Person` 类。`__init__(self, name, age)`。`@classmethod from_birth_year(cls, name, year)` 用当前年（用 `2026`）减去年份得到年龄，调用 `cls(name, age)` 创建实例。`__str__` 返回 `"name, age"`。

## Q12 ⭐⭐⭐ @property 面积
实现 `Circle` 类。`__init__(self, radius)`。`@property radius`、`@radius.setter`（禁止负数）。`@property area`（返回 π*r²，π 用 3.14159）。`@property circumference`（返回 2*π*r）。
