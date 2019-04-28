import csv
import numpy as np
import matplotlib.pyplot as plt

# Taking in data from the csv file
with open('iris.csv', 'r') as csvFile:
    # Reading that data
    reader = csv.reader(csvFile)
    # Create lists for seperated data
    setosaList = []
    versicolorList = []
    virginicaList = []
    
    # Seperate data in accordance with the iris type
    for row in reader:
        if row[4] == "Iris-setosa":
            setosaList.append(row[0:4])

        elif row[4] == "Iris-versicolor":
            versicolorList.append(row[0:4])
            
        elif row[4] == "Iris-virginica":
            virginicaList.append(row[0:4])
        
        else:
            print("Unlabled entry.")
        
# Check to see if all data is there (50 in each)
if len(virginicaList) != 50 | len(versicolorList) != 50 | len(setosaList):
        print("Error with size of Lists.")

# Convert lists to numpy arrays
Setosa = np.array(setosaList).astype(np.float)
Versicolor = np.array(versicolorList).astype(np.float)
Virginica = np.array(virginicaList).astype(np.float)

# Make an array with each iris as an element for easier access
flowers = [Setosa, Versicolor, Virginica]

# Function that will go through and lable iris type (name) and call minMaxMean
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

# Calculate min, max and mean of each element of the data for each iris
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

# Call function to go through each Iris and produce min, max and mean
allFlowers(flowers)

# Creating scatter plots