from V03 import Application, Element, VerticalLayout, Graphics, Input
from V03.Objects.Label import Label
from V03.Objects.ReSizable import ReSizable
from V03.Objects.Draggable import Draggable
from V03.Objects.TextField import TextField


app = Application()


root = Element(
    parent = None,
    layout = VerticalLayout(5, 2),
    # give the root a visible background so you can see its bounds
    graphics = Graphics((40, 40, 40)),
    input = ReSizable()
)
#

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
    graphics = Graphics(background_color=(80,80,80)),
    input=ReSizable()
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

app.elements.append(root)
app.run()
