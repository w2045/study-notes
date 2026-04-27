"""Python基础 · 第九章 — 自动批改"""
import math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "判断可变性", "classify_mutable", [
        (([1, 2, 3],), "mutable"), (("hello",), "immutable"),
        (({1: 2},), "mutable"), ((42,), "immutable"),
    ]),
    ("Q2", "克隆列表", "clone_list", [
        (([1, 2, 3],), lambda r: r == [1, 2, 3] and r is not [1, 2, 3]),
        (([],), lambda r: r == []),
    ]),
    ("Q3", "去重", "dedup", [
        (([1, 2, 2, 3, 1],), [1, 2, 3]), (([5, 5, 5],), [5]), (([],), []),
    ]),
    ("Q4", "反转字典", "invert_dict", [
        (({"a": 1, "b": 2},), {1: "a", 2: "b"}), (({},), {}),
    ]),
    ("Q5", "词频", "word_frequency", [
        (("hi hi hello",), {"hi": 2, "hello": 1}),
        (("",), {}),
    ]),
    ("Q6", "安全追加", "safe_append", [
        ((1,), [1]), ((1, None), [1]),
        ((), lambda f: f(1, None) == [1] and f(2, None) == [2]),
    ]),
    ("Q7", "合并字典", "merge_dicts", [
        (({"a": 1}, {"a": 2, "b": 3}), {"a": 3, "b": 3}),
        (({"x": "he"}, {"x": "llo"}), {"x": "hello"}),
        (({}, {"a": 1}), {"a": 1}),
    ]),
    ("Q8", "集合运算", "common_elements", [
        (([[1, 2, 3], [2, 3, 4]],), {2, 3}),
        (([[1], [2]],), set()),
        (([[1, 2]],), {1, 2}),
    ]),
    ("Q9", "去极值", "trim_list", [
        ((), lambda f: (tmp := [1, 5, 2, 5, 3]) is not None and (f(tmp) is None) and len(tmp) == 3),
    ]),
    ("Q10", "分组计数", "group_and_count", [
        (([1, 2, 3, 4], lambda x: x % 2), {1: 2, 0: 2}),
        ((["a", "ab", "abc"], len), {1: 1, 2: 1, 3: 1}),
    ]),
    ("Q11", "查找重复", "find_duplicates", [
        (([1, 2, 2, 3, 3, 3],), {2, 3}),
        (([1, 2, 3],), set()),
    ]),
    ("Q12", "嵌套更新", "deep_update", [
        ((), lambda f: (d := {"a": 1, "c": {"x": 1}}) is not None and (f(d, {"c": {"y": 2}}) is None) and d == {"a": 1, "c": {"x": 1, "y": 2}}),
    ]),
]

def run_test(func, case):
    args, expected = case
    # Handle special test cases where we need to eval in context
    if callable(expected):
        if len(args) > 0:
            result = func(*args)
        else:
            result = func  # Predicate receives the function itself
        ok = expected(result)
        return ok, f"期望满足谓词" if not ok else ""
    result = func(*args)
    ok = math.isclose(result, expected, rel_tol=1e-9) if isinstance(expected, float) else result == expected
    if not ok:
        return False, f"期望 {expected}, 得 {result}"
    return True, ""

def main():
    sys.path.insert(0, ".")
    import homework
    total = 0
    max_s = len(TEST_CASES)
    print("=" * 60)
    print("  Python基础 · 第九章 · 可变性 — 自动批改")
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
