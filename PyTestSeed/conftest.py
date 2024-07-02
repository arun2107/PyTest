import pytest



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(autouse=True)
def confsetUp():
    print("setup successful")
    print("before yeild")
    yield
    print("After yeild")
    print("teardown successful")