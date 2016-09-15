import pytest

@pytest.fixture
def foo():
    return 42

def test_foo(foo):
    assert foo == 42

class TestBar:
    @pytest.yield_fixture
    def bar(self):
        yield 7
        print('Teardown of fixture bar')

    def test_bar(self, foo, bar):
        assert foo != bar
