import pytest

def test_isupper():
    assert "FOO".isupper()
    assert not "Foo".isupper()

def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']
    with pytest.raises(TypeError):
        s.split(2)
