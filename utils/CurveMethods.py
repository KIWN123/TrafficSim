from CreationNode import *
import numpy as np

def create_eq_from_nodes(piece_node_list, x_coords, y_coords):
    poly = np.poly1d(np.polyfit(x_coords, y_coords, len(piece_node_list) - 1))
    return poly

