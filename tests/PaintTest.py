from tkinter import *
import tkinter.font

class WindowHandler:
    drawing_tool = "text"

    left_but = "rel"

    x_pos, y_pos = None, None

    x1_line, y1_line, x2_line, y2_line = None, None, None, None

    def __init__(self, root):
        drawing_area = Canvas(root)

        drawing_area.pack()

        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_press)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_rel)

    def left_but_press(self, event=None):
        self.left_but = "press"

        self.x1_line = event.x
        self.y1_line = event.y

    def left_but_rel(self, event=None):
        self.left_but = "rel"

        self.x_pos = None
        self.y_pos = None

        self.x2_line = event.x
        self.y2_line = event.y

        if self.drawing_tool == "line":
            self.line_draw(event)
        elif self.drawing_tool == "arc":
            self.arc_draw(event)
        elif self.drawing_tool == "oval":
            self.oval_draw(event)
        elif self.drawing_tool == "rectangle":
            self.rectangle_draw(event)
        elif self.drawing_tool == "text":
            self.text_draw(event)

    def motion(self, event=None):
        if self.drawing_tool == "pencil":
            self.pencil_draw(event)

    def pencil_draw(self, event=None):
        if self.left_but == "press":
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE)

            self.x_pos = event.x
            self.y_pos = event.y

    def line_draw(self, event=None):
        if None not in (self.x1_line, self.y1_line, self.x2_line, self.y2_line):
            event.widget.create_line(self.x1_line, self.y1_line, self.x2_line, self.y2_line, smooth=TRUE, fill="green")

    def arc_draw(self, event=None):
        if None not in (self.x1_line, self.y1_line, self.x2_line, self.y2_line):
            coords = self.x1_line, self.y1_line, self.x2_line, self.y2_line

            event.widget.create_arc(coords, start=0, extent=150, style=ARC)

    def oval_draw(self, event=None):
        if None not in (self.x1_line, self.y1_line, self.x2_line, self.y2_line):
            event.widget.create_oval(self.x1_line, self.y1_line, self.x2_line, self.y2_line, fill="midnight blue", outline="yellow", width=2)

    def rectangle_draw(self, event=None):
        if None not in (self.x1_line, self.y1_line, self.x2_line, self.y2_line):
            event.widget.create_rectangle(self.x1_line, self.y1_line, self.x2_line, self.y2_line, fill="midnight blue", outline="yellow", width=2)

    def text_draw(self, event=None):
        if None not in (self.x1_line, self.y1_line):
            text_font = tkinter.font.Font(family='Helvetica', size=20, weight='bold', slant='italic')

            event.widget.create_text(self.x1_line, self.y1_line, fill="green", font=text_font, text='wow')

root = Tk()
WindowHandler = WindowHandler(root)
root.mainloop()