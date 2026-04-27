# Python基础 · 第二章 · 控制流 — 参考答案

<details><summary>Q1 — sign</summary>

```python
def sign(n):
    if n > 0: return 1
    elif n < 0: return -1
    else: return 0
```
</details>

<details><summary>Q2 — my_abs</summary>

```python
def my_abs(n):
    return n if n >= 0 else -n
```
</details>

<details><summary>Q3 — sum_to</summary>

```python
def sum_to(n):
    total = 0; i = 1
    while i <= n:
        total += i; i += 1
    return total
```
</details>

<details><summary>Q4 — fizzbuzz</summary>

```python
def fizzbuzz(n):
    result = []
    for i in range(1, n+1):
        if i % 15 == 0: result.append("FizzBuzz")
        elif i % 3 == 0: result.append("Fizz")
        elif i % 5 == 0: result.append("Buzz")
        else: result.append(str(i))
    return result
```
</details>

<details><summary>Q5 — factorial</summary>

```python
def factorial(n):
    result = 1; i = 1
    while i <= n:
        result *= i; i += 1
    return result
```
</details>

<details><summary>Q6 — gcd</summary>

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```
</details>

<details><summary>Q7 — is_prime</summary>

```python
def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
```
</details>

<details><summary>Q8 — digit_sum</summary>

```python
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10; n //= 10
    return total
```
</details>

<details><summary>Q9 — max_of_three</summary>

```python
def max_of_three(a, b, c):
    if a >= b and a >= c: return a
    elif b >= c: return b
    else: return c
```
</details>

<details><summary>Q10 — print_table</summary>

```python
def print_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i*j:3}", end="")
        print()
```
</details>

<details><summary>Q11 — collatz_steps</summary>

```python
def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps
```
</details>

<details><summary>Q12 — fibonacci</summary>

```python
def fibonacci(k):
    if k == 0: return 0
    a, b = 0, 1
    for _ in range(k - 1):
        a, b = b, a + b
    return b
```
</details>
