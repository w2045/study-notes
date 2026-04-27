"""
线性代数 · 第二章 — 自动批改脚本

用法: python3 grader.py
"""
import math, sys
from typing import Any, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1", "点积", "dot_product", [
        (([1, 2], [3, 4]), 11),
        (([1, 0], [0, 1]), 0),
        (([2, 2], [2, 2]), 8),
        (([], []), 0),
    ]),
    ("Q2", "ℓ2范数", "norm_l2", [
        (([3, 4],), 5.0),
        (([1, 0, 0],), 1.0),
        (([0, 0],), 0.0),
        (([5, 12],), 13.0),
    ]),
    ("Q3a", "ℓ1范数", "norm_l1", [
        (([3, -4],), 7.0),
        (([1, 2, 3],), 6.0),
        (([0, 0],), 0.0),
    ]),
    ("Q3b", "ℓ∞范数", "norm_linf", [
        (([3, -4, 2],), 4.0),
        (([1, 2, 3],), 3.0),
        (([-5, 0, 3],), 5.0),
    ]),
    ("Q4", "归一化", "normalize", [
        (([3, 4],), [0.6, 0.8]),
        (([0, 0],), None),
        (([5, 0],), [1.0, 0.0]),
    ]),
    ("Q5", "余弦相似度", "cosine_similarity", [
        (([1, 0], [0, 1]), 0.0),
        (([1, 2], [2, 4]), 1.0),
        (([1, 0], [-1, 0]), -1.0),
        (([0, 0], [1, 1]), None),
    ]),
    ("Q6", "正交判定", "is_orthogonal", [
        (([1, 0], [0, 1]), True),
        (([1, 2], [3, 4]), False),
        (([1, 2], [-2, 1]), True),
        (([0, 0], [1, 1]), True),
    ]),
    ("Q7", "正交投影", "projection", [
        (([1, 0], [3, 4]), [3.0, 0.0]),
        (([0, 1], [3, 4]), [0.0, 4.0]),
        (([1, 1], [2, 2]), [2.0, 2.0]),
    ]),
    ("Q8", "Gram-Schmidt一步", "gram_schmidt_step", [
        (([0, 1, 1], [[1, 1, 0]]), [-0.5, 0.5, 1.0]),
        (([1, 2, 3], []), [1, 2, 3]),
    ]),
    ("Q9", "完整Gram-Schmidt", "gram_schmidt", [
        (([[1, 1, 0], [0, 1, 1]],),
         lambda r: len(r) == 2 and all(
             math.isclose(r[0][0], 1) and math.isclose(r[0][1], 1) and math.isclose(r[0][2], 0)
         ) and all(math.isclose(sum(r[0][i]*r[1][i] for i in range(3)), 0))),
    ]),
    ("Q10", "Cauchy-Schwarz验证", "satisfies_cauchy_schwarz", [
        (([1, 2], [3, 4]), True),
        (([1, 2], [2, 4]), True),  # 等号成立（共线）
    ]),
    ("Q11", "三角不等式验证", "satisfies_triangle", [
        (([1, 2], [3, 4]), True),
        (([1, 0], [2, 0]), True),
    ]),
    ("Q12", "正交向量组判定", "is_orthogonal_set", [
        (([[1, 0], [0, 1]],), True),
        (([[1, 0], [1, 1]],), False),
        (([[1, 0, 0], [0, 1, 0], [0, 0, 1]],), True),
        (([[0, 0], [1, 1]],), False),
    ]),
]


def list_close(a, b):
    if a is None and b is None: return True
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b): return False
        return all(math.isclose(x, y, rel_tol=1e-9) for x, y in zip(a, b))
    if isinstance(a, float) and isinstance(b, float):
        return math.isclose(a, b, rel_tol=1e-9)
    return a == b


def main():
    sys.path.insert(0, ".")
    try: import homework
    except (ImportError, SyntaxError) as e:
        print(f"无法导入: {e}"); sys.exit(1)

    total = 0; max_s = len(TEST_CASES)
    print("=" * 60)
    print("  线性代数 · 第二章 · 内积空间、范数与正交性 — 自动批改")
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
