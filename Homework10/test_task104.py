# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


@pytest.mark.usefixtures("test_session_start_end")
class TestClass:

    def test_1(self):
        assert 10244525 + 5243124132 == 5253368657

    @pytest.mark.usefixtures("test_time")
    def test_2(self):
        assert 100 * 10 == 1000

    def test_3(self):
        assert (5 - 1)**0.5 == 2
