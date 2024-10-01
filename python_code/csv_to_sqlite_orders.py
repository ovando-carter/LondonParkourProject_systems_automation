################################################################################################################################
# Set up #######################################################################################################################
import csv # To import csv files
import sqlite3  # to connect to sqlite3
from datetime import datetime # to modify dates to the SQL standard
import os


################################################################################################################################
# Import bank statements from csv file
################################################################################################################################


#Check the names of the files in the directory
dirList = os.listdir('/Users/apple/Documents/corporate_organisation/systems_automation/program/csv/csv_orders/')

print()

for name in dirList: 
    print(name)

#select the new csv file you would like to add to the database
csv_file = input('type the csv file name that you wish to use: ')

#Create a list of emails from the CSV file downloaded from eventbrite  

# needs a way to check if a file has been uploaded already. Or at least to make sure that there is no repeated inputs

Event_Name = []
Event_ID = []
Order_no = []
Order_Date = []
First_Name = []
Surname = []
Email = []
Quantity = []
Price_Tier = []
Ticket_Type = []
Attendee_no = []
Order_Type = []
Currency = []
Total_Paid = []
Fees_Paid = []
Eventbrite_Fees = []
Eventbrite_Payment_Processing = []
Attendee_Status = []
Mobile_Phone = []
Birth_Date = []
Shipping_Address_1 = []
Shipping_Address_2 = []
Shipping_City = []
Shipping_County = []
Shipping_Postcode = []
Shipping_Country = []
Billing_Address_1 = []
Billing_Address_2 = []
Billing_City = []
Billing_State_Province_County = []
Billing_Postcode = []
Billing_Country = []



# Open bank statement csv file as bank_statement
with open('/Users/apple/Documents/corporate_organisation/systems_automation/program/csv/csv_orders/' + csv_file) as stocks_statement:
    
  stocks_statement_dict = csv.DictReader(stocks_statement) 
  # select information from each row and place 
  # them in to their respective lists
  for row in stocks_statement_dict:
      # make sure there is no space on the first line.
      # This will read the first line of the code.
      Event_Name.append(row['Event Name'])
      Event_ID.append(row['Event ID'])
      Order_no.append(row['Order no.'])
      Order_Date.append(row['Order Date'])
      First_Name.append(row['First Name'])
      Surname.append(row['Surname'])
      Email.append(row['Email'])
      Quantity.append(row['Quantity'])
      Price_Tier.append(row['Price Tier'])
      Ticket_Type.append(row['Ticket Type'])
      Attendee_no.append(row['Attendee no.'])
      Order_Type.append(row['Order Type'])
      Currency.append(row['Currency'])
      Total_Paid.append(row['Total Paid'])
      Fees_Paid.append(row['Fees Paid'])
      Eventbrite_Fees.append(row['Eventbrite Fees'])
      Eventbrite_Payment_Processing.append(row['Eventbrite Payment Processing'])
      Attendee_Status.append(row['Attendee Status'])
      Mobile_Phone.append(row['Mobile Phone'])
      Birth_Date.append(row['Birth Date'])
      Shipping_Address_1.append(row['Shipping Address 1'])
      Shipping_Address_2.append(row['Shipping Address 2'])
      Shipping_City.append(row['Shipping City'])
      Shipping_County.append(row['Shipping County'])
      Shipping_Postcode.append(row['Shipping Postcode'])
      Shipping_Country.append(row['Shipping Country'])
      Billing_Address_1.append(row['Billing Address 1'])
      Billing_Address_2.append(row['Billing Address 2'])
      Billing_City.append(row['Billing City'])
      Billing_State_Province_County.append(row['Billing State/Province/County'])
      Billing_Postcode.append(row['Billing Postcode'])
      Billing_Country.append(row['Billing Country'])
      

################################################################################################################################
# Connect to sqlite
################################################################################################################################

connection = sqlite3.connect("/Users/apple/Documents/corporate_organisation/systems_automation/program/database/londonParkourProject1.db")

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
cursor.execute("CREATE TABLE IF NOT EXISTS Orders (Date date, Time_bought date, Event_Name varchar(255), Event_ID varchar(255), First_Name varchar(255), Surname varchar(255), Email varchar(255), Quantity int, Price_Tier varchar(255), Ticket_Type varchar(255), Attendee_no varchar(255), Order_Type varchar(255), Currency varchar(255), Total_Paid float, Fees_Paid float, Eventbrite_Fees float, Eventbrite_Payment_Processing float, Attendee_Status varchar(255), Mobile_Phone varchar(255), Birth_Date varchar(255), Shipping_Address_1 varchar(255), Shipping_Address_2 varchar(255), Shipping_City varchar(255), Shipping_County varchar(255), Shipping_Postcode varchar(255), Shipping_Country varchar(255), Billing_Address_1 varchar(255), Billing_Address_2 varchar(255), Billing_City varchar(255), Billing_State_Province_County varchar(255), Billing_Postcode varchar(255), Billing_Country varchar(255))") 


# Insert data from lists 
for i in range(0, len(First_Name)):

    # changing the date format so I can use SQLite commands on the data later
    date_input = Order_Date[i]
    datetimeobject = datetime.strptime(date_input,'%Y-%m-%d %H:%M:%S%z') 

    # separate date into date and time
    Date = datetimeobject.strftime('%Y-%m-%d')

    Time_bought = datetimeobject.strftime('%H:%M:%S')

    # use SQL-parameters to insert the data into to the INSERT statement
    params = (Date, Time_bought, Event_Name[i], Event_ID[i], First_Name[i], Surname[i], Email[i], Quantity[i], Price_Tier[i], Ticket_Type[i], Attendee_no[i], Order_Type[i], Currency[i], Total_Paid[i], Fees_Paid[i], Eventbrite_Fees[i], Eventbrite_Payment_Processing[i], Attendee_Status[i], Mobile_Phone[i], Birth_Date[i], Shipping_Address_1[i], Shipping_Address_2[i], Shipping_City[i], Shipping_County[i], Shipping_Postcode[i], Shipping_Country[i], Billing_Address_1[i], Billing_Address_2[i], Billing_City[i], Billing_State_Province_County[i], Billing_Postcode[i], Billing_Country[i]) 

    # Insert data into table
    cursor.execute("INSERT INTO  Orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
  


# Save the changes to the database
connection.commit()

'''
# We can retrieve those rows using a SELECT SQL statement
rows = cursor.execute("select * from Orders").fetchall()
print('\n',rows)


'''

