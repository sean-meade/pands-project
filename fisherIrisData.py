import csv

with open('iris.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    x = 0
    setosa = []
    versicolor = []
    virginica = []
    
    for row in reader:
        if row[4] == "Iris-setosa":
            setosa.append(row[0:4])

        elif row[4] == "Iris-versicolor":
            versicolor.append(row[0:4])
            
        elif row[4] == "Iris-virginica":
            virginica.append(row[0:4])
        
        else:
            print("Unlabled entry.")
        
    if len(virginica) != 50 | len(versicolor) != 50 | len(setosa):
        print("Error with size of Lists.")

    def mean(list_name, index):
        count = len(list_name)
        total = 0
        for j in range(0, count):
            total = total + float(list_name[j][index])
        mean = total/count
        return mean

    print(mean(versicolor, 0))




        
        
        
        
        
        
"""sepalL.append(row[0])
sepalW.append(row[1])
petalL.append(row[2])
petalw.append(row[3])
sepalL = []
sepalW = []
petalL = []
petalW = []
    """