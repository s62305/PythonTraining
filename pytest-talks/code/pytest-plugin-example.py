# conftest.py
def pytest_addoption(parser):
    parser.addoption(
        "--backend",
        choices=("webkit", "webengine"),
        default="webkit"
    )

# test_foo.py
def test_foo(request):
    if request.config.getoption("--backend") == "webkit":
       # ...
    else:
       # ...
