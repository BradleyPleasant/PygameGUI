import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame
from V03 import Element, VerticalLayout, Graphics
from V03.Objects.Label import Label
from V03.Objects.ReSizable import ReSizable
from V03.Objects.Draggable import Draggable

pygame.init()

root = Element(parent=None, layout=VerticalLayout(5,2), graphics=Graphics((40,40,40)), input=ReSizable())
root.size = (400,300)
root.x = 10
root.y = 10

c1 = Element(parent=root, layout=VerticalLayout(5,2), graphics=Label("A", None, 22, background_color=(80,80,80)), input=Draggable())

c2 = Element(parent=root, layout=VerticalLayout(5,2), graphics=Label("B", None, 22, background_color=(80,80,80)), input=ReSizable())

c2c1 = Element(parent=c2, layout=VerticalLayout(5,2), graphics=Label("C1", None, 18, background_color=(150,150,150)), input=Draggable())

c2c2 = Element(parent=c2, layout=VerticalLayout(5,2), graphics=Label("C2", None, 18, background_color=(150,150,150)), input=ReSizable())

# measure + arrange
if root.layout:
    root.min_size = root.layout.measure(root)
    root.layout.arrange(root)

# render and save snapshot
screen = pygame.Surface((800,600))
surf = root.graphics.render(root)
screen.blit(surf, (int(root.x), int(root.y)))
pygame.image.save(screen, 'tools_debug_v03_playground_test.png')
print('Saved tools_debug_v03_playground_test.png')

