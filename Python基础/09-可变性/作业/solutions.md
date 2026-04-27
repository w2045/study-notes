# Python基础 · 第九章 · 可变性 — 参考答案

<details><summary>Q1 — classify_mutable</summary>

```python
def classify_mutable(obj):
    if isinstance(obj, (list, dict, set)):
        return "mutable"
    return "immutable"
```
**要点**：`isinstance` 接收元组一次检查多种类型。
</details>

<details><summary>Q2 — clone_list</summary>

```python
def clone_list(lst):
    result = []
    for x in lst:
        result.append(x)
    return result
```
**要点**：手动浅复制。也可以 `result = [x for x in lst]`。
</details>

<details><summary>Q3 — dedup</summary>

```python
def dedup(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
```
**要点**：`set` 追踪已见过的元素，保持原顺序添加到结果。
</details>

<details><summary>Q4 — invert_dict</summary>

```python
def invert_dict(d):
    return {v: k for k, v in d.items()}
```
**要点**：字典推导式，交换 k 和 v。
</details>

<details><summary>Q5 — word_frequency</summary>

```python
def word_frequency(sentence):
    freq = {}
    for word in sentence.split():
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
    return freq
```
**要点**：`dict.get(key, default)` 是不发生 KeyError 的惯用写法。
</details>

<details><summary>Q6 — safe_append</summary>

```python
def safe_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```
**要点**：修复默认参数陷阱的关键——每次调用时检查并新建列表。
</details>

<details><summary>Q7 — merge_dicts</summary>

```python
def merge_dicts(d1, d2):
    result = dict(d1)
    for k, v in d2.items():
        if k in result:
            result[k] += v
        else:
            result[k] = v
    return result
```
**要点**：先复制 d1，再遍历 d2 合并。值冲突时累加（`+=` 对数和字符串都适用）。
</details>

<details><summary>Q8 — common_elements</summary>

```python
def common_elements(lists):
    if not lists:
        return set()
    result = set(lists[0])
    for lst in lists[1:]:
        result &= set(lst)
    return result
```
**要点**：从第一个子列表的集合开始，依次与后续子列表取交集（`&=`）。
</details>

<details><summary>Q9 — trim_list</summary>

```python
def trim_list(lst):
    if not lst:
        return
    lst.remove(max(lst))
    lst.remove(min(lst))
```
**要点**：`remove` 只移除第一个匹配的值。有多个相同极值时只移除一个。
</details>

<details><summary>Q10 — group_and_count</summary>

```python
def group_and_count(items, key_func):
    counts = {}
    for item in items:
        k = key_func(item)
        counts[k] = counts.get(k, 0) + 1
    return counts
```
**要点**：模式同词频统计——key 由 key_func 计算。
</details>

<details><summary>Q11 — find_duplicates</summary>

```python
def find_duplicates(lst):
    seen = set()
    dups = set()
    for x in lst:
        if x in seen:
            dups.add(x)
        else:
            seen.add(x)
    return dups
```
**要点**：第一次见→加入 seen。第二次见→加入 dups。返回 dups 就是出现次数 >1 的元素。
</details>

<details><summary>Q12 — deep_update</summary>

```python
def deep_update(d, updates):
    for k, v in updates.items():
        if k in d and isinstance(d[k], dict) and isinstance(v, dict):
            deep_update(d[k], v)
        else:
            d[k] = v
```
**要点**：递归判断——两个值都是 dict → 递归合并；否则直接覆盖。原地修改不返回。
</details>
