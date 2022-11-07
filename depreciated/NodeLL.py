from CreationNode import *

class NodeLL:
    def __init__(self):
        self.head = None

    def printLL(self):
        temp = self.head
        while (temp):
            print(temp.get_loc())
            temp = temp.next

    def push(self, x_loc, y_loc):
        new_node = CreationNode(x_loc, y_loc)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, x_loc, y_loc):
        if prev_node is None:
            print("Previous node does not exist.")
            return

        new_node = CreationNode(x_loc, y_loc)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, x_loc, y_loc):
        new_node = CreationNode(x_loc, y_loc)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def delete_node(self, x_loc, y_loc):
        temp = self.head

        if (temp is not None):
            if (temp.get_loc() == (x_loc, y_loc)):
                self.head = temp.next
                temp = None
                return

        while (temp is not None):
            if temp.get_loc() == (x_loc, y_loc):
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return

        prev.next = temp.next
        temp = None