from main_program import add, product
import pytest

@pytest.mark.parametrize("x, y, result",
[(4, 5, 9), (-5, -7, -12), ('hello', 'world', 'helloworld')])
def test_add(x, y, result):
	assert add(x, y)==result

@pytest.mark.parametrize("x, y, result",
[(2, 3, 6), (4, -6, -24), (2, 'haii', 'haiihaii')])
def test_product(x, y, result):
	assert product(x, y)==result
