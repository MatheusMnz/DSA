# Generic Tree

class NodeTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        # Passo a minha instância como pai
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        node_parent = self.parent
        while node_parent:
            level += 1
            node_parent = node_parent.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                # Chamo Recusrivamente para cada filho
                child.print_tree()


def build_product_tree():
    root = NodeTree("Electronics")

    laptop = NodeTree("Laptop")
    laptop.add_child(NodeTree("Mac"))
    laptop.add_child(NodeTree("Surface"))
    laptop.add_child(NodeTree("Thinkpad"))

    cellphone = NodeTree("Cell Phone")
    cellphone.add_child(NodeTree("iPhone"))
    cellphone.add_child(NodeTree("Google Pixel"))
    cellphone.add_child(NodeTree("Vivo"))

    tv = NodeTree("TV")
    tv.add_child(NodeTree("Samsung"))
    tv.add_child(NodeTree("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()

