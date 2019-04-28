import csv
import numpy as np
import matplotlib.pyplot as plt

with open('iris.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    x = 0
    setosaList = []
    versicolorList = []
    virginicaList = []
    
    for row in reader:
        if row[4] == "Iris-setosa":
            setosaList.append(row[0:4])
            name = "Setosa"

        elif row[4] == "Iris-versicolor":
            versicolorList.append(row[0:4])
            name = "Versicolor"
            
        elif row[4] == "Iris-virginica":
            virginicaList.append(row[0:4])
            name = "Virginica"
        
        else:
            print("Unlabled entry.")
        

if len(virginicaList) != 50 | len(versicolorList) != 50 | len(setosaList):
        print("Error with size of Lists.")

Setosa = np.array(setosaList).astype(np.float)
Versicolor = np.array(versicolorList).astype(np.float)
Virginica = np.array(virginicaList).astype(np.float)

def mean(arrayName):

    SepLmean = np.mean(arrayName[:,0])
    SepWmean = np.mean(arrayName[:,1])
    PetLmean = np.mean(arrayName[:,2])
    PetWmean = np.mean(arrayName[:,3])

    print(f"For {name}:\nSepal Length mean: {SepLmean}\nSepal width mean: {SepWmean}\nPetal length mean: {PetLmean}\nPetal width mean: {PetWmean}")


mean(Setosa)