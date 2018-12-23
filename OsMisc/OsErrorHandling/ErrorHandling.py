'''
https://docs.python.org/3/library/exceptions.html
https://docs.python.org/3.3/tutorial/errors.html
'''

import sys

def ioError_Example(fname,mode):
    try:
        f = open(fname,mode)
        if mode == 'r':
            print(f.read())
        if mode == 'w':
            f.write("add a new line to file \n")
        f.close()
    except IOError as err:
        print("I/O error: {0}".format(err))
        

if __name__ == '__main__':
    ioError_Example('./ErrorHandling.pyX','r') #I/O error: [Errno 2] No such file or directory: './ErrorHandling.pyX'
    ioError_Example('testFile.txt','r')
    ioError_Example('testFileNonWrite.txt','w')
    ioError_Example('testFileNonWrite.txt','r')  #I/O error: [Errno 13] Permission denied: 'testFileNonWrite.txt'