class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        new_node = Node(homepage)
        self.head = new_node
        self.tail = new_node
        self.current = new_node  # Página atual

    # Add method ( Tail )
    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node
        self.tail = new_node

    # Atualiza curr e retorna curr.val
    def back(self, steps: int) -> str:
        count = 0

        # Enquanto não alcançar o número de passos e ainda houver nós anteriores
        if steps is not None:
            while count < steps and self.current.prev is not None:
                self.current = self.current.prev
                count += 1  

        # Atualiza o ponteiro atual para a nova posição

        return self.current.val  # Retorna o valor do nó atual, que é a URL

    # Atualiza curr e retorna curr.val
    def forward(self, steps: int) -> str:
        count = 0
        while count < steps and self.current.next is not None:
            self.current = self.current.next
            count += 1

        return self.current.val
