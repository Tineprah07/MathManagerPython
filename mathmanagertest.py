import unittest
from mathmanager import mathmanager

class mathmanagertest(unittest.TestCase):

    def setUp(self):
        self.mm = mathmanager()

    def testAdd(self):
        self.assertEqual(self.mm.add(0, 3), 3)

    def testSubtract(self):
        self.assertEqual(self.mm.subtract(0, 3), -3)

    def testMultiply(self):
        self.assertEqual(self.mm.multiply(0, 3), 0)

    def test_calculate_monthly_interest(self):
        self.assertAlmostEqual(self.mm.calculate_monthly_interest(1200, 1), 3.8)
        self.assertAlmostEqual(self.mm.calculate_monthly_interest(1200, 2), 3.6)

    def test_calculate_tax(self):
        self.assertEqual(self.mm.calculate_tax(10000), 0)
        self.assertEqual(self.mm.calculate_tax(20000), 1486.0)
        self.assertEqual(self.mm.calculate_tax(60000), 11432.0)
        self.assertEqual(self.mm.calculate_tax(130000), 39675.0) 

if __name__ == '__main__':
    unittest.main(verbosity=2)
