class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Referência ao último nó (tail)

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:  # Se a lista estiver vazia
            self.head = new_node
            self.tail = new_node  # O tail também será o novo nó
        else:
            self.tail.next = new_node  # Adiciona o novo nó após o tail atual
            new_node.prev = self.tail  # O novo nó aponta de volta para o tail
            self.tail = new_node  # Atualiza o tail para o novo nó

    def insert_at_index(self, data, index):
        new_node = Node(data)

        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            return

        temp = self.head
        curr_index = 0

        while temp is not None and curr_index < index:
            temp = temp.next
            curr_index += 1

        # Inserir no fim
        if temp.next is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        # Inserir no meio
        else:
            prev_node = temp.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = temp
            temp.prev = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def print_list_reversal(self):
        temp = self.tail  # Agora podemos começar direto do último nó (tail)
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.prev
        print("None")



if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert_at_index(5, 1)
    ll.print_list()          # Impressão normal
    ll.print_list_reversal()  # Impressão reversa
