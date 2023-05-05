#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
process.py : data processing script
adapt your file name and column_names
(column_names : names of columns that contain labeled data)
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# needed to save non-blank png files under Linux Mint, comment if needed
plt.switch_backend('agg') 


# input file
filename = "zomatocleaned_v2.csv"

# folder where charts will be saved
output_folder = "output"

print("Data processing script:")

print("reading file: " + filename)
df = pd.read_csv(filename)

print("count the number of items with the same value in columns:")
columns = ['online_order', 'book_table', 'location', 'rest_type', 'type']
for column in columns:
    print("column: " + column)
    counts = df[column].value_counts()
    print(counts)

print("case of columns where cells can contain multiple values:")
columns = ['dish_liked', 'cuisines']
possible_values = []

for column_name in columns:
    for cell in df[column_name]:
        if isinstance(cell, str):
            values = cell.split(",")
            for value in values:
                value = value.strip()
                if value not in possible_values:
                    possible_values.append(value)
    # unusable data
    #print("column: " + column_name + ' possible values')
    #print(possible_values)

"""
plots the restaurant by type in a pie chart:
"""
# Creates a new dataframe with one column
new_df = pd.DataFrame(df['rest_type'])

# Group the DataFrame by the rest_type column and sum the counts
grouped = new_df.groupby('rest_type').size()

print("grouped type: ")
print(type(grouped))
#print(grouped)

# data consolidation
# Group the DataFrame by similar rest_type values and sum the counts
grouped = new_df.groupby(df['rest_type'].str.split(',\s*', expand=True)[0]).size()

# Rename the index to "rest_type" to reflect that the DataFrame has been consolidated by this column
grouped.index.name = 'rest_type'

# Sort the values by count in descending order
grouped = grouped.sort_values(ascending=False)

# Print the consolidated results
print(grouped)

# Calculate the total number of restaurants
total = grouped.sum()

# Calculate the percentages of each restaurant type
percentages = grouped / total * 100

# Filter out the labels with less than 3% of the total
filtered_series = grouped[percentages >= 3]

# TODO: would be better to add a 'miscellanious' category

# Create a new figure
fig = plt.figure()

# Create a pie chart using the filtered Series
plt.pie(filtered_series, labels=filtered_series.index, autopct='%1.1f%%')
plt.title('Restaurants by Type')
# can't show the chart after the plt.switch_backend('agg') command
#plt.show()

# save the plot in the output folder
# Create the output directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Save the plot as a PNG file in the output directory
print("saving the file as png")
filename = os.path.join('output', 'restaurant_by_type.png')
plt.savefig(filename, dpi=300)

"""
Plot the approx_cost vs. rating
"""
x_plot = 'rating'
y_plot = 'approx_cost'
# Plot the data
df.plot(x=x_plot, y=y_plot, kind='scatter')

# Add axis labels and a title
plt.xlabel(x_plot)
plt.ylabel(y_plot)
plt.title('Scatter plot of {} vs. {}'.format(y_plot, x_plot))

# Show the plot
#plt.show()

# Save the plot as a PNG file in the output directory
print("saving the file as png")
filename = os.path.join('output', 'approx_cost_vs_rating.png')
plt.savefig(filename, dpi=300)
