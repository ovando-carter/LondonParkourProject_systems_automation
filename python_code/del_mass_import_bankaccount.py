#####################################################################################################
# Creator: Ovando Carter
# purpose: uploads multiple csv files at the same
# time and then creates a new csv file with multiple columns
# Original date: 2-12-2021
#####################################################################################################

# Set up
import csv # To import csv files
import sqlite3  # to connect to sqlite3
from datetime import datetime # to modify dates to the SQL standard
import sys 
import os
import glob
import pandas as pd

################################################################################################################################
# Delete table
################################################################################################################################

connection = sqlite3.connect("/Users/apple/Documents/corporate_organisation/systems_automation/program/database/londonParkourProject.db")

'''
# connection.total_changes is the total number of database rows that have been changed by connection
print(connection.total_changes)
'''

# connection.cursor() returns a Cursor object. 
# Cursor objects allow us to send SQL statements 
# to a SQLite database using cursor.execute().
cursor = connection.cursor()

# Delete table
cursor.execute("drop table IF EXISTS BusinessAccount;")

# Leave SQLite3
connection.close()


################################################################################################################################
# Mass import csv file
################################################################################################################################

# get data file names
path =r'/Users/apple/Documents/corporate_organisation/systems_automation/program/csv/csv_bankstatement/'
filenames = glob.glob(path + "/*.csv")

Dates = []
Types = []
Descriptions = []
Values = []
Balances = []
Account_Names = []
Account_Numbers = []

for filename in filenames:

    print(filename)
    # will take out and replace filename for csv_file after we check it works.
    csv_file = filename 

    # Open bank statement csv file as bank_statement
    with open(csv_file) as bank_statement:

        bank_statement_dict = csv.DictReader(bank_statement) 
        # select information from each row and place 
        # them in to their respective lists
        for row in bank_statement_dict:
            # make sure there is no space on the first line.
            # This will read the first line of the code.
            Dates.append(row['Date'])
            Types.append(row['Type'])
            Descriptions.append(row['Description'])
            Values.append(row['Value'])
            Balances.append(row['Balance'])
            Account_Names.append(row['Account Name'])
            Account_Numbers.append(row['Account Number'])


################################################################################################################################
# Connect to sqlite
################################################################################################################################

connection = sqlite3.connect("/Users/apple/Documents/corporate_organisation/systems_automation/program/database/londonParkourProject.db")

'''
# connection.total_changes is the total number of database rows that have been changed by connection
print(connection.total_changes)
'''

# connection.cursor() returns a Cursor object. 
# Cursor objects allow us to send SQL statements 
# to a SQLite database using cursor.execute().
cursor = connection.cursor()

################################################################################################################################
# Create table
################################################################################################################################

cursor.execute("CREATE TABLE IF NOT EXISTS BusinessAccount (Dates date, Types varchar(255), Descriptions varchar(255), Value int, Balances int, Account_Names varchar(255), Account_Numbers int)")

# Insert data from lists 
for i in range(0, len(Dates)):
    
    # changing the date format so I can use SQLite commands on the data later
    date_input = Dates[i]
    datetimeobject = datetime.strptime(date_input,'%d/%m/%Y')

    # converte the date to SQLite format
    new_format = datetimeobject.strftime('%Y-%m-%d')

    # use SQL-parameters to insert the data into to the INSERT statement
    params = (new_format, Types[i], Descriptions[i], Values[i], Balances[i], Account_Names[i], Account_Numbers[i])

    # Insert data into table
    cursor.execute("INSERT INTO  BusinessAccount VALUES (?, ?, ?, ?, ?, ?, ?)", params)
    
'''
# We can retrieve those rows using a SELECT SQL statement
rows = cursor.execute("select * from BusinessAccount").fetchall()
print('\n',rows)
'''

'''
check it works
# fetch the sum of the information between two dates. 
sumValue = cursor.execute("select sum(Value) from BusinessAccount where Dates between '2021-11-01' and '2021-12-01' and Value > 0;").fetchall()
print('\n',str('{:.2f}'.format(sumValue[0][0])))
'''


# Save the changes to the database
connection.commit()

