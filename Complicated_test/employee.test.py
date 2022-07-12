import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
     #setUp run before the test run

    def setUp(self):
        self.emp_1 = Employee('stephen', 'kihuni', 40000)
        self.emp_2 = Employee('michael', 'kihuni', 90000)
    
    #tearDown run after the test has run
    def tearDown(self):
        pass


    def test_email(self):
        self.assertEqual(self.emp_1.email, 'stephen.kihuni@email.com')
        self.assertEqual(self.emp_1.email, 'michael.kihuni@email.com')

        self.emp_1.first = 'john'
        self.emp_2.first = 'jane'

        self.assertEqual(self.emp_1.email, 'john.kihuni@email.com')
        self.assertEqual(self.emp_2.email, 'jane.kihuni@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'stephen kihuni')
        self.assertEqual(self.emp_2.fullname, 'michael kihuni')

        self.emp_1.first = 'john'
        self.emp_2.first = 'jane'

        self.assertEqual(self.emp_1.fullname, 'john kihuni')
        self.assertEqual(self.emp_2.fullname, 'jane kihuni')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 40000 )
        self.assertEqual(self.emp_2.pay, 90000 )


if __name__ == '__main__':
    unittest.main()

