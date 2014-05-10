#!/usr/bing/env python
try:
    import matplotlib.pyplot as plt
except:
    raise
import sys
import networkx as nx

G = nx.Graph()
G.add_nodes_from(list(range(5)))
pos1 = [(0,4), (0,3), (0,2), (0,1), (0,0)]

H = nx.Graph()
H.add_nodes_from(list(range(5)))
pos2 = [(1,4), (1,3), (1,2), (1,1), (1,0)]



nx.draw(G, pos1,
        with_labels=False,
        node_color=["yellow", "green", "white", "black", "red"],
        node_size=1000)

nx.draw(H, pos2,
        labels={0 : "Proposer or Proposee",
                1 : "Least Desirable",
                2 : "Most Desirable",
                3 : "Not Under Consideration",
                4 : "Default"},
        node_size=0)
#nx.draw_networkx_nodes(G, pos,
#                       nodelist=[0],
#                       node_color="yellow",
#                       node_size=500)
#
#nx.draw_networkx_nodes(G, pos,
#                       nodelist=[1],
#                       node_color="green",
#                       node_size=500)
#
#nx.draw_networkx_nodes(G, pos,
#                       nodelist=[2],
#                       node_color="white",
#                       node_size=500)
#
#nx.draw_networkx_nodes(G, pos,
#                       nodelist=[3],
#                       node_color="black",
#                       node_size=500)
#
#nx.draw_networkx_nodes(G, pos,
#                       nodelist=[4],
#                       node_color="red",
#                       node_size=500)

#plt.text(x,y+0.1,s='some text', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')

#plt.text(1,0,"Focus (Proposer/Proposee)",bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
#plt.text(1,1,"Least Desirable to Focus",bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
#plt.text(1,2,"Most Desirable to Focus",bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
#plt.text(1,3,"Not in Consideration to Focus")
#plt.text(1,4,"Same gender as Focus or No Focus")

#plt.axis('off')
for i in range(6):
    plt.savefig("gs_pic" + str(i).zfill(3) + ".png")
plt.show()
