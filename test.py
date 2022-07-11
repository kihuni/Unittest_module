import unittest
from unittest import result
import calc

class TestUnitestMethods(unittest.TestCase):

    def test_add(self):
        result = calc.add(10,15)
        self.assertEqual(result, 25)
