# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0),1)
        self.assertEqual(utils.fact(3),6)
        pass
    
    def test_roots(self):
        self.assertEqual(utils.roots(2,5,3),(-2,-3))

        pass
    
    def test_integrate(self):
        self.assertEqual((5,0,2),10)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
