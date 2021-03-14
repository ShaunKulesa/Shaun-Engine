from tkinter import *
from pyopengltk import OpenGLFrame
from OpenGL import GL, GLU
import tkinter.ttk as ttk
from viewport import *

# The Tk class parameter makes the class the window widget "root = Tk()"
class window_and_gui(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.init()

    # Calls all functions
    def init(self):
        self.left_pannel_create()
        self.viewport_pannel_create()
        self.viewport_create()
        self.transformation_section()

    # The GUI on the left
    def left_pannel_create(self):
        self.m1 = PanedWindow(self, relief=RAISED, sashrelief=RAISED)
        self.m1.pack(fill=BOTH, expand=1)
    
    # Right pannel for the viewport to be stored in
    def viewport_pannel_create(self):
        self.m2 = PanedWindow(self.m1, width=300, height=1080)
        self.m1.add(self.m2)
    
    # Opengl viewport from the class "Viewport" in "viewport.py"
    def viewport_create(self):
        viewport = Viewport(self.m1, width=1500, height=1080)
        self.m1.add(viewport)
        viewport.animate = 1
        viewport.after(100, viewport.printContext)
        viewport.bind("<B1-Motion>", viewport.drag_handler)

    # Transformation notebook tab and contents
    def transformation_section(self):
        transformation_frame = Frame(self.m2, height=1080, bg = "#3a3b3d")
        self.m2.add(transformation_frame)
