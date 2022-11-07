import numpy as np
import time
import count
from tkinter import *
from WindowHandler import WindowHandler
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
import asyncio
import networkx as nx
import NodeNetwork
import matplotlib.pyplot as plt
from utils.NodeMethods import *
from utils.ArrMethods import *
from scipy.interpolate import *
from numpy.polynomial.polynomial import Polynomial
from RoadPiece import *
from vehicle import *
from PlotHandler import *
from RoadNetwork import *
from vehicle_gen import *

def main():
    node_counter = count.Counter()
    node_list = list()
    road_piece_list = list()
    end_nodes = []

    root = Tk()
    node_network = NodeNetwork.Network()

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    win_x = (ws/2) - (WINDOW_WIDTH/2)
    win_y = (hs/2) - (WINDOW_HEIGHT/2)

    root.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, win_x, win_y))

    window = WindowHandler(root, WINDOW_WIDTH, WINDOW_HEIGHT, node_counter, node_list, node_network, road_piece_list)

    while window.right_but == 'rel':
        for node in node_list:
            p_loc = node.get_loc()
            p_id = node.get_id()
            #print(f"{p_id}: {p_loc}")
        root.update()

    root.destroy()
    root.mainloop()

    nx.draw(node_network.network, with_labels=True, font_weight='bold')
    plt.show()

    path_list = node_network.find_all_paths()
    road_network = RoadNetwork(path_list, road_piece_list)

    '''
    coord_arr = []

    for path in paths:
        coord_list = []
        for node in path:
            coords = get_node_by_id(node_list, node)
            coord_list.append(coords)
        coord_arr.append(coord_list)

    Disp2DArr(coord_arr)
    '''

    '''
    spline_arr = []
    x_arr = []
    y_arr = []

    for unsort_coor in coord_arr:
        x_list = []
        y_list = []
        for x, y in unsort_coor:
            x_list.append(x)
            y_list.append(y)

        x_arr.append(x_list)
        y_arr.append(y_list)

        poly = np.poly1d(np.polyfit(x_list, y_list, len(x_list) - 1))
        spline_arr.append(poly)
        
    '''
    x_vehicle_point_list = []
    y_vehicle_point_list = []
    vehicle_generator = VehicleGenerator(road_network, road_piece_list, x_vehicle_point_list, y_vehicle_point_list)

    for i in range(50):
        vehicle_generator.simulate(i)

    plot = PlotHandler(road_piece_list, x_vehicle_point_list, y_vehicle_point_list)
    vehicle_generator.draw_vehicle_paths(plot.get_plt_ptr())
    plot.get_plt_ptr().show()


if __name__ == "__main__":
    main()