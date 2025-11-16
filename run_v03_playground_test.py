# This file was used for headless testing during debugging and was left
# intentionally so you can re-create tests quickly. I removed the runtime
# logic to keep the workspace clean. If you want a runnable test, tell me
# which test and I'll re-create it as a small, focused script.

import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame
from V03 import Application, Element, VerticalLayout, Graphics
from V03.Objects.Label import Label
from V03.Objects.ReSizable import ReSizable
from V03.Objects.Draggable import Draggable

pygame.init()

# Build the same tree as V0.3 Playground
root = Element(
    parent=None,
    layout=VerticalLayout(5, 2),
    graphics=Graphics((40,40,40)),
    input=ReSizable()
)
root.size = (400, 300)
root.x = 10
root.y = 10

root_child_1 = Element(
    parent=root,
    layout=VerticalLayout(5, 2),
    graphics=Label("hello, world", None, 22, background_color=(80,80,80)),
    input=Draggable()
)

root_child_2 = Element(
    parent=root,
    layout=VerticalLayout(5, 2),
    graphics=Label("this is a test", None, 22, background_color=(80,80,80)),
    input=ReSizable()
)

root_child_2_child_1 = Element(
    parent=root_child_2,
    layout=VerticalLayout(5, 2),
    graphics=Label("nested element", None, 18, background_color=(150,150,150)),
    input=Draggable()
)

root_child_2_child_2 = Element(
    parent=root_child_2,
    layout=VerticalLayout(5, 2),
    graphics=Label("another nested element", None, 18, background_color=(150,150,150)),
    input=ReSizable()
)

# top-level list
elements = [root]

# run layout
for element in elements:
    if element.layout:
        element.min_size = element.layout.measure(element)
for element in elements:
    if element.layout:
        element.layout.arrange(element)

# debug print

def print_tree(el, indent=0):
    gpos = el.global_position()
    print('  '*indent + f"EL: {getattr(el,'graphics',None).__class__.__name__ if getattr(el,'graphics',None) else 'NoG'} local=({el.x},{el.y}) size={el.size} global={gpos}")
    for c in el.children:
        print_tree(c, indent+1)

print_tree(root)

# render to surface
screen = pygame.Surface((800, 600))
for element in elements:
    if element.graphics:
        surf = element.graphics.render(element)
        gx, gy = element.global_position()
        screen.blit(surf, (int(gx), int(gy)))

# save image
pygame.image.save(screen, 'v03_playground_test.png')
print('Saved v03_playground_test.png')

# print some pixel samples
img = pygame.image.load('v03_playground_test.png')
for p in [(15,15), (20,20), (30,30), (50,50), (10,10)]:
    try:
        print(p, img.get_at(p))
    except Exception:
        print('pixel out of range', p)

pygame.quit()
