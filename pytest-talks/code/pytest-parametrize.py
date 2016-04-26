#!coding: utf-8
import pytest

@pytest.mark.parametrize(
    "string,is_upper",
    (
    	("UPPER", True),
    	("lower", False),
    	("CamelCase", False),
    	(u"СПУТНИК", True)
	)
)
def test_isupper(string, is_upper):
    assert string.isupper() == is_upper