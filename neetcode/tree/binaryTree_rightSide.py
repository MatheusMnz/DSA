from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        elements = []

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                curr = queue.popleft()

                # Se for o último nó do nível, adicione à lista
                if i == level_length - 1:
                    elements.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return elements
