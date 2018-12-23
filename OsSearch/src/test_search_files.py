'''
Created on Jul 19, 2016

@author: rduvalwa2
'''

import unittest
from search_files import find_file


class Test(unittest.TestCase):

    def test_1_find_file_0_file(self):
        '''
        Test for finding 1 file by specified name in path
        '''
        expected = 'test_file.txt Not found'
        ob = find_file()
        result = ob.find_file( 'test_file.txt','./')
#        print("test 1 ",result)
        self.assertEqual(expected,result,"more that one file instance or no file instance found")

    def test_2_find_file_1_file(self):
        '''
        Test for finding 1 file by specified name in path
        '''
        expected = 'test_file.txt'
        ob = find_file()
        result = ob.all_files( 'test_file.txt','../test_directory')
        self.assertEqual(len(result),1,"more that one file instance or no file instance found")
        count = 0
 #       print(count + 1 ,result[0]['name'])
 
        
    def test_3_all_files_filename(self):
        '''
        Test for finding 2 file by specified name in path
        '''
        expected = 'test_file.txt'
        ob = find_file()
        result = ob.all_files('test_file.txt','../')
        self.assertEqual(len(result),2,"more that one file instance or no file instance found")
        count = 0
        for item in result:
            self.assertEqual(expected, result[count]['name'], "file not match expected")
            
    def test_4_get_result_count(self):
        ob = find_file()
        result = ob.all_files('test_file.txt','../')
        self.assertEqual(2,ob.get_count(result),'get_count failed')
               
    def test_5_all_files_asterix(self):
        '''
        '''
        ob = find_file()
        result = ob.all_files( '*','../../')
        expectedCount = len(result)
        self.assertEqual(expectedCount,ob.get_count(result),'get_count failed')
        self.assertTrue(str(result).__contains__('test_file.txt'),'key file not found')
        self.assertTrue(str(result).__contains__('.pydevproject'),'key file not found')
        self.assertTrue(str(result).__contains__('search_files.py'),'key file not found')
        self.assertTrue(str(result).__contains__('test_search_files.cpython-35.pyc'),'key file not found')

    def test_6_all_files_constraint(self):
        '''
        '''
        ob = find_file()
        result = ob.all_files( '*.py','../../')
        expectedCount = len(result)
#        print(expectedCount)
        self.assertEqual(expectedCount,ob.get_count(result),'get_count failed')
        self.assertFalse(str(result).__contains__('test_file.txt'),'key file not found')
        self.assertTrue(str(result).__contains__('.pydevproject'),'key file not found')
        self.assertTrue(str(result).__contains__('search_files.py'),'key file not found')
        self.assertTrue(str(result).__contains__('test_search_files.cpython-35.pyc'),'key file not found')
        
    def test_7_file_not_found(self):
        '''
        '''
        ob = find_file()
        result = ob.all_files( '*.jpg','../../')
#        print("result is ",result)
        self.assertEqual('No Files found',ob.get_count(result),'get_count failed')
        self.assertEqual('No Files found',result,'Message wrong')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testfind_file_constraints']
    unittest.main()