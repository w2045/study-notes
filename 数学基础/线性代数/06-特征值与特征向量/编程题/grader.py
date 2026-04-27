"""
线性代数 · 第六章 — 自动批改脚本

用法: python3 grader.py
"""
import math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "特征多项式系数", "char_poly_2x2", [
        (([[3, 0], [0, 5]],), (1.0, -8.0, 15.0)),
        (([[4, 1], [2, 3]],), (1.0, -7.0, 10.0)),
    ]),
    ("Q2", "2x2特征值", "eigenvalues_2x2", [
        (([[3, 0], [0, 5]],), [3.0, 5.0]),
        (([[2, 1], [1, 2]],), [1.0, 3.0]),
    ]),
    ("Q3", "验证特征向量", "is_eigenvector", [
        (([[4, 2], [1, 3]], [2, 1]), 5.0),
        (([[4, 2], [1, 3]], [1, 1]), None),
        (([[3, 0], [0, 5]], [0, 1]), 5.0),
    ]),
    ("Q4", "迹", "trace", [
        (([[1, 2], [3, 4]],), 5.0),
        (([[2, 0], [0, 3]],), 5.0),
    ]),
    ("Q5", "行列式2x2", "determinant_2x2", [
        (([[3, 0], [0, 5]],), 15.0),
        (([[1, 2], [3, 4]],), -2.0),
        (([[2, 1], [1, 2]],), 3.0),
    ]),
    ("Q6", "矩阵-向量乘", "mat_vec_mul", [
        (([[1, 2], [3, 4]], [5, 6]), [17, 39]),
        (([[2, 0], [0, 3]], [1, 1]), [2, 3]),
    ]),
    ("Q7", "对角化验证", "check_diagonalization", [
        (([[2, 1], [1, 2]], [[1, 1], [-1, 1]], [[1, 0], [0, 3]]), True),
        (([[3, 0], [0, 5]], [[1, 0], [0, 1]], [[3, 0], [0, 5]]), True),
    ]),
    ("Q8", "特征值乘积=行列式", "verify_eigenvalue_det", [
        (([[3, 0], [0, 5]],), True),
        (([[4, 1], [2, 3]],), True),
    ]),
    ("Q9", "幂迭代法", "power_iteration", [
        (([[2, 1], [1, 2]],),
         lambda r: (isinstance(r, tuple) and len(r) == 2
                    and abs(r[1] - 3.0) < 1e-6)),
    ]),
    ("Q10", "三角矩阵特征值", "eigenvalues_triangular", [
        (([[2, 5, -3], [0, -1, 4], [0, 0, 6]],), [2.0, -1.0, 6.0]),
        (([[1, 0], [0, 1]],), [1.0, 1.0]),
    ]),
    ("Q11", "Rayleigh商", "rayleigh_quotient", [
        (([[2, 0], [0, 3]], [1, 0]), 2.0),
        (([[2, 0], [0, 3]], [0, 1]), 3.0),
        (([[2, 1], [1, 2]], [1, 1]), 3.0),
    ]),
    ("Q12", "矩阵幂-对角化", "matrix_power_diag", [
        (([[1, 2], [0, -1]], 2), [[1.0, 0.0], [0.0, 1.0]]),
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
    print("  线性代数 · 第六章 · 特征值与特征向量 — 自动批改")
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
