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
        self.assertEqual(func_unittestSetup.add(-5,-2), -7)
        self.assertEqual(func_unittestSetup.add(3,-3), 0)
        #NOTES: Syntax 
        # 1. 'self'.assert
        # 2. 'moduleName'.functionName

    def test_mult(self): 
        self.assertEqual(func_unittestSetup.mult(5,3), 15)
        self.assertEqual(func_unittestSetup.mult(-5,-2), 10)
        self.assertEqual(func_unittestSetup.mult(3,-3), -9)

    def test_div(self):
# Task:     Test error handling in code
#
# Challenge:If code error handler correctly identified invalid data and raises an exception
#            We want the unit test to PASS (not fail by registing the error raised in code)
# 
# Method 1: Let unittest call function on your behalf
#       self.assertRaises(ValueError, func_unittestSetup.div(0,3)) >> WRONG SYNTAX: will lead to value error being raised (code abort)
        self.assertRaises(ValueError, func_unittestSetup.div,0,3)
        self.assertRaises(ValueError, func_unittestSetup.div,3,0)        
# Method 2: Use context handler
        with self.assertRaises(ValueError):
            func_unittestSetup.div(0,3)
        with self.assertRaises(ValueError):
            func_unittestSetup.div(3,0)



# Allow module to be executed directly 
# (rather than having to execute unittest with the module as a parameter)
# > With the addition of the line below, you can now run the unit test via
#   1. The terminal: $ python test_func_unittestSetup.py 
#   2. By 'run'ing the local file from the IDE
if __name__=='__main__':
    unittest.main()