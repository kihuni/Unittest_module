import unittest
from unittest import result
import calc

class TestUnitestMethods(unittest.TestCase):

    def test_add(self):
        result = calc.add(10,15)
        self.assertEqual(result, 25)
    
    def test_sub(self):
        self.assertEqual(calc.sub(11,5), 6)
        
if __name__ == '__main__':
    unittest.main()
