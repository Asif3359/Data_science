import pandas as pd
import numpy as np

# Load CSV file with header
data_csv = pd.read_csv("../DataSet/percent_bachelors_degrees_women_usa.csv")
print(data_csv.head())
print(data_csv.tail())

# List of columns
print(data_csv.columns)

# Information of dataset
print(data_csv.info())

# Drop missing values
data_csv = data_csv.dropna()  # No missing values in the dataset

# Fill missing values with "NALL" (if there were any)
data_csv = data_csv.fillna("NALL")

# remove duplicates data
data_csv = data_csv.drop_duplicates()
print(data_csv.info())