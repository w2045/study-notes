"""Python基础 · 第二章 — 自动批改"""
import math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "判断正负零", "sign", [
        ((5,), 1), ((-3,), -1), ((0,), 0), ((100,), 1), ((-50,), -1),
    ]),
    ("Q2", "绝对值", "my_abs", [
        ((-5.5,), 5.5), ((3.0,), 3.0), ((0,), 0), ((-0.1,), 0.1),
    ]),
    ("Q3", "累加", "sum_to", [
        ((5,), 15), ((1,), 1), ((0,), 0), ((10,), 55),
    ]),
    ("Q4", "FizzBuzz", "fizzbuzz", [
        ((3,), ["1", "2", "Fizz"]),
        ((5,), ["1", "2", "Fizz", "4", "Buzz"]),
        ((15,)[:], ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]),
    ]),
    ("Q5", "阶乘", "factorial", [
        ((5,), 120), ((0,), 1), ((1,), 1), ((7,), 5040),
    ]),
    ("Q6", "最大公约数", "gcd", [
        ((48, 18), 6), ((17, 5), 1), ((100, 10), 10), ((7, 7), 7),
    ]),
    ("Q7", "判断素数", "is_prime", [
        ((7,), True), ((4,), False), ((2,), True), ((1,), False), ((9,), False), ((13,), True),
    ]),
    ("Q8", "数字之和", "digit_sum", [
        ((123,), 6), ((0,), 0), ((999,), 27), ((1001,), 2),
    ]),
    ("Q9", "最大数", "max_of_three", [
        ((1,5,3), 5), ((7,7,7), 7), ((-1,-5,-3), -1), ((0,0,1), 1),
    ]),
    ("Q10", "乘法表", "print_table", []),  # 手动检查
    ("Q11", "Collatz", "collatz_steps", [
        ((6,), 8), ((1,), 0), ((8,), 3),
    ]),
    ("Q12", "斐波那契", "fibonacci", [
        ((0,), 0), ((1,), 1), ((6,), 8), ((10,), 55),
    ]),
]

def main():
    sys.path.insert(0, ".")
    import homework
    total = 0; max_s = len([t for t in TEST_CASES if t[2] != "print_table"])
    print("=" * 60)
    print("  Python基础 · 第二章 · 控制流 — 自动批改")
    print("=" * 60)
    for qid, title, fn, cases in TEST_CASES:
        func = getattr(homework, fn, None)
        if func is None: print(f"\n{qid} [{title}] ❌ 函数缺失"); continue
        if fn == "print_table":
            print(f"\n{qid} [{title}] 👀 手动检查"); continue
        if len(func.__code__.co_code) <= 6: print(f"\n{qid} [{title}] ⚠️ 空函数"); continue
        passed = 0; errors = []
        for i, (args, exp) in enumerate(cases, 1):
            try: result = func(*args)
            except Exception as e: errors.append(f"  用例{i}: {e}"); continue
            ok = math.isclose(result, exp, rel_tol=1e-9) if isinstance(exp, float) else result == exp
            if ok: passed += 1
            else: errors.append(f"  用例{i}: 期望{exp}, 得{result}")
        if passed == len(cases): print(f"\n{qid} [{title}] ✅ {passed}/{len(cases)}"); total += 1
        else:
            print(f"\n{qid} [{title}] ❌ {passed}/{len(cases)}")
            for e in errors: print(e)
    print(f"\n{'='*60}\n  总分: {total}/{max_s}\n{'='*60}")

if __name__ == "__main__": main()
