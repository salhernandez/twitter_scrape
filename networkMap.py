import networkx as nx
import matplotlib.pyplot as plt
import os
import pydot # import pydot or you're not going to get anywhere my friend :D
from PIL import Image
import sys

def draw_graph(graph, labels=None, graph_layout='shell',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)

    # draw graph
    #nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
    #                       alpha=node_alpha, node_color=node_color)
    #nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
    #                       alpha=edge_alpha,edge_color=edge_color)
    #nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
    #                        font_family=text_font)

    if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
    #nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
    #                             label_pos=edge_text_pos)

    nx.draw(G)
    #nx.draw_random(G)
    #nx.draw_spectral(G)
    # show graph
    plt.savefig("graph.png")
    plt.show()
    #nx.show()

inFile = sys.argv[1]
anchor = inFile.split(".")[0]
currentDirectory = os.getcwd()+"/"

imgPath = currentDirectory+"data/images/"
myPath = currentDirectory+"data/users/"
twitter = "https://twitter.com/"
url = ""
file = myPath+inFile
# first you create a new graph, you do that with pydot.Dot()
#graph = pydot.Dot(graph_type='graph')

# the idea here is not to cover how to represent the hierarchical data
# but rather how to graph it, so I'm not going to work on some fancy
# recursive function to traverse a multidimensional array...
# I'm going to hardcode stuff... sorry if that offends you
arr = []
mArr = []
lArr = []
# let's add the relationship between the king and vassals
with open(file, "r") as f:
    for line in f:
        line= line[:-1]
        arr.append(line)
        # and we obviosuly need to add the edge to our graph
        mArr.append(anchor)
        lArr.append(line)

arr2 = []
for element in arr:
    with open(myPath+element+".txt", "r") as f:
        for line in f:
            line= line[:-1]
            arr2.append(line)
            mArr.append(element)
            lArr.append(line)
'''        
arr3 = []
for element in arr2:
    with open(myPath+element+".txt", "r") as f:
        for line in f:
            line= line[:-1]
            arr3.append(line)
            mArr.append(element)
            lArr.append(line)
'''            
graph = []

for i in range(0,len(mArr)):
    graph.append((mArr[i], lArr[i]))


# you may name your edge labels
#labels = map(chr, range(65, 65+len(graph)))
#draw_graph(graph, labels)

# if edge labels is not specified, numeric labels (0, 1, 2...) will be used
draw_graph(graph)