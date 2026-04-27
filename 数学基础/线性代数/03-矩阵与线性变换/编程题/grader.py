"""
线性代数 · 第三章 — 自动批改脚本

用法: python3 grader.py
"""
import math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "矩阵-向量乘法", "mat_vec_mul", [
        (([[1, 2], [3, 4]], [5, 6]), [17, 39]),
        (([[1, 0, 0], [0, 1, 0]], [1, 2, 3]), [1, 2]),
        (([[2, -1], [0, 3], [1, 1]], [1, 2]), [0, 6, 3]),
    ]),
    ("Q2", "矩阵乘法", "mat_mul", [
        (([[1, 2], [3, 4]], [[0, 1], [1, 0]]), [[2, 1], [4, 3]]),
        (([[1, 0, 2], [0, 1, 1]], [[1, 0], [0, 1], [1, 1]]), [[3, 2], [1, 2]]),
        (([[1, 0], [0, 1]], [[5, 6], [7, 8]]), [[5, 6], [7, 8]]),
    ]),
    ("Q3", "矩阵转置", "transpose", [
        (([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]]),
        (([[1, 2], [3, 4]],), [[1, 3], [2, 4]]),
        (([[5]],), [[5]]),
    ]),
    ("Q4", "对称反对称分解", "sym_skew_split", [
        (([[1, 3], [-1, 2]],),
         lambda r: (isinstance(r, tuple) and len(r) == 2
                    and all(math.isclose(r[0][i][j], [[1,1],[1,2]][i][j]) for i in range(2) for j in range(2))
                    and all(math.isclose(r[1][i][j], [[0,2],[-2,0]][i][j]) for i in range(2) for j in range(2)))),
    ]),
    ("Q5", "单位矩阵", "identity", [
        ((3,), [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]),
        ((1,), [[1.0]]),
    ]),
    ("Q6", "迹", "trace", [
        (([[1, 2], [3, 4]],), 5.0),
        (([[1, 0, 0], [0, 2, 0], [0, 0, 3]],), 6.0),
        (([[5]],), 5.0),
    ]),
    ("Q7", "对称矩阵判定", "is_symmetric", [
        (([[1, 2], [2, 1]],), True),
        (([[1, 2], [3, 4]],), False),
        (([[1, 0, 2], [0, 1, 3], [2, 3, 1]],), True),
    ]),
    ("Q8", "正交矩阵判定", "is_orthogonal", [
        (([[1, 0], [0, 1]],), True),
        (([[0, -1], [1, 0]],), True),
        (([[1, 1], [1, -1]],), False),
        (([[0.6, 0.8], [-0.8, 0.6]],), True),
    ]),
    ("Q9", "Frobenius范数", "frobenius_norm", [
        (([[3, 0], [0, 4]],), 5.0),
        (([[1, 2], [3, 4]],), math.sqrt(30)),
        (([[0, 0], [0, 0]],), 0.0),
    ]),
    ("Q10", "对角矩阵生成", "diag_matrix", [
        (([1, 2, 3],), [[1.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 3.0]]),
        (([5],), [[5.0]]),
    ]),
    ("Q11", "Kronecker积", "kronecker", [
        (([[1, 0], [0, 1]], [[1, 2], [3, 4]]),
         [[1.0, 2.0, 0.0, 0.0], [3.0, 4.0, 0.0, 0.0], [0.0, 0.0, 1.0, 2.0], [0.0, 0.0, 3.0, 4.0]]),
        (([[1]], [[2, 3], [4, 5]]), [[2.0, 3.0], [4.0, 5.0]]),
    ]),
    ("Q12", "线性变换复合", "compose_transforms", [
        (([[0, -1], [1, 0]], [[2, 0], [0, 1]], [1, 1]), [-1.0, 2.0]),
        (([[1, 0], [0, 1]], [[1, 2], [3, 4]], [1, 0]), [1, 3]),
    ]),
]


def list_close(a, b):
    if a is None and b is None: return True
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b): return False
        return all(list_close(x, y) for x, y in zip(a, b))
    if isinstance(a, float) and isinstance(b, float):
        return math.isclose(a, b, rel_tol=1e-9)
    if isinstance(a, int) and isinstance(b, float):
        return math.isclose(a, b, rel_tol=1e-9)
    if isinstance(a, float) and isinstance(b, int):
        return math.isclose(a, b, rel_tol=1e-9)
    return a == b


def main():
    sys.path.insert(0, ".")
    try: import homework
    except (ImportError, SyntaxError) as e:
        print(f"无法导入: {e}"); sys.exit(1)

    total = 0; max_s = len(TEST_CASES)
    print("=" * 60)
    print("  线性代数 · 第三章 · 矩阵与线性变换 — 自动批改")
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
