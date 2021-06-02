#implementation of pytest
import pytest

@pytest.fixture()
def setup():
    print("opening url")
    yield
    print("closing browser")


def test_loginbyMail(setup):
    print("mail login")

def test_loginbyFacebook(setup):
    print("facebook login")
    
    
#to run specific method from file test_login.py 
#run the command pytest -v -s test_login::test_loginbyFacebook
