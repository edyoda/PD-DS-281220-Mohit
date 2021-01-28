pipi = '4.5'
print('AM I IMPORTED, hI I AM MODULE1')

def spacex(work_given_to_spacex):
	ceo = 'elon musk'
	document = [ceo,work_given_to_spacex]
	print('globals are ',globals())
	print('locals are ',locals())
	return document

def google(work_given_to_google):
	ceo = 'sundar pichai'
	document = [ceo,work_given_to_google]
	print(__name__)
	return document