To Do List:

1.  Graph load function is definitely repeated twice.
2.  Get the dialog working with text annotations marking the times entered.
3.  Would be nice to generalize isConnected and the graph coloring to more than one hop to correspond to scan statistic parameter (k).
4.  Would like the color by eigenvector centrality, betweeness to transition after box is clicked rather than reloaded.  I know this can be done using transition and duration with d3.
5.  Fix the axes.  They seem off. The circular tooltip appears in the scan statistics and then appears on the left y axis when there is only one time series.  We may want to separate the scan statistics into two different windows.
6.  Add feature where a node can be clicked on or highlighted and some summary information about the vertex appears such as the betweenness, etc as well as a summary of the edge attributes related to the vertex.
7.  Add edge thickness based on the percentage of time those edges were present in the near past when viewing the scan statistics.


-----------------------------------------------------------------------------------------------------------------------

Scan Statistics -- us -- red -> measures deviation in the number of edges present in a subgraph, them -- blue -> measures shifts in edge patterns in subgraphs.

Density -- number of edges present in network / # of possible edges = 2*E / n(n-1) where E is the number of edges and n is the number of nodes (or size of the network) in the network.

Average clustering coefficient -- measure to which nodes tend to cluster together.  Formally calculated as the number of closed triplets / number of connected triples of vertices.

Assortativity -- Measure of nodes tendency to be connected to similar nodes (in this case based on node degree).  High assortativty implies high degree nodes tend to be connected to other high degree nodes and low degree nodes tend to be connected to other low degree nodes.

Connected components -- A connected component is a set of nodes in which any two nodes are connected by paths.  The number of connected components counts the total number of unique connected components in the network
