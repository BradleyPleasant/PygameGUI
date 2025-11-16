from ..Input import Input
from ..Element import Element

class TextField(Input):
    def __init__(self):
        super().__init__(selectable=True)
        self.text = ""
        raise NotImplementedError()