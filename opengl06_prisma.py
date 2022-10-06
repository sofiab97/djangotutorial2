from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

ancho_pantalla, alto_pantalla = 1000,1000

# Rotación gral.

rotacion_base = [30, 1, 1, 0]

vertices = (
    (0.5, -0.5, 0.5),
    (0.5, 0.5, 0.5),
    (-0.5, 0.5, 0.5),
)

colores = (
    (0.2,0.2,0.2),
    (0.2,0.4,0.5),
    (0.6,0.2,0.6),
    (0.3,0.7,0.2),
    (0.8,0.1,0.3),
    (0.4,0.2,0.7),
    (0.8,0.6,0.9),
    (0.2,0.9,0.6),
)



def inicializar():

    # Selecciona la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Inicializar la matriz.

    # Ángulo, ratio, near, far
    gluPerspective(30, 600/600, 0.1, 50)
    
    gluLookAt(0,0,4,0,0,0,0,1,0) # Posición de la "camara" (ojo)

    #glOrtho(-1,1,-1,1,-1,1)


    # Seleccionar la matriz modelview
    glMatrixMode(GL_MODELVIEW)

    # Borrar la pantalla
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

def ejes():
    #glPushMatrix()
    glRotatef(rotacion_base[0], rotacion_base[1], rotacion_base[2], rotacion_base[3])

    # Le decimos a OPENGL que interprete los vértices como líneas
    glBegin(GL_LINES)

    # Dibuja el eje x en rojo
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    # Dibuja el eje y en verde
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)

    # Dibuja el eje z en azul
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)
    glEnd()
    #glPopMatrix()

# Dibuja una cara, con los colres (r,g,b) en las posiciones "vertices"
def triangle(r,g,b,v1,v2,v3):
    
    glColor3f(r,g,b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3fv(v1)
    glVertex3fv(v2)
    glVertex3fv(v3)
    glEnd()

    
def rectangle(r,g,b,v1,v2,v3,v4):
    
    glColor3f(r,g,b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3fv(v1)
    glVertex3fv(v2)
    glVertex3fv(v3)
    glVertex3fv(v4)
    glEnd()

def prisma(size):
    glPushMatrix()
    glRotatef(rotacion_base[0], rotacion_base[1], rotacion_base[2], rotacion_base[3])
    
    glPushMatrix()
    glScalef(size,size,size)
    triangle(1,0.8,0.8,vertices[0],vertices[1],vertices[2])
    glPopMatrix()

    glPushMatrix()
    glScalef(size,size,size)
    triangle(1,0,0,(0.5, -0.5, 1),(0.5, 0.5, 1),(-0.5, 0.5, 1))
    glPopMatrix()
    
    glPushMatrix()
    glScalef(size,size,size)
    glRotatef(90,0,0,1)
    rectangle(0,0.8,0,(0.5, 0.5, 0.5),(0.5, 0.5, 1),(0.5, -0.5, 1),(0.5, -0.5, 0.5))
    glPopMatrix()

    glPushMatrix()
    glScalef(size,size,size)
    rectangle(0,0.5,0.8,(0.5, 0.5, 0.5),(0.5, 0.5, 1),(0.5, -0.5, 1),(0.5, -0.5, 0.5))
    glPopMatrix()
    

    glPopMatrix()

def display():
    inicializar()
    ejes()
    prisma(0.6)
    glFlush()

def main():
    glutInit(sys.argv)
    #glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    #https://stackoverflow.com/questions/59510466/pyopengl-depth-test-doesnt-do-anything
    glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH )
    glutInitWindowSize(ancho_pantalla, alto_pantalla)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(u'Matrix Operations')
    glutDisplayFunc(display)
    glutMainLoop()


main()
