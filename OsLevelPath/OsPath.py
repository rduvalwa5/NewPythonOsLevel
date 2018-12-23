'''
Created on Aug 10, 2016
    https://docs.python.org/3/library/os.path.html
@author: rduvalwa2
'''

import os

class os_path:
    '''
    URL:  https://docs.python.org/3/library/os.path.html
    Functions:
    os.path.abspath(path)         os.path.basename(path)    os.path.commonpath(paths)
    os.path.commonprefix(list)    os.path.dirname(path)     os.path.exists(path)
    os.path.lexists(path)         os.path.expanduser(path)  os.path.expandvars(path)
    os.path.getatime(path)        os.path.getmtime(path)    os.path.getctime(path)
    os.path.getsize(path)         os.path.isabs(path)       os.path.isfile(path)
    os.path.isdir(path)           os.path.islink(path)      os.path.ismount(path)
    os.path.join(path,*paths)     os.path.normcase(path)    os.path.normpath(path)
    os.path.realpath(path)        os.path.relpath(path,start=os.curdir)
    os.path.samefile(path1,path2) os.path.sameopenfile(fp1, fp2)
    os.path.samestat(stat1,stat2) os.path.split(path)       os.path.splitdrive(path)
    os.path.splitext(path)        os.path.splitunc(path)
                                     Deprecated since version 3.1: Use splitdrive instead.
    os.path.supports_unicode_filenames¶
'''
    def get_absolute_path(self,inp = './'):
        '''
        os.path.abspath(path)
        Return a normalized absolutized version of the pathname path. On most platforms, this is equivalent 
        to calling the function normpath() as follows: normpath(join(os.getcwd(), path)).
        '''
        return  os.path.abspath(inp)

    def get_path_basename(self, inp = './'):
        '''
        os.path.basename(path)
        Return the base name of pathname path. This is the second element of the pair returned by passing path
        to the function split(). Note that the result of this function is different from the Unix basename 
        program; where basename for '/foo/bar/' returns 'bar', the basename() function returns an empty 
        string ('').
        '''
        return os.path.basename(inp)

    def get_common_path(self,lst):
        '''
        os.path.commonpath(paths)
        Return the longest common sub-path of each pathname in the sequence paths. 
        Raise ValueError if paths contains both absolute and relative pathnames, or if paths is empty. 
        Unlike commonprefix(), this returns a valid path.
        Availability: Unix, Windows
        '''
        return os.path.commonpath(lst)
    
    def get_commonprefix(self,lst):
        '''
        os.path.commonprefix(list)
        Return the longest path prefix (taken character-by-character) that is a prefix of all paths in list. 
        If list is empty, return the empty string ('').
        '''
        return  os.path.commonprefix(lst)

    def verify_path(self,path):
        '''
        os.path.exists(path)
        Return True if path refers to an existing path or an open file descriptor. 
        Returns False for broken symbolic links. On some platforms, this function may return False if permission is not granted to execute os.stat() on the requested file, even if the path physically exists.
        Changed in version 3.3: path can now be an integer: True is returned if it is an open file descriptor, 
        False otherwise.
        '''
        return  os.path.exists(path)

    def verify_path_lexist(self,path):
        '''
        os.path.lexists(path)
        Return True if path refers to an existing path. Returns True for broken symbolic links. Equivalent to exists() 
        on platforms lacking os.lstat().
        '''
        return  os.path.lexists(path)

    def verify_symolic_link(self,path):
        '''
        os.path.islink(path)
        Return True if path refers to a directory entry that is a symbolic link. Always False 
        if symbolic links are not supported by the Python runtime.
        '''
        return  os.path.islink(path)


    def get_dir_name(self,path):
        '''
        os.path.dirname(path)
        Return the directory name of pathname path. This is the first element of the pair returned by passing path to 
        the function split().
        '''
        return os.path.dirname(path)


    def get_expanduser(self,path):
        '''
        os.path.expanduser(path)
        On Unix and Windows, return the argument with an initial component of ~ or ~user replaced by that user‘s home directory.
        Unix, an initial ~ is replaced by the environment variable HOME if it is set; otherwise the current user’s home directory 
        is looked up in the password directory through the built-in module pwd. An initial ~user is looked up directly in 
        the password directory.
        On Windows, HOME and USERPROFILE will be used if set, otherwise a combination of HOMEPATH and HOMEDRIVE will be used. 
        An initial ~user is handled by stripping the last directory component from the created user path derived above.
        If the expansion fails or if the path does not begin with a tilde, the path is returned unchanged.
        '''
        return os.path.expanduser(path) 

    def get_expandvars(self,path):
        '''
        os.path.expandvars(path)
        Return the argument with environment variables expanded. Substrings of the form $name or ${name} are 
        replaced by the value of environment variable name. Malformed variable names and references to 
        non-existing variables are left unchanged.
        On Windows, %name% expansions are supported in addition to $name and ${name}.
        '''
        return  os.path.expandvars(path)
         
    def print_docstring(self):
        '''
        print_docstring()
        https://www.python.org/dev/peps/pep-0257/
        Python documentation strings (or docstrings) provide a convenient way of
        associating documentation with Python modules, functions, classes, and methods. 
        Example:
        print (my_function.__doc__)
        '''
        return(print(self.__doc__))
    
        
if __name__ == '__main__':
    a = os_path()
    print('default ', a.get_absolute_path())
    print('input ./ ', a.get_absolute_path('./'))
    print('input ../ ', a.get_absolute_path('../'))  
    print('input /Users/rduvalwa2/hell ', a.get_absolute_path('/Users/rduvalwa2/hell'))        
    print('base name is: ', a.get_path_basename('/Users/rduvalwa2/hell'))
    l = ['/Users/rduvalwa2/Documents/','/Users/rduvalwa2/Workspace/BasicPython070816/','/Users/rduvalwa2/Workspace/BasicPython070816/OSPath/src']
    print('common path', a.get_common_path(l))
    l2 = ['/sbin/newfs_udf','/sbin/launchd','/sbin/mount_exfat']
    print('common_prefix ', a.get_commonprefix(l2))
    print('get_dir_name' ,a.get_dir_name('/Users/rduvalwa2/testFile.txt'))
    print('path exist ', a.verify_path('/Users/rduvalwa2/testFile.txt'))
    print('path exist ', a.verify_path('/Users/rduvalwa2/testFile'))  
    symbolic_link = '/sbin/newfs_exfat'
    not_symbolic_link = '/Users/rduvalwa2/Documents/'
    print('path exist true', a.verify_path(symbolic_link))
    print('path exist true ', a.verify_path(not_symbolic_link))    
    print('is sym link true', a.verify_symolic_link(symbolic_link))
    print('is sym link false', a.verify_symolic_link(not_symbolic_link))
    print('expanduser  ', a.get_expanduser('~/Library'))
    print('expandvars ', a.get_expandvars('$HOME/Documents'))
    print('expandvars ', a.get_expandvars('$USER'))
    print('expandvars ', a.get_expandvars('$SHELL'))
        
    '''   
    a.print_docstring()
    print(a.get_path_basename.__doc__)
    print(a.print_docstring.__doc__)
    '''