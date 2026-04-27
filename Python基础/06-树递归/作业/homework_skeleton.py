"""Python基础 · 第六章 · 树递归 — 作业"""

from typing import List

# Q1
def fib(n: int) -> int:
    """树递归斐波那契 >>> fib(6) == 8"""
    pass

# Q2
def C(n: int, k: int) -> int:
    """树递归组合数 C(n,k) >>> C(5,2) == 10"""
    pass

# Q3
def grid_paths(m: int, n: int) -> int:
    """网格路径数，只向右/下 >>> grid_paths(2,2) == 6"""
    pass

# Q4
def coin_change(amount: int, coins: tuple) -> int:
    """硬币找零方法数 >>> coin_change(5, (1,2,5)) == 4"""
    pass

# Q5
def count_partitions(n: int, m: int) -> int:
    """整数划分，最大部分不超过m >>> count_partitions(4, 2) == 3"""
    pass

# Q6
def subsets(lst: List) -> List[List]:
    """所有子集 >>> len(subsets([1,2,3])) == 8"""
    pass

# Q7
def hanoi(n: int, source: str, target: str, auxiliary: str) -> List[str]:
    """汉诺塔移动序列 >>> len(hanoi(3, 'A', 'C', 'B')) == 7"""
    pass

# Q8
def triple_steps(n: int) -> int:
    """上楼梯 1/2/3 步 >>> triple_steps(4) == 7"""
    pass

# Q9
def pascal_row(k: int) -> List[int]:
    """帕斯卡三角形第k行(0-index) >>> pascal_row(3) == [1,3,3,1]"""
    pass

# Q10
def permutations(lst: List) -> List[List]:
    """所有排列 >>> len(permutations([1,2,3])) == 6"""
    pass

# Q11
def max_subset_sum(lst: List[int]) -> int:
    """非相邻元素最大和 >>> max_subset_sum([3,2,5,10,7]) == 15"""
    pass

# Q12
def coin_change_ways(amount: int, coins: tuple) -> List[List[int]]:
    """所有找零方案 >>> len(coin_change_ways(4, (1,2))) == 3"""
    pass

if __name__ == "__main__":
    import doctest; doctest.testmod()
