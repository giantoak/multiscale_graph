To Do List:

1.  Graph load function is definitely repeated twice.
2.  Get the dialog working with text annotations marking the times entered.
3.  Would be nice to generalize isConnected and the graph coloring to more than one hop to correspond to scan statistic parameter (k).
4.  Would like the color by eigenvector centrality, betweeness to transition after box is clicked rather than reloaded.  I know this can be done using transition and duration with d3.
5.  Fix the axes.  They seem off. The circular tooltip appears in the scan statistics and then appears on the left y axis when there is only one time series.  We may want to separate the scan statistics into two different windows.
6.  Add feature where a node can be clicked on or highlighted and some summary information about the vertex appears such as the betweenness, etc as well as a summary of the edge attributes related to the vertex.
7.  Add edge thickness based on the percentage of time those edges were present in the near past when viewing the scan statistics.
