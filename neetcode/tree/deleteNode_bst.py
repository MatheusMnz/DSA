# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]: # type: ignore
        if not root:
            return None
        
        if key > root.val:
            if root.right:
                root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            if root.left:
                root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left


            # Caso o nó a ser deletado tenha 2 filhos
            # Substitui o nó pelo menor valor da subárvore direita
            min_val = self.min(root.right)
            root.val = min_val
            # Deleta o nó que tinha o menor valor na subárvore direita
            root.right = self.deleteNode(root.right, min_val)
            
        return root

