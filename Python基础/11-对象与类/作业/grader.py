"""Python基础 · 第十一章 — 自动批改"""
import math, sys, time
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "矩形类", "Rectangle", [
        ((3, 4), lambda r: r.area() == 12 and r.perimeter() == 14),
        ((5, 5), lambda r: r.area() == 25 and r.perimeter() == 20),
    ]),
    ("Q2", "Counter", "Counter", [
        ((), lambda c: c.inc() == 1 and c.inc() == 2 and c.get() == 2 and c.reset() is None and c.get() == 0),
    ]),
    ("Q3", "向量类", "Vector", [
        ((), lambda cls: (v1 := cls(1,2)) is not None and (v2 := cls(3,4)) is not None
         and v1+v2==cls(4,6) and v1!=v2 and cls(1,2)==cls(1,2)),
    ]),
    ("Q4", "Student", "Student", [
        (("Alice", [90, 100]), lambda s: s.average() == 95.0 and s.grade() == "A"),
        (("Bob", [70, 80, 75]), lambda s: s.average() == 75.0 and s.grade() == "C"),
    ]),
    ("Q5", "银行账户", "BankAccount", [
        (("Bob", 100), lambda a: a.deposit(50) == 150 and a.withdraw(30) == 120
         and str(a).startswith("Bob")),
    ]),
    ("Q6", "Fraction", "Fraction", [
        ((), lambda cls: cls(1,2) + cls(1,3) == cls(5,6)
         and cls(1,2) * cls(2,3) == cls(1,3)),
        ((), lambda cls: cls(2,4) == cls(1,2)),
    ]),
    ("Q7", "温度类", "Temperature", [
        ((), lambda cls: (t := cls(0)) is not None and t.fahrenheit == 32.0
         and (setattr(t, 'fahrenheit', 212)) is None and abs(t.fahrenheit - 212.0) < 0.01),
    ]),
    ("Q8", "复数类", "Complex", [
        ((), lambda cls: cls(1,2)+cls(3,4)==cls(4,6)
         and cls(3,4)-cls(1,2)==cls(2,2)
         and cls(1,0)*cls(0,1)==cls(0,1)),
    ]),
    ("Q9", "计时器", "Timer", [
        ((), lambda t: t.elapsed() >= 0 and (time.sleep(0.02)) is None and t.elapsed() > 0.01),
    ]),
    ("Q10", "TodoList", "TodoList", [
        ((), lambda t: t.add('a') is None and t.add('b') is None and len(t) == 2
         and t.list_all() == ['a','b'] and t.remove('a') is None
         and len(t) == 1 and t.clear() is None and len(t) == 0),
    ]),
    ("Q11", "Person", "Person", [
        ((), lambda cls: (p := cls.from_birth_year('Alice', 2000)) is not None
         and p.name == 'Alice' and p.age == 26 and 'Alice, 26' in str(p)),
    ]),
    ("Q12", "Circle", "Circle", [
        ((), lambda cls: (c := cls(5)) is not None
         and math.isclose(c.area, 78.53975, rel_tol=1e-4)
         and math.isclose(c.circumference, 31.4159, rel_tol=1e-4)),
    ]),
]

def run_test(cls, case):
    args, expected = case
    if len(args) > 0:
        obj = cls(*args)
        return expected(obj), ""
    else:
        # No constructor args: try to instantiate, if works, pass instance
        # for Counter/Timer/TodoList, etc. If fails (requires args), pass class
        try:
            obj = cls()
            ok = expected(obj)
        except Exception:
            ok = expected(cls)
        return ok, "" if ok else "期望满足谓词"

def main():
    sys.path.insert(0, ".")
    import homework
    total = 0
    print("=" * 60)
    print("  Python基础 · 第十一章 · 对象与类 — 自动批改")
    print("=" * 60)
    for qid, title, fn_name, cases in TEST_CASES:
        cls = getattr(homework, fn_name, None)
        if cls is None:
            print(f"\n{qid} [{title}] ❌ 类缺失")
            continue
        passed = 0; errors = []
        for i, case in enumerate(cases, 1):
            try: ok, msg = run_test(cls, case)
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
