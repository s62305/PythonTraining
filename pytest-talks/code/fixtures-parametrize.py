@pytest.fixture(params=['ora', 'pg', 'sqlite'])
def dburi(request):
    return create_db_uri(request.param)

@pytest.fixture(params=['ipv4', 'ipv6'])
def addr_family(request):
    return socket.AF_INET if request.param == 'ipv4' else socket.AF_INET6

def test_txn(dburi):
    inst = MyObj(dburi)
    assert inst.transaction_works()

def test_conn(dburi, addr_family):
    inst = MyObj(dburi, addr_family)
    assert inst.it_works()
