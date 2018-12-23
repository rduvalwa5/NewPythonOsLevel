'''
Created on Dec 22, 2018
https://docs.python.org/3.3/tutorial/errors.html
@author: rduvalwa2
'''

x = 1
try:
    for item in x:
            print("item is ", item)
except TypeError as err:   
    print("Type error: {0}".format(err))     
#    print("TypeError: 'int' object is not iterable")