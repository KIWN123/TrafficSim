import numpy as np
import random
from utils.CurveMethods import *
from CreationNode import *
import matplotlib.pyplot as plt
from utils.ColorPicker import get_rand_color

class RoadPiece:
    lanes = 1
    lane_width = 20

    def __init__(self, node):
        self.piece_start_node = node
        self.piece_end_node = None
        self.piece_node_list = []
        self.piece_node_list.append(node)
        self.center_eq = None
        self.lanes_eq = []
        self.x_coords = []
        self.y_coords = []

        self.color = get_rand_color()

    def add_node_to_road_piece(self, node):
        self.piece_node_list.append(node)

    def finish_road_piece(self):
        self.piece_end_node = self.piece_node_list[-1]

        for piece_node in self.piece_node_list:
            x, y = piece_node.get_loc()
            self.x_coords.append(x)
            self.y_coords.append(y)

        self.center_eq = create_eq_from_nodes(self.piece_node_list, self.x_coords, self.y_coords)

        print(self.center_eq)

        for i in range(1, self.lanes + 1):
            self.lanes_eq.append(self.center_eq + (i * self.lane_width))
            self.lanes_eq.append(self.center_eq - (i * self.lane_width))

    def get_colour(self):
        return self.color

    def get_center_eq(self):
        return self.center_eq

    def get_x_y_coords(self):
        return self.x_coords, self.y_coords

    def get_start_node(self):
        return self.piece_start_node

    def get_end_node(self):
        return self.piece_end_node

    def print_list(self):
        print(self.piece_node_list)

    def generate_and_draw_road(self, plt_win):
        x_new = np.linspace(min(self.x_coords), max(self.x_coords), 1000)
        plt_win.plot(x_new, self.center_eq(x_new), color="black")
        #plt_win.scatter(self.x_coords, self.y_coords, color=self.color)

        for lanes in self.lanes_eq:
            plt_win.plot(x_new, lanes(x_new), color="black")
