import unittest
from account import *


class MyTestCase(unittest.TestCase):
    def test_init(self):
        name = Account('David')
        self.assertEqual(name.get_name(), 'David')
        self.assertEqual(name.get_balance(), 0)




if __name__ == '__main__':
    unittest.main()
