import pytest

def func(x):
	if x%2==0:
		return x+5
	else:
		return x-5

@pytest.mark.bhavya
def test_case_by_Abhishek():
	assert func(3) == -2

@pytest.mark.abhishek
def test_case_by_bhavya():
	assert func(2) == 7

def test_case_3():
	assert func(10) == 15