"""
    Description: Testing simple key value store useful for POCs
"""


import os 

from library.filekvstore import KVStore

class TestKV():

    def __init__(self):

        ## Initialize a key value store on disk 
        self.kvobj = KVStore("test-kv1")


    def results(self, headingstr, keys):
        """
            Description: Display results in a common format.
        """

        ## Get results for string key value pairs
        print("-"*80)
        print(f"Results of {headingstr}".center(80))
        print("-"*80)

        for key in keys:
            print(f"Lookup result ['{key}']: "  + str(self.kvobj.get(key)))

        print("-"*80 + "\n\n")

    def string_kvtests(self):
        """
            Description: Basic string value tests. Add more as per usecase
        """

        ## Add as many keys as required for testing
        testkeys   = ['test_string1', 'test_string2', 'test_string3',
                'test_string4', 'test_string5', 'test_string6']

        ## Add as many values as keys for testing
        testvalues = ['value1', 'value2', 'value3', 'value4', 'value5', 'value6']

        ## Add kv string objects
        for key, value in zip(testkeys, testvalues):
            self.kvobj.add(key, value)

        ## Display lookup results
        self.results("basic string tests", testkeys)

    def list_kvtests(self):
        """
            Description: Basic list value tests. Add more as per usecase
        """
        ## Add as many keys as required for testing
        testkeys   = ['test_string1', 'test_string2', 'test_string3',
                'test_string4', 'test_string5', 'test_string6']

        ## Add kv string objects
        for testidx, key in enumerate(testkeys, start=1):
            self.kvobj.add(key, [f"value{testidx}1", f"value{testidx}2"])

        ## Display lookup results
        self.results("basic list tests", testkeys)


    def basic_tests(self):
        """
            Description: Execute some basic tests to check if module
                         serves a given set of requirements.
        """

        self.string_kvtests()
        self.list_kvtests()


if __name__ == '__main__':

    tesstkv = TestKV()
    tesstkv.basic_tests()
