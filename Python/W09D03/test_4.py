import pytest

@pytest.fixture
def pre_data():
	data = {'python':3,'java':8,'c++':14}
	return data

def test_case_1(pre_data):
	var = 3 ## this single line is being tested.
	assert pre_data['python'] == var

def test_case_2(pre_data):
	var_2 = 8## this single line is being tested.
	assert pre_data['c++'] == var_2