"""
线性代数 · 第一章 — 自动批改脚本

用法: python3 grader.py
"""
import math
import sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "向量加法", "vector_sum", [
        (([1, 2], [3, 4]), [4, 6]),
        (([0, 0], [0, 0]), [0, 0]),
        (([-1, 2], [1, -2]), [0, 0]),
        (([1.5, 2.5], [3.5, 4.5]), [5.0, 7.0]),
    ]),
    ("Q2", "向量减法", "vector_diff", [
        (([5, 7], [2, 3]), [3, 4]),
        (([0, 0], [1, 2]), [-1, -2]),
        (([3, 3], [3, 3]), [0, 0]),
    ]),
    ("Q3", "标量乘法", "scalar_mult", [
        ((3, [1, 2, 3]), [3, 6, 9]),
        ((0, [5, 5]), [0, 0]),
        ((-2, [1, 2]), [-2, -4]),
        ((0.5, [10, 20]), [5.0, 10.0]),
    ]),
    ("Q4", "线性组合", "linear_combination", [
        (([[1, 0], [0, 1]], [3, 4]), [3.0, 4.0]),
        (([[1, 2, 3]], [5]), [5.0, 10.0, 15.0]),
        (([[1, 1], [2, 2]], [3, -1]), [1.0, 1.0]),
        (([[1, 0], [0, 1], [1, 1]], [1, 1, 2]), [3.0, 3.0]),
        (([], []), []),
    ]),
    ("Q5", "零向量判定", "is_zero_vector", [
        (([0, 0, 0],), True),
        (([1, 0, 0],), False),
        (([0.0, 0.0],), True),
        (([1e-10],), True),
    ]),
    ("Q6", "标准基向量", "standard_basis", [
        ((1, 3), [1.0, 0.0, 0.0]),
        ((3, 4), [0.0, 0.0, 1.0, 0.0]),
        ((2, 2), [0.0, 1.0]),
        ((1, 1), [1.0]),
    ]),
    ("Q7", "二维线性无关", "are_independent_2d", [
        (([1, 0], [0, 1]), True),
        (([1, 2], [2, 4]), False),
        (([0, 0], [1, 2]), False),
        (([3, 4], [6, 8]), False),
        (([1, 2], [3, 4]), True),
    ]),
    ("Q8", "span 包含判定", "is_in_span_2d", [
        (([2, 3], [4, 6]), True),
        (([2, 3], [4, 5]), False),
        (([0, 0], [0, 0]), True),
        (([0, 0], [5, 5]), False),
        (([1, 1], [-3, -3]), True),
    ]),
    ("Q9", "含零向量判定", "contains_zero_vector", [
        (([[1, 2], [0, 0], [3, 4]],), True),
        (([[1, 2], [3, 4]],), False),
        (([],), False),
        (([[0.0, 0.0, 0.0]],), True),
    ]),
    ("Q10", "基坐标表示", "coordinates_in_basis", [
        (([[1, 0], [0, 1]], [3, 4]), [3.0, 4.0]),
        (([[1, 1], [1, -1]], [2, 0]), [1.0, 1.0]),
        (([[2, 0], [0, 2]], [3, 5]), [1.5, 2.5]),
        (([[1, 2], [2, 4]], [3, 5]), None),
        (([[0, 0], [1, 1]], [2, 3]), None),
    ]),
    ("Q11", "三维线性无关", "are_independent_3d", [
        (([1, 0, 0], [0, 1, 0], [0, 0, 1]), True),
        (([1, 0, 0], [0, 1, 0], [1, 1, 0]), False),
        (([0, 0, 0], [1, 2, 3], [4, 5, 6]), False),
        (([1, 2, 3], [4, 5, 6], [7, 8, 9]), False),
        (([1, 2, 3], [4, 5, 6], [7, 8, 10]), True),
    ]),
    ("Q12", "扩充为基(二维)", "extend_to_basis_2d", [
        (([1, 0],), lambda r: r is not None and len(r) == 2
         and are_independent_local(r[0], r[1])
         and all(math.isclose(r[0][i], [1, 0][i]) for i in range(2))),
        (([0, 0],), None),
        (([3, 4],), lambda r: r is not None and len(r) == 2
         and are_independent_local(r[0], r[1])
         and all(math.isclose(r[0][i], [3, 4][i]) for i in range(2))),
    ]),
]


def are_independent_local(u: List[float], v: List[float]) -> bool:
    """local helper for Q12 predicates."""
    # check not collinear and not zero
    cross = u[0] * v[1] - u[1] * v[0]
    return not math.isclose(abs(cross), 0)


def list_close(a: Any, b: Any) -> bool:
    if a is None and b is None:
        return True
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        return all(math.isclose(x, y, rel_tol=1e-9) for x, y in zip(a, b))
    if isinstance(a, float) and isinstance(b, float):
        return math.isclose(a, b, rel_tol=1e-9)
    return a == b


def main():
    sys.path.insert(0, ".")
    try:
        import homework
    except (ImportError, SyntaxError) as e:
        print(f"无法导入 homework.py: {e}")
        sys.exit(1)

    total_score = 0
    max_score = len(TEST_CASES)

    print("=" * 60)
    print("  线性代数 · 第一章 · 向量与向量空间 — 自动批改")
    print("=" * 60)

    for qid, title, fn_name, cases in TEST_CASES:
        func = getattr(homework, fn_name, None)
        if func is None:
            print(f"\n{qid} [{title}] 函数 `{fn_name}` 未定义")
            continue

        if not callable(func):
            print(f"\n{qid} [{title}] `{fn_name}` 不是函数")
            continue

        if len(func.__code__.co_code) <= 6:
            print(f"\n{qid} [{title}] 函数体为空 (pass)")
            continue

        passed = 0
        errors = []
        for i, (args, expected) in enumerate(cases, 1):
            try:
                if callable(expected):
                    result = func(*args) if isinstance(args, tuple) else func(args)
                    ok = expected(result)
                    if not ok:
                        errors.append(f"  用例 {i}: 谓词测试未通过, 结果={result}")
                else:
                    result = func(*args) if isinstance(args, tuple) else func(args)
                    if list_close(result, expected):
                        ok = True
                    else:
                        ok = False
                        errors.append(f"  用例 {i}: 期望 {expected}, 得到 {result}")
            except Exception as e:
                errors.append(f"  用例 {i}: {type(e).__name__}: {e}")
                continue
            if ok:
                passed += 1

        if passed == len(cases):
            print(f"\n{qid} [{title}] {passed}/{len(cases)}")
            total_score += 1
        else:
            print(f"\n{qid} [{title}] {passed}/{len(cases)}")
            for e in errors:
                print(e)

    print("\n" + "=" * 60)
    print(f"  总分: {total_score}/{max_score}")
    if total_score == max_score:
        print("  全部正确！")
    else:
        print(f"  还有 {max_score - total_score} 题待修正")
    print("=" * 60)


if __name__ == "__main__":
    main()
