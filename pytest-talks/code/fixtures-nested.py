@pytest.fixture(scope='session')
def db_conn():
    return create_db_conn()

@pytest.yield_fixture(scope='module')
def db_table(db_conn):
    table = create_table(db_conn, 'foo')
    yield table
    drop_table(db_conn, table)

def test_bar(db_table):
    pass