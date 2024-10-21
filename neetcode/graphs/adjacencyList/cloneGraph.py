# # Definition for a Node.
# class Node:
#     def __init__(self, val=0, neighbors=[]):
#         self.val = val
#         self.neighbors = neighbors

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']: # type: ignore
        # Dicionário para armazenar a lista. Verifico se a lista é vazia ou se já foi clonado
        # Cria um novo nó, adiciona
        # Para cada vizinho do no original, chamo o método de clonar
        # e adiciono aos vizinhos

        cloned_nodes = {}

        def clone_node(node):
            if not node:
                return None
            
            # Se já existir, retorna ele
            if node in cloned_nodes:
                return cloned_nodes[node]
            
            # Criando novo nó
            cloned_node = Node(node.val) # type: ignore
            cloned_nodes[node] = cloned_node

            # Recursivamente, clono cada nó
            for neighbor in node.neighbors:
                cloned_neighbor = clone_node(neighbor)
                cloned_node.neighbors.append(cloned_neighbor)

            return cloned_node
        
        return clone_node(node)