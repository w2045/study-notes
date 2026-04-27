"""Python基础 · 第十二章 — 自动批改"""
import math, sys
from typing import Any, List, Tuple
from abc import ABC, abstractmethod

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "基本继承", "Animal", [
        ((), lambda cls: (d := cls.__subclasses__()) is not None and len(d) >= 2),
    ]),
    ("Q1b", "Dog", "Dog", [
        ((), lambda cls: cls("Rex").speak() == "woof"),
    ]),
    ("Q1c", "Cat", "Cat", [
        ((), lambda cls: cls("Kitty").speak() == "meow"),
    ]),
    ("Q2", "super init", "Student", [
        (("Alice", 20, "MIT"), lambda s: str(s) == "Alice (20) - MIT"),
    ]),
    ("Q3", "isinstance", "count_animals", [
        (([],), 0),
    ]),
    ("Q4", "方法重写", "Square", [
        ((3,), lambda s: s.area() == 9 and s.description() == "I am a shape"),
    ]),
    ("Q4b", "Circle面积", "Circle", [
        ((5,), lambda c: math.isclose(c.area(), 78.53975, rel_tol=1e-4)),
    ]),
    ("Q6", "Vehicle继承", "Car", [
        (("Toyota", "Camry"), lambda c: c.info() == "Toyota Camry"),
    ]),
    ("Q7", "CEO薪资", "CEO", [
        (("Alice", 80000, 20000), lambda c: c.get_salary() == 120000),
    ]),
    ("Q8", "多态", "all_speak", [
        (([],), []),
    ]),
    ("Q9", "抽象基类", "WashingMachine", [
        ((), lambda cls: issubclass(cls, ABC) and hasattr(cls, 'turn_on')),
    ]),
    ("Q10", "自定义异常", "withdraw", [
        ((100, 30), 70),
    ]),
    ("Q12", "组合", "Car2", [
        ((), lambda cls: (c := cls()) is not None and "started" in c.start()),
    ]),
]

def _brief(x):
    s = str(x); return s[:60] + "..." if len(s) > 60 else s

def run_test(func, case):
    args, expected = case
    if callable(expected):
        if isinstance(func, type) and len(args) == 0:
            # Class with predicate, no args
            try:
                obj = func()
                ok = expected(obj)
            except Exception:
                ok = expected(func)
        elif isinstance(func, type):
            obj = func(*args)
            ok = expected(obj)
        elif len(args) == 0:
            ok = expected(func)
        else:
            result = func(*args)
            ok = expected(result)
        return ok, "" if ok else "期望满足谓词"
    if isinstance(func, type):
        obj = func(*args) if args else func()
        result = obj
        ok = result == expected
    else:
        result = func(*args)
        ok = math.isclose(result, expected, rel_tol=1e-9) if isinstance(expected, float) else result == expected
    return ok, "" if ok else f"期望 {expected}, 得 {_brief(result)}"

