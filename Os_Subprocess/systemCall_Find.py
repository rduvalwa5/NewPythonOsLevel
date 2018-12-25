'''
Created on Dec 24, 2018

@author: rduvalwa2
'''
'''
Created on Dec 23, 2018
https://docs.python.org/3/library/subprocess.html
@author: rduvalwa2

subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, 
timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)¶

'''
import os, subprocess

print("Shell Find command using subprocess")
subprocess.run(["find", "/etc/", "-name", "hosts"])
print("Shell Find command using os.system")
os.system("find /etc/ -name hosts")
'''
If you use one ampersand it sends that cmd off to its own thread, and immediately begins the next cmd on another thread. 
I wanted to sleep before executing something and so needed to use: os.system("sleep 5 && <some command>"). NOTE the two 
ampersands
'''
os.system("ls -l && cd /Users/ && pwd && ls -l")