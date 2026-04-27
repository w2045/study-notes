"""Python基础 · 第五章 — 自动批改"""
import math, sys, io
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "递归阶乘", "factorial", [
        ((5,), 120), ((0,), 1), ((1,), 1), ((7,), 5040),
    ]),
    ("Q2", "数字之和", "sum_digits", [
        ((123,), 6), ((0,), 0), ((99999,), 45), ((1001,), 2),
    ]),
    ("Q3", "递归求幂", "power", [
        ((2, 3), 8), ((5, 0), 1), ((3, 4), 81), ((10, 3), 1000),
    ]),
    ("Q4", "判断回文", "is_palindrome", [
        (("Racecar",), True), (("hello",), False), (("A",), True), (("",), True),
        (("ABBA",), True),
    ]),
    ("Q5", "递归计数", "count_up", []),  # 手动检查
    ("Q6", "递归最大公约数", "gcd", [
        ((48, 18), 6), ((17, 5), 1), ((100, 10), 10), ((7, 7), 7), ((42, 56), 14),
    ]),
    ("Q7", "列表长度", "my_len", [
        (([1,2,3],), 3), (([],), 0), ((([None]*10),), 10),
    ]),
    ("Q8", "反转字符串", "reverse_string", [
        (("abc",), "cba"), (("hello",), "olleh"), (("",), ""), (("a",), "a"),
        (("racecar",), "racecar"),
    ]),
    ("Q9", "递归求和", "recursive_sum", [
        (([1,2,3,4],), 10), (([],), 0), (([-1, 1],), 0), (([3.5, 2.5],), 6.0),
    ]),
    ("Q10", "递归最大值", "recursive_max", [
        (([3,1,4,1,5],), 5), (([-1,-5,-3],), -1), (([42],), 42), (([0,0,0],), 0),
    ]),
    ("Q11", "统计出现次数", "count", [
        ((1, [1,2,1,3]), 2), ((99, [1,2,3]), 0), (("x", ["x","y","x","x"]), 3),
        ((None, []), 0),
    ]),
    ("Q12", "二分查找", "binary_search", [
        (([1,3,5,7,9], 5), 2), (([1,3,5,7,9], 6), -1), (([1], 1), 0),
        (([], 5), -1), (([0,2,4,6,8], 8), 4),
    ]),
]

def run_test(func, case):
    args, expected = case
    result = func(*args)
    ok = math.isclose(result, expected, rel_tol=1e-9) if isinstance(expected, float) else result == expected
    if not ok:
        return False, f"期望 {expected}, 得 {result}"
    return True, ""

def check_no_loops(func):
    """检测函数是否使用了 for/while 循环 (启发式检查字节码)"""
    import dis
    try:
        code = func.__code__
        # 检查函数本身及其内部定义的函数
        instrs = list(dis.get_instructions(func))
        has_loop = any('FOR_ITER' in str(instr.opname) or 'SETUP_LOOP' in str(instr.opname)
                      for instr in instrs)
        # Also check nested functions (closures)
        for const in code.co_consts:
            if hasattr(const, 'co_code'):
                nested = list(dis.get_instructions(const))
                has_loop = has_loop or any(
                    'FOR_ITER' in str(instr.opname) for instr in nested
                )
        return not has_loop
    except Exception:
        return True  # 检查失败时放行

def main():
    sys.path.insert(0, ".")
    import homework
    total = 0
    manual = {"print_table", "count_up"}
    max_s = len([t for t in TEST_CASES if t[2] not in manual])
    print("=" * 60)
    print("  Python基础 · 第五章 · 递归 — 自动批改")
    print("=" * 60)
    for qid, title, fn_name, cases in TEST_CASES:
        func = getattr(homework, fn_name, None)
        if func is None:
            print(f"\n{qid} [{title}] ❌ 函数缺失")
            continue
        if fn_name in manual:
            if len(func.__code__.co_code) <= 6:
                print(f"\n{qid} [{title}] ⚠️ 空函数")
            else:
                print(f"\n{qid} [{title}] 👀 手动检查（必须用递归，无循环）")
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
                errors.append(f"  用例{i}: RecursionError — 检查基本情况")
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
