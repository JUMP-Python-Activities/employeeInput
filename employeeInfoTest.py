import unittest 
from unittest.mock import patch
from io import StringIO

import employeeInfo as employee

class TestUserInput(unittest.TestCase):

    @patch('sys.stdin', StringIO('Ethan Winters\n39'))
    @patch('sys.stdout', new_callable= StringIO)
    def test_output(self, stdout):
        #Run the function
        x = employee
        x.employee()

        #Save what we are expecting
        expected= "Full Name: Age: First Name: Ethan\nLast Name: Winters\nBirth Year: 1984\nEmail: Ethan.Winters@company.com\n"

        #Check values
        self.assertEqual(stdout.getvalue(), expected)

    
if __name__ == '__main__':
    unittest.main()