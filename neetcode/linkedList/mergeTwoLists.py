# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        # Pego o menor elemento entre as duas listas, ele será o primeiro elemento do novo array
        # Verifico qual o próximo menor elemento, se é o next da lista 1 ou da lista 2

        # Base cases
        if not list1:
            return list2
        
        if not list2:
            return list1

        if not (list1 and list2):
            return None

        curr = dummy = ListNode() # type: ignore
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1  # Add the smaller node to the merged list
                list1 = list1.next  # Move to the next node in list1
            else:
                curr.next = list2  # Add the smaller node to the merged list
                list2 = list2.next  # Move to the next node in list2
            curr = curr.next  # Move to the next node in the merged list

        
        if list1 or list2:
            curr.next = list1 if list1 else list2

        return dummy.next
