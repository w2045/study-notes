# Python基础 · 第五章 · 递归 — 参考答案

<details><summary>Q1 — factorial</summary>

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```
**要点**：基本情况 n==0，递归步骤 n * (n-1)!。
</details>

<details><summary>Q2 — sum_digits</summary>

```python
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)
```
**要点**：每次取最后一位（n%10），递归处理剩余位数（n//10）。
</details>

<details><summary>Q3 — power</summary>

```python
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

# 高效版本：快速幂（O(log n)）
def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half
```
**要点**：线性递归：`x^n = x × x^(n-1)`。快速幂用二分思想，n 次减为 n/2 次。
</details>

<details><summary>Q4 — is_palindrome</summary>

```python
def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
```
**要点**：首尾比较，`s[1:-1]` 去掉首尾字符后递归检查。
</details>

<details><summary>Q5 — count_up</summary>

```python
def count_up(n):
    if n == 0:
        return
    count_up(n - 1)
    print(n)

# 如果从大到小：
def count_up(n):
    if n == 0:
        return
    print(n)
    count_up(n - 1)
```
**要点**：先递归到底（n=0），返回时打印。这样最小的 1 最先被打印（从栈底返回）。
</details>

<details><summary>Q6 — gcd</summary>

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```
**要点**：欧几里得算法的递归形式——`gcd(b, a % b)`。基本情况是 `b==0` 时返回 `a`。
</details>

<details><summary>Q7 — my_len</summary>

```python
def my_len(lst):
    if lst == []:
        return 0
    return 1 + my_len(lst[1:])
```
**要点**：空列表→0；非空→1 + 剩余长度。
</details>

<details><summary>Q8 — reverse_string</summary>

```python
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]
```
**要点**：递归反转剩余部分，然后把第一个字符追加到最后。
</details>

<details><summary>Q9 — recursive_sum</summary>

```python
def recursive_sum(lst):
    if lst == []:
        return 0
    return lst[0] + recursive_sum(lst[1:])
```
**要点**：列表递归的标准模式——首元素 + 剩余元素的和。
</details>

<details><summary>Q10 — recursive_max</summary>

```python
def recursive_max(lst):
    if len(lst) == 1:
        return lst[0]
    rest_max = recursive_max(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max
```
**要点**：把当前元素和子列表的最大值比较。单元素列表直接返回该元素。
</details>

<details><summary>Q11 — count</summary>

```python
def count(x, lst):
    if lst == []:
        return 0
    head_match = 1 if lst[0] == x else 0
    return head_match + count(x, lst[1:])
```
**要点**：检查头元素是否等于 x，加上剩余列表中的出现次数。
</details>

<details><summary>Q12 — binary_search</summary>

```python
def binary_search(lst, target):
    def helper(lo, hi):
        if lo > hi:
            return -1
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            return helper(mid + 1, hi)
        else:
            return helper(lo, mid - 1)
    return helper(0, len(lst) - 1)
```
**要点**：辅助函数 `helper(lo, hi)` 管理递归范围。每次比较中间元素，将搜索范围减半。`lo > hi` 是没找到的基本情况。
</details>
