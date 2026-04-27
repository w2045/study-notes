"""Python基础 · 第十章 — 自动批改"""
import inspect, math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "手动迭代", "first_n", [
        ((iter([1, 2, 3, 4]), 2), [1, 2]),
        ((iter([1, 2, 3]), 5), [1, 2, 3]),
        ((iter([]), 3), []),
    ]),
    ("Q2", "简易生成器", "count_up", [
        ((3,), lambda f: list(f) == [1, 2, 3]),
        ((1,), lambda f: list(f) == [1]),
        ((0,), lambda f: list(f) == []),
    ]),
    ("Q3", "筛选生成器", "filter_gen", [
        ((lambda x: x > 0, iter([-1, 2, -3, 4])), lambda f: list(f) == [2, 4]),
        ((lambda x: x % 2 == 0, iter(range(6))), lambda f: list(f) == [0, 2, 4]),
    ]),
    ("Q4", "生成器表达式", "even_squares", [
        ((5,), lambda f: list(f) == [0, 4, 16]),
        ((0,), lambda f: list(f) == [0]),
    ]),
    ("Q5", "合并迭代器", "interleave", [
        ((iter([1, 3]), iter([2, 4, 5])), lambda f: list(f) == [1, 2, 3, 4, 5]),
        ((iter([]), iter([1])), lambda f: list(f) == [1]),
    ]),
    ("Q6", "自定义Range", "MyRange", [
        ((2, 8, 2), lambda f: list(f) == [2, 4, 6]),
        ((0, 3), lambda f: list(f) == [0, 1, 2]),
    ]),
    ("Q7", "斐波那契生成器", "fib_gen", [
        ((), lambda f: [next(f) for _ in range(7)] == [0, 1, 1, 2, 3, 5, 8]),
    ]),
    ("Q8", "无限计数器", "Counter", [
        ((0, 2), lambda f: [next(f) for _ in range(3)] == [0, 2, 4]),
    ]),
    ("Q9", "模拟enumerate", "my_enumerate", [
        ((['a', 'b'],), lambda f: list(f) == [(0, 'a'), (1, 'b')]),
        ((['x', 'y', 'z'], 5), lambda f: list(f) == [(5, 'x'), (6, 'y'), (7, 'z')]),
    ]),
    ("Q10", "组块生成器", "chunked", [
        ((iter([1, 2, 3, 4, 5]), 2), lambda f: list(f) == [[1, 2], [3, 4], [5]]),
        ((iter([1, 2]), 3), lambda f: list(f) == [[1, 2]]),
    ]),
    ("Q11", "管道", "pipe", [
        ((), lambda f: list(f(
            lambda it: (x*2 for x in it),
            lambda it: (x for x in it if x > 5)
        )(iter([1, 2, 3, 4]))) == [6, 8]),
    ]),
    ("Q12", "素数生成器", "primes", [
        ((), lambda f: [next(f) for _ in range(5)] == [2, 3, 5, 7, 11]),
    ]),
]

def run_test(func, case):
    args, expected = case
    if callable(expected):
        if args:
            result = func(*args)
        elif isinstance(func, type):
            # Class: instantiate then apply predicate
            result = func
        else:
            # Generator function or other zero-arg callable
            if inspect.isgeneratorfunction(func):
                result = func()
            else:
                result = func
        ok = expected(result)
        return ok, f"期望满足谓词" if not ok else ""
    result = func(*args)
    ok = math.isclose(result, expected, rel_tol=1e-9) if isinstance(expected, float) else result == expected
    return ok, (f"期望 {expected}, 得 {result}" if not ok else "")

def main():
    sys.path.insert(0, ".")
    import homework
    total = 0
    print("=" * 60)
    print("  Python基础 · 第十章 · 迭代器与生成器 — 自动批改")
    print("=" * 60)
    for qid, title, fn_name, cases in TEST_CASES:
        func = getattr(homework, fn_name, None)
        if func is None:
            print(f"\n{qid} [{title}] ❌ 函数缺失")
            continue
        if fn_name not in ("fib_gen", "primes", "count_up", "pipe") and isinstance(func, type):
            # Class: test constructor directly
            pass
        if callable(func) and not isinstance(func, type) and len(func.__code__.co_code) <= 6:
            print(f"\n{qid} [{title}] ⚠️ 空函数")
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
    print(f"\n{'=' * 60}\n  总分: {total}/{len(TEST_CASES)}\n{'=' * 60}")

if __name__ == "__main__":
    main()
