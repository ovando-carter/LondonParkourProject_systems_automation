################################################################################################################################
# Set up #######################################################################################################################
import csv # To import csv files
import sqlite3  # to connect to sqlite3
import os


################################################################################################################################
# Import bank statements from csv file
################################################################################################################################


#Check the names of the files in the directory
dirList = os.listdir('/Users/apple/Documents/corporate_organisation/systems_automation/program/csv/csv_marketing')

print()

for name in dirList: 
    print(name)

#select the new csv file you would like to add to the database
csv_file = input('type the csv file name that you wish to use: ')

#Create a list of emails from the CSV file downloaded from eventbrite  

# needs a way to check if a file has been uploaded already. Or at least to make sure that there is no repeated inputs

Name = []
FirstName = []
LastName = []
Email = []


# Open bank statement csv file as bank_statement
with open('/Users/apple/Documents/corporate_organisation/systems_automation/program/csv/csv_marketing/' + csv_file) as uni_contacts:
    
  uni_contacts_dict = csv.DictReader(uni_contacts)
  
  # check what the dictionary has labled as a key. For some reason it has saved it as \ufeffName. 
  #print(list(uni_contacts_dict))
  
  # select information from each row and place 
  # them in to their respective lists
  for row in uni_contacts_dict:
      # make sure there is no space on the first line.
      Name.append(row['\ufeffName'])      
      Email.append(row['email'])
      
for n in Name: 
    nom = n.split(" ")
    FirstName.append(nom[0])
    LastName.append(nom[-1])
     
################################################################################################################################
# Connect to sqlite
################################################################################################################################

connection = sqlite3.connect("/Users/apple/Documents/corporate_organisation/systems_automation/program/database/uniContacts.db")

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
cursor.execute("CREATE TABLE IF NOT EXISTS uniContacts (FirstName varchar(255), LastName varchar(255), Email varchar(255))") 


# Insert data from lists 
for i in range(0, len(Name)):

    # use SQL-parameters to insert the data into to the INSERT statement
    params = (FirstName[i], LastName[i], Email[i]) 

    # Insert data into table
    cursor.execute("INSERT INTO  uniContacts VALUES (?, ?, ?)", params)
  


# Save the changes to the database
connection.commit()

'''
# We can retrieve those rows using a SELECT SQL statement
rows = cursor.execute("select * from Orders").fetchall()
print('\n',rows)


'''

