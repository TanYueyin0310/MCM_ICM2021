import networkx as nx
import csv


def load_network(filename):
    G = nx.DiGraph()
    nodelist = []
    with open(filename, encoding='gb18030', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            influencer = row['influencer_id']
            follower = row['follower_id']
            if not (influencer in nodelist):
                G.add_node(influencer, id = row['influencer_id'],name=row['influencer_name'], genre=row['influencer_main_genre'],
                           year=row['influencer_active_start'])
                nodelist.append(influencer)
            if not (follower in nodelist):
                G.add_node(follower, id = row['follower_id'], name=row['follower_name'], genre=row['follower_main_genre'],
                           year=row['follower_active_start'])
                nodelist.append(follower)
            G.add_edge(influencer, follower)
    return G, nodelist
