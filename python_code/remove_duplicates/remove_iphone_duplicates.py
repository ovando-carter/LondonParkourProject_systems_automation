import sqlite3  # to connect to sqlite3
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

database_file = 'londonParkourProject.db'

connection = sqlite3.connect("/Users/apple/Documents/corporate_organisation/systems_automation/program/database/" + database_file)

cursor = connection.cursor()

# We can retrieve those rows using a SELECT SQL statement  - people from trials



#this will show if there are any duplicates
cursor.execute('select FirstName, LastName, phone_number1, phone_number2, count(*) as count from iphoneContacts group by phone_number1, phone_number2 having count (*) > 1 order by phone_number1, phone_number2;')
#check1 = cursor.fetchall()
#print("number of duplicates: ", check1)

# create a new table but only with the group by numbers
cursor.execute('create table IF NOT EXISTS iphoneContacts2 as select FirstName, LastName, phone_number1, phone_number2 from iphoneContacts group by phone_number1, phone_number2;')

#check again to show if there are any duplicates, there should be none
cursor.execute('select FirstName, LastName, phone_number1, phone_number2, count(*) as count from iphoneContacts group by phone_number1, phone_number2 having count (*) > 1 order by phone_number1, phone_number2;')
#check2 = cursor.fetchall()
#print("number of duplicates: ", check2)

# check the count
# compare the count to original table to new table
cursor.execute('select count(*) from iphoneContacts;')
numContacts_oldTable = cursor.fetchall()
print("number of contacts in old table: ", numContacts_oldTable)

cursor.execute('select count(*) from iphoneContacts2;')
numContacts_newTable = cursor.fetchall()
print("number of contacts in new table: ", numContacts_newTable)


#check tables
#cursor.execute('.table')
#tables = cursor.fetchall()
#print(tables)

#delete a table 
cursor.execute('drop table iphoneContacts;')

# remove non uk numbers - starting with +44 or 07 
cursor.execute("select * from iphoneContacts2 group by phone_number1, phone_number2 having phone_number1 like '+44%' or phone_number1 like '07%' or phone_number2 like '+44%' or phone_number2 like '07%';")

