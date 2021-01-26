# import mod1

# print(mod1.pipi)

# print(mod1.spacex('land us on MARS'))
# print(mod1.google('Stop spying!!'))
###################

# from mod1 import * # import everything from the
# module AND i can use those things like if
# they are present in the same file.

# print(spacex('GET US A PERFECT LANDING VEHICLE'))

# print(google("Please don't spy"))

# Question 1) Make a module mod2.py , write 
# functions microsoft,netflix
# You will have to import them in main.py and
# use them.

# import mod2

# print(mod2.microsoft('some work'))

# from mod2 import *

# print(microsoft('some work to microsoft'))

# import sys

# print("We can import modules from these paths=>")
# for i in sys.path:
# 	print(i)

# dir() function tells us about all the names in the
# current namespace

# print(dir())

# from mod2 import netflix
# from mod2 import *
# import mod2

# print(mod2.netflix('lets watch something!!'))

# print(dir())


######################

# import mod1

# print(dir(mod1))

# print(mod1.__file__)


############### ALIASING

# import mod1 as sudhanshu

# print(sudhanshu.google('Please do something for global warming!!'))


# import math as Mathematics

# print(Mathematics.pi)


# globals() and locals()

# from mod1 import spacex

# spacex('some good work!!')

########### __name__

# from mod1 import google

# google('goolie work')