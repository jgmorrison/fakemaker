import unittest
import os
<<<<<<< HEAD
import fakemaker
=======
import fake_maker
>>>>>>> 7639aa97c757e5aeb094a8fcde7869ad4e6ddd4b
from random import randint

class TestFakeMake(unittest.TestCase):

    #Verify that fakemaker.csv was created in current working directory.
    def test_for_file(self):
        def file_check():
<<<<<<< HEAD
            test_inst = fakemaker.FakeMake()
=======
            test_inst = fake_maker.FakeMake()
>>>>>>> 7639aa97c757e5aeb094a8fcde7869ad4e6ddd4b
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
<<<<<<< HEAD
            test_inst = fakemaker.FakeMake()
=======
            test_inst = fake_maker.FakeMake()
>>>>>>> 7639aa97c757e5aeb094a8fcde7869ad4e6ddd4b
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
