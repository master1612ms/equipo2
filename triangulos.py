import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy

pygame.init()

screen_width = 800
screen_height = 800

#Variables para dibujar los ejes del sistema
X_MIN=-500
X_MAX=500
Y_MIN=-500
Y_MAX=500

V1 = numpy.array([[-300,0],[-150,300],[0,0]])
V2 = numpy.array([[0,0],[300,0],[150,300]])


def Axis():
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    #X axis in red
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(X_MIN,0.0)
    glVertex2f(X_MAX,0.0)
    glEnd()
    
    #y axis in blue
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(0.0,Y_MIN)
    glVertex2f(0.0,Y_MAX)
    glEnd()
    glLineWidth(1.0)

def display1():
    glPolygonMode(GL_BACK,GL_FILL)
    glShadeModel(GL_SMOOTH)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex2i(*V1[0])
    #glVertex2i(-300,0)
    glColor3f(0.0,1.0,0.0)
    glVertex2i(*V1[1])
    #glVertex(-150,300)
    glColor3f(0.0,0.0,1.0)
    glVertex2i(*V1[2])
    #glVertex2i(0,0)
    glEnd()

def display2():
    glPolygonMode(GL_FRONT,GL_FILL)
    glShadeModel(GL_SMOOTH)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    #glVertex2i(0,0)
    glVertex2i(*V2[0])
    glColor3f(0.0,0.0,1.0)
    #glVertex(300,0)
    glVertex2i(*V2[1])
    glColor3f(0.0,1.0,0.0)
    glVertex2i(*V2[2])
    #glVertex2i(150,300)
    glEnd()
    
screen = pygame.display.set_mode(
    (screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL: ejes 2D") #asignar nombre a la ventana

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
#gluPerspective(FOVY, screen_width/screen_height, ZNEAR, ZFAR)

gluOrtho2D(-400,400,-400,400)#mapeo
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glClearColor(0,0,0,0)

glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT)
    #glPushMatrix()
    Axis()
    display1()
    display2()
  
    pygame.display.flip() #incluir siempre al final
    pygame.time.wait(100)

pygame.quit()