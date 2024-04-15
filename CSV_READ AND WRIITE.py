import csv
with open('Giants.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)

with open(path + "/ErrorAnnotatedList.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["NAME", "INDEX"])

with open(path + "/ErrorAnnotatedList.csv", 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([data_img, index])
    writer.writerow([data_txt, index])



'''

# importing the csv module
import csv

# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
		{'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
		{'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
		{'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
		{'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
		{'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv dict writer object
	writer = csv.DictWriter(csvfile, fieldnames=fields)

	# writing headers (field names)
	writer.writeheader()

	# writing data rows
	writer.writerows(mydict)

-------------------------------

import csv

# Define the data to be written to the CSV file
data = [
	['Name', 'Age', 'City'],
	['Alice', 25, 'New York'],
	['Bob', 30, 'Los Angeles'],
	['Charlie', 35, 'Chicago']
]

# Specify the file name
filename = 'data_pipe_delimited.csv'

# Write data to the CSV file with a pipe delimiter
with open(filename, 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter='|')
	csvwriter.writerows(data)

print(f"Data has been written to {filename}")



'''