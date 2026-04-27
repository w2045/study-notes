"""
线性代数 · 第一章 — 自动批改脚本

用法: python3 grader.py
"""

import math
import sys
from typing import Any, Callable, List, Tuple

TEST_CASES: List[Tuple[str, str, str, List[Tuple[tuple, Any]]]] = [
    ("Q1a", "向量加法", "vector_sum", [
        (([1, 2], [3, 4]), [4, 6]),
        (([0, 0], [0, 0]), [0, 0]),
        (([-1, 2], [1, -2]), [0, 0]),
        (([1.5, 2.5], [3.5, 4.5]), [5.0, 7.0]),
    ]),
    ("Q1b", "向量减法", "vector_diff", [
        (([5, 7], [2, 3]), [3, 4]),
        (([0, 0], [1, 2]), [-1, -2]),
        (([3, 3], [3, 3]), [0, 0]),
    ]),
    ("Q2", "标量乘法", "scalar_mult", [
        ((3, [1, 2, 3]), [3, 6, 9]),
        ((0, [5, 5]), [0, 0]),
        ((-2, [1, 2]), [-2, -4]),
        ((0.5, [10, 20]), [5.0, 10.0]),
    ]),
    ("Q3", "欧几里得范数", "euclidean_norm", [
        (([3, 4],), 5.0),
        (([1, 0, 0],), 1.0),
        (([0, 0],), 0.0),
        (([5, 12],), 13.0),
        (([1, 1, 1, 1],), 2.0),
    ]),
    ("Q4", "点积", "dot_product", [
        (([1, 2], [3, 4]), 11),
        (([1, 0], [0, 1]), 0),
        (([2, 2], [2, 2]), 8),
        (([1, 2, 3], [4, 5, 6]), 32),
        (([], []), 0),
    ]),
    ("Q5", "归一化", "normalize", [
        (([3, 4],), [0.6, 0.8]),
        (([0, 0],), None),
        (([5, 0],), [1.0, 0.0]),
        (([1, 1],), [1/math.sqrt(2), 1/math.sqrt(2)]),
    ]),
    ("Q6", "余弦相似度", "cosine_similarity", [
        (([1, 0], [0, 1]), 0.0),
        (([1, 2], [2, 4]), 1.0),
        (([1, 0], [-1, 0]), -1.0),
        (([0, 0], [1, 1]), None),
        (([1, 1], [0, 0]), None),
    ]),
    ("Q7", "判断正交性", "is_orthogonal", [
        (([1, 0], [0, 1]), True),
        (([1, 2], [3, 4]), False),
        (([1, 2], [-2, 1]), True),
        (([0, 0], [1, 1]), True),     # 零向量与任何向量正交 (内积=0)
    ]),
    ("Q8", "检查子空间条件", "is_subspace_candidate", [
        (([[1, 2], [0, 0], [3, 4]],), True),
        (([[1, 2], [3, 4]],), False),
        (([],), False),
        (([[0.0, 0.0]],), True),
    ]),
    ("Q9", "线性组合", "linear_combination", [
        (([[1, 0], [0, 1]], [3, 4]), [3.0, 4.0]),
        (([[1, 2, 3]], [5]), [5.0, 10.0, 15.0]),
        (([[1, 1], [2, 2]], [3, -1]), [1.0, 1.0]),
        (([[1, 0], [0, 1], [1, 1]], [1, 1, 2]), [3.0, 3.0]),
    ]),
    ("Q10", "判断共线性 (二维)", "are_collinear_2d", [
        (([1, 2], [2, 4]), True),
        (([1, 2], [3, 4]), False),
        (([0, 0], [1, 2]), True),
        (([1, 0], [-5, 0]), True),
    ]),
    ("Q11", "平行四边形面积", "span_area_2d", [
        (([1, 0], [0, 1]), 1.0),
        (([3, 0], [0, 4]), 12.0),
        (([1, 2], [2, 4]), 0.0),
        (([2, 1], [1, 3]), 5.0),
    ]),
    ("Q12", "三角形判定 (向量)", "is_triangle_vector", [
        (([0, 0], [1, 0], [0, 1]), True),
        (([0, 0], [1, 1], [2, 2]), False),
        (([1, 1], [1, 1], [2, 3]), False),
        (([0, 0], [3, 0], [0, 4]), True),
    ]),
]


def list_close(a: Any, b: Any) -> bool:
    """比较 float list 或 float/None。"""
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
        print(f"❌ 无法导入 homework.py: {e}")
        sys.exit(1)

    total_score = 0
    max_score = len(TEST_CASES)

    print("=" * 60)
    print("  线性代数 · 第一章 · 向量与向量空间 — 自动批改")
    print("=" * 60)

    for qid, title, fn_name, cases in TEST_CASES:
        func = getattr(homework, fn_name, None)
        if func is None:
            print(f"\n{qid} [{title}] ❌ 函数 `{fn_name}` 未定义")
            continue

        # 检查空函数体
        if len(func.__code__.co_code) <= 6:
            print(f"\n{qid} [{title}] ⚠️  函数体为空 (pass)")
            continue

        passed = 0
        errors = []
        for i, (args, expected) in enumerate(cases, 1):
            try:
                result = func(*args) if isinstance(args, tuple) else func(args)
            except Exception as e:
                errors.append(f"  用例 {i}: 抛出 {type(e).__name__}: {e}")
                continue
            if list_close(result, expected):
                passed += 1
            else:
                errors.append(f"  用例 {i}: 期望 {expected}, 得到 {result}")

        if passed == len(cases):
            print(f"\n{qid} [{title}] ✅ {passed}/{len(cases)}")
            total_score += 1
        else:
            print(f"\n{qid} [{title}] ❌ {passed}/{len(cases)}")
            for e in errors:
                print(e)

    print("\n" + "=" * 60)
    print(f"  总分: {total_score}/{max_score}")
    if total_score == max_score:
        print("  🎉 全部正确！")
    else:
        print(f"  还有 {max_score - total_score} 题待修正")
    print("=" * 60)


if __name__ == "__main__":
    main()
