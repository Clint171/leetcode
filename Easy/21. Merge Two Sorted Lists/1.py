# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def insertNode(l1 , l2):
            if l1 == None and l2 == None:
                return None
            l3 = ListNode()
            if l1 == None:
                l3.val = l2.val
                l3.next = insertNode(None , l2.next)
            elif l2 == None:
                l3.val = l1.val
                l3.next = insertNode(l1.next , None)
            elif l1.val <= l2.val:
                l3.val = l1.val
                l3.next = insertNode(l1.next , l2)
            else:
                l3.val = l2.val
                l3.next = insertNode(l1 , l2.next)
            return l3
        
        return insertNode(list1 , list2)

