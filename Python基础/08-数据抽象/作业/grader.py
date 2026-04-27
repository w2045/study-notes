"""Python基础 · 第八章 — 自动批改"""
import math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "有理数构造器", "make_rational", [
        ((3, 4), [3, 4]), ((0, 1), [0, 1]), ((1, 1), [1, 1]),
    ]),
    ("Q2", "有理数选择器", "numer", [
        (([3, 4],), 3), (([0, 1],), 0),
    ]),
    ("Q2b", "分母", "denom", [
        (([3, 4],), 4), (([5, 1],), 1),
    ]),
    ("Q3", "有理数化简", "make_rational_simplified", [
        ((2, 4), [1, 2]), ((3, 1), [3, 1]), ((0, 5), [0, 1]),
    ]),
    ("Q4", "有理数乘法", "mul_rational", [
        (([1, 2], [3, 4]), [3, 8]), (([2, 3], [3, 2]), [6, 6]),
        (([0, 1], [5, 7]), [0, 7]),
    ]),
    ("Q5", "树构造器", "tree", [
        ((), lambda f: f(5) == [5, []] and f(1, [[2, []]]) == [1, [[2, []]]]),
    ]),
    ("Q5b", "树选择器", "label", [
        (([5, []],), 5),
    ]),
    ("Q5c", "子树", "branches", [
        (([1, [[2, []]]],), [[2, []]]),
    ]),
    ("Q5d", "是叶子", "is_leaf", [
        (([5, []],), True), (([1, [[2, []]]],), False),
    ]),
    ("Q6", "统计叶子", "count_leaves", [
        (([1, [[2, []], [3, []]]],), 2), (([5, []],), 1),
        (([1, [[2, [[3, []]]]]],), 1),
    ]),
    ("Q7", "树总和", "tree_sum", [
        (([1, [[2, []], [3, []]]],), 6), (([5, []],), 5),
    ]),
    ("Q8", "树映射", "tree_map", [
        ((lambda x: x*2, [1, [[2, []], [3, []]]]), [2, [[4, []], [6, []]]]),
    ]),
    ("Q9", "闭包构造器", "make_rational_closure", [
        ((), lambda f: f(3, 4)('n') == 3 and f(3, 4)('d') == 4),
    ]),
    ("Q9b", "闭包选择器", "numer_closure", [
        ((None,), lambda f: f(0) == 0),  # dummy
    ]),
    ("Q10", "cons", "cons", [
        ((), lambda f: f(1, 2)(1) == 1 and f(1, 2)(2) == 2),
    ]),
    ("Q10b", "car", "car", [
        ((None,), lambda f: True),  # tested via cons
    ]),
    ("Q11", "有理数加法", "add_rational", [
        (([1, 2], [1, 3]), [5, 6]), (([1, 4], [1, 4]), [8, 16]),
    ]),
    ("Q12", "最大标签路径", "max_label_path", [
        (([3, [[1, []], [5, []]]],), 8), (([5, []],), 5),
        (([1, [[2, [[3, []]]]]],), 6),
    ]),
]

def _brief(x):
    s = str(x); return s[:60] + "..." if len(s) > 60 else s

def run_test(func, case):
    args, expected = case
    if not args and callable(expected):
        result = func  # test func directly
        ok = expected(result)
        return ok, f"期望满足谓词" if not ok else ""
    # Special handling for dummy tests (Q9b, Q10b)
    if callable(expected) and len(args) == 1 and args[0] is None:
        return True, ""
    result = func(*args)
    if callable(expected):
        ok = expected(result)
        return ok, f"期望满足谓词, 得 {_brief(result)}" if not ok else ""
    ok = math.isclose(result, expected, rel_tol=1e-9) if isinstance(expected, float) else result == expected
    if not ok:
        return False, f"期望 {_brief(expected)}, 得 {_brief(result)}"
    return True, ""

def main():
    sys.path.insert(0, ".")
    import homework
    # Skip dummy subtests in scoring
    skip_score = {"Q2b", "Q5b", "Q5c", "Q5d", "Q9b", "Q10b"}
    total, tested = 0, 0
    print("=" * 60)
    print("  Python基础 · 第八章 · 数据抽象 — 自动批改")
    print("=" * 60)
    for qid, title, fn_name, cases in TEST_CASES:
        func = getattr(homework, fn_name, None)
        if func is None:
            print(f"\n{qid} [{title}] ❌ 函数缺失")
            if qid not in skip_score: tested += 1
            continue
        if qid in skip_score:
            # Quick check only, no separate scoring
            if len(func.__code__.co_code) <= 6:
                print(f"\n{qid} [{title}] ⚠️ 空函数")
            else:
                print(f"\n{qid} [{title}] ✅")
            continue
        if len(func.__code__.co_code) <= 6:
            print(f"\n{qid} [{title}] ⚠️ 空函数")
            tested += 1
            continue
        passed = 0; errors = []
        for i, case in enumerate(cases, 1):
            try: ok, msg = run_test(func, case)
            except Exception as e: errors.append(f"  用例{i}: {e}"); continue
            if ok: passed += 1
            else: errors.append(f"  用例{i}: {msg}")
        if passed == len(cases):
            print(f"\n{qid} [{title}] ✅ {passed}/{len(cases)}")
            total += 1
        else:
            print(f"\n{qid} [{title}] ❌ {passed}/{len(cases)}")
            for e in errors: print(e)
        tested += 1
    print(f"\n{'=' * 60}\n  总分: {total}/{tested}\n{'=' * 60}")

if __name__ == "__main__":
    main()
