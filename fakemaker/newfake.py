from random import randint
from faker import Faker


class Customer(object):

    def __init__(self):
        self.fake = Faker()
        self.gender = _gender()
        self.first_name = _first_name(gender)
        self.last_name = fake.last_name()
        self.age = str(randint(18, 90))
        self.street = fake.street_address()
        self.city = fake.city()
        self.state = fake.state_abbr()
        self.zip = str(randint(10000, 99500))
        self.date = fake.date()
        self.email = fake.email()

#have not changed anything below

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

    def personal_data(self, amount):
        fake_file = open('fakemaker.csv', 'w')
        fake_file.write('First_Name,Last_Name,Address,City,State,Zip,Joined,\
Age,Gender,Email\n')

        for i in range(amount):
            gender = self._gender()
            data = [self._first_name(gender), self.fake.last_name(),
                    self.fake.street_address(), self.fake.city(),
                    self.fake.state_abbr(), str(randint(10000, 99500)),
                    self.fake.date(), str(randint(18, 90)), gender,
                    self.fake.email(), "\n"]

            for item in data:
                if item == data[-2] or item == data[-1]:
                    fake_file.write(item)
                else:
                    fake_file.write(item + ",")

        fake_file.close()

#    call the make function so that it is automatic on instantiation /
#    with amount.
