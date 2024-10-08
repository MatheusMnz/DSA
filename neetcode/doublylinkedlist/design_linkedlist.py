class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        temp = self.head
        curr_index = 0

        while temp is not None and curr_index < index:
            temp = temp.next
            curr_index += 1

        return temp.val if temp is not None else -1  # Retorna o valor do nó ou -1 se não for encontrado

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:  # Lista vazia
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)

        if index == 0:  # Adicionar na cabeça
            self.addAtHead(val)
            return

        temp = self.head
        curr_index = 0

        while temp is not None and curr_index < index:
            temp = temp.next
            curr_index += 1

        if temp is None:  # Se o índice for maior que o tamanho da lista, não insere
            if curr_index == index:  # Mas se o índice for igual ao tamanho, insere ao final
                self.addAtTail(val)
            return

        # Inserir no meio
        prev_node = temp.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = temp
        temp.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        temp = self.head
        curr_index = 0

        while temp is not None and curr_index < index:
            temp = temp.next
            curr_index += 1

        if temp is None:  # Índice fora dos limites
            return

        # Se for o único nó na lista
        if temp == self.head and temp == self.tail:
            self.head = None
            self.tail = None
        elif temp == self.head:  # Deletar a cabeça
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif temp == self.tail:  # Deletar a cauda
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:  # Deletar no meio
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
