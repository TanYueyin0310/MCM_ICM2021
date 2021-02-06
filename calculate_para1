import numpy as np
from load_network import load_network
import networkx as nx

filename = 'influence_data.csv'
G, nodelist = load_network(filename)
nodes = G.nodes()
for index1 in nodes:
    outDegree = G.out_degree(index1)
    inDegree = G.in_degree(index1)
    if not inDegree == 0:
        G.nodes[index1]['para1'] = np.true_divide(outDegree, inDegree)
    else:
        G.nodes[index1]['para1'] = outDegree
for index2 in nodes:
    successor2 = [*G.successors(index2)]
    successor_year_list = [int(G.nodes[i]['year']) for i in successor2]
    # for successor in [*G.successors(index2)]:
    influencer_year = int(G.nodes[index2]['year'])
    if not successor2:
        G.nodes[index2]['para2'] = 0
    else:
        lastest_follower_year = np.max(successor_year_list)
        G.nodes[index2]['para2'] = lastest_follower_year - influencer_year
for index3 in nodes:
    successor3 = [*G.successors(index3)]
    successor_genre_list = np.unique([G.nodes[i]['genre'] for i in successor3])
    if not successor3:
        G.nodes[index3]['para3'] = 0
    else:
        G.nodes[index3]['para3'] = len(successor_genre_list)
