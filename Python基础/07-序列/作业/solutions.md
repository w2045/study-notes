# Python基础 · 第七章 · 序列 — 参考答案

<details><summary>Q1 — reverse_list</summary>

```python
def reverse_list(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result
```
**要点**：从末尾向前遍历，逐个 append。也可以用 `for x in lst: result.insert(0, x)`。
</details>

<details><summary>Q2 — is_anagram</summary>

```python
def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)
```
**要点**：变位词 → 排序后字符串相同。先统一小写、去掉空格。
</details>

<details><summary>Q3 — running_sum</summary>

```python
def running_sum(lst):
    result = []
    total = 0
    for x in lst:
        total += x
        result.append(total)
    return result
```
**要点**：维护累积和，每次迭代追加当前值。
</details>

<details><summary>Q4 — remove_duplicates</summary>

```python
def remove_duplicates(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
```
**要点**：`set` 记录见过的元素。只在首次出现时加入结果。
</details>

<details><summary>Q5 — longest_word</summary>

```python
def longest_word(words):
    if not words:
        return ""
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest
```
**要点**：遍历更新最长值。初始化第一个，相同时不更新 → 保持了「第一个最长」的语义。
</details>

<details><summary>Q6 — flatten</summary>

```python
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result
```
**要点**：只展开一层。列表元素 `extend`，非列表元素 `append`。
</details>

<details><summary>Q7 — pairwise</summary>

```python
def pairwise(lst):
    result = []
    for i in range(len(lst) - 1):
        result.append((lst[i], lst[i + 1]))
    return result
```
**要点**：i 从 0 到 len-2，每次取 lst[i] 和 lst[i+1] 构成元组。
</details>

<details><summary>Q8 — group_by_key</summary>

```python
def group_by_key(items, key):
    groups = {}
    for item in items:
        k = item[key]
        if k not in groups:
            groups[k] = []
        groups[k].append(item)
    return groups
```
**要点**：标准分组模式。键不存在时初始化为空列表。
</details>

<details><summary>Q9 — rotate_list</summary>

```python
def rotate_list(lst, k):
    if not lst:
        return []
    k = k % len(lst)
    return lst[-k:] + lst[:-k]
```
**要点**：取模避免 k 大于长度时的多余旋转。`lst[-k:]` 是右端 k 个元素，`lst[:-k]` 是剩余部分。
</details>

<details><summary>Q10 — merge_sorted</summary>

```python
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```
**要点**：归并排序的核心操作。两指针比较，取较小的，最后追加剩余部分。
</details>

<details><summary>Q11 — word_freq</summary>

```python
def word_freq(text):
    for ch in ".,!?":
        text = text.replace(ch, "")
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
```
**要点**：先清理标点 → 转小写 → 分割 → 字典计数。`dict.get(key, default)` 避免 KeyError。
</details>

<details><summary>Q12 — sliding_window_max</summary>

```python
def sliding_window_max(lst, k):
    if not lst or k <= 0:
        return []
    result = []
    for i in range(len(lst) - k + 1):
        result.append(max(lst[i:i + k]))
    return result
```
**要点**：每 k 个元素的窗口取 `max`。简单 O(nk) 方法，n 为列表长度。
</details>
