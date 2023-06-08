# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import datetime


class TestClass:

    def test_1(self, test_time):
        assert 10244525 + 5243124132 == 5253368657

    def test_2(self):
        assert 100 * 10 == 1000

    def test_3(self, test_time):
        assert (5 - 1)**0.5 == 2


@pytest.fixture(scope="session", autouse=True)
def test_session_start_end(request):
    start_time = datetime.datetime.now()
    print(f"\nTest session started at {start_time}")

    def session_end():
        end_time = datetime.datetime.now()
        print(f"\nTest session ended at {end_time}")
        duration = end_time - start_time
        print(f"Test session duration: {duration}")

    request.addfinalizer(session_end)


@pytest.fixture(scope="function")
def test_time(request):
    start_time = datetime.datetime.now()
    print(f"\nTest started at {start_time}")

    def test_end():
        end_time = datetime.datetime.now()
        print(f"\nTest ended at {end_time}")
        duration = end_time - start_time
        print(f"Test duration: {duration}")

    request.addfinalizer(test_end)
