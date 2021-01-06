# CSV files stand for (Common Separated Value) which is a simple file format  used to store tabular data, such as spreadsheet or database..
import csv

# csv filename
filename = "Machine_readable_file_bd_employ.csv"

# initialize the title and row list
fields = []
rows = []
# Reading csv file
with open(filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # creating the csv reader object
    for data in csv_reader:
        print(data)
