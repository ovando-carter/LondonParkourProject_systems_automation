################################################################################################################################
# Set up #######################################################################################################################
import csv # To import csv files
import sqlite3  # to connect to sqlite3
import os


################################################################################################################################
# Import bank statements from csv file
################################################################################################################################

'''
#Check the names of the files in the directory
dirList = os.listdir('/Users/apple/Documents/corporate_organisation/systems_automation/program/csv/csv_marketing')

print()

for name in dirList: 
    print(name)

#select the new csv file you would like to add to the database
csv_file = input('type the csv file name that you wish to use: ')
'''

csv_file = 'iphoneContacts.csv'
  

# needs a way to check if a file has been uploaded already. Or at least to make sure that there is no repeated inputs


Display_Name = []
Email = []
phone_number1 = []
phone_number2 = []
FirstName = []
LastName = []




# Open bank statement csv file as bank_statement
with open('/Users/apple/Documents/corporate_organisation/systems_automation/program/csv/csv_marketing/' + csv_file) as iphone_contacts:
    
  iphone_contacts_dict = csv.DictReader(iphone_contacts)
  
  # check what the dictionary has labled as a key. For some reason it has saved it as \ufeffName. 
  #print(list(uni_contacts_dict))
  
  # select information from each row and place 
  # them in to their respective lists
  for row in iphone_contacts_dict:
      # make sure there is no space on the first line.
      #Name.append(row['\ufeffName'])      
      Display_Name.append(row['Display Name'])
      Email.append(row['E-mail Address'])
      phone_number1.append(row['Home Phone'])
      phone_number2.append(row['Mobile Phone'])

      #print(row['Display Name'])
      #print('join: ', row['Home Phone'].join(row['Mobile Phone'])) # not working - trying to put the detials of this line into one place 

      
      
      
for n in Display_Name: 
    nom = n.split(" ")
    FirstName.append(nom[0])
    LastName.append(nom[-1])
'''
for num1 in phone_number1:
    for num2 in phone_number1:
        num = num1.join(num2)
        print(num)
'''
     
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
# SQL commands
################################################################################################################################

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS iphoneContacts (FirstName varchar(255), LastName varchar(255), Email varchar(255), phone_number1 varchar(255), phone_number2 varchar(255))") 


# Insert data from lists 
for i in range(0, len(Display_Name)):

    # use SQL-parameters to insert the data into to the INSERT statement
    params = (FirstName[i], LastName[i], Email[i], phone_number1[i], phone_number2[i]) 

    # Insert data into table
    cursor.execute("INSERT INTO  iphoneContacts VALUES (?, ?, ?, ?, ?)", params)
  


# Save the changes to the database
connection.commit()

'''
# We can retrieve those rows using a SELECT SQL statement
rows = cursor.execute("select * from Orders").fetchall()
print('\n',rows)


'''

