"""
线性代数 · 第九章 — 自动批改脚本

用法: python3 grader.py
"""
import math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "矩阵转置", "transpose", [
        (([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]]),
    ]),
    ("Q2", "矩阵-向量乘", "mat_vec_mul", [
        (([[1, 2], [3, 4]], [5, 6]), [17, 39]),
    ]),
    ("Q3", "矩阵乘法", "mat_mul", [
        (([[1, 2], [3, 4]], [[0, 1], [1, 0]]), [[2, 1], [4, 3]]),
    ]),
    ("Q4", "向量范数", "norm", [
        (([3, 4],), 5.0),
        (([0, 0],), 0.0),
    ]),
    ("Q5", "幂迭代SVD", "power_iteration_svd", [
        (([[3, 0], [4, 5]],),
         lambda r: isinstance(r, tuple) and len(r) == 3 and r[2] > 4.0),
    ]),
    ("Q6", "A^T A", "compute_AtA", [
        (([[1, 0], [0, 2], [0, 0]],), [[1, 0], [0, 4]]),
    ]),
    ("Q7", "谱范数", "spectral_norm", [
        (([[3, 0], [0, 2]],), 3.0),
    ]),
    ("Q8", "Frobenius范数", "frobenius_norm", [
        (([[3, 0], [0, 4]],), 5.0),
        (([[1, 2], [3, 4]],), math.sqrt(30)),
    ]),
    ("Q9", "低秩近似", "low_rank_approx", [
        (([[0.6, -0.8], [0.8, 0.6]], [5.0, 3.0], [[0.6, 0.8], [-0.8, 0.6]], 1),
         [[1.8, 2.4], [2.4, 3.2]]),
    ]),
    ("Q10", "SVD重构误差", "svd_reconstruction_error", [
        (([[3, 0], [4, 5]], [[0.6, -0.8], [0.8, 0.6]], [6.0, 2.0],
          [[0.6, 0.8], [-0.8, 0.6]], 1),
         lambda r: abs(r - 2.0) < 0.5),
    ]),
    ("Q11", "条件数", "condition_number", [
        (([5.0, 3.0],), 5.0/3.0),
        (([100.0, 0.01],), 10000.0),
    ]),
    ("Q12", "压缩比", "compress_ratio", [
        ((100, 100, 10), 10000 / (10 * 201)),
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
    print("  线性代数 · 第九章 · 奇异值分解 SVD — 自动批改")
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
