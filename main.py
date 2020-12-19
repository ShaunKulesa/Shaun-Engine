import time
import tkinter
from tkinter import *
from OpenGL import GL
from pyopengltk import OpenGLFrame

import sys, math, time
if sys.version_info[0] < 3:
    from Tkinter import Tk, YES, BOTH
else:
    from tkinter import Tk, YES, BOTH
from OpenGL import GL, GLU
from pyopengltk import OpenGLFrame
from tkinter.filedialog import askopenfilename, asksaveasfilename

class AppOgl(OpenGLFrame):

    def initgl(self):
        self.waves()

    def redraw(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glBegin(GL.GL_POINTS)
        npt = 100
        for i in range(npt):
            x = -5.0 + i * 10.0 / npt
            y = math.sin(x + time.time())*5/2
            GL.glVertex2f(x, y)
        GL.glEnd()
        GL.glFlush()
        self.nframes += 1
        tm = time.time() - self.start
        print("fps", self.nframes / tm, end="\r")
    
    def waves(self):
        GL.glViewport(0, 0, self.width, self.height)
        GL.glClearColor(1.0, 1.0, 1.0, 0.0)
        GL.glColor3f(0.0, 0.0, 0.0)
        GL.glPointSize(4.0)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluOrtho2D(-5, 5, -5, 5)
        self.start = time.time()
        self.nframes = 0


class main():

    def run_app(self):
        print("run")
        self.runv = False

    def open_file(self):
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Python Files", "*.py")]
        )
        if not filepath:
            return
        self.right.delete(1.0, END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.right.insert(END, text)
        window.title(f"Text Editor Application - {filepath}")

    def __init__(self, master):

        self.runv = True 

        m1 = PanedWindow(relief=RAISED, sashrelief=RAISED)
        m1.pack(fill=BOTH, expand=1)

        frame1 = Frame(m1, bg="#3a3b3d")

        menubutton = Menubutton(frame1, text = "File", bg="#3a3b3d", fg="#ffffff", activebackground="#3a3b3d")    
            
        menubutton.menu = Menu(menubutton)   
        menubutton["menu"]= menubutton.menu   
        
        var1 = IntVar() 
        var2 = IntVar() 
        var3 = IntVar() 
        
        menubutton.menu.add_checkbutton(label = "New", 
                                        variable = var1, command=self.run_app)   
        open_file_button = menubutton.menu.add_checkbutton(label = "Open", 
                                        variable = var2, command=self.open_file) 
        menubutton.menu.add_checkbutton(label = "Save", 
                                        variable = var3) 
            
        menubutton.pack(anchor="nw")  

        self.app = AppOgl(m1, width=1500, height=1080)
        m1.add(self.app)

        m1.add(frame1, width=400)
        self.right = Text(frame1, bg="#3a3b3d", fg="#ffffff", insertbackground='white')
        self.right.pack(fill=BOTH, expand=1)

        rightb = Button(frame1, text="run", command=self.run_app)
        rightb.pack()

        while self.runv == True:
            print("true")
            self.app.animate = 1
            self.app.after(100, self.app.printContext)
            self.app.mainloop()

        print("false")
        self.app.animate = 0
        self.app.after(100, self.app.printContext)
        self.app.mainloop()
        
if __name__ == '__main__':
    root = tkinter.Tk()
    main = main(root)


    # app.pack(fill=tkinter.BOTH, expand=tkinter.YES)
