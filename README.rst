Fake Maker
==========

Easily make a CSV with individual personal data for as many rows as needed. Useful for testing applications that require user or customer data. each row will contain separate columns for First_Name, Last_Name, Address, City, State, Zip, Joined, Age, Gender, Email. 


**Installation:**

    ``pip install git+https://github.com/jgmorrison/fake_maker.git``

**Usage:**

Simply pass the amount of rows as an argument to the personal_data() function attached to an instance of fake_maker.FakeMake(). The result will be a useable CSV file named fakemaker.csv in your current working directory.

   ``from fake_maker Import FakeMake``

   ``fake = Fake_Make()``

   ``fake.personal_data(100)``
