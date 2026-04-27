# Python基础 · 第十章 · 迭代器与生成器 — 参考答案

<details><summary>Q1 — first_n</summary>

```python
def first_n(it, n):
    result = []
    for _ in range(n):
        try:
            result.append(next(it))
        except StopIteration:
            break
    return result
```
**要点**：手动调用 `next()` 并用 `try/except` 捕获 `StopIteration`。
</details>

<details><summary>Q2 — count_up</summary>

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```
</details>

<details><summary>Q3 — filter_gen</summary>

```python
def filter_gen(predicate, it):
    for x in it:
        if predicate(x):
            yield x
```
</details>

<details><summary>Q4 — even_squares</summary>

```python
def even_squares(n):
    return (x * x for x in range(n + 1) if x % 2 == 0)
```
</details>

<details><summary>Q5 — interleave</summary>

```python
def interleave(a, b):
    a_done, b_done = False, False
    ait, bit = iter(a), iter(b)
    while not (a_done and b_done):
        if not a_done:
            try:
                yield next(ait)
            except StopIteration:
                a_done = True
        if not b_done:
            try:
                yield next(bit)
            except StopIteration:
                b_done = True
```
</details>

<details><summary>Q6 — MyRange</summary>

```python
class MyRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        val = self.current
        self.current += self.step
        return val
```
</details>

<details><summary>Q7 — fib_gen</summary>

```python
def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```
</details>

<details><summary>Q8 — Counter</summary>

```python
class Counter:
    def __init__(self, start=0, step=1):
        self.val = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        result = self.val
        self.val += self.step
        return result
```
</details>

<details><summary>Q9 — my_enumerate</summary>

```python
def my_enumerate(iterable, start=0):
    idx = start
    for val in iterable:
        yield idx, val
        idx += 1
```
</details>

<details><summary>Q10 — chunked</summary>

```python
def chunked(it, n):
    while True:
        chunk = []
        for _ in range(n):
            try:
                chunk.append(next(it))
            except StopIteration:
                break
        if not chunk:
            break
        yield chunk
```
</details>

<details><summary>Q11 — pipe</summary>

```python
def pipe(*funcs):
    def run(iterator):
        result = iterator
        for f in funcs:
            result = f(result)
        return result
    return run
```
</details>

<details><summary>Q12 — primes</summary>

```python
def primes():
    yield 2
    found = [2]
    n = 3
    while True:
        is_prime = True
        for p in found:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            yield n
            found.append(n)
        n += 2
```
</details>
