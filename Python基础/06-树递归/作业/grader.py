"""Python基础 · 第六章 — 自动批改"""
import math, sys
from typing import Any, List, Tuple

def sorted_deep(lst):
    """递归排序嵌套列表，用于和期望结果比较（顺序无关）"""
    if isinstance(lst, list):
        return sorted([sorted_deep(x) for x in lst], key=str)
    return lst

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "斐波那契", "fib", [
        ((0,), 0), ((1,), 1), ((6,), 8), ((10,), 55), ((15,), 610),
    ]),
    ("Q2", "组合数", "C", [
        ((5, 2), 10), ((4, 0), 1), ((4, 4), 1), ((6, 3), 20), ((10, 7), 120),
    ]),
    ("Q3", "网格路径", "grid_paths", [
        ((1, 1), 2), ((2, 2), 6), ((3, 2), 10), ((0, 5), 1),
    ]),
    ("Q4", "硬币找零", "coin_change", [
        ((5, (1, 2, 5)), 4), ((1, (1,)), 1), ((4, (1, 2)), 3),
    ]),
    ("Q5", "整数划分", "count_partitions", [
        ((4, 2), 3), ((3, 3), 3), ((5, 3), 5), ((1, 1), 1),
    ]),
    ("Q6", "生成子集", "subsets", [
        (([1, 2, 3],), lambda r: len(r) == 8 and all(isinstance(s, list) for s in r)),
        (([],), lambda r: r == [[]]),
        (([42],), lambda r: sorted_deep(r) == sorted_deep([[], [42]])),
    ]),
    ("Q7", "汉诺塔", "hanoi", [
        ((1, 'A', 'C', 'B'), ['A→C']),
        ((2, 'A', 'C', 'B'), ['A→B', 'A→C', 'B→C']),
        ((3, 'A', 'C', 'B'), lambda r: len(r) == 7 and r[0] == 'A→C' and r[-1] == 'A→C'),
    ]),
    ("Q8", "上楼梯", "triple_steps", [
        ((4,), 7), ((0,), 1), ((1,), 1), ((5,), 13),
    ]),
    ("Q9", "帕斯卡", "pascal_row", [
        ((0,), [1]), ((3,), [1, 3, 3, 1]), ((5,), [1, 5, 10, 10, 5, 1]),
    ]),
    ("Q10", "生成排列", "permutations", [
        (([1, 2, 3],), lambda r: len(r) == 6 and all(len(p) == 3 for p in r)),
        (([1],), lambda r: r == [[1]]),
        (([],), lambda r: r == [[]]),
    ]),
    ("Q11", "最大子集和", "max_subset_sum", [
        (([3, 2, 5, 10, 7],), 15), (([1, 2, 3],), 4), (([],), 0), (([5],), 5),
    ]),
    ("Q12", "找零方案", "coin_change_ways", [
        ((4, (1, 2)), lambda r: len(r) == 3),
        ((1, (1,)), lambda r: r == [[1]]),
        ((0, (1,)), lambda r: r == [[]]),
    ]),
]

def run_test(func, case):
    args, expected = case
    result = func(*args)
    if callable(expected):
        ok = expected(result)
        return ok, f"期望满足谓词, 得 {_brief(result)}" if not ok else ""
    ok = math.isclose(result, expected, rel_tol=1e-9) if isinstance(expected, float) else result == expected
    if not ok:
        return False, f"期望 {expected}, 得 {_brief(result)}"
    return True, ""

def _brief(x):
    s = str(x)
    return s[:50] + "..." if len(s) > 50 else s

def main():
    sys.path.insert(0, ".")
    import homework
    total = 0
    max_s = len(TEST_CASES)
    print("=" * 60)
    print("  Python基础 · 第六章 · 树递归 — 自动批改")
    print("=" * 60)
    for qid, title, fn_name, cases in TEST_CASES:
        func = getattr(homework, fn_name, None)
        if func is None:
            print(f"\n{qid} [{title}] ❌ 函数缺失")
            continue
        if len(func.__code__.co_code) <= 6:
            print(f"\n{qid} [{title}] ⚠️ 空函数")
            continue
        passed = 0
        errors = []
        for i, case in enumerate(cases, 1):
            try:
                ok, msg = run_test(func, case)
            except RecursionError:
                errors.append(f"  用例{i}: RecursionError")
                continue
            except Exception as e:
                errors.append(f"  用例{i}: {e}")
                continue
            if ok:
                passed += 1
            else:
                errors.append(f"  用例{i}: {msg}")
        if passed == len(cases):
            print(f"\n{qid} [{title}] ✅ {passed}/{len(cases)}")
            total += 1
        else:
            print(f"\n{qid} [{title}] ❌ {passed}/{len(cases)}")
            for e in errors:
                print(e)
    print(f"\n{'=' * 60}\n  总分: {total}/{max_s}\n{'=' * 60}")

if __name__ == "__main__":
    main()
