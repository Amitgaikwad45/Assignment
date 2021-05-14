
import pytest

@pytest.fixture()
def setup():
    print("opening url for signup")
    yield
    print("closing browser signup")


def test_signupbyMail(setup):
    print("mail signup")

def test_signupbyFacebook(setup):
    print("facebook signup")
