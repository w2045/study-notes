"""Python基础 · 第九章 · 可变性 — 作业"""

from typing import List, Dict, Set, Any, Callable

# Q1
def classify_mutable(obj: Any) -> str:
    """判断可变性 >>> classify_mutable([1,2,3]) == 'mutable'"""
    pass

# Q2
def clone_list(lst: List) -> List:
    """手动浅复制 >>> clone_list([1,2,3]) == [1,2,3]"""
    pass

# Q3
def dedup(lst: List) -> List:
    """去重保持顺序 >>> dedup([1,2,2,3,1]) == [1,2,3]"""
    pass

# Q4
def invert_dict(d: Dict) -> Dict:
    """键值互换 >>> invert_dict({'a':1,'b':2}) == {1:'a',2:'b'}"""
    pass

# Q5
def word_frequency(sentence: str) -> Dict[str, int]:
    """词频 >>> word_frequency('hi hi hello') == {'hi':2,'hello':1}"""
    pass

# Q6
def safe_append(item: Any, lst: List = None) -> List:
    """安全追加——修复默认参数陷阱 >>> safe_append(1) == [1]"""
    pass

# Q7
def merge_dicts(d1: Dict, d2: Dict) -> Dict:
    """合并字典 >>> merge_dicts({'a':1},{'a':2,'b':3}) == {'a':3,'b':3}"""
    pass

# Q8
def common_elements(lists: List[List]) -> Set:
    """共有元素 >>> common_elements([[1,2,3],[2,3,4]]) == {2,3}"""
    pass

# Q9
def trim_list(lst: List[int]) -> None:
    """原地移除一个最大值一个最小值（不返回）"""
    pass

# Q10
def group_and_count(items: List, key_func: Callable) -> Dict[Any, int]:
    """分组计数 >>> group_and_count([1,2,3,4], lambda x: x%2) == {1:2, 0:2}"""
    pass

# Q11
def find_duplicates(lst: List) -> Set:
    """查找重复值 >>> find_duplicates([1,2,2,3,3,3]) == {2,3}"""
    pass

# Q12
def deep_update(d: Dict, updates: Dict) -> None:
    """递归合并字典（原地修改 d）"""
    pass

if __name__ == "__main__":
    import doctest; doctest.testmod()
