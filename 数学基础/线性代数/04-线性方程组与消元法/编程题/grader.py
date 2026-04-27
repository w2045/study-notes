"""
线性代数 · 第四章 — 自动批改脚本

用法: python3 grader.py
"""
import math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "增广矩阵构造", "make_augmented", [
        (([[1, 2], [3, 4]], [5, 6]), [[1, 2, 5], [3, 4, 6]]),
        (([[1, 0], [0, 1]], [0, 0]), [[1, 0, 0], [0, 1, 0]]),
    ]),
    ("Q2", "行交换", "row_swap", [
        (([[1, 2], [3, 4]], 0, 1), [[3, 4], [1, 2]]),
        (([[1, 2, 3], [4, 5, 6]], 0, 0), [[1, 2, 3], [4, 5, 6]]),
    ]),
    ("Q3", "行缩放", "row_scale", [
        (([[1, 2], [3, 4]], 0, 2.0), [[2.0, 4.0], [3, 4]]),
        (([[1, 0], [0, 1]], 1, 0.5), [[1, 0], [0.0, 0.5]]),
    ]),
    ("Q4", "行加减", "row_add", [
        (([[1, 2], [3, 4]], 1, 0, -3.0), [[1, 2], [0.0, -2.0]]),
        (([[1, 0], [0, 1]], 0, 1, 2.0), [[1.0, 2.0], [0, 1]]),
    ]),
    ("Q5", "前向消元无主元", "forward_elimination", [
        (([[1, 2], [3, 4]], [5, 11]),
         lambda r: (isinstance(r, tuple) and len(r) == 2
                    and all(math.isclose(r[0][0][0], 1) and math.isclose(r[0][0][1], 2)
                            and math.isclose(r[0][1][0], 0) and math.isclose(r[0][1][1], -2))
                    and all(math.isclose(r[1][0], 5) and math.isclose(r[1][1], -4)))),
    ]),
    ("Q6", "回代", "back_substitution", [
        (([[1, 2], [0, -2]], [5, -4]), [1.0, 2.0]),
        (([[1, 2, 1], [0, 1, 3], [0, 0, 2]], [4, 7, 2]), [-3.0, 4.0, 1.0]),
        (([[1, 0], [0, 0]], [3, 1]), None),
    ]),
    ("Q7", "列主元前向消元", "forward_elimination_pivot", [
        (([[0.0001, 1], [1, 1]], [1, 2]),
         lambda r: (isinstance(r, tuple) and len(r) == 2
                    and abs(r[0][0][0]) > 0.9)),  # 大元素应该被换到第一行
    ]),
    ("Q8", "LU分解", "lu_decomposition", [
        (([[2, 1], [6, 8]],),
         lambda r: (isinstance(r, tuple) and len(r) == 2
                    and all(math.isclose(r[0][i][j], [[1,0],[3,1]][i][j]) for i in range(2) for j in range(2))
                    and all(math.isclose(r[1][i][j], [[2,1],[0,5]][i][j]) for i in range(2) for j in range(2)))),
    ]),
    ("Q9", "前代", "forward_substitution", [
        (([[1, 0], [3, 1]], [3, 10]), [3.0, 1.0]),
        (([[1, 0, 0], [2, 1, 0], [3, 4, 1]], [3, 10, 19]), [3.0, 4.0, -6.0]),
    ]),
    ("Q10", "完整高斯消元", "gaussian_solve", [
        (([[1, 2, 1], [2, 6, 1], [1, 1, 4]], [2, 7, 3]), [-3.0, 2.0, 1.0]),
        (([[1, 2], [3, 4]], [5, 11]), [1.0, 2.0]),
    ]),
    ("Q11", "判断解的情况", "classify_solution", [
        (([[1, 0], [0, 1]], [3, 4]), 'unique'),
        (([[1, 2], [0, 0]], [3, 0]), 'infinite'),
        (([[1, 2], [0, 0]], [3, 1]), 'none'),
    ]),
    ("Q12", "LU求解", "lu_solve", [
        (([[1, 0], [3, 1]], [[2, 1], [0, 5]], [3, 10]), [1.0, 1.0]),
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
    print("  线性代数 · 第四章 · 线性方程组与消元法 — 自动批改")
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
