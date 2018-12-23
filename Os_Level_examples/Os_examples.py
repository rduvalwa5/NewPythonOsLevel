'''
Created on Nov 25, 2015
http://www.tutorialspoint.com/python/python_files_io.htm
@author: rduvalwa2
'''
import os, glob, sys
#import os
# import os
from os.path import join, getsize

class os_info:
    def __init__(self, path = "."):
            self.path = path
    
    def get_encoding(self):
        encoding =  sys.getfilesystemencoding()
        if encoding == 'mbcs':
            encoding = 'Multi-Byte Character Set'
        return encoding
    
    
    def get_intput(self):
            pth = input("Enter path: ");
            self.path = pth
    
    def get_os_env(self):
            env = os.environ
            return env

    def get_os_name(self):
            return os.name

    def get_cpu_count(self):
            cpus = os.cpu_count()
            return cpus

    def get_cur_dir(self):
            current_dir =  os.curdir
            return  current_dir

    def get_number_of_bytes_in_directories(self, path = '.'):
            bitts = 0
            for root, dirs, files in os.walk(self.path):
                    print(self.path)
                    bitts = bitts + (sum(getsize(join(root, name)) for name in files))
            return  bitts

    def list_files_in_directories(self,path = '.'):
        '''
            Creates a file information genrator
            list_files_in_directories(self,path = '../')
            http://www.tutorialspoint.com/python/os_stat.htm
            Description
                The method stat() performs a stat system call on the given path.
            Syntax
            Following is the syntax for stat() method:
                os.stat(path)
            Parameters
                path -- This is the path, whose stat information is required.
            Return Value
            Here is the list of members of stat structure:
                st_mode: protection bits.
                st_ino: inode number.
                st_dev: device.
                st_nlink: number of hard links.
                st_uid: user id of owner.
                st_gid: group id of owner.
                st_size: size of file, in bytes.
                st_atime: time of most recent access.
                st_mtime: time of most recent content modification.
                st_ctime: time of most recent metadata change.
        '''
        allFilesInfo = []
        for root, dirs, files in os.walk(self.path):
            fEnv = self.get_os_env()
            for name in files:
                if name[0] != ".":
                    file_info = os.stat(join(root, name))
                    file_mode = file_info.st_mode
                    file_size = file_info.st_size
                    file_device =    file_info.st_dev
                    file_userid = file_info.st_uid
                    file_group = file_info.st_gid
                    file_access_time = file_info.st_atime
                    file_path = os.path.abspath(self.path)
#                    print("absolute path: " , file_path)
                    fileInfo = {'ab_path':file_path,'name':name,'mode':file_mode,'size':file_size,'device':file_device,'userid':file_userid,'group':file_group,'access_time':file_access_time}
#                print("\t", name, ":",":",file_mode,":",file_size,":","device:",file_device,"file_userid,":",file_group,":",file_access_time,":",file_last_mod,":", file_meta_chg)
#                print(fileInfo)
                    allFilesInfo.append(fileInfo)
        return allFilesInfo

    def find_file(self,sFile,path = '.'):
#        mydic = {}
#mydic['key_name'] = 'value_name'
        allFoundFiles = []
        for root, dirs, files in os.walk(path):
            print(root)
            for name in files:
                foundFile = {}
                if name == sFile:
                    file_info = os.stat(join(root, name))
                    foundFile['file_size'] = file_info.st_size
                    foundFile['file_access_time'] = file_info.st_atime
                    foundFile['file_path'] = os.path.abspath(self.path)
                    foundFile['name'] = name
#                    fileInfo = {'ab_path':file_path,'name':name,'size':file_size,'access_time':file_access_time}
                    allFoundFiles.append(foundFile)
        return allFoundFiles
        
        
if __name__ == "__main__":
    from subprocess import call


    a = os_info('../')
    print('encoding is: ', a.get_encoding())
#    print(a.get_intput())
    thisEnv =  a.get_os_env()
    print("Should be posix ", a.get_os_name())
    if a.get_os_name() != 'nt':
        print(thisEnv['USER'])
        print(thisEnv['SHELL'])
        print(thisEnv['HOME'])
        myHome = thisEnv['HOME']
        print(thisEnv['LOGNAME']) 
    if a.get_os_name() == 'nt':
        myHome = thisEnv['HOMEPATH']
        print(myHome)
    print("CPU count ", a.get_cpu_count())
    print("Current directory", a.get_cur_dir(), "\n")

    print("Number of bytes in ", myHome, ": ", a.get_number_of_bytes_in_directories(myHome))
    print("list_files_in_directories \n")
#    a.list_files_in_directories()
    print(len( a.list_files_in_directories("../")))
    for item in a.list_files_in_directories("../"):
        print(item)
 # fileInfo = {'ab_path':file_path,'name':name,'size':file_size,'access_time':file_access_time}
    searchFile =  'os_module_notes.txt' 
#    for item in a.find_file(searchFile):
#        print(item.name)
           
    for item in a.find_file(searchFile,'/Users/rduvalwa2/git/'):
#            myDict = value
#            print(myDict)
            print( item['file_path'],"/",item['name'],"  ", item['file_size'], " ", item['file_access_time'])


'''
C1246895-Air:src rduvalwa2$ python3.5 Os_examples.py
environ({
'ANT_HOME': '~/Ant/bin', 
'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.KX1MxshOjP/Listeners', 
'GLASSFISH_HOME': '/usr/local/glassfish4-3/bin',
'XPC_SERVICE_NAME': '0', 
'TMPDIR': '/var/folders/yv/dbpkqmlj30b5h2f7xxvn1fw40000gq/T/', 
'LANG': 'en_US.UTF-8', 'SHELL': '/bin/bash', 'XPC_FLAGS': '0x0', 
'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.wvH288mh0u/Render', 
'OLDPWD': '/Users/rduvalwa2/new_git/File_Handling', 
'TERM': 'xterm-256color', 
'TERM_PROGRAM': 'Apple_Terminal', 
'LOGNAME': 'rduvalwa2', 
'SHLVL': '1', 
'__PYVENV_LAUNCHER__': '/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5', 
'PWD': '/Users/rduvalwa2/new_git/File_Handling/src', 
'_': '/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5', 
'MAVEN_HOME': '/usr/bin', 
'HOME': '/Users/rduvalwa2', 
'JAVA_HOME': '/Library/Java/JavaVirtualMachines/jdk1.8.0_31.jdk/Contents/Home', 
'PATH': '/Library/Frameworks/Python.framework/Versions/3.5/bin:/Library/Frameworks/Python.framework/Versions/3.4/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Library/Frameworks/Python.framework/Versions/3.4/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/git/bin:/Library/Java/JavaVirtualMachines/jdk1.8.0_31.jdk/Contents/Home:~/Ant/bin:/usr/local/glassfish4-3/bin', '__CF_USER_TEXT_ENCODING': '0x1F7:0x0:0x0', 'TERM_SESSION_ID': 'DEB6163D-995E-4E2F-8B38-42DB9E920438', 'USER': 'rduvalwa2', 'TERM_PROGRAM_VERSION': '361'})

/Users/rduvalwa2/new_git/File_Handling/src
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
/Users/rduvalwa2
/Library/Java/JavaVirtualMachines/jdk1.8.0_31.jdk/Contents/Home
rduvalwa2
C1246895-Air:src rduvalwa2$ 


'''