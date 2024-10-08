# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        curr = head
        prev = None

        if not head:
            return None

        while curr is not None:
            # Próximo elemento
            next = curr.next 

            # Inverte a ordem
            curr.next = prev 

            # atualiza o prev e curr
            prev = curr
            curr = next
        return prev
            
