import scipy.stats as st
import numpy as np
import csv

# import data
filename_pca = 'PCA_Vector_Normalized.csv'
data_artist_pca = np.zeros(9)
with open(filename_pca, errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        temp = np.array(
            [float(row['artist_id']), float(row['genre']), float(row['PCA1']), float(row['PCA2']), float(row['PCA3']),
             float(row['PCA4']), float(row['PCA5']), float(row['PCA6']), float(row['PCA7'])], )
        data_artist_pca = np.vstack((data_artist_pca, temp))
data_artist_pca = data_artist_pca[1:, :]
artist_id = data_artist_pca[:, 0]
w = np.array([0.264869027, 0.249185418, 0.12477397, 0.09577692, 0.078685968, 0.048863698, 0.043861053, ])

filename_pca = 'influence_data_processed.csv'
data_inf_and_fol = np.zeros(2)
with open(filename_pca, errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        temp = np.array(
            [float(row['influencer_id']), float(row['follower_id'])])
        data_inf_and_fol = np.vstack((data_inf_and_fol, temp))
data_inf_and_fol = data_inf_and_fol[1:, :]
for i in range(len(data_inf_and_fol)):
    inf_idx = fol_idx = 0
    sim = 0
    inf_id = data_inf_and_fol[i, 0]
    fol_id = data_inf_and_fol[i, 1]
    inf_idx = np.argwhere(artist_id==inf_id)
    fol_idx = np.argwhere(artist_id==fol_id)
    if not len(inf_idx)==0 and not len(fol_idx)==0:
        inf_idx = inf_idx[0, 0]
        fol_idx = fol_idx[0, 0]
        inf_pca = data_artist_pca[inf_idx, 2:9]
        fol_pca = data_artist_pca[fol_idx, 2:9]
        diff = inf_pca - fol_pca
        sim = np.sqrt(np.dot(w, np.power(diff, 2)))
    print(i, sim)
