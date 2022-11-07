import networkx as nx
import matplotlib.pyplot as plt

class Network:
    network = None

    def __init__(self):
        self.network = nx.Graph()

    def add_node_to_net(self, id):
        self.network.add_node(id)

    def connect_nodes(self, id1, id2):
        self.network.add_edge(id1, id2)

    def find_all_paths(self):
        end_nodes = []

        for (node, val) in self.network.degree():
            if val == 1 and node != 1:
                end_nodes.append(node)

        path_gen = nx.all_simple_paths(self.network, 1, end_nodes)
        return path_gen

