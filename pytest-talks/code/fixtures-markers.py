@pytest.fixture
def mongo_client(request):
    marker = request.node.get_marker('mongo_db')
    if not marker:
        db = 'TestDB'
    else:
        db = marker.args[0]
        # a better (and reliable) way to do this:
        # db = (lambda x: x)(*marker.args, **marker.kwargs)
    return pymongo.MongoClient('127.0.0.1/{}'.format(db))

@pytest.mark.mongo_db('Users')
def test_something(mongo_client):
    pass