from DynamicUI import *


app = Application()


root = Element(
    manager=None,
    organizer=VerticalOrganizer(element_padding=10, children_padding=5),
    renderer=Renderer(background_color=(20, 20, 20)),
    input_handler=None,
    rect=(50, 200, 500, 200)
)

child1 = Element(
    manager=None,
    organizer=VerticalOrganizer(element_padding=5, children_padding=5),
    renderer=Renderer(background_color=(200, 20, 20)),
    input_handler=None,
    parent=root,
    rect=(0, 0, 30, 100)
)

child2 = Element(
    manager=None,
    organizer=VerticalOrganizer(element_padding=5, children_padding=5),
    renderer=Renderer(background_color=(20, 200, 20)),
    input_handler=None,
    parent=root,
    rect=(0, 0, 30, 100)
)

child3 = Element(
    manager=None,
    organizer=VerticalOrganizer(element_padding=5, children_padding=5),
    renderer=Renderer(background_color=(20, 20, 200)),
    input_handler=None,
    parent=root,
    rect=(0, 0, 50, 100)
)

app.add_element(root)
app.run()