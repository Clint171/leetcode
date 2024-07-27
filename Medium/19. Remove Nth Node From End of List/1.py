# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        def returnNode(node):
            if node is None:
                return [None, 0]

            newNode = ListNode(node.val)
            returnValues = returnNode(node.next)
            nodeChild = returnValues[0]
            count = returnValues[1]

            count += 1

            if count == n:

                return [nodeChild , count]

            else:

                newNode.next = nodeChild
                return [newNode , count]

        return returnNode(head)[0]