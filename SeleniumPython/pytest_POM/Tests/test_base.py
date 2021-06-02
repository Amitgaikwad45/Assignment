import pytest

#from conftest.py
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

