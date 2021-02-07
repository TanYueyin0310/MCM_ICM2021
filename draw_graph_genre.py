import networkx as nx
import csv
G = nx.DiGraph()
nodelist = []
filename = 'influence_data_by_genre_weight.csv'
with open(filename, encoding='gb18030', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        influencer_genre = row['influencer_main_genre_flag']
        follower_genre = row['follower_main_genre_flag']
        if not (influencer_genre in nodelist):
            G.add_node(influencer_genre)
            nodelist.append(influencer_genre)
        if not (follower_genre in nodelist):
            G.add_node(follower_genre)
            nodelist.append(follower_genre)
        G.add_edge(influencer_genre, follower_genre, weight=row['weight'])

a