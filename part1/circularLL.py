class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:  # Se a lista estiver vazia
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                
            temp.next = new_node
            new_node.next = self.head

            
    def print_list(self):
        if self.head is None:
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:  # Para quando chegar no início novamente
                break
        print("(head)")



if __name__ == '__main__':
    ll = CircularLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.print_list()          # Impressão normal
