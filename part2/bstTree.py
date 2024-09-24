class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # Add on left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            # Add on right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)


    def in_order_traversal(self):
        elements = []

        # Left subtree recursion
        if self.left:
            elements += self.left.in_order_traversal()
        
        # Base node
        elements.append(self.data)

        # Right subtree recursion        
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    
    def search(self, value):
        if self.data == value:
            return True

        # Value in Left Subtree
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        # Value in Right Subtree
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
            
    # Find min 
    def min(self):
        current = self

        while current.left is not None:
            current = current.left
        return current.data

    # Find max
    def max(self):
        current = self
        
        while current.right is not None:
            current = current.right
        return current.data

    # Calculate sum
    def sum(self):
        acc = 0
        current = self

        # Loop Down on left subtree
        while current.left is not None:
            acc += current.data
            current = current.left
        
        while current.right is not None:
            acc += current.data
            current = current.right
        
        return acc


    # post_order_traversal
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    
    # pre_order_traversal
    def pre_order_traversal(self):
        elements = []
        
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # Caso o nó a ser deletado tenha 0 ou 1 filho
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            # Caso o nó a ser deletado tenha 2 filhos
            # Substitui o nó pelo menor valor da subárvore direita
            min_val = self.right.min()
            self.data = min_val
            # Deleta o nó que tinha o menor valor na subárvore direita
            self.right = self.right.delete(min_val)
            
        return self

            
    

def build_tree(elements):
    root = BinaryTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1 , 20 , 9 , 23, 18 , 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print(f'Existe na arvore? {numbers_tree.search(18)}')
    print(f'In_Order: {numbers_tree.in_order_traversal()}')
    print(f'Post_Order: {numbers_tree.post_order_traversal()}')
    print(f'Pre_Order: {numbers_tree.pre_order_traversal()}')
    print(f'Valor mínimo: {numbers_tree.min()}')
    print(f'Valor máximo: {numbers_tree.max()}')
    numbers_tree.delete(9)
    print(f'In_Order: {numbers_tree.in_order_traversal()}')
