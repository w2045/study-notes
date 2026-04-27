"""
线性代数 · 第八章 — 自动批改脚本

用法: python3 grader.py
"""
import math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "二次型计算", "quadratic_form", [
        (([[2, 0], [0, 3]], [1, 1]), 5.0),
        (([[1, 2], [2, 1]], [1, 0]), 1.0),
    ]),
    ("Q2", "正定性(特征值)", "is_positive_definite_eigen", [
        (([[3, 0], [0, 1]],), True),
        (([[1, 2], [2, 1]],), False),
        (([[2, -1], [-1, 2]],), True),
    ]),
    ("Q3", "Sylvester判据", "is_positive_definite_sylvester", [
        (([[4, 1], [1, 1]],), True),
        (([[1, 2], [2, 0]],), False),
    ]),
    ("Q4", "直线投影", "project_onto_line", [
        (([1, 0], [3, 4]), [3.0, 0.0]),
        (([2, 1], [2, 2]), [2.4, 1.2]),
    ]),
    ("Q5", "Cholesky 2x2", "cholesky_2x2", [
        (([[4, 2], [2, 5]],), [[2.0, 0.0], [1.0, 2.0]]),
        (([[1, 2], [2, 1]],), None),
    ]),
    ("Q6", "投影矩阵", "projection_matrix", [
        (([[1, 0], [0, 1], [0, 0]],),
         lambda r: all(math.isclose(r[i][j], [[1,0,0],[0,1,0],[0,0,0]][i][j]) for i in range(3) for j in range(3))),
    ]),
    ("Q7", "最小二乘(正规方程)", "least_squares", [
        (([[1, 0], [0, 1], [0, 0]], [2, 3, 4]), [2.0, 3.0]),
    ]),
    ("Q8", "Gram-Schmidt Q", "gram_schmidt_q", [
        (([[3, 0], [4, 5]],),
         lambda r: len(r) == 2 and len(r[0]) == 2 and all(
             math.isclose(sum(r[j][i]**2 for j in range(2)), 1.0) for i in range(2))),
    ]),
    ("Q9", "QR分解", "qr_decomposition", [
        (([[3, 0], [4, 5]],),
         lambda r: (isinstance(r, tuple) and len(r) == 2
                    and all(math.isclose(sum(sum(r[0][j][i]**2 for j in range(2)) for i in range(2)), 2.0)))),
    ]),
    ("Q10", "最小二乘(QR)", "least_squares_qr", [
        (([[1, 1], [1, 2], [1, 3]], [1, 2, 2]),
         lambda r: all(math.isclose(r[i], [2/3, 0.5][i], rel_tol=1e-4) for i in range(2))),
    ]),
    ("Q11", "投影幂等性", "is_projection", [
        (([[1, 0], [0, 0]],), True),
        (([[1, 0], [0, 1]],), True),
        (([[1, 1], [0, 0]],), False),
    ]),
    ("Q12", "Cholesky n×n", "cholesky", [
        (([[4, 2, 2], [2, 5, 1], [2, 1, 6]],),
         lambda r: r is not None and len(r) == 3 and len(r[0]) == 3 and all(
             math.isclose(r[i][i], [2, 2, math.sqrt(5)][i], rel_tol=1e-6) for i in range(3))),
    ]),
]


def list_close(a, b):
    if a is None and b is None: return True
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b): return False
        return all(list_close(x, y) for x, y in zip(a, b))
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(float(a), float(b), rel_tol=1e-9)
    return a == b


def main():
    sys.path.insert(0, ".")
    try: import homework
    except (ImportError, SyntaxError) as e:
        print(f"无法导入: {e}"); sys.exit(1)

    total = 0; max_s = len(TEST_CASES)
    print("=" * 60)
    print("  线性代数 · 第八章 · 正定矩阵、投影与QR分解 — 自动批改")
    print("=" * 60)

    for qid, title, fn_name, cases in TEST_CASES:
        func = getattr(homework, fn_name, None)
        if func is None: print(f"\n{qid} [{title}] 函数未定义"); continue
        if len(func.__code__.co_code) <= 6: print(f"\n{qid} [{title}] 空函数"); continue
        passed = 0; errors = []
        for i, (args, expected) in enumerate(cases, 1):
            try:
                if callable(expected):
                    result = func(*args) if isinstance(args, tuple) else func(args)
                    ok = expected(result)
                    if not ok: errors.append(f"  用例{i}: 谓词失败, 结果={result}")
                else:
                    result = func(*args) if isinstance(args, tuple) else func(args)
                    if list_close(result, expected): ok = True
                    else: ok = False; errors.append(f"  用例{i}: 期望 {expected}, 得 {result}")
            except Exception as e: errors.append(f"  用例{i}: {type(e).__name__}: {e}"); continue
            if ok: passed += 1
        if passed == len(cases): print(f"\n{qid} [{title}] {passed}/{len(cases)}"); total += 1
        else:
            print(f"\n{qid} [{title}] {passed}/{len(cases)}")
            for e in errors: print(e)

    print(f"\n{'=' * 60}\n  总分: {total}/{max_s}\n{'=' * 60}")


if __name__ == "__main__":
    main()
