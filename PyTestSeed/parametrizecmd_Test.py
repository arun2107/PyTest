import pytest


def testadd(browser):
    if browser == "chrome":
     print("Launching chrome successful")
    else:
     print("Launching the other browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption('--browser')
