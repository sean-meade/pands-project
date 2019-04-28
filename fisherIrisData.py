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

        elif row[4] == "Iris-versicolor":
            versicolorList.append(row[0:4])
            
        elif row[4] == "Iris-virginica":
            virginicaList.append(row[0:4])
        
        else:
            print("Unlabled entry.")
        

if len(virginicaList) != 50 | len(versicolorList) != 50 | len(setosaList):
        print("Error with size of Lists.")

Setosa = np.array(setosaList).astype(np.float)
Versicolor = np.array(versicolorList).astype(np.float)
Virginica = np.array(virginicaList).astype(np.float)

flowers = [Setosa, Versicolor, Virginica]

def allFlowers(allFlowers):
    for i in range(0,len(allFlowers)):
        
        if i == 0:
            name = "Setosa"
        elif i == 1:
            name = "Versicolor"
        elif i == 2:
            name = "Virginica"
        else:
            print("Error with data set. Please investigate.")
        minMaxMin(allFlowers[i], name)


def minMaxMin(arrayName, name):

    name = name
    SepLmin = np.min(arrayName[:,0])
    SepLmax = np.max(arrayName[:,0])
    SepLmean = np.mean(arrayName[:,0])
    SepWmin = np.min(arrayName[:,1])
    SepWmax = np.max(arrayName[:,1])
    SepWmean = np.mean(arrayName[:,1])
    PetLmin = np.min(arrayName[:,2])
    PetLmax = np.max(arrayName[:,2])
    PetLmean = np.mean(arrayName[:,2])
    PetWmin = np.min(arrayName[:,3])
    PetWmax = np.max(arrayName[:,3])
    PetWmean = np.mean(arrayName[:,3])

    print(f"\nFor {name}:\nSepal Length min, max and mean:{SepLmin}, {SepLmax}, {SepLmean}\n"
        f"Sepal width min, max and mean: {SepWmin}, {SepWmax}, {SepWmean}\n"
        f"Petal length min, max and mean: {PetLmin}, {PetLmax}, {PetLmean}\n"
        f"Petal width min, max and mean: {PetWmin}, {PetWmax}, {PetWmean}")


allFlowers(flowers)