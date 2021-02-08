import csv
import scipy.stats as st
import numpy as np

# import data
filename = 'PCA_Vector_Normalized.csv'
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

w = np.array([0.264869027, 0.249185418, 0.12477397, 0.09577692, 0.078685968, 0.048863698, 0.043861053, ])
# withinSum = withinCount = 0
# btwSum = btwCount = 0
for genreID in range(1, 21):
    within = []
    btw = []
    for i in range(len(data)):
        if data[i][1] == genreID:
            for j in range(len(data)):
                if data[j][1] == genreID and j > i:
                    charct1 = data[i][2:9]
                    charct2 = data[j][2:9]
                    diff = charct1 - charct2
                    within.append(np.sqrt(np.dot(w, np.power(diff, 2))))
                # withinSum += np.dot(w,np.power(diff,2))
                # withinCount+=1
                if not data[j][1] == genreID:
                    charct1 = data[i][2:9]
                    charct2 = data[j][2:9]
                    diff = charct1 - charct2
                    btw.append(np.sqrt(np.dot(w, np.power(diff, 2))))
                # btwSum += np.dot(w, np.power(diff, 2))
                # btwCount += 1
    if (not within == []) and (not btw == []):
        within_mean = np.mean(within)
        within_var = np.var(within)
        btw_mean = np.mean(btw)
        btw_var = np.var(btw)
        levene_stat, levene_prob = st.levene(within, btw)
        t_stat, t_prob = st.ttest_ind(within, btw, equal_var=(levene_prob > 0.05))
        print(genreID, within_mean, within_var, btw_mean, btw_var, levene_stat, levene_prob, (levene_prob > 0.05),
              t_stat, t_prob, (t_prob > 0.05))
