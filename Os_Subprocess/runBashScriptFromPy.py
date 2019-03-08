'''
Created on Dec 23, 2018

@author: rduvalwa2
'''
import os

print("this os is ", os.name)
if os.name == 'nt':
    print("found nt!")
    print("this ",os.system("bashScriptWindows.sh"))
    os.system("bashScriptWindows.sh")
if os.name == 'posix':
    print("found posix")
#    print("this ",os.system("./bashScript.sh"))
    os.system("./bashScript.sh")


