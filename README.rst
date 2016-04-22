Fake Maker
==========

Easily make a CSV with individual personal data for as many rows as needed. Useful for testing applications that require user or customer data. Each row will contain separate columns for First_Name, Last_Name, Address, City, State, Zip, Joined, Age, Gender, Email. 


**Installation:**

    ``pip install git+https://github.com/jgmorrison/fake_maker.git``

**Usage:**

Simply pass the amount of rows as an argument to the personal_data() function attached to an instance of FakeMake(). The result will be a useable CSV file named fakemaker.csv in your current working directory.

   ``from fake_maker Import FakeMake``

   ``fake = Fake_Make()``

   ``fake.personal_data(100)``

**Example Results:**

``First_Name, Last_Name, Address, City, State, Zip, Joined, Age, Gender, Email``

``Marianita,Mosciski,66080 Van Stream Suite 650,Schuppeside,IA,97010,1973-12-23,60,Female,spinkaantionette@rodriguez.com``

``Edmon,Robel,39585 Abbott Pass Apt. 256,Stanburgh,MP,98269,2000-07-18,70,Male,zsawayn@yahoo.com``

``Tula,Wilderman,90494 Gladyce Viaduct Apt. 102,Marcellebury,GA,74831,2012-10-04,22,Female,asatterfield@gmail.com``

``Brandy,Kling,497 Son Key Apt. 168,Deckowside,OK,79522,2009-10-30,77,Male,fsmitham@gutmann.com``

``Jeanette,Smith,6171 Bins Extension,Dolahaven,NY,74042,2001-11-13,52,Female,wongcollins@gmail.com``
