# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("x, y, z, expected", [
    pytest.param(250, 5, 50, 1), (1050, 25, 42, 1),
    pytest.param(300, 0, 35, None, marks=pytest.mark.skip(reason="Skipped division by zero")),
], ids=["smoke_test", "norm_test", "skip_test"])
def test_division(x, y, z, expected):
    assert all_division(x, y, z) == expected
