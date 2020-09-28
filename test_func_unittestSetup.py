# Unit Test Module:
# 1. FilenameConvention: test_[nameOfModuleToBeTested]
# 2. Import unittest library
# 3. Import the module to be tested

import unittest
import func_unittestSetup

# Create Test Cases: Build new class that inherits from unittest's TestCase

class test_unittestSetupModule(unittest.TestCase):
    def test_add(self): # Syntax: test method MUST start with "test_" and receive i/p parameter 'self'
        self.assertEqual(func_unittestSetup.add(5,3), 8)
        #NOTES: Syntax 
        # 1. 'self'.assert
        # 2. 'moduleName'.functionName


# NOTES: Execution
# > Terminal:   
#       You CANNOT simply execute this code ($python -m test_func_unittestSetup)!
#       You must execute unittest and pass the unittest FILE as a parameter
#
#       $ python -m unittest test_func_unittestSetup.py