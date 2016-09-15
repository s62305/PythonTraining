try:
    import cx_Oracle as ora
except ImportError:
    ora = None

needs_ora = pytest.mark.skipif(ora is None, reason='No Oracle installed')

@pytest.fixture(params=['pg', needs_ora('ora')])
def dburi(request):
    return create_db_uri(request.param)

@needs_ora
def test_one():
    pass

def test_two(dburi):
    pass
