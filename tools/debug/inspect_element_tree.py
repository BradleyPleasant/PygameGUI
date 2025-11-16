from V03 import Element, VerticalLayout, Graphics
from V03.Objects.Label import Label
from V03.Objects.ReSizable import ReSizable
from V03.Objects.Draggable import Draggable

root = Element(parent=None, layout=VerticalLayout(5,2), graphics=Graphics((40,40,40)), input=ReSizable())
root.size = (400,300)
root.x = 10
root.y = 10

c1 = Element(parent=root, layout=VerticalLayout(5,2), graphics=Label("A", None,22, background_color=(80,80,80)), input=Draggable())

c2 = Element(parent=root, layout=VerticalLayout(5,2), graphics=Label("B", None,22, background_color=(80,80,80)), input=ReSizable())

c2c1 = Element(parent=c2, layout=VerticalLayout(5,2), graphics=Label("C1", None,18, background_color=(150,150,150)), input=Draggable())

c2c2 = Element(parent=c2, layout=VerticalLayout(5,2), graphics=Label("C2", None,18, background_color=(150,150,150)), input=ReSizable())

# Print relationships
for n in [root, c1, c2, c2c1, c2c2]:
    print(f"Node id={id(n)} type={getattr(n,'graphics',None).__class__.__name__ if getattr(n,'graphics',None) else 'NoG'} parent_id={id(n.parent) if n.parent else None} children_ids={[id(c) for c in n.children]}")

