#test ovando_run.sh file

# could create a system that updates the database first - then retrieves the data

# update the database 
cd /Users/apple/Documents/corporate_organisation/systems_automation/program/python_code
python3 mass_import_bankaccount.py
python3 csv_to_sqlite_iphone_contacts.py
#csv_to_sqlite_uni_contacts2.py
#python3 csv_to_sqlite_orders.py

# remove duplicates - iphone
cd /Users/apple/Documents/corporate_organisation/systems_automation/program/python_code/remove_duplicates
python3 remove_iphone_duplicates.py

# output the data to a csv file
sqlite3 -header -csv /Users/apple/Documents/corporate_organisation/systems_automation/program/database/iphoneContacts.db "select * from iphoneContacts2 group by phone_number1, phone_number2 having phone_number1 like '+44%' or phone_number1 like '07%' or phone_number2 like '+44%' or phone_number2 like '07%';" > /Users/apple/Documents/corporate_organisation/systems_automation/program/csv/csv_marketing/iphoneCont_groupby.csv

# update client map
#cd /Users/apple/Documents/corporate_organisation/systems_automation/program/analytics/
cd /Users/apple/Documents/corporate_organisation/systems_automation/program/analytics/json_choropleth_map 
python3 client_map_2.py

# retrieve the data
cd /Users/apple/Documents/corporate_organisation/systems_automation/program/analytics
python3 retrieve_orders_fn.py
python3 retrieve_Tasters_fn.py