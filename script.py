import csv

# Get last row
with open('sample_data.csv', newline='') as file:
    csv_reader = csv.reader(file)
    last_row = (list(csv_reader)[-1])
    last_row_index = len(list(csv_reader))

    # Go back to start of csv and get first row as bonus
    file.seek(0)
    next(csv_reader)

    try:
        first_row = next(csv_reader)
    except StopIteration as s:
        # csv doesn't have row for column names
        pass

# Iterate through csv
with open('sample_data.csv', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        pass

# Add an entry
# Throws PermissionError if the file is open in a different program
with open('sample_data.csv', mode='a', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Samosa', '10', '5', '3'])