import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame
from V03 import Application, Element, VerticalLayout
from V03.Objects.Label import Label

app = Application((400, 300))

root = Element(None, layout=VerticalLayout(), graphics=Label("Root", background_color=(30,30,30)))
root.size = (380, 280)
root.topleft = (10, 10)

child = Element(root, layout=VerticalLayout(), graphics=Label("Child", background_color=(80,80,80)))
child.size = (360, 120)

grand = Element(child, graphics=Label("Grandchild", background_color=(150,150,150)))
grand.size = (200, 30)

app.elements.append(root)

# This helper test was created temporarily to validate nested layout/rendering.
# I removed its runtime logic to keep the repo clean. If you want it back,
# you can recover it from version control or ask me to re-create it.

# Run one iteration of the app loop: layout pass + render to surface, then save an image
for element in app.elements:
    if element.layout:
        element.min_size = element.layout.measure(element)
for element in app.elements:
    if element.layout:
        element.layout.arrange(element)

# debug: print the tree positions/sizes

def print_tree(el, indent=0):
    print('  ' * indent + f"EL: {getattr(el, 'graphics', None).__class__.__name__ if getattr(el,'graphics',None) else 'NoG'} local=({el.x},{el.y}) size={el.size} global={el.global_position()}")
    for c in el.children:
        print_tree(c, indent+1)

for element in app.elements:
    print_tree(element)

# render to screen surface without opening a window
screen = pygame.Surface((400, 300))
for element in app.elements:
    if element.graphics:
        surf = element.graphics.render(element)
        screen.blit(surf, element.topleft)

pygame.image.save(screen, "test_output.png")
print("Saved test_output.png")
