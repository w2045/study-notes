"""
第一章 · 表达式与函数 — 自动批改脚本

用法:
    python3 grader.py

对 homework.py 中的每道题运行测试用例，输出 ✅/❌ 和得分。
"""

import math
import sys
from typing import Any, Callable, List, Tuple

# ─── 测试用例定义 ───
# 格式: 每道题 = (题号, 标题, 函数名, [(参数, 期望输出), ...])

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    (
        "Q1", "华氏度转摄氏", "f_to_c",
        [
            ((32,), 0.0),
            ((212,), 100.0),
            ((98.6,), 37.0),
            ((-40,), -40.0),
            ((0,), round((0 - 32) * 5 / 9, 1)),
        ]
    ),
    (
        "Q2", "判断偶数", "is_even",
        [
            ((4,), True),
            ((7,), False),
            ((0,), True),
            ((-2,), True),
            ((-3,), False),
            ((100,), True),
            ((101,), False),
        ]
    ),
    (
        "Q3", "球体积", "sphere_volume",
        [
            ((1,), (4/3) * math.pi * 1**3),
            ((3,), (4/3) * math.pi * 27),
            ((0,), 0.0),
        ]
    ),
    (
        "Q4", "三个数的中间值", "middle",
        [
            ((1, 2, 3), 2),
            ((3, 2, 1), 2),
            ((5, 1, 9), 5),
            ((1, 5, 9), 5),
            ((9, 5, 1), 5),
            ((3, 3, 1), 3),
            ((7, 7, 7), 7),
            ((-5, 0, 5), 0),
        ]
    ),
    (
        "Q5", "编写 doctest", "add_and_double",
        [
            ((2, 3), 10),
            ((0, 0), 0),
            ((-1, 1), 0),
            ((-2, -3), -10),
        ]
    ),
    (
        "Q6", "自由落体时间", "fall_time",
        [
            ((0,), 0.0),
            ((4.9,), 1.0),
            ((19.6,), 2.0),
            ((44.1,), 3.0),
        ]
    ),
    (
        "Q7", "判断三角形", "is_triangle",
        [
            ((3, 4, 5), True),
            ((1, 1, 3), False),
            ((5, 5, 5), True),
            ((0, 4, 5), False),
            ((2, 2, 3), True),
            ((10, 1, 1), False),
        ]
    ),
    (
        "Q8", "数字反转", "reverse_digits",
        [
            ((37,), 73),
            ((90,), 9),
            ((10,), 1),
            ((99,), 99),
            ((21,), 12),
        ]
    ),
    (
        "Q9", "距离公式", "distance",
        [
            ((0, 0, 3, 4), 5.0),
            ((1, 2, 4, 6), 5.0),
            ((0, 0, 0, 0), 0.0),
            ((1, 1, 1, 1), 0.0),
            ((-1, -1, 2, 3), 5.0),
        ]
    ),
    (
        "Q10", "找 bug (square_of_sum)", "square_of_sum",
        [
            ((2, 3), 25),
            ((1, 4), 25),
            ((0, 5), 25),
            ((-1, 1), 0),
            ((-2, -3), 25),
        ]
    ),
    (
        "Q11", "四舍五入", "round_to",
        [
            ((3.14159, 2), 3.14),
            ((3.14159, 4), 3.1416),
            ((2.5, 0), 3.0),
            ((1.2345, 3), 1.235),
            ((9.8765, 2), 9.88),
        ]
    ),
    (
        "Q12", "二次方程求根", "solve_quadratic",
        [
            ((1, -3, 2), (1.0, 2.0)),
            ((1, -2, 1), (1.0, 1.0)),
            ((1, 0, 1), None),
            ((2, 5, -3), (-3.0, 0.5)),
            ((1, -5, 6), (2.0, 3.0)),
            ((1, 0, -4), (-2.0, 2.0)),
        ]
    ),
]


def is_close(a: Any, b: Any) -> bool:
    """安全比较两个值: 浮点数用 math.isclose, 其余用 ==。"""
    if isinstance(a, float) and isinstance(b, float):
        return math.isclose(a, b, rel_tol=1e-9)
    if isinstance(a, tuple) and isinstance(b, tuple):
        if len(a) != len(b):
            return False
        return all(is_close(x, y) for x, y in zip(a, b))
    return a == b


def grade_one(func: Callable, cases: List[Tuple[tuple, Any]]) -> Tuple[int, int, List[str]]:
    """跑一道题的所有测试用例。返回 (通过数, 总数, 错误消息列表)。"""
    passed, total = 0, len(cases)
    errors: List[str] = []

    for i, (args, expected) in enumerate(cases, 1):
        try:
            result = func(*args)
        except Exception as e:
            errors.append(f"  用例 {i} {args!r}: 抛出异常 {type(e).__name__}: {e}")
            continue

        if is_close(result, expected):
            passed += 1
        else:
            errors.append(f"  用例 {i} {args!r}: 期望 {expected!r}, 得到 {result!r}")

    return passed, total, errors


def main():
    # 动态导入 homework
    sys.path.insert(0, ".")
    try:
        import homework
    except ImportError as e:
        print(f"❌ 无法导入 homework.py: {e}")
        sys.exit(1)
    except SyntaxError as e:
        print(f"❌ homework.py 语法错误: {e}")
        sys.exit(1)

    total_score = 0
    max_score = len(TEST_CASES)

    print("=" * 60)
    print("  第一章 · 表达式与函数 — 自动批改")
    print("=" * 60)

    for qid, title, func_name, cases in TEST_CASES:
        func = getattr(homework, func_name, None)

        if func is None:
            print(f"\n{qid} [{title}] ❌ 函数 `{func_name}` 未定义")
            continue

        # 检查是否只写了 pass 但没实现
        src = func.__code__.co_code
        if len(src) <= 6:  # 空函数只有 LOAD_CONST + RETURN_VALUE for None
            print(f"\n{qid} [{title}] ⚠️  函数体为空 (pass), 跳过测试")
            continue

        passed, total, errors = grade_one(func, cases)

        if passed == total:
            print(f"\n{qid} [{title}] ✅ {passed}/{total} 全部通过")
            total_score += 1
        else:
            print(f"\n{qid} [{title}] ❌ {passed}/{total} 通过")
            for err in errors:
                print(err)

    print("\n" + "=" * 60)
    print(f"  总分: {total_score}/{max_score}")
    if total_score == max_score:
        print("  🎉 全部正确！干得漂亮！")
    else:
        remaining = max_score - total_score
        print(f"  还有 {remaining} 题待修正，加油！")
    print("=" * 60)


if __name__ == "__main__":
    main()
