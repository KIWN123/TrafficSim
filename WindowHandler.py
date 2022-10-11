from tkinter import *
import tkinter.font
from constants import CIRCLE_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT
import count
import node

class WindowHandler:
    left_but = "rel"
    right_but = "rel"

    counter = None
    node_list = None

    x_cursor_pos, y_cursor_pos = None, None

    x_click_loc, y_click_loc, x_rel_loc, y_rel_loc = None, None, None, None

    def __init__(self, root, width, height, node_counter, node_list):
        drawing_area = Canvas(root, width=width, height=height)

        self.counter = node_counter
        self.node_list = node_list
        drawing_area.pack()

        drawing_area.bind("<ButtonPress-1>", self.left_but_press)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_rel)
        drawing_area.bind("<ButtonRelease-3>", self.right_but_rel)

    def left_but_press(self, event=None):
        self.left_but = "press"

        self.x_click_loc = event.x
        self.y_click_loc = event.y

    def left_but_rel(self, event=None):
        self.left_but = "rel"

        self.x_rel_loc = event.x
        self.y_rel_loc = event.y

        self.draw_node(event)
        new_node = node.Node(self.x_rel_loc, self.y_rel_loc)
        self.node_list.append(new_node)

        last_node_x, last_node_y = self.node_list[-1].get_loc()
        slast_node_x, slast_node_y = self.node_list[-2].get_loc()
        event.widget.create_line(last_node_x, last_node_y, slast_node_x, slast_node_y, smooth=True, fill="black", width=5)


    def draw_node(self, event=None):
        if None not in (self.x_rel_loc, self.y_rel_loc):
            event.widget.create_oval(self.x_rel_loc + CIRCLE_SIZE, self.y_rel_loc + CIRCLE_SIZE, self.x_rel_loc - CIRCLE_SIZE, self.y_rel_loc - CIRCLE_SIZE, fill="slate grey", outline="grey")

            text_font = tkinter.font.Font(family='Times New Roman', size=10, weight='bold')
            node_id = self.counter.get_num()

            event.widget.create_text(self.x_rel_loc, self.y_rel_loc - 20, fill="black", font=text_font, text=f"Node {node_id}")


    def right_but_rel(self, event=None):
        self.right_but = "press"