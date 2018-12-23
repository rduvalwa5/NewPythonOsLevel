'''
Created on Jul 16, 2016
purpose search for files
@author: rduvalwa2
'''
import glob
import os

from os.path import join, getsize
import string

class find_file:
    def __init__(self):
            self.allFoundFiles = []
            self.constrainedFiles = []
            self.allDirectories = []
            self.artist = []

    def find(self,myFile, path = '.'):
        for root, dirs, files in os.walk(path):
            print(dirs)
            for name in files:
                foundFile = {}
                if name == myFile:
                    file_info = os.stat(join(root, name))
#                    foundFile['Dir'] = dirs
                    foundFile['file_size'] = file_info.st_size
                    foundFile['file_access_time'] = file_info.st_atime
                    foundFile['file_path'] = os.path.abspath(path)
                    foundFile['name'] = name
                    self.allFoundFiles.append(foundFile)

    def findAll(self,path = '.'):
        for root, dirs, files in os.walk(path):
            print(dirs)
            for name in files:
                foundFile = {}
                file_info = os.stat(join(root, name))
#                foundFile['Dir'] = dirs
                foundFile['file_size'] = file_info.st_size
                foundFile['file_access_time'] = file_info.st_atime
                foundFile['file_path'] = os.path.abspath(path)
                foundFile['name'] = name
                self.allFoundFiles.append(foundFile)
        
    def findConstrained(self,myConstraint, path = '.'):
#        dirCount = 0
        for root, dirs, files in os.walk(path):
            self.allDirectories = dirs
            print('directories ',dirs)
#            print('files ',files)
            for name in files:
                if myConstraint in name:
                    foundFile = {}
                    file_info = os.stat(join(root, name))
#                    foundFile['Dir'] = dirs
                    foundFile['file_path'] = os.path.abspath(path)
                    foundFile['name'] = name
                    self.constrainedFiles.append(foundFile)
#            dirCount = dirCount + 1
            
    def find_file(self,myFile, path = '.'):
        self.find(myFile, path)
        if self.allFoundFiles != []:
            return  self.allFoundFiles
        else:
            return myFile + " Not found"
       
    def find_fileAll(self,path = '.'):
        self.findAll(path)
        if self.allFoundFiles != []:
            return  self.allFoundFiles
        else:
            return "No Files found"

    def find_fileConstraint(self,constraint,path = os.path.abspath('.')):
        self.findConstrained(constraint, path)
        if self.constrainedFiles != []:
            return  self.constrainedFiles
        else:
            return "No Files found"

    def all_files(self,constr,path = os.path.abspath('./')):
        if  len(constr) == 1:
            if constr[0] == '*':
#                print("find_fileAll")
                return  self.find_fileAll(path)
        if  len(constr) > 1:
            if constr[0] == '*':
#                print("all_files find_fileConstraint")
                constraint = constr[1:]
#                print('constraint ', constraint)
                return  self.find_fileConstraint(constraint, path) 
            else:
                return  self.find_file(constr,path)
        else:
            return "Input makes no sense"
 
    def get_directories(self, path = os.path.abspath('./')):
        for root, dirs, files in os.walk(path):
            if dirs != []:
                self.allDirectories.append(dirs)
        return self.allDirectories
 
    def get_roots(self, path = os.path.abspath('./')):
        for root, dirs, files in os.walk(path):
            if root != []:
                self.artist.append(root)
        return self.artist       
 
    def get_count(self, result): 
        if isinstance(result,str):
            return(result)
        else:
            return  len(result)
 
                            
    def printResult(self,result):
        print("**************")  
        if isinstance(result,str):
            print(result)
        else:
            print(self.get_count(result))
            for item in result:
                print(item)
                    
if __name__ == "__main__":

    '''
    print("F1_____")
    f1 = find_file()
    result = f1.all_files('*','../')
    f1.printResult(result)

    print("F2_____")    
    f2 = find_file()
    result2 = f2.all_files('*.py','./')
    f2.printResult(result2) 

    print("F3_____")
    f3 = find_file()
    result3 = f3.all_files('test_file.txt','../')
    f3.printResult(result3) 
    
    print("F4_____")       
    f4 = find_file() 
    result4 = f4.all_files('*.jpg','../../')
    print("result is ", result4)
    f4.printResult(result4)   

    print("F5_____")       
    f5 = find_file() 
    result5 = f5.all_files('*test','../../')
    f5.printResult(result5) 
    print(len(result5))  
'''
    songPath = '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music'
    allSongNames = []
    

    print("F6_____")       
    f6 = find_file() 
    result6 = f6.all_files('*.m4p',songPath)
    for name in result6:
        allSongNames.append(name['name'])
#    f6.printResult(result5) 
    print(len(result6))
    for item in allSongNames:
        print(item) 
    fdir = find_file() 
    result6 = f6.all_files('*.m4p',songPath)        
    di = f6.get_directories(songPath)
    print(len(di))
    for directory in di:
        print(directory)
    rot = f6.get_roots(songPath)
    print(rot)
 
    '''    
    f7 = find_file() 
    result7 = f7.all_files('*.m4a',songPath)
#    print(result7) 
    print(len(result7))  
    for name in result7:
        print(os.path.abspath(songPath + '/' + name['name']))
#        allSongNames.append(name[name])

    f8 = find_file() 
    result8 = f8.all_files('*.m4p','/Users/rduvalwa2/Music/iTunes/iTunes Music/Music')
    print(len(result8)) 
    for name in result8:
        allSongNames.append(name['name'])
'''    
    print(len(allSongNames))
    