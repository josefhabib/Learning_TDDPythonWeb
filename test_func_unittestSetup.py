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

# Allow module to be executed directly 
# (rather than having to execute unittest with the module as a parameter)
# > With the addition of the line below, you can now run the unit test via
#   1. The terminal: $ python test_func_unittestSetup.py 
#   2. By 'run'ing the local file from the IDE
if __name__=='__main__':
    unittest.main()