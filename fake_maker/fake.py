from faker import Faker
import random

class FakeMake(object):

    def __init__(self): 
        self.fake = Faker()
        

    def _gender(self):
        x = random.randint(1,2)
        if x == 1:
            return "Male"
        elif x == 2:
            return "Female"

    def _first_name(self, gender):
        if gender == "Male":
        	return self.fake.first_name_male()
        elif gender == "Female":
        	return self.fake.first_name_female()

    def personal_data(self, amount):
        file = open('fakemaker.csv', 'w')
        file.write('First_Name, Last_Name, Address, City, State, Zip, Joined, Age, Gender, Email\n')

        for run in range(amount):
            gender = self._gender()
            data = [self._first_name(gender), self.fake.last_name(), self.fake.street_address(), \
            self.fake.city(), self.fake.state_abbr(), self.fake.postalcode(), self.fake.date(), \
            str(random.randint(18, 90)), gender, self.fake.email(), "\n"]
            
            for item in data:
                if item == data[-2] or item == data[-1]:
                    file.write(item)
                else:
                    file.write(item + ",")
            
        file.close()

    #call the make function so that it is automatic on instantiation with amount.