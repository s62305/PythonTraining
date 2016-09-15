import pytest
@pytest.yield_fixture(scope='session')
def foo():
    print('session setup')
    yield 'foo'
    print('session finalizer')

@pytest.yield_fixture(scope='function')  # default scope
def bar():
    print('funtion setup')
    yield 'bar'
    print('function finalizer')

def test_one(foo, bar):
    pass

def test_two(foo, bar):
    pass