from pyopengltk import OpenGLFrame
from OpenGL import GL, GLU

class Viewport(OpenGLFrame):

    def initgl(self):
        self._add_quad = False
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scroll_x = 0
        self.scroll_y = 0
        self.old_direction = (0, 0) # Static variables for direction()
        print(GL.glBindFramebuffer)
        print(GL.glGenFramebuffers)
        
    def draw_quad(self):
       
        self._add_quad = True

    def redraw(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

        # GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(
            self.scroll_x,
            self.width + self.scroll_x,
            self.scroll_y,
            self.height + self.scroll_y,
            1, -1
        )

        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glBegin(GL.GL_QUADS)

        if self._add_quad == True:
            GL.glVertex2f(100, 200)
            GL.glVertex2f(100, 100)
            GL.glVertex2f(200, 100)
            GL.glVertex2f(200, 200)


        GL.glVertex3f(100,   200, 0)
        GL.glVertex3f(100,   100,   0)


        GL.glVertex3f(0,   200, 0)
        GL.glVertex3f(0,   100,   0)
        GL.glVertex3f(200, 100,   0)
        GL.glVertex3f(200, 200, 0)

        # array = ["100", "200", "100", "100"]
        # GL.glGenVertexArrays(1, array)

        GL.glEnd()
        
    def add_quad(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

        # GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(
            self.scroll_x,
            self.width + self.scroll_x,
            self.scroll_y,
            self.height + self.scroll_y,
            1, -1
        )

        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glBegin(GL.GL_QUADS)

        GL.glBegin(GL.GL_QUADS)
        GL.glVertex2f(100, 200)
        GL.glVertex2f(100, 100)
        GL.glVertex2f(200, 100)
        GL.glVertex2f(200, 200)
        GL.glEnd()
    
    def direction(self, x, y):
        old_x, old_y = self.old_direction
        THRESHOLD = 0.1 # Parameter for how sensitive is your detection
        if abs(x-old_x) >= THRESHOLD or abs(y-old_y) >= THRESHOLD:
            if x > old_x:
                self.scroll_x += 8
            elif x < old_x:
                self.scroll_x += -8
            if y > old_y:
                self.scroll_y += -8
            elif y < old_y:
                self.scroll_y += 8
            self.old_direction = (x, y) 

    def drag_handler(self, event):
        self.direction(event.x, event.y)
