# Notes:
# 1. References at the end.
# 2. Used reference [2] throughout.
# 3. Data downloaded from reference [7].
import csv
import numpy as np
import matplotlib.pyplot as plt

'''
Used reference [3] and [4] for dealing with lists and arrays here. 
'''
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

# Convert lists to numpy arrays with floats
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
        minMaxMean(allFlowers[i], name)

# Calculate min, max and mean of each element of the data for each iris
def minMaxMean(arrayName, name):

    name = name
    #set values for each
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
    
    # Print all values
    print(f"\nFor {name}:\n"
            f"Sepal Length min, max, mean and standard deviation: {round(SepLmin, 2)}, {round(SepLmax, 2)}, {round(SepLmean, 2)}, {round(SepLstd, 2)}\n"
            f"Sepal width min, max, mean and standard deviation: {round(SepWmin, 2)}, {round(SepWmax, 2)}, {round(SepWmean, 2)}, {round(SepWstd, 2)}\n"
            f"Petal length min, max, mean and standard deviation: {round(PetLmin, 2)}, {round(PetLmax, 2)}, {round(PetLmean, 2)}, {round(PetLstd, 2)}\n"
            f"Petal width min, max, mean and standard deviation: {round(PetWmin, 2)}, {round(PetWmax, 2)}, {round(PetWmean, 2)}, {round(PetWstd, 2)}")
    print("\n")

# Call function to go through each Iris and produce min, max and mean
allFlowers(flowers)
'''
Used reference [5] and [6] to mainly get the graphs looking the way I wanted and to tidy code
'''
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
# Set one by one grid
ax = fig.add_subplot(1, 1, 1)

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha = 0.8, c=color, edgecolors='none', s=30, label=group)

plt.xlabel("length (cm)")
plt.ylabel("width (cm)")

plt.title("Sepal Length vs Sepal Width")
plt.legend(loc=2)
plt.show()

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
plt.show()

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
plt.show()

'''
Used Reference 1 'Machine Learning with Python Cookbook' for all next section except prompts and if statement.
'''
# K-Nearest Neighbors
# Using this algorithm wit the data we have we can find a new data entry (an unidentified iris)
# and find a closest match to it.

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

x = irisDataSet
# Set targets
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
 2, 2])

# Create standardizer
standardizer = StandardScaler()

# Standardize data set
data_standardized = standardizer.fit_transform(x)

# Train knn classifier
nearest_neighbors = KNeighborsClassifier(n_neighbors=5, n_jobs=-1).fit(data_standardized, y)

# A new entry to test (i.e. a new unidentified iris with measurements)

sepalLength = float(input("Please enter sepal length measurement for unidentified iris: "))
sepalWidth = float(input("Please enter sepal width measurement for unidentified iris: "))
petalLength = float(input("Please enter petal length measurement for unidentified iris: "))
petalWidth = float(input("Please enter petal width measurement for unidentified iris: \n"))

new_entry = [sepalLength, sepalWidth, petalLength, petalWidth]

#Predict the class of new_entry
predict = nearest_neighbors.predict([new_entry, new_entry])

# Print what type it is to console
if predict[0] == 0:
    print("It matches close to a Setosa in data set.")
elif predict[0] == 1:
    print("It matches close to a virginica in data set.")
elif predict[0] == 2:
    print("It matches close to a versicolor in data set.")

'''References:
Books:
[1] - Albon, C., 2018. Machine Learning with Python Cookbook: Practical Solutions from 
Preprocessing to Deep Learning. 1st ed. 1005 Gravenstein Highway North Sebastopol, CA 95472: O'Reilly Media, 
Incorporated, 2018.
[2] - Shaw, Zed. Learn Python 3 the hard way : a very simple introduction to the terrifyingly beautiful 
world of computers and code. Boston: Addison-Wesley, 2017. Print.

Websites:
[3] - https://www.dataquest.io/blog/numpy-tutorial-python/
[4] - https://stackoverflow.com/questions/28393103/typeerror-cannot-perform-reduce-with-flexible-type
[5] - https://pythonspot.com/matplotlib-scatterplot/
[6] - https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xlabel.html
[7] - http://archive.ics.uci.edu/ml/datasets/Iris
'''
