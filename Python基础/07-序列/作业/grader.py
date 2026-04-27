"""Python基础 · 第七章 — 自动批改"""
import math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "反转列表", "reverse_list", [
        (([1, 2, 3],), [3, 2, 1]), (([],), []), (([42],), [42]),
        ((["a", "b", "c"],), ["c", "b", "a"]),
    ]),
    ("Q2", "判断变位词", "is_anagram", [
        (("Listen", "Silent"), True), (("hello", "world"), False),
        (("a b c", "c b a"), True), (("", ""), True),
    ]),
    ("Q3", "累积和", "running_sum", [
        (([1, 2, 3],), [1, 3, 6]), (([5],), [5]), (([],), []),
        (([1, -1, 1],), [1, 0, 1]),
    ]),
    ("Q4", "去除重复", "remove_duplicates", [
        (([1, 2, 2, 3, 1],), [1, 2, 3]), (([],), []), (([1, 1, 1],), [1]),
    ]),
    ("Q5", "最长单词", "longest_word", [
        ((["a", "ab", "abc"],), "abc"), ((["x", "y"],), "x"),
        ((["hello", "world"],), "hello"),
    ]),
    ("Q6", "扁平化一层", "flatten", [
        (([[1, 2], [3, [4]], 5],), [1, 2, 3, [4], 5]),
        (([],), []), (([[1]],), [1]),
        (([1, [2, 3]],), [1, 2, 3]),
    ]),
    ("Q7", "相邻配对", "pairwise", [
        (([1, 2, 3, 4],), [(1, 2), (2, 3), (3, 4)]), (([1],), []), (([],), []),
    ]),
    ("Q8", "按键分组", "group_by_key", [
        (([{"a": 1}, {"a": 2}, {"a": 1}], "a"),
         lambda r: len(r) == 2 and len(r.get(1, [])) == 2 and len(r.get(2, [])) == 1),
    ]),
    ("Q9", "旋转列表", "rotate_list", [
        (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]), (([1, 2, 3], 0), [1, 2, 3]),
        (([1, 2, 3], 3), [1, 2, 3]), (([1, 2, 3], 5), [2, 3, 1]),
    ]),
    ("Q10", "合并有序列表", "merge_sorted", [
        (([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]),
        (([], [1, 2]), [1, 2]), (([1], []), [1]),
        (([1, 2, 3], [1, 2, 3]), [1, 1, 2, 2, 3, 3]),
    ]),
    ("Q11", "词频统计", "word_freq", [
        (("Hi hi!",), lambda r: r.get("hi") == 2),
        (("Hello, world! Hello.",), lambda r: r.get("hello") == 2 and r.get("world") == 1),
        (("",), lambda r: r == {}),
    ]),
    ("Q12", "滑动窗口最大值", "sliding_window_max", [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
        (([1, 2, 3], 1), [1, 2, 3]),
        (([5, 4, 3], 2), [5, 4]),
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
        return False, f"期望 {_brief(expected)}, 得 {_brief(result)}"
    return True, ""

def _brief(x):
    s = str(x)
    return s[:60] + "..." if len(s) > 60 else s

def main():
    sys.path.insert(0, ".")
    import homework
    total = 0
    max_s = len(TEST_CASES)
    print("=" * 60)
    print("  Python基础 · 第七章 · 序列 — 自动批改")
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
