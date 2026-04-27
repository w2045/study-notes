"""Python基础 · 第四章 — 自动批改"""
import math, sys, time
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "Lambda基础", "square", [
        ((), lambda f: f(5) == 25 and f(0) == 0 and f(-3) == 9),
    ]),
    ("Q1b", "Lambda基础", "is_even", [
        ((), lambda f: f(4) == True and f(5) == False and f(0) == True),
    ]),
    ("Q1c", "Lambda基础", "add", [
        ((), lambda f: f(3, 5) == 8 and f(-1, 1) == 0),
    ]),
    ("Q2", "创建乘法器", "make_multiplier", [
        ((3,), lambda f: f(7) == 21 and f(0) == 0 and f(-2) == -6),
        ((0,), lambda f: f(100) == 0),
        ((1.5,), lambda f: math.isclose(f(2), 3.0)),
    ]),
    ("Q3", "Lambda排序", "sort_by_last_letter", [
        ((['apple', 'kiwi', 'banana'],), ['banana', 'apple', 'kiwi']),
        ((['dog', 'cat', 'bird'],), ['bird', 'dog', 'cat']),
        ((['a', 'b', 'c'],), ['a', 'b', 'c']),
        (([],), []),
    ]),
    ("Q4", "创建平均值器", "make_averager", [
        ((), lambda f: (f(10), f(20), math.isclose(f(30), 20.0))),
    ]),
    ("Q5", "银行账户", "make_bank_account", [
        ((100,), lambda f: f(50) == 150 and f(-30) == 120 and f(-200) == "余额不足" and f(0) == 120),
    ]),
    ("Q6", "柯里化幂函数", "curry_power", [
        ((2,), lambda f: f(3) == 8 and f(0) == 1 and f(10) == 1024),
        ((5,), lambda f: f(2) == 25),
    ]),
    ("Q7", "两数应用", "apply_to_two", [
        ((), lambda f: f(lambda x, y: x + y, 3, 5) == 8 and f(lambda x, y: x * y, 4, 7) == 28),
    ]),
    ("Q8", "计数器工厂", "make_counter", [
        ((), lambda f: f() == 0 and f() == 1 and f() == 2),
        ((2,), lambda f: f() == 0 and f() == 2 and f() == 4),
        ((5,), lambda f: f() == 0 and f() == 5),
    ]),
    ("Q9", "筛选后变换", "filter_map", [
        ((lambda x: x > 0, lambda x: x * 2, [-3, 5, -2, 7]), [10, 14]),
        ((lambda x: x % 2 == 0, lambda x: x ** 2, [1, 2, 3, 4, 5]), [4, 16]),
        ((lambda x: True, lambda x: x, []), []),
    ]),
    ("Q10", "嵌套Lambda解码", "decode_lambda", [
        ((), 8),
    ]),
    ("Q11", "Lambda问候语", "make_greeting", [
        (('Hello',), lambda f: f('World') == 'Hello, World!' and f('Python') == 'Hello, Python!'),
        (('Good morning',), lambda f: f('Alice') == 'Good morning, Alice!'),
    ]),
    ("Q12", "闭包计时器", "make_timer", [
        ((), lambda f: (time.sleep(0.15), f() > 0.09)[1]),
    ]),
]

def run_test(func, case):
    args, expected = case
    if len(args) == 0 and callable(expected) and callable(func):
        # Zero-arg factory or direct function: try calling func() first
        try:
            called = func()
            if callable(called):
                result = called  # Factory returned a function → test it
            else:
                result = func   # Direct value → test as-is
        except Exception:
            result = func       # func requires args → test directly
        ok = expected(result)
        return ok, f"期望满足谓词, 未满足" if not ok else ""
    result = func(*args)
    if callable(expected):
        ok = expected(result)
        return ok, f"期望满足谓词, 得 {result}" if not ok else ""
    ok = math.isclose(result, expected, rel_tol=1e-9) if isinstance(expected, float) else result == expected
    if not ok:
        return False, f"期望 {expected}, 得 {result}"
    return True, ""

def main():
    sys.path.insert(0, ".")
    import homework
    total, passed_all = 0, 0
    # Map Q1 sub-items to same score
    q_names = {"Q1", "Q1b", "Q1c"}
    max_s = len([t for t in TEST_CASES if t[0] not in q_names]) + 1  # Q1 counts as 1
    print("=" * 60)
    print("  Python基础 · 第四章 · 环境图与Lambda — 自动批改")
    print("=" * 60)
    q1_parts = 0
    q1_pass = 0
    for qid, title, fn_name, cases in TEST_CASES:
        func = getattr(homework, fn_name, None)
        if func is None:
            print(f"\n{qid} [{title}] ❌ 函数缺失")
            continue
        if qid not in q_names:
            if callable(func) and len(func.__code__.co_code) <= 6:
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
        if qid in q_names:
            q1_parts += 1
            if passed == len(cases):
                q1_pass += 1
            if qid != "Q1":
                continue  # Print only once for Q1 group (handled below)
        if passed == len(cases):
            print(f"\n{qid} [{title}] ✅ {passed}/{len(cases)}")
            total += 1
        else:
            print(f"\n{qid} [{title}] ❌ {passed}/{len(cases)}")
            for e in errors:
                print(e)
    # Print Q1 consolidated
    if q1_pass == q1_parts:
        print(f"\nQ1 [Lambda基础] ✅ {q1_pass}/{q1_parts}")
        total += 1
    else:
        print(f"\nQ1 [Lambda基础] ❌ {q1_pass}/{q1_parts}")
    print(f"\n{'=' * 60}\n  总分: {total}/{max_s}\n{'=' * 60}")

if __name__ == "__main__":
    main()
