"""Python基础 · 第七章 · 序列 — 作业"""

from typing import List, Tuple, Dict, Any

# Q1
def reverse_list(lst: List) -> List:
    """反转列表，不用切片 >>> reverse_list([1,2,3]) == [3,2,1]"""
    pass

# Q2
def is_anagram(s1: str, s2: str) -> bool:
    """判断变位词 >>> is_anagram('Listen', 'Silent') == True"""
    pass

# Q3
def running_sum(lst: List[int]) -> List[int]:
    """累积和 >>> running_sum([1,2,3]) == [1,3,6]"""
    pass

# Q4
def remove_duplicates(lst: List) -> List:
    """去重保持顺序 >>> remove_duplicates([1,2,2,3,1]) == [1,2,3]"""
    pass

# Q5
def longest_word(words: List[str]) -> str:
    """最长单词 >>> longest_word(['a','ab','abc']) == 'abc'"""
    pass

# Q6
def flatten(lst: List) -> List:
    """扁平化一层 >>> flatten([[1,2],[3,[4]],5]) == [1,2,3,[4],5]"""
    pass

# Q7
def pairwise(lst: List) -> List[Tuple]:
    """相邻配对 >>> pairwise([1,2,3,4]) == [(1,2),(2,3),(3,4)]"""
    pass

# Q8
def group_by_key(items: List[Dict], key: str) -> Dict[Any, List[Dict]]:
    """按键分组 >>> len(group_by_key([{'a':1},{'a':2},{'a':1}], 'a')) == 2"""
    pass

# Q9
def rotate_list(lst: List, k: int) -> List:
    """右旋k位 >>> rotate_list([1,2,3,4,5], 2) == [4,5,1,2,3]"""
    pass

# Q10
def merge_sorted(a: List[int], b: List[int]) -> List[int]:
    """合并有序列表 >>> merge_sorted([1,3,5],[2,4,6]) == [1,2,3,4,5,6]"""
    pass

# Q11
def word_freq(text: str) -> Dict[str, int]:
    """词频统计 >>> word_freq('Hi hi!') == {'hi': 2}"""
    pass

# Q12
def sliding_window_max(lst: List[int], k: int) -> List[int]:
    """滑动窗口最大值 >>> sliding_window_max([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]"""
    pass

if __name__ == "__main__":
    import doctest; doctest.testmod()
