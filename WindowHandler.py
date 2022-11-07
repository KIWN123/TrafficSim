from tkinter import *
import tkinter.font
from constants import CIRCLE_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT
import count
from CreationNode import *
from utils.NodeMethods import *
from NodeNetwork import *
from RoadPiece import *

class WindowHandler:
    left_but = "rel"
    right_but = "rel"

    node_counter = None
    node_list = None
    node_network = None
    current_road_piece = None
    road_piece_list = None

    connection_state = False
    node1loc = []
    node1id = None
    node2loc = []
    node2id = None

    x_cursor_pos, y_cursor_pos = None, None

    x_click_loc, y_click_loc, x_rel_loc, y_rel_loc = None, None, None, None

    def __init__(self, root, width, height, node_counter, node_list, node_network, road_piece_list):
        drawing_area = Canvas(root, width=width, height=height)
        next_piece_button = Button(root, text="Next Road Piece", command=self.GetNextRoadPiece)
        next_piece_button.pack(side="bottom")

        self.root = root
        self.node_counter = node_counter
        self.node_list = node_list
        self.node_network = node_network
        self.road_piece_list = road_piece_list

        drawing_area.pack()

        drawing_area.bind("<ButtonPress-1>", self.left_but_press)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_rel)
        drawing_area.bind("<ButtonRelease-3>", self.right_but_rel)

    def left_but_press(self, event=None):
        self.left_but = "press"

        self.x_click_loc = event.x
        self.y_click_loc = event.y

        close_node_id = detect_close_node(self.node_list, self.x_click_loc, self.y_click_loc)

        if (close_node_id != None):
            self.connection_state = True
            self.node1id = close_node_id
            self.node1loc = get_node_by_id(self.node_list, close_node_id).get_loc()

    def left_but_rel(self, event=None):
        self.left_but = "rel"

        self.x_rel_loc = event.x
        self.y_rel_loc = event.y

        close_node_id = detect_close_node(self.node_list, self.x_rel_loc, self.y_rel_loc)
        if (close_node_id == None) and (self.connection_state == False):
            id = self.node_counter.get_and_advance()
            self.draw_node(id, event)
            new_node = CreationNode(self.x_rel_loc, self.y_rel_loc, id)
            self.node_list.append(new_node)
            self.node_network.add_node_to_net(id)

        elif (close_node_id != None) and (self.connection_state == True):
            self.node2id = close_node_id
            self.node2loc = get_node_by_id(self.node_list, close_node_id).get_loc()
            self.node_network.connect_nodes(self.node1id, close_node_id)

            if self.current_road_piece == None:
                self.current_road_piece = RoadPiece(get_node_by_id(self.node_list, self.node1id))
                self.current_road_piece.add_node_to_road_piece(get_node_by_id(self.node_list, self.node2id))
            else:
                self.current_road_piece.add_node_to_road_piece(get_node_by_id(self.node_list, self.node2id))

            event.widget.create_line(self.node1loc[0], self.node1loc[1], self.node2loc[0], self.node2loc[1], smooth=True, fill=self.current_road_piece.get_colour(), width=5)

        self.node1loc = []
        self.node1id = None
        self.node2loc = []
        self.connection_state = False

        '''
        if self.current_road_piece != None:
            self.current_road_piece.print_list()
            print(self.road_piece_list)
        '''

    def draw_node(self, id, event=None):
        if None not in (event.x, event.y):
            event.widget.create_oval(event.x + CIRCLE_SIZE, event.y + CIRCLE_SIZE, event.x - CIRCLE_SIZE, event.y - CIRCLE_SIZE, fill="slate grey", outline="grey")

            text_font = tkinter.font.Font(family='Times New Roman', size=10, weight='bold')

            event.widget.create_text(event.x, event.y - 20, fill="black", font=text_font, text=f"Node {id}")

    def right_but_rel(self, event=None):
        self.GetNextRoadPiece()
        print(self.road_piece_list)
        self.right_but = "press"

    def GetNextRoadPiece(self):
        self.current_road_piece.finish_road_piece()
        self.road_piece_list.append(self.current_road_piece)
        self.current_road_piece = None
