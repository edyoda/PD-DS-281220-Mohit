print(__name__) ## __name__ is a builtin variable which gives us 
## different values based on what context this print statement is 
## running.

print('oh i printed the name because probably I am imported somewhere')
print('whenever I get imported, the global automatically runs')

def xyz(a):
	print('Even I ran when the module X(my parent) was imported')
	print("But I beleve that these print statments will only")
	print('run if somebody calls me, either here, or where I am')
	print(' imported')

# xyz('happy') ## calling a fun