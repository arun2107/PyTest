import pytest

@pytest.fixture(params=["a","b"])
def setUp(request):
    print("setup successful")
    print("before yeild")
    print(request.param)
    yield
    print("After yeild")
    print("teardown successful")

def testArrage(setUp):
    print("Arrange successful")



