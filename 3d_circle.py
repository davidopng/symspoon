import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [
    [0, 1, 0],
    [0.951, 0.309, 0],
    [0.588, -0.809, 0],
    [-0.588, -0.809, 0],
    [-0.951, 0.309, 0],
]

edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 0],
]

colors = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
    [1, 0, 1],
]

def circle():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        circle()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
