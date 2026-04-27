# Python基础 · 第九章 · 可变性 — 作业

> 完成 `homework.py`。运行 `python3 grader.py` 自动批改。

---

## Q1 ⭐ 判断可变性
实现 `classify_mutable(obj)`：返回字符串 `"mutable"` 或 `"immutable"`。判断依据：对 `list`、`dict`、`set` 返回 `"mutable"`；对 `int`、`float`、`str`、`tuple`、`bool` 返回 `"immutable"`。

## Q2 ⭐ 克隆列表
实现 `clone_list(lst)`：返回列表的浅复制。不允许用 `lst[:]` 或 `list(lst)`——用循环手动实现。

## Q3 ⭐⭐ 去除列表中重复项（保持顺序）
实现 `dedup(lst)`：返回新列表，保留原顺序，但去除重复元素。用 `set` 辅助。

## Q4 ⭐⭐ 反转字典
实现 `invert_dict(d)`：键值互换。假设值都是唯一的。如 `{"a":1, "b":2} → {1:"a", 2:"b"}`。

## Q5 ⭐⭐ 单词频率
实现 `word_frequency(sentence)`：返回字典，用小写单词作为键，出现次数作为值。单词以空格分隔。

## Q6 ⭐⭐⭐ 安全追加
实现 `safe_append(item, lst=None)`：如果 `lst` 是 `None`，创建新列表；把 `item` 追加到列表末尾并返回。修复默认参数陷阱！

## Q7 ⭐⭐ 字典默认值
实现 `merge_dicts(d1, d2)`：合并两个字典，如果键冲突，取值的和（字符串则拼接）。

## Q8 ⭐⭐⭐ 集合运算
实现 `common_elements(lists)`：接收列表的列表，返回所有子列表**共有**的元素集合。

## Q9 ⭐⭐ 列表去极值
实现 `trim_list(lst)`：原地修改列表，移除最大值和最小值。如果有多个最大/最小值，只移除一个。

## Q10 ⭐⭐⭐ 分组后统计
实现 `group_and_count(items, key_func)`：用 `key_func` 对每个元素计算键，按此键分组，返回每组元素数量的字典。如 `group_and_count([1, 2, 3, 4], lambda x: x%2) → {1:2, 0:2}`。

## Q11 ⭐⭐ 查找重复
实现 `find_duplicates(lst)`：返回列表中出现次数 >1 的元素集合。

## Q12 ⭐⭐⭐ 嵌套字典更新
实现 `deep_update(d, updates)`：将 `updates` 字典的内容递归合并到 `d` 中。如果两个都是 dict，递归合并；否则直接覆盖。
