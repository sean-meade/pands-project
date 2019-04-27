import csv

with open('iris.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    x = 0
    sepalW = []
    
    for row in reader:
        sepalW.append(row[0])
        
print(len(sepalW))