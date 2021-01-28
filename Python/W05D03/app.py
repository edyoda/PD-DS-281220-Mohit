# print('1->',dir())
# from package import * # without an __all__ list.
# print('2->',dir())
# print(module1.pipi)

# does not work because this kind of import needs
# an init file inside package(we'll learn about init after
# 10 mins.)

# print('1->',dir())
# from package import module1
# print('2->',dir())
# print(module1.pipi)

# print('1->',dir())
# from package.subpackage import module2
# print('2->',dir())
# print(module2.netflix('show me the series DARK'))

# Package can contain a lot of things, and we don't want to
# import everything(static image files, icons svgs, some text
# or csv files,etc etc)
# To import only things we need, We do a controlled import.

## PACKAGE INITIALIZATION
## Creating a file named as __init__.py
# 1) now if we use the import package line, we can import the
# whateever files that we want to be imported.
# 2) It can do some pre-requisites for us.

## without defining the __all__
# print('1->',dir())
# from package import *
# print('2->',dir())
# print(module1.pipi)


# from package import * + __all__ does all the magic!!

## after defining the __all__ list with 'module1'
# print('1->',dir())
# from package import *
# print('2->',dir())
# print(module1.pipi)
# print(module3.xyz)