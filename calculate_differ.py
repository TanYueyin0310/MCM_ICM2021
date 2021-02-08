import scipy.stats as st
import numpy as np
import csv

# import data
filename_pca = 'data_by_artist_with_explicit_normalization.csv'
data_artist_pca = np.zeros(16)
with open(filename_pca, errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        temp = np.array(
            [float(row['artist_id']), float(row['genre']), float(row['danceability']), float(row['energy']), float(row['valence']),
             float(row['tempo']), float(row['loudness']), float(row['mode']), float(row['key']),float(row['acousticness']),
             float(row['instrumentalness']),float(row['liveness']),float(row['speechiness']),float(row['explicit']),
             float(row['duration_ms']),float(row['popularity'])], )
        data_artist_pca = np.vstack((data_artist_pca, temp))
data_artist_pca = data_artist_pca[1:, :]
artist_id = data_artist_pca[:, 0]

filename_pca = 'influence_data_processed.csv'
data_inf_and_fol = np.zeros(2)
with open(filename_pca, errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        temp = np.array(
            [float(row['influencer_id']), float(row['follower_id'])])
        data_inf_and_fol = np.vstack((data_inf_and_fol, temp))
data_inf_and_fol = data_inf_and_fol[1:, :]
diff_sum = np.zeros(14)
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
        inf_pca = data_artist_pca[inf_idx, 2:17]
        fol_pca = data_artist_pca[fol_idx, 2:17]
        diff_temp = np.abs(inf_pca - fol_pca)
        diff_sum = np.vstack((diff_sum, diff_temp))
    else:
        diff_sum = np.vstack((diff_sum, np.zeros(14)))
with open('result_diff_normalization.csv', 'w', newline='') as csvfile:
    # spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    headers = ['artist_id','genre','danceability','energy',	'valence',	'tempo','loudness',	'mode',	'key',
               'acousticness',	'instrumentalness',	'liveness',	'speechiness',	'explicit',	'duration_ms',	'popularity', ]
    result_writer = csv.writer(csvfile, dialect='excel')
    result_writer.writerow(headers)
    for i in range(len(diff_sum)):
        info = [ j for j in diff_sum[i,:]]
        result_writer.writerow(info)