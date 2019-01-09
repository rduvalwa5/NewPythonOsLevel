'''
Created on Dec 23, 2018

https://docs.python.org/3/library/subprocess.html

#!/path/to/interpreter
OSXAir:Os_Subprocess rduvalwa2$ python3.7 systemCall_Find.py ./  testFile.txt
call is  systemCall_Find.py ./ testFile.txt
.//testFile.txt
OSXAir:Os_Subprocess rduvalwa2$ 
'''
#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7

if __name__ == "__main__":
    import os, subprocess, sys
    
    print(subprocess.run(["ls", "-l"], capture_output=True) )   
    print("call is ", sys.argv[0], sys.argv[1], sys.argv[2] )
    subprocess.run(["find", sys.argv[1], "-name",sys.argv[2]])
    print(subprocess.run(["find", sys.argv[1], "-name",sys.argv[2]]))
    
    subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)               
                