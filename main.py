import count
from tkinter import *
from WindowHandler import WindowHandler
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
import asyncio


def main():
    node_counter = count.Counter()
    node_list = list()

    root = Tk()
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window = WindowHandler(root, WINDOW_WIDTH, WINDOW_HEIGHT, node_counter, node_list)

    while window.right_but == 'rel':
        for node in node_list:
            print(node.get_loc())
        root.update()

    if window.right_but != 'rel':
        root.destroy()

    root.mainloop()

if __name__ == "__main__":
    main()