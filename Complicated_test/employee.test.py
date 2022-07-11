import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('stephen', 'kihuni', 40000)
        emp_2 = Employee('michael', 'kihuni', 90000)

        self.assertEqual(emp_1.email, 'stephen.kihuni@email.com')
        self.assertEqual(emp_1.email, 'michael.kihuni@email.com')

if __name__ == '__main__':
    unittest.main()

