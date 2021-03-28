import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))

from main_program import add, product

def test_add():
	assert add(5, 4)==9
	assert add(-9, 0)==-9

def test_product():
	assert product(5, 4)==20
	assert product(-9, 0)==0
