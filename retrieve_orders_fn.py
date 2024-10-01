# other plots for seaborn https://seaborn.pydata.org

################################################################################################################################
# Set up #######################################################################################################################
#import csv # To import csv files
import sqlite3  # to connect to sqlite3
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



database_file = 'londonParkourProject.db'

sqlite_code = "select distinct Date, count(Date) from Orders where Event_Name not like '%TRIAL%' or Event_Name not like '%TASTER%' group by Date order by Date"


def con_sqlite3(database_file, sqlite_code):

    ################################################################################################################################
    # Connect to sqlite
    ################################################################################################################################

    connection = sqlite3.connect("/Users/apple/Documents/corporate_organisation/systems_automation/program/database/" + database_file)

    # connection.cursor() returns a Cursor object. 
    # Cursor objects allow us to send SQL statements 
    # to a SQLite database using cursor.execute().
    cursor = connection.cursor()

    # We can retrieve those rows using a SELECT SQL statement  - people from trials
    cursor.execute(sqlite_code)
    rows = cursor.fetchall()

    
    ################################################################################################################################
    # convert to dataframe
    ################################################################################################################################

    df_rows = pd.DataFrame(rows)

    # convert to pandas datetime
    df_rows[0] = pd.to_datetime(df_rows[0])

    # using the quarter property
    df_rows['Quarter'] = df_rows[0].dt.quarter

    # using the month property
    df_rows['Month'] = df_rows[0].dt.month

    # using the year property
    df_rows['Year'] = df_rows[0].dt.year
    # display the dataframe
    #print(df_rows.to_string())

    return df_rows


################################################################################################################################
# draw the plot
################################################################################################################################

df_rows = con_sqlite3(database_file, sqlite_code)




ax = sns.barplot(data = df_rows, x='Month', y=1, estimator = sum, hue = 'Year',  ci=None)
ax.set(xlabel='Month', ylabel='Number of Orders  per Month')
# include numbers in the centre of the bars
ax.bar_label(ax.containers[0])  # values for bars of each class
#plt.title("Number of Trail Orders  per Month")
plt.legend(title="Year", loc="upper right")
plt.tight_layout()
plt.show()


ax = sns.barplot(data = df_rows, x='Quarter', y=1, estimator = sum, hue = 'Year', ci=None)
ax.set(xlabel='Quarter', ylabel='Number of Orders  per Quarter')
# include numbers in the centre of the bars
ax.bar_label(ax.containers[0])  # values for bars of each class
#plt.title("Number of Trial Orders  per Month")
plt.legend(title="Year", loc="upper right")
plt.tight_layout()
plt.show()


