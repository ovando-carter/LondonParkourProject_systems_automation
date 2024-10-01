################################################################################################################################
# Set up #######################################################################################################################
import sqlite3  # to connect to sqlite3
from datetime import datetime # to modify dates to the SQL standard


################################################################################################################################
# Connect to sqlite
################################################################################################################################

connection = sqlite3.connect("company_bankstatement.db")

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

# fetch the sum of the information between two dates. 
sumNov = cursor.execute("select sum(Value) from BusinessAccount where Dates between '2020-11-01' and '2020-12-01' and Value > 0;").fetchall()
print('\n Total Recipts Nov: £', str('{:,.2f}'.format(sumNov[0][0])))

sumCoaching = cursor.execute("select sum(Value) from BusinessAccount where Dates between '2020-11-01' and '2020-12-01' and Descriptions like '%TO A/C 49054287%';").fetchall()
modSumCoaching = abs(sumCoaching[0][0])
print('\n Coaching expences Nov: £', str('{:,.2f}'.format(modSumCoaching)))

sumTotRevenue = cursor.execute("select sum(Value) from BusinessAccount where Value > 0;").fetchall()
print('\n Total Revenue 2020/21: £', str('{:,.2f}'.format(sumTotRevenue[0][0])))

sumTotExpense = cursor.execute("select sum(Value) from BusinessAccount where Value < 0;").fetchall()
modSumTotExpense = abs(sumTotExpense[0][0])
print('\n Total Expense 2020/21: £', str('{:,.2f}'.format(modSumTotExpense)))

sumSalesCoaching = cursor.execute("select sum(Value) from BusinessAccount where Dates between '2020-11-01' and '2020-12-01' and Value > 0 and Descriptions like '%EVENTBRITE%';").fetchall()
print('\n Total Revenue Coaching Nov: £', str('{:,.2f}'.format(sumSalesCoaching[0][0])))

sumSalesNov = cursor.execute("select sum(Value) from BusinessAccount where Dates between '2020-11-01' and '2020-12-01' and Value > 0;").fetchall()
print('\n Total Revenue Nov: £', str('{:,.2f}'.format(sumSalesNov[0][0])))


# Save the changes to the database
connection.commit()

'''
# other commands
# If I want to select specific payments to be separated into categories
select * from bankstatement where Descriptions like '%EVENTBRITE INC.%';

# If I want to sellect only positive values (income)
select * from bankstatement where Value < 0;

# If I want to sellect two values between two dates and for positive values (income)
select * from bankstatement where Dates between '2020-11-01' and '2020-12-01' and Value > 0;

# If I want to sum the values within a specifi selection - only positive values, between two dates
select sum(Value) from bankstatement where Dates between '2020-11-30' and '2020-11-9' and Value > 0;

# A way to categorise each transaction - if it has an eventbrite description, a positive value, 
# and is in the month of Nov then it is a coaching based income. 
select * from bankstatement where Dates between '2020-11-01' and '2020-12-01' and Value > 0 and Descriptions like '%EVENTBRITE%';

# This will sume the value of all that are selected within a certain range
select sum(Value) from bankstatement where Dates between '2020-11-01' and '2020-12-01' and Value > 0 and Descriptions like '%EVENTBRITE%';

# able to do a total sum of all income in this month
select sum(Value) from bankstatement where Dates between '2020-11-01' and '2020-12-01' and Value > 0;


# find all the payments that the company made to me, including loan payback
select sum(Value) from bankstatement where Descriptions like '%TO A/C 49054287%';

# find how much the company made in revenue this year
select sum(Value) from bankstatement where Value > 0;

# find out how much the company spent this year
select sum(Value) from bankstatement where Value < 0;
'''