#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
clean.py : data cleaning script
adapt your file name and column_names
(column_names : names of columns that contain numerical data)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "zomatocleaned_v1.csv"
filename_clean = "zomatocleaned_v2.csv"

print("Data cleaning script")

# load a csv in a dataframe
df = pd.read_csv(filename)

print("Shape: ")
print(df.shape)
print("Head:")
print(df.head())
#print(df)

# Get the column names as a list
cols = list(df.columns)
print("Column names as a list:")
for col in cols:
    print(col)

# To drop missing values, use the .dropna() method
df.dropna(inplace=True)

# To fill in missing values, use the .fillna() method
#df.fillna(value=0, inplace=True)

# duplicates
print("df.duplicated().sum():")
print(df.duplicated().sum())
print("Dropping duplicates...")
df.drop_duplicates(inplace = True)

# outliers
# specify the columns to plot
column_names =['rating','votes', 'approx_cost']

# create a boxplot for each column
for column_name in column_names:
    plt.boxplot(df[column_name])
    plt.title(column_name)
    plt.show()

# User message
print("Edit the code to drop outliers")

# drop outliers
# rating
upper_bound = 4.75
lower_bound = 1
print("Dropping rating < {} and rating > {}".format(lower_bound, upper_bound))
df = df[df['rating'] > lower_bound]
df = df[df['rating'] < upper_bound]

# votes
upper_bound = 4500
lower_bound = 0
print("Dropping votes < {} and votes > {}".format(upper_lower, upper_bound))
df = df[df['votes'] > lower_bound]
df = df[df['votes'] < upper_bound]

# approx_cost
upper_bound = 400
lower_bound = 0
print("Dropping approx_cost < {} and approx_cost > {}".format(lower_bound, upper_bound))
df = df[df['approx_cost'] > lower_bound]
df = df[df['approx_cost'] < upper_bound]

# create a boxplot for each column
for column_name in column_names:
    plt.boxplot(df[column_name])
    plt.title(column_name)
    plt.show()

# inconsistant data
"""
plt.scatter(df['column_name1'], df['column_name2'])
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.title('Scatter Plot')
plt.show()
df = df[df['column_name'] == 'appropriate_value']

"""

# save the clean data
print("Saving the clean data as {}".format(filename_clean))
df.to_csv(filename_clean, index=False)
