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

>>> subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)

>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')
'''
import os, subprocess

print("One shell commands")
subprocess.run(["ls","-l"])

print("Two shell commands")
subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)

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