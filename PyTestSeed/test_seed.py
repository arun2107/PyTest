import pytest


@pytest.mark.smoke
@pytest.mark.skip
def testadd():
    assert 4+3 == 8
    print("add successful")


@pytest.mark.regression
@pytest.mark.xfail
def testsub():
    assert 8-4 == 3
    print("sub successful")