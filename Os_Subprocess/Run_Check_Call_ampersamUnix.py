'''
Created on Jan 8, 2019
https://docs.python.org/3/library/subprocess.html

'''
import os, subprocess

print("One shell commands")
subprocess.run(["ls","-l"])

print("Two shell commands")
subprocess.check_call("cd /Users/rduvalwa2/Documents ; ls -CF ; pwd ", shell=True)

print("Three shell commands")
os.system("ls -l && cd /Users/ && pwd && ls -l")