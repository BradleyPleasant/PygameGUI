from PyUi import Application, Element, VerticalLayout, Graphics, Input
from PyUi.Objects.Label import Label
from PyUi.Objects.ReSizable import ReSizable
from PyUi.Objects.Draggable import Draggable
from PyUi.Objects.TextField import TextField


app = Application()


root = Element(
    parent = None,
    layout = VerticalLayout(5, 2),
    # give the root a visible background so you can see its bounds
    graphics = Graphics((40, 40, 40)),
    input = ReSizable()
)

root_child_1 = Element(
    parent = root,
    layout = VerticalLayout(5, 2),
    # label with its own background so it's visible on top of the root
    graphics = Label("hello, world", None, 22, background_color=(80,80,80)),
    input=Draggable()
)

root_child_2 = Element(
    parent = root,
    layout = VerticalLayout(5, 2),
    graphics = Graphics(background_color=(80,80,80,0)),
    input = ReSizable()
)

root_child_2_child_1 = Element(
    parent = root_child_2,
    layout = VerticalLayout(5, 2),
    graphics = Label("nested element", None, 18, background_color=(150,150,150)),
    input=Draggable()
)

root_child_2_child_2 = Element(
    parent = root_child_2,
    layout = VerticalLayout(5, 2),
    graphics = Label("another nested element", None, 18, background_color=(150,150,150)),
    input=TextField()
)

root_child_2_child_3 = Element(
    parent = root_child_2,
    layout = VerticalLayout(5, 2),
    graphics = Label("resize me too!", None, 18, background_color=(150,150,150)),
    input=ReSizable()
)

root_child_3 = Element(
    parent = root,
    layout = VerticalLayout(5, 2),
    graphics = Label("goodbye, world", None, 22, background_color=(80,80,80)),
    input=Draggable()
)

root.size = (300, 200)

app.elements.append(root)
app.run()
