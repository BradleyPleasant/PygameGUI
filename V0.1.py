import pygame
from GUI import Application, UIObject, VerticalLayout, HorizontalLayout, Layout, Label
from GUI import DraggableBar


pygame.init()
app = Application()
root = UIObject(app, (200, 100), (50, 30), VerticalLayout(padding=10, item_padding=20), color=(200, 200, 200))
child1 = DraggableBar(app, (0, 0), (100, 50), layout=HorizontalLayout(padding=0, item_padding=10), color=(255, 0, 0),
                  selectable=True)
child2 = UIObject(app, (30, 70), (200, 100), layout=VerticalLayout(padding=5, item_padding = 5), color=(0, 0, 255))
child3 = Label(app, (0, 0), (200, 200),layout=Layout(padding=10), color=(0, 255, 0), text = "test text", font = pygame.font.Font(None, 20))
child4 = UIObject(app, (0, 0), (400, 30), color=(255, 255, 0))

# use add_child so parents are set
root.add_child(child1)
root.add_child(child2)
child2.add_child(child3)
child2.add_child(child4)

app.objects.append(root)
app.run()
