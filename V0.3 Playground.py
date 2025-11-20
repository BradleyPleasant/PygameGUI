from PyUi import Application, Element, VerticalLayout, Graphics, Input
from PyUi.Objects.Label import Label
from PyUi.Objects.ReSizable import ReSizable
from PyUi.Objects.Draggable import Draggable
from PyUi.Objects.TextField import TextField
from PyUi.Objects.Button import Button


app = Application()


root = Element(
    parent = None,
    layout = VerticalLayout(5, 2),
    graphics = Graphics((40, 40, 40)),
    input = ReSizable()
)

root_child_1 = Element(
    parent = root,
    graphics = Label("hello, world", None, 22, background_color=(80,80,80)),
    input=Draggable()
)

root_child_2 = Element(
    parent = root,
    graphics = Graphics(background_color=(80,80,80,0)),
    input = ReSizable()
)

root_child_2_child_1 = Element(
    parent = root_child_2,
    input=Draggable()
)

root_child_2_child_1_child_1 = Element(
    parent = root_child_2_child_1,
    graphics = Label("deeply nested element", None, 14, background_color=(200,200,200)),
    input=Input()
)

root_child_2_child_1_child_2 = Element(
    parent = root_child_2_child_1,
    graphics = Label("resize me!", None, 14, background_color=(200,200,200)),
    input=ReSizable()
)

root_child_2_child_1_child_3 = Element(
    parent = root_child_2_child_1,
    graphics = Label("drag me!", None, 14, background_color=(200,200,200)),
    input=Draggable()
)

root_child_2_child_2 = Element(
    parent = root_child_2,
    graphics = Label("another nested element", None, 18, background_color=(150,150,150)),
    input=TextField()
)

root_child_2_child_3 = Element(
    parent = root_child_2,
    graphics = Label("resize me too!", None, 18, background_color=(150,150,150)),
    input=ReSizable()
)

def click_element(element):
    print("clicked:", element)

root_child_3 = Element(
    parent = root,
    graphics = Label("goodbye, world", None, 22, background_color=(80,80,80)),
    input=Button(click_element)
)

root.size = (300, 200)

app.elements.append(root)
app.run()
