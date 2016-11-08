from random import randint
from faker import Faker


class Customer(object):

    def __init__(self):
        self.fake = Faker()
        self.gender = self._gender()
        self.first_name = self._first_name(self.gender)
        self.last_name = self.fake.last_name() 
        self.age = randint(18, 90)
        self.street_address = self.fake.street_address()
        self.state = self.fake.state_abbr()
        self.zip_code = randint(10000, 99500)
        self.date = self.fake.date()
        self.email = self.fake.email()

    def _gender(self):
        selection = randint(1, 2)
        if selection == 1:
            return "Male"
        elif selection == 2:
            return "Female"

    def _first_name(self, gender):
        if gender == "Male":
            return self.fake.first_name_male()
        elif gender == "Female":
            return self.fake.first_name_female()

    def __repr__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.last_name, self.first_name, self.age, self.gender, self.street_address, self.state, self.zip_code, self.date, self.email)


def printer(amount):
    for i in range(amount):
        customer = Customer()
        print(customer)
