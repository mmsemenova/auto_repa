import pytest
import datetime


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
