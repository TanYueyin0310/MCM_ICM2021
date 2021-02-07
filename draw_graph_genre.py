import networkx as nx
import csv
import matplotlib.pyplot as plt
import numpy as np
G = nx.DiGraph()
nodelist = []
filename = 'influence_data_by_genre_weight.csv'
with open(filename, errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        influencer_genre = row['influencer_genre_id']
        follower_genre = row['follower_genre_id']
        if not (influencer_genre in nodelist):
            G.add_node(influencer_genre,id=row['influencer_genre_id'])
            nodelist.append(influencer_genre)
        if not (follower_genre in nodelist):
            G.add_node(follower_genre,id = row['follower_genre_id'])
            nodelist.append(follower_genre)
        G.add_edge(influencer_genre, follower_genre, weight=row['weight'])

options = {
    'arrowstyle': '->',
}
pos = nx.random_layout(G)
plt.figure(figsize=(15, 9))
nx.draw_networkx_nodes(G, pos,alpha=0.9, node_size=400)
for i in G.nodes:
    for j in G.nodes:
        if j in G[i]:
            nx.draw_networkx_edges(G, pos, G.edges([i, j]), width=4*(float(G.edges[i, j]['weight'])),**options)
node_labels = nx.get_node_attributes(G,'id')
nx.draw_networkx_labels(G, pos, font_size=10, labels = node_labels)
plt.show()
