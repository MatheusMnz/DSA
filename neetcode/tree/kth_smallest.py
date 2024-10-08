# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: # type: ignore
        def inorder(root):
            elements = []
            if root:
                # Processa a subárvore esquerda
                elements += inorder(root.left)
                # Adiciona o valor do nó atual
                elements.append(root.val)
                # Processa a subárvore direita
                elements += inorder(root.right)
            return elements
        
        # Faz o percurso em ordem e obtém todos os elementos em ordem crescente
        elements = inorder(root)
        
        # Retorna o k-ésimo menor elemento (note que k é 1-based, por isso k-1)
        return elements[k - 1]
