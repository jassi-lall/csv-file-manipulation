"""
Take home points:
csv.reader(file) is an iterable
Testing is key for good application development
FileNotFound possible when using mode='r'
PermissionError 
"""
import csv

with open('sample_data.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    for i, j in enumerate(csv_reader):
        print(f"{i}) {j}")