# Definição do nó da árvore binária
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: # type: ignore
        # Se não houver mais nós para adicionar
        if not preorder or not inorder:
            return None
        
        # A raiz é o primeiro elemento do preorder
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Encontra a posição da raiz no inorder
        inorder_index = inorder.index(root_val)
        
        # Constrói recursivamente as subárvores
        root.left = self.buildTree(preorder[1:inorder_index + 1], inorder[:inorder_index])
        root.right = self.buildTree(preorder[inorder_index + 1:], inorder[inorder_index + 1:])
        
        return root
