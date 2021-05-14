import pytest

@pytest.fixture()
def setup():
    print("once before every method")
    yield
    print("once after every method")

def test_method(setup):
    print("method1")


def test_method2(setup):
    print("method2")