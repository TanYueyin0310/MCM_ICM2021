import networkx as nx
import csv
import matplotlib.pyplot as plt
import numpy as np

# import data
filename = 'PCA_Vector.csv'
data = np.zeros((9))
with open(filename, errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        temp = np.array(
            [float(row['artist_id']), float(row['genre']), float(row['PCA1']), float(row['PCA2']), float(row['PCA3']),
             float(row['PCA4']), float(row['PCA5']), float(row['PCA6']), float(row['PCA7'])], )
        data = np.vstack((data, temp))
data = data[1:, :]
# calculate similarity means
genreID = 1
w = np.array([0.264869027,0.249185418,0.12477397,0.09577692,0.078685968,0.048863698,0.043861053,])
#withinSum = withinCount = 0
#btwSum = btwCount = 0
within = []
btw = []
for i in range(len(data)):
    if data[i][1] == genreID:
        for j in range(len(data)):
            if data[j][1] == genreID and j > i:
                charct1 = data[i][2:9]
                charct2 = data[j][2:9]
                diff = charct1 - charct2
                within.append(np.dot(w,np.power(diff,2)))
            # withinSum += np.dot(w,np.power(diff,2))
            # withinCount+=1
            if not data[j][1] == genreID:
                charct1 = data[i][2:9]
                charct2 = data[j][2:9]
                diff = charct1 - charct2
                btw.append(np.dot(w, np.power(diff, 2)))
            # btwSum += np.dot(w, np.power(diff, 2))
            # btwCount += 1
a

