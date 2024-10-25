import pandas as pd
import sqlite3

from matplotlib.table import table

data_csv = pd.read_csv('../DataSet/housing.csv')
print(data_csv.head())

data_text = pd.read_csv('../DataSet/StudentSchools.txt', header=0, sep=",")
print(data_text.head())

excel_file = pd.ExcelFile("../DataSet/abc.xlsx")
print("Available sheet names:", excel_file.sheet_names)
data_excel = pd.read_excel("../DataSet/abc.xlsx", sheet_name="Sheet1")
print(data_excel.head())

data_json = pd.read_json("../DataSet/iris.json")
print(data_json.head())
conn = sqlite3.connect('../DataSet/iris.db')
# List all tables in the database
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Available tables: \n", tables)

# Define the data to insert
cursor = conn.cursor()
sepal_length = 5.9
sepal_width = 2.8
petal_length = 5.2
petal_width = 2
species_id = 3
cursor.execute('''
    INSERT INTO Observation (sepal_length, sepal_width, petal_length, petal_width, species_id)
    VALUES (?, ?, ?, ?, ?)
''', (sepal_length, sepal_width, petal_length, petal_width, species_id))
conn.commit()
print("Data inserted successfully.")


# Replace 'table_name' with the actual name of the table in iris.db
data_from_db = pd.read_sql_query("SELECT * FROM Observation", conn)
print(data_from_db.tail())