import CreationNode
from constants import *

'''
def detect_if_node_close(node_list, x_loc, y_loc):
    for node in node_list:
        x, y = node.get_loc()
        if (x - NODE_EX_ZONE <= x_loc <= x + NODE_EX_ZONE) and (y - NODE_EX_ZONE <= y_loc <= y + NODE_EX_ZONE):
            return True
    return False

def get_close_node_loc(node_list, x_loc, y_loc):
    for node in node_list:
        x, y = node.get_loc()
        if (x - NODE_EX_ZONE <= x_loc <= x + NODE_EX_ZONE) and (y - NODE_EX_ZONE <= y_loc <= y + NODE_EX_ZONE):
            return x, y
    return None
    
def get_node_loc_by_id(node_list, id):
    for node in node_list:
        if node.get_id() == id:
            return node.get_loc()
    return None

'''

def detect_close_node(node_list, x_loc, y_loc):
    for node in node_list:
        x, y = node.get_loc()
        if (x - NODE_EX_ZONE <= x_loc <= x + NODE_EX_ZONE) and (y - NODE_EX_ZONE <= y_loc <= y + NODE_EX_ZONE):
            return node.get_id()
    return None

def get_node_by_id(node_list, id):
    for node in node_list:
        if node.get_id() == id:
            return node
    return None
