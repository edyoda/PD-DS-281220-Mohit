def func(x):
	if x%2==0:
		return x+5
	else:
		return x-4

def test_method():
	assert func(3) == -2

def test_method_2():
	assert func(2) == 7
