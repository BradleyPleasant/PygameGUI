from V03 import Application, Element, VerticalLayout, Graphics, Label, Input


app = Application()


root = Element(
    parent = None,
    layout = VerticalLayout(5, 2),
    graphics = Graphics(),
)
root.size = (400, 300)

root_child_1 = Element(
    parent = root,
    layout = VerticalLayout(5, 2),
    graphics = Label("hello, world", None, 22),
    input=Input()
)

app.elements.append(root)
app.run()
