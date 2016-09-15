@pytest.mark.linux
def test_mem_stack():
    assert MemSizes().stack == 42

@pytest.fixture(autouse=True)
def _platform_skip(request):
    marker = request.node.get_marker('linux')
    if marker and platform.system() != 'Linux':
        pytest.skip('N/A on {}'.format(platform.system()))
