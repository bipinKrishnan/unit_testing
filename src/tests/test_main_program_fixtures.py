import pytest
from main_program import add, product

@pytest.fixture
def gen_num():
	print("\nGenerating number")
	yield 5
	print("\nStopping generator")

def test_add(gen_num):
	assert add(gen_num, gen_num)==10

def test_product(gen_num):
	assert product(gen_num, gen_num)==25
