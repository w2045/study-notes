# Python基础 · 第十二章 · 继承 — 作业

> 完成 `homework.py`。运行 `python3 grader.py` 自动批改。

---

## Q1 ⭐ 基本继承
实现 `Animal` 基类：`__init__(self, name)`，方法 `speak()` 返回 `"..."`。实现 `Dog(Animal)` 子类：`speak()` 返回 `"woof"`。实现 `Cat(Animal)` 子类：`speak()` 返回 `"meow"`。

## Q2 ⭐⭐ super().__init__
实现 `Person` 类：`__init__(self, name, age)`，`__str__` 返回 `"name (age)"`。`Student(Person)`：`__init__(self, name, age, school)`，用 `super().__init__`，`__str__` 返回 `"name (age) - school"`。

## Q3 ⭐⭐ isinstance
实现 `count_animals(lst)`：统计列表中有多少是 `Animal` 的实例。用 `isinstance`。

## Q4 ⭐⭐ 方法重写
实现 `Shape` 基类：`area()` 返回 0，`description()` 返回 `"I am a shape"`。`Square(Shape)`：`__init__(self, side)`，重写 `area()` 返回 side²。`Circle(Shape)`：`__init__(self, radius)`，重写 `area()` 返回 πr²（π=3.14159）。

## Q5 ⭐⭐ 属性继承
实现 `Vehicle` 类：`__init__(self, brand)`，`info()` 返回品牌。`Car(Vehicle)`：`__init__(self, brand, model)`，用 `super().__init__`，重写 `info()` 返回 `"brand model"`。

## Q6 ⭐⭐⭐ 员工类层次
实现 `Employee`：`__init__(self, name, base_salary)`，`get_salary()` 返回 base_salary。`Manager(Employee)`：`__init__(self, name, base_salary, bonus)`，`get_salary()` 返回 base_salary + bonus。`CEO(Manager)`：`get_salary()` 返回 base_salary + bonus*2。

## Q7 ⭐⭐ 多态
实现 `all_speak(animals)`：接收 Animal 实例的列表，对每个调用 `speak()`，返回字符串列表。

## Q8 ⭐⭐⭐ 抽象基类
实现抽象类 `Appliance(ABC)`：带 `@abstractmethod turn_on()` 和 `turn_off()`。实现 `WashingMachine(Appliance)` 和 `Refrigerator(Appliance)`。

## Q9 ⭐⭐ 生成所有实例方法名
实现 `get_methods(cls)`：返回类所有**非下划线开头**的实例方法名（含继承的），排序列表。不要 dunder 方法（`__xxx__`）。

## Q10 ⭐⭐⭐ 自定义异常
实现 `BankError(Exception)` 基异常。`InsufficientFunds(BankError)` 异常。`withdraw(balance, amount)` 函数：余额不足时抛 `InsufficientFunds`，否则返回新余额。

## Q11 ⭐⭐ 组合
实现 `Engine` 类：`start()` 返回 `"Engine started"`，`stop()` 返回 `"Engine stopped"`。`Car` 类：`__init__` 创建 Engine 实例（组合），`start()` 和 `stop()` 委托给 Engine。

## Q12 ⭐⭐⭐ Mixin
实现 `LogMixin` 类：提供 `log(self, msg)` 方法，print `"[CLASS_NAME] msg"`。`Account` 类继承 `LogMixin`：`__init__(self, owner)`，`deposit(amount)` 记录 log，`balance` 属性。
