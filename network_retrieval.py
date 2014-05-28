import networkx as nx
import tangelo
from networkx.readwrite import json_graph
import pandas as pd


def run(date=""):
	ER=pd.DataFrame.from_csv('/Users/wgmueller/Desktop/Data/enron/weeks.csv',sep="\t")
	sub_ER=ER[(ER['V2'] == int(date))] #& (ER['sender'] == 155)]
	g=nx.Graph(zip(sub_ER['sender'],sub_ER['receiver']))
	ec=nx.eigenvector_centrality(g)
        deg=g.degree()
	nx.set_node_attributes(g,'degree',deg)
	nx.set_node_attributes(g,'eigcen',ec)
	return json_graph.dumps(g)