def main():
    sys.path.insert(0, ".")
    import homework
    total = 0
    q1_parts = ["Q1", "Q1b", "Q1c"]
    q4_parts = ["Q4", "Q4b"]
    skip_score = set(q1_parts[1:] + q4_parts[1:] + ["Q1c"])  # sub-parts don't count separately
    # Actually let me simplify: Q1 counts as 1 (needs all 3), Q4 counts as 1 (needs both)
    print("=" * 60)
    print("  Python基础 · 第十二章 · 继承 — 自动批改")
    print("=" * 60)

    # Q3 special: needs Dog/Cat imported
    try:
        Dog = getattr(homework, "Dog", None)
        Cat = getattr(homework, "Cat", None)
        Animal = getattr(homework, "Animal", None)
    except: pass

    max_s = 10  # Q1, Q2, Q3, Q4, Q6, Q7, Q8, Q9, Q10, Q12
    results = {}
    for qid, title, fn_name, cases in TEST_CASES:
        func = getattr(homework, fn_name, None)
        if func is None:
            results[qid] = (f"❌ 缺失", 0, len(cases))
            continue
        if not isinstance(func, type) and callable(func) and len(func.__code__.co_code) <= 6:
            results[qid] = ("⚠️ 空函数", 0, len(cases))
            continue
        passed = 0; errors = []
        for i, case in enumerate(cases, 1):
            try: ok, msg = run_test(func, case)
            except Exception as e: errors.append(f"  用例{i}: {e}"); continue
            if ok: passed += 1
            else: errors.append(f"  用例{i}: {msg}")
        if passed == len(cases):
            results[qid] = (f"✅ {passed}/{len(cases)}", 1, len(cases))
        else:
            results[qid] = (f"❌ {passed}/{len(cases)}", 0, len(cases))
            for e in errors: results[qid] = (results[qid][0], results[qid][1], results[qid][2])

    # Print results
    q1_ok = results.get("Q1", ("", 0, 0))[1] + results.get("Q1b", ("", 0, 0))[1] + results.get("Q1c", ("", 0, 0))[1]
    q1_total = 3
    print(f"\nQ1 [基本继承] {'✅' if q1_ok >= 2 else '❌'} ({q1_ok}/{q1_total} pass)")
    total += (1 if q1_ok >= 2 else 0)

    for qid, title in [("Q2", "super init"), ("Q3", "isinstance"), ("Q4", "方法重写"),
                        ("Q6", "Vehicle继承"), ("Q7", "CEO薪资"), ("Q8", "多态"),
                        ("Q9", "抽象基类"), ("Q10", "自定义异常"), ("Q12", "组合")]:
        if qid == "Q3":
            # Test count_animals with actual Animal instances
            fn = getattr(homework, "count_animals", None)
            if fn and Dog and Cat and Animal:
                try:
                    r = fn([Dog("a"), Cat("b"), 42])
                    ok = (r == 2)
                    print(f"\n{qid} [{title}] {'✅' if ok else '❌'} 1/1")
                    total += (1 if ok else 0)
                except Exception as e:
                    print(f"\n{qid} [{title}] ❌ {e}")
            else:
                print(f"\n{qid} [{title}] ❌ 无法测试")
            continue
        if qid == "Q4":
            q4_ok = results.get("Q4", ("", 0, 0))[1] + results.get("Q4b", ("", 0, 0))[1]
            print(f"\n{qid} [{title}] {'✅' if q4_ok == 2 else '❌'} 2/2")
            total += (1 if q4_ok == 2 else 0)
            continue
        if qid == "Q8":
            fn = getattr(homework, "all_speak", None)
            if fn and Dog and Cat:
                try:
                    r = fn([Dog("a"), Cat("b")])
                    ok = (r == ["woof", "meow"])
                    print(f"\n{qid} [{title}] {'✅' if ok else '❌'} 1/1")
                    total += (1 if ok else 0)
                except Exception as e:
                    print(f"\n{qid} [{title}] ❌ {e}")
            else:
                print(f"\n{qid} [{title}] ❌ 无法测试")
            continue
        if qid == "Q9":
            # Check abstract classes
            WM = getattr(homework, "WashingMachine", None)
            Ref = getattr(homework, "Refrigerator", None)
            if WM and Ref:
                ok = issubclass(WM, ABC) and issubclass(Ref, ABC)
                print(f"\n{qid} [{title}] {'✅' if ok else '❌'} 1/1")
                total += (1 if ok else 0)
            else:
                print(f"\n{qid} [{title}] ❌ 类缺失")
            continue
        r = results.get(qid, (f"❌ 缺失", 0, 0))
        print(f"\n{qid} [{title}] {r[0]}")
        total += r[1]

    print(f"\n{'=' * 60}\n  总分: {total}/{max_s}\n{'=' * 60}")

if __name__ == "__main__":
    main()
