# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int: # type: ignore
        # DFS
        def dfs(node, actual_max):
            if not node:
                return 0

            # Verifica se o nó atual é "good"
            if node.val >= actual_max:
                good_nodes = 1   
            else:
                good_nodes = 0

            # Atualiza o valor máximo e realiza DFS nas subárvores
            good_nodes += dfs(node.left, max(actual_max, node.val))
            good_nodes += dfs(node.right, max(actual_max, node.val))

            return good_nodes
        
        # Inicia a DFS com o valor da raiz como o valor máximo inicial
        return dfs(root, root.val)
