import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame
from V03 import Application, Element, VerticalLayout
from V03.Objects.Label import Label

pygame.init()

# Simple headless smoke test: root -> child -> grandchild
root = Element(None, layout=VerticalLayout(), graphics=Label("Root", background_color=(30,30,30)))
root.size = (380, 280)
root.x = 10
root.y = 10

child = Element(root, layout=VerticalLayout(), graphics=Label("Child", background_color=(80,80,80)))
child.size = (360, 120)

grand = Element(child, graphics=Label("Grandchild", background_color=(150,150,150)))
grand.size = (200, 30)

# measure + arrange
if root.layout:
    root.min_size = root.layout.measure(root)
    root.layout.arrange(root)

# render composition and save
screen = pygame.Surface((400, 300))
surf = root.graphics.render(root)
# blit at global position (root.x, root.y)
screen.blit(surf, (int(root.x), int(root.y)))
pygame.image.save(screen, 'tools_debug_test_output.png')
print('Saved tools_debug_test_output.png')

