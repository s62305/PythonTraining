@pytest.fixture(scope='session')
def redis_client():
    servers = ['localhost', 'venera.clockhouse']
    for hostname in servers:
        try:
            return redis.StrictRedis(hostname)
        except redis.ConnectionError:
            continue
    else:
        pytest.skip('No Redis server found')
