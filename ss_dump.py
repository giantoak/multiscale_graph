import rpy2
import rpy2.robjects as robjects
import numpy as np
import tangelo
import json  
import pandas as pd
import pandas.rpy.common as com
import networkx as nx
from networkx.readwrite import json_graph

robjects.r['load']("/Users/wgmueller/Desktop/R_Scripts_and_Examples/enron.RData")

ss=com.load_data('ss.df2')


def run():
	return ss.to_json(orient="records")

