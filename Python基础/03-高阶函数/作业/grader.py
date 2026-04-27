"""Python基础 · 第三章 — 自动批改"""
import math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "应用函数", "apply_func", [
        ((lambda x: x * 2, 5), 10),
        ((lambda x: x + 1, 0), 1),
        ((abs, -7), 7),
        ((lambda x: x.upper(), "hi"), "HI"),
    ]),
    ("Q2", "创建加法器", "make_adder", [
        ((5,), lambda f: f(10) == 15 and f(0) == 5 and f(-3) == 2),
        ((0,), lambda f: f(100) == 100),
        ((-3,), lambda f: f(3) == 0),
    ]),
    ("Q3", "条件筛选", "keep_if", [
        ((lambda x: x > 0, [-3, 5, -2, 0, 7]), [5, 7]),
        ((lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]), [2, 4, 6]),
        ((lambda x: len(x) > 2, ["a", "ab", "abc", "x"]), ["abc"]),
        ((lambda x: True, []), []),
    ]),
    ("Q4", "列表变换", "transform_list", [
        ((abs, [-3, 5, -2, 0]), [3, 5, 2, 0]),
        ((lambda x: x * 2, [1, 2, 3]), [2, 4, 6]),
        ((str.upper, ["hello", "world"]), ["HELLO", "WORLD"]),
        ((lambda x: x, []), []),
    ]),
    ("Q5", "函数组合", "compose", [
        ((lambda x: x + 1, lambda x: x * 2), lambda f: f(3) == 7),
        ((lambda x: x * 2, lambda x: x + 1), lambda f: f(3) == 8),
        ((abs, lambda x: -x), lambda f: f(5) == 5),
    ]),
    ("Q6", "柯里化", "curry2", [
        ((lambda x, y: x + y,), lambda f: f(3)(5) == 8 and f(0)(0) == 0),
        ((lambda x, y: x * y,), lambda f: f(4)(7) == 28),
        ((lambda x, y: x - y,), lambda f: f(10)(3) == 7),
    ]),
    ("Q7", "创建幂函数", "make_power", [
        ((2,), lambda f: f(3) == 9 and f(0) == 0 and f(-2) == 4),
        ((3,), lambda f: f(2) == 8 and f(10) == 1000),
        ((0,), lambda f: f(5) == 1 and f(0) == 1),
    ]),
    ("Q8", "重复应用", "make_repeater", [
        ((lambda x: x * 2, 0), lambda f: f(5) == 5),
        ((lambda x: x * 2, 1), lambda f: f(1) == 2),
        ((lambda x: x * 2, 3), lambda f: f(1) == 8),
        ((lambda x: x + 1, 5), lambda f: f(0) == 5),
    ]),
    ("Q9", "通用累积", "accumulate", [
        ((lambda a, b: a + b, 0, 5, lambda x: x), 15),
        ((lambda a, b: a * b, 1, 5, lambda x: x), 120),
        ((lambda a, b: a + b, 0, 3, lambda x: x * x), 14),
        ((lambda a, b: a * b, 1, 0, lambda x: x), 1),
    ]),
    ("Q10", "合取谓词", "make_and", [
        ((lambda x: x > 0, lambda x: x % 2 == 0), lambda f: f(4) == True and f(-2) == False and f(3) == False),
        ((lambda x: True, lambda x: False), lambda f: f(1) == False),
    ]),
    ("Q11", "平方映射", "square_list", [
        (([1, 2, 3, 4],), [1, 4, 9, 16]),
        (([0, -1, -2],), [0, 1, 4]),
        (([],), []),
    ]),
    ("Q12", "交替函数", "make_alternator", [
        ((lambda x: x + 1, lambda x: x * 10), lambda f: (f(5), f(5), f(5), f(5)) == (6, 50, 6, 50)),
        ((lambda x: f"f{x}", lambda x: f"g{x}"), lambda f: (f(1), f(2), f(3)) == ("f1", "g2", "f3")),
    ]),
]

def run_test(func, case):
    """Run a single test case. case is (args_tuple, expected_or_lambda)"""
    args, expected = case
    result = func(*args)
    if callable(expected):
        return expected(result), f"期望满足谓词, 得 {result}"
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
    print("  Python基础 · 第三章 · 高阶函数 — 自动批改")
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
