import csv

packing_list = [['Item', 'Quantity'], ['Towels', 5], ['Pants', 10], ['Socks', 15]]

try:
    with open('packing_list.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print('Creating new file...')
    with open('packing_list.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(packing_list)