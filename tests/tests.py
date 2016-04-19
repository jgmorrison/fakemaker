import unittest
import os
import fake_maker
from random import randint

class TestFakeMake(unittest.TestCase):

    #Verify that fakemaker.csv was created in current working directory.
    def test_for_file(self):
        def file_check():
            test_inst = fake_maker.FakeMake()
            test_inst.personal_data(1)
            if 'fakemaker.csv' in os.listdir('./'):
                return True
            else:
                return False
        self.assertTrue(file_check())

    #Verify the first line is the header column.
    #def test_header_column(self):

    #verify the correct amount of rows were created from the amount
    #passed to the personal_data() command
    def test_row_amount(self):
        def line_count():
            amount = randint(2, 20)
            test_inst = fake_maker.FakeMake()
            test_inst.personal_data(amount)
            test_file = open('fakemaker.csv', 'r').readlines()
            count = 0
            for line in test_file:
                count += 1

            if count - 1 == amount:
                return True
            else:
                return False
        self.assertTrue(line_count())

if __name__ == '__main__':
    unittest.main()
