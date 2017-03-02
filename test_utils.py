# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):  # comm inutile
    def test_fact(self):
        self.assertEqual(utils.fact(0), 1)
        self.assertEqual(utils.fact(3), 6)
        with self.assertRaises(NameError):
            utils.fact(ouygouy)

    def test_roots(self):
        self.assertEqual(utils.roots(1, 2, 3),"Ce polynôme n'a pas de racines")
        self.assertEqual(utils.roots(1, 2, 1), (-1,-1))
        self.assertEqual(utils.roots(1, -5, 4), (4, 1))

    def test_integrate(self):
        self.assertEqual(utils.integrate('x ** 2 - 1', -1, 1), -1.3333)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
