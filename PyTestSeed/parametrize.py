import pytest


@pytest.mark.parametrize("a,b,final",[(2,6,8),(4,4,8),(5,5,9)])
def testadd(a, b,final):
    assert a+b == final
    print("Add with parameters successful")


