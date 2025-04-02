import csv
import os

landing = f'{os.path.abspath(os.curdir)}/in'

# Define the headers and rows for the CSV file
headers = ['Name', 'Age', 'Occupation']
rows = [
    ['John Dutton', 65, 'Governor'],
    ['Jaime Dutton', 36, 'Attorney'],
    ['Beth Dutton', 22, 'Trader'],
    ['Kayce Dutton', 34, 'Commissioner'],
    ['Tate Dutton', 6, 'Student']
]

# Define the CSV file path
csvfile = f'{landing}/dutton_family.csv'

with open(csvfile, 'w', newline='', encoding='utf-8') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(headers)
    csvwriter.writerows(rows)


