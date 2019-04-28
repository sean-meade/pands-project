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
    allDataSet = []
    
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
    
    # Collect all data into one array
        allDataSet.append(row[0:4])
        
# Check to see if all data is there (50 in each)
if len(virginicaList) != 50 | len(versicolorList) != 50 | len(setosaList):
        print("Error with size of Lists.")

# Convert lists to numpy arrays
Setosa = np.array(setosaList).astype(np.float)
Versicolor = np.array(versicolorList).astype(np.float)
Virginica = np.array(virginicaList).astype(np.float)
irisDataSet = np.array(allDataSet).astype(np.float)

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
    SepLstd = np.std(arrayName[:,0])
    
    SepWmin = np.min(arrayName[:,1])
    SepWmax = np.max(arrayName[:,1])
    SepWmean = np.mean(arrayName[:,1])
    SepWstd = np.std(arrayName[:,1])
    
    PetLmin = np.min(arrayName[:,2])
    PetLmax = np.max(arrayName[:,2])
    PetLmean = np.mean(arrayName[:,2])
    PetLstd = np.std(arrayName[:,2])
    
    PetWmin = np.min(arrayName[:,3])
    PetWmax = np.max(arrayName[:,3])
    PetWmean = np.mean(arrayName[:,3])
    PetWstd = np.std(arrayName[:,3])

    print(f"\nFor {name}:\n"
            f"Sepal Length min, max, mean and standard deviation:{round(SepLmin, 2)}, {round(SepLmax, 2)}, {round(SepLmean, 2)}, {round(SepLstd, 2)}\n"
            f"Sepal width min, max, mean and standard deviation: {round(SepWmin, 2)}, {round(SepWmax, 2)}, {round(SepWmean, 2)}, {round(SepWstd, 2)}\n"
            f"Petal length min, max, mean and standard deviation: {round(PetLmin, 2)}, {round(PetLmax, 2)}, {round(PetLmean, 2)}, {round(PetLstd, 2)}\n"
            f"Petal width min, max, mean and standard deviation: {round(PetWmin, 2)}, {round(PetWmax, 2)}, {round(PetWmean, 2)}, {round(PetWstd, 2)}")
    print("\n")

# Call function to go through each Iris and produce min, max and mean
allFlowers(flowers)

# Creating scatter plots

# First scatter plot: Sepal length vs. sepal width

# Setosa Sepal length and width
setSepLvW = (Setosa[:,0], Setosa[:,1])
# Versicolor Sepal length and width
verSepLvW = (Versicolor[:,0], Versicolor[:,1])
# Virginica Sepal length and width
virSepLvW = (Virginica[:,0], Virginica[:,1])

# Setting up graph
data = (setSepLvW, verSepLvW, virSepLvW)
colors = ("red", "green", "blue")
groups = ("Setosa", "Versicolor", "Virginica")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha = 0.8, c=color, edgecolors='none', s=30, label=group)

plt.xlabel("length (cm)")
plt.ylabel("width (cm)")

plt.title("Sepal Length vs Sepal Width")
plt.legend(loc=2)
'''plt.show()'''

# Second scatter plot: Petal length vs. Petal width

# Setosa Petal length and width
setPetLvW = (Setosa[:,2], Setosa[:,3])
# Versicolor Petal length and width
verPetLvW = (Versicolor[:,2], Versicolor[:,3])
# Virginica Petal length and width
virPetLvW = (Virginica[:,2], Virginica[:,3])

# Setting up graph
data = (setPetLvW, verPetLvW, virPetLvW)
colors = ("red", "green", "blue")
groups = ("Setosa", "Versicolor", "Virginica")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha = 0.8, c=color, edgecolors='none', s=30, label=group)

plt.xlabel("length (cm)")
plt.ylabel("width (cm)")

plt.title("Petal Length vs Petal Width")
plt.legend(loc=2)
'''plt.show()'''

# Third scatter plot: Sepal length*width vs. Petal length*width

# Setosa Sepal length*width
setSepLbW = (Setosa[:,0]*Setosa[:,1])
# Setosa Petal length*width
setPetLbW = (Setosa[:,2]*Setosa[:,3])
# Setosa Sepal and Petal
setosaPlot = (setSepLbW, setPetLbW)

# Versicolor Sepal length*width
verSepLbW = (Versicolor[:,0]*Versicolor[:,1])
# Versicolor Petal length*width
verPetLbW = (Versicolor[:,2]*Versicolor[:,3])
# Versicolor Sepal and Petal
versicolorPlot = (verSepLbW, verPetLbW)

# Virginica length*width
virSepLbW = (Virginica[:,0]*Virginica[:,1])
# Virginica length*width
virPetLbW = (Virginica[:,2]*Virginica[:,3])
# Virginica Sepal and Petal
virginicaPlot = (virSepLbW, virPetLbW)


# Setting up graph
data = (setosaPlot, versicolorPlot, virginicaPlot)
colors = ("red", "green", "blue")
groups = ("Setosa", "Versicolor", "Virginica")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha = 0.8, c=color, edgecolors='none', s=30, label=group)

plt.xlabel("Sepal L x W (cm^2)")
plt.ylabel("Petal L X W (cm^2)")

plt.title("Sepal Length by Width vs. Petal Length by Width")
plt.legend(loc=2)
'''plt.show()'''

# K-Nearest Neighbors
# Using this algorithm wit the data we have we can find a new data entry (an unidentified iris)
# and find a closest match to it.

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

# Create standardizer
standardizer = StandardScaler()

# Standardize data set
data_standardized = standardizer.fit_transform(irisDataSet)

# Two nearest neighbors
nearest_neighbors = NearestNeighbors(n_neighbors=2).fit(data_standardized)

# A new entry to test (i.e. a new unidentified iris with measurements)

sepalLength = float(input("Please enter sepal length measurement for unidentified iris: "))
sepalWidth = float(input("Please enter sepal width measurement for unidentified iris: "))
petalLength = float(input("Please enter petal length measurement for unidentified iris: "))
petalWidth = float(input("Please enter petal width measurement for unidentified iris: "))

new_entry = [sepalLength, sepalWidth, petalLength, petalWidth]

# Find 
distances, indices = nearest_neighbors.kneighbors([new_entry])

nearestN = data_standardized[indices]

nearestN = np.array(nearestN).astype(np.float)
# [[nearestN[0][0][0], nearestN[0][0][1], nearestN[0][0][2], nearestN[0][0][3]], [nearestN[0][1][0], nearestN[0][1][1], nearestN[0][1][2], nearestN[0][1][3]]]
print(f"The two nearest fits are {nearestN[0][0]} and {nearestN[0][1]}")
print(nearestN[0])
print(Setosa[1])
for i in range(0, len(setosaList)):
    if Setosa[i] == nearestN[0] | Setosa[i] == nearestN[1]:
        print("It matches close to a Setosa in data set.")
    elif Virginica[i] == nearestN[0] | Virginica[i] == nearestN[1]:
        print("It matches close to a virginica in data set.")
    elif Versicolor[i] == nearestN[0] | Versicolor[i] == nearestN[1]:
        print("It matches close to a versicolor in data set.")


# By these outputs it can be determined to some degree of sucess which iris it is.
