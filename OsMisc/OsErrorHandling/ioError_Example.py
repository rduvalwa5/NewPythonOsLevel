'''
Created on Dec 22, 2018
https://docs.python.org/3/library/exceptions.html
https://docs.python.org/3.3/tutorial/errors.html

'''
try:
    f = open('myfile.txt')
except IOError as err:
    print("I/O error: {0}".format(err))