import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import csv

G = nx.DiGraph()
nodelist = []
with open('influence_data_processed.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        influencer = row['influencer_id']
        follower = row['follower_id']
        connection = (influencer, follower)
        if not (influencer in nodelist):
            G.add_node(influencer,genre = row['influencer_main_genre_value'],year = row['influencer_active_start'])
            nodelist.append(influencer)
        if not (follower in nodelist):
            G.add_node(follower,genre = row['follower_main_genre_value'],year =row['follower_active_start'])
            nodelist.append(follower)
        G.add_edge(influencer,follower)
options = {
    'node_size': 20,
    'width': 0.3,
}
plt.figure(figsize=(15,9))
nx.draw(G,**options)
plt.show()