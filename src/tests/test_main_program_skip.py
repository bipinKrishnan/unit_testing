from main_program import add, product
import pytest

@pytest.mark.skip(reason="Not completely implemented")
def test_add_number():
        assert add(5, 4)==9
        assert add(-9, 0)==-9

@pytest.mark.strings
def test_add_string():
        assert add('hello', 'world')=='helloworld'

@pytest.mark.numbers
def test_product_number():
        assert product(5, 4)==20
        assert product(-9, 0)==0

@pytest.mark.strings
def test_product_string():
        assert product(3, 'hello')=='hellohellohello'
