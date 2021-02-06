import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import csv
import copy

G = nx.DiGraph()
nodelist = []
ancestor = []
with open('influence_data.csv', encoding='gb18030', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        influencer_id = row['influencer_id']
        follower_id = row['follower_id']
        influencer_name = row['influencer_name']
        follower_name = row['follower_name']
        connection = (influencer_id, follower_id)
        if influencer_name == 'Katy Perry' or follower_name == 'Katy Perry':
            if not (influencer_id in nodelist):
                G.add_node(influencer_id, name= row['influencer_name'],genre=row['influencer_main_genre'], year=row['influencer_active_start'])
                nodelist.append(influencer_id)
            if not (follower_id in nodelist):
                G.add_node(follower_id, name= row['follower_name'],genre=row['follower_main_genre'], year=row['follower_active_start'])
                nodelist.append(follower_id)
            G.add_edge(influencer_id, follower_id)
            if not influencer_id in ancestor:
                ancestor.append(influencer_id)
options = {
    'node_size': 400,
    'width': 1,
}
successor = copy.copy(nodelist)
for node in nodelist:
    if node in ancestor:
        successor.remove(node)
ancestor.remove('859589')
node_labels = nx.get_node_attributes(G,'name')
plt.figure(figsize=(10, 6.18))
pos = nx.shell_layout(G)
nx.draw_networkx_nodes(G, pos, nodelist=ancestor, node_color='Goldenrod', node_size=700)
nx.draw_networkx_nodes(G, pos, nodelist=successor, node_color='Orchid',node_size=700)
nx.draw_networkx_nodes(G, pos, nodelist=['859589'], node_color='Salmon',node_size=800)
nx.draw_networkx_edges(G,pos,arrowstyle='->',arrowsize=30,alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=6, labels = node_labels)
# nx.draw(G,pos,**options)
plt.show()
