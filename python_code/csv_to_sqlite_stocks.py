################################################################################################################################
# Set up #######################################################################################################################
import csv # To import csv files
import sqlite3  # to connect to sqlite3
from datetime import datetime # to modify dates to the SQL standard
import os

# find this file here: /Users/apple/Documents/corporate_organisation/systems_automation/program/python_code


################################################################################################################################
# Delete table
################################################################################################################################

connection = sqlite3.connect("/Users/apple/Documents/corporate_organisation/systems_automation/program/database/stocks_account2.db")

'''
# connection.total_changes is the total number of database rows that have been changed by connection
print(connection.total_changes)
'''

# connection.cursor() returns a Cursor object. 
# Cursor objects allow us to send SQL statements 
# to a SQLite database using cursor.execute().
cursor = connection.cursor()

# Delete table
cursor.execute("drop table IF EXISTS Stocks;")

# Leave SQLite3
connection.close()



################################################################################################################################
# Import bank statements from csv file
################################################################################################################################


#Check the names of the files in the directory
dirList = os.listdir('/Users/apple/Documents/corporate_organisation/systems_automation/program/csv/csv_personal/csv_stocks/')

print()

for name in dirList: 
    print(name)

#select the new csv file you would like to add to the database
csv_file = input('type the csv file name that you wish to use: ')

#Create a list of emails from the CSV file downloaded from eventbrite  

# needs a way to check if a file has been uploaded already. Or at least to make sure that there is no repeated inputs

Action = []
Time = []
ISIN = []
Ticker = []
Name = []
No_shares = []
Price = []
Currency = []
Exchange_rate =[]
Result = []
Total = []
Charge_amount = []
Notes = []
ID = []



# Open bank statement csv file as bank_statement
with open('/Users/apple/Documents/corporate_organisation/systems_automation/program/csv/csv_personal/csv_stocks/' + csv_file) as stocks_statement:
  stocks_statement_dict = csv.DictReader(stocks_statement) 
  # select information from each row and place 
  # them in to their respective lists
  for row in stocks_statement_dict:
      # make sure there is no space on the first line.
      # This will read the first line of the code.
      Action.append(row['Action'])
      Time.append(row['Time'])
      ISIN.append(row['ISIN'])
      Ticker.append(row['Ticker'])
      Name.append(row['Name'])
      No_shares.append(row['No. of shares'])
      Price.append(row['Price / share'])
      Currency.append(row['Currency (Price / share)'])
      Exchange_rate.append(row['Exchange rate'])
      #Result.append(row['Result (GBP)'])
      Total.append(row['Total (GBP)'])
      Charge_amount.append(row['Charge amount (GBP)'])
      Notes.append(row['Notes'])
      ID.append(row['ID'])
      

################################################################################################################################
# Connect to sqlite
################################################################################################################################

connection = sqlite3.connect("/Users/apple/Documents/corporate_organisation/systems_automation/program/database/stocks_account2.db")

'''
# connection.total_changes is the total number of database rows that have been changed by connection
print(connection.total_changes)
'''

# connection.cursor() returns a Cursor object. 
# Cursor objects allow us to send SQL statements 
# to a SQLite database using cursor.execute().
cursor = connection.cursor()

################################################################################################################################
# SQL commands
################################################################################################################################

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS Stocks (Date date, Time_bought date, Action varchar(255), ISIN varchar(255), Ticker varchar(255), Name varchar(255), No_shares float, stock_split float, Price float, Currency varchar(255), Exchange_rate float, Result float, Total float, Charge_amount float, Notes varchar(255), ID varchar(255), Current_value float)") 


# Insert data from lists 
for i in range(0, len(Time)):

    # changing the date format so I can use SQLite commands on the data later
    date_input = Time[i]
    datetimeobject = datetime.strptime(date_input,'%Y-%m-%d %H:%M:%S')

    # separate date into date and time
    Date = datetimeobject.strftime('%Y-%m-%d')

    Time_bought = datetimeobject.strftime('%H:%M:%S')

    Current_value = 0

    stock_split = 0
   
    Result = 0 #the last csv file did not have this so I had to take it up. But normally this would be in params as Result[i]
    # use SQL-parameters to insert the data into to the INSERT statement
    params = (Date, Time_bought, Action[i], ISIN[i], Ticker[i], Name[i], No_shares[i], stock_split, Price[i], Currency[i], Exchange_rate[i], Result, Total[i], Charge_amount[i], Notes[i], ID[i], Current_value) 

    # Insert data into table
    cursor.execute("INSERT INTO  Stocks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
  
'''
# We can retrieve those rows using a SELECT SQL statement
rows = cursor.execute("select * from BusinessAccount").fetchall()
print('\n',rows)
'''

# Save the changes to the database

connection.commit()




