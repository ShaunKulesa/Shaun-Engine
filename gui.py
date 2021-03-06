from opengl_code import *

import time
from tkinter import *
from OpenGL import GL
from pyopengltk import OpenGLFrame
import sys
from OpenGL import GL, GLU
import tkinter.ttk as ttk


if __name__ == '__main__':
    root = Tk()
    print(root.winfo_height)
    print(root.winfo_width)
    
    





    m1 = PanedWindow(relief=RAISED, sashrelief=RAISED)
    m1.pack(fill=BOTH, expand=1)

    m2 = PanedWindow(m1, orient=HORIZONTAL)
    m1.add(m2)

    frame1 = Frame(m1, bg="#3a3b3d")
    frame2 = Frame(m1, bg="#3a3b3d")


    m2.add(frame2, width=400)

    app = AppOgl(m1, width=1500, height=1080)
    m1.add(app)

    note = ttk.Notebook(frame2)

    tab1 = Frame(note)
    tab2 = Frame(note)
    tab3 = Frame(note)
    Button(tab1, text='Exit', command=root.destroy).pack()

    note.add(tab1, text = "Transformations", compound=TOP)
    note.add(tab2, text = "Texturing")
    note.add(tab3, text = "Code")
    note.pack(fill=X)

  


    

    m1.add(frame1, width=400)



    

    
    




    
    
    # pan = PanedWindow(root)
    # pan.pack(side=LEFT, fill=BOTH, expand=1)

    # Label(pan, text="size").pack()

    # app.pack(fill=BOTH, expand=YES, side=LEFT)
    app.animate = 1
    app.after(100, app.printContext)
    app.bind("<B1-Motion>", app.drag_handler)
    
    root.mainloop()