'''
Created on Dec 22, 2018
https://docs.python.org/3/library/exceptions.html
https://docs.python.org/3.3/tutorial/errors.html

'''

myArray = [1,2,3,4]

try:
    for item in range(5):
        print(myArray[item])
except IOError as err:
    print("I/O error: {0}".format(err)) #IndexError: list index out of range