from V03 import Element, VerticalLayout, Graphics
from V03.Objects.Label import Label
from V03.Objects.ReSizable import ReSizable
from V03.Objects.Draggable import Draggable

root = Element(parent=None, layout=VerticalLayout(5,2), graphics=Graphics((40,40,40)), input=ReSizable())
root.size = (400,300)
root.x = 10
root.y = 10

root_child_1 = Element(parent=root, layout=VerticalLayout(5,2), graphics=Label("hello, world", None,22, background_color=(80,80,80)), input=Draggable())
root_child_2 = Element(parent=root, layout=VerticalLayout(5,2), graphics=Label("this is a test", None,22, background_color=(80,80,80)), input=ReSizable())

root_child_2_child_1 = Element(parent=root_child_2, layout=VerticalLayout(5,2), graphics=Label("nested element", None,18, background_color=(150,150,150)), input=Draggable())
root_child_2_child_2 = Element(parent=root_child_2, layout=VerticalLayout(5,2), graphics=Label("another nested element", None,18, background_color=(150,150,150)), input=ReSizable())

all_nodes = [root, root_child_1, root_child_2, root_child_2_child_1, root_child_2_child_2]

for n in all_nodes:
    print(f"Node id={id(n)} type={getattr(n,'graphics',None).__class__.__name__ if getattr(n,'graphics',None) else 'NoG'} parent_id={id(n.parent) if n.parent else None} children_ids={[id(c) for c in n.children]}")

# Also print full tree using recursion

def print_tree(node, indent=0):
    print('  '*indent + f"id={id(node)} type={getattr(node,'graphics',None).__class__.__name__ if getattr(node,'graphics',None) else 'NoG'} parent_id={id(node.parent) if node.parent else None} children={[id(c) for c in node.children]}")
    for c in node.children:
        print_tree(c, indent+1)

print('\nRecursive tree:')
print_tree(root)

