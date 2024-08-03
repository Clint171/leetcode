# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        def insert_to_heap(heap , num):
            if len(heap) < 1:
                heap.append(num)
                return heap
            
            #append element to empty slot in heap
            heap.append(num)

            # Heapify up
            num_idx = len(heap) - 1

            while num_idx > 0 :
                num_parent_idx = num_idx//2
                
                # Check if parent is greater than child
                if heap[num_parent_idx] > heap[num_idx]:

                    # Swap the elements
                    temp = heap[num_idx]
                    heap[num_idx] = heap[num_parent_idx]
                    heap[num_parent_idx] = temp

                    num_idx = num_parent_idx
                
                else:
                    break
            
            return heap
        
        def heapify(heap , root_idx):
            lchild_idx = (root_idx * 2) + 1
            rchild_idx = (root_idx * 2) + 2

            if lchild_idx >= len(heap):
                return
            
            if rchild_idx >= len(heap):
                rchild_idx = None

            # Compare root with left child
            if(heap[root_idx] > heap[lchild_idx]):
                # Switch elements
                temp = heap[lchild_idx]
                heap[lchild_idx] = heap[root_idx]
                heap[root_idx] = temp

                # Call the function recursively
                heapify(heap , lchild_idx)

            if(not(rchild_idx == None) and heap[root_idx] > heap[rchild_idx]):
                # Switch elements
                temp = heap[rchild_idx]
                heap[rchild_idx] = heap[root_idx]
                heap[root_idx] = temp

                # Call the function recursively
                heapify(heap , rchild_idx)

        def delete_from_heap(heap):
            if len(heap) < 1:
                return None
            # Pick the first element in the array
            element = heap[0]

            # Replace the element with the last element
            heap[0] = heap[len(heap)-1]
            heap.pop()

            # Heapify
            heapify(heap , 0)

            return element

        dummyHead = ListNode()

        last = dummyHead

        heap = []

        for i in lists:
            node = i

            while not(node == None):
                insert_to_heap(heap , node.val)
                node = node.next
        
        print(heap)
        
        for i in range(len(heap)):
            newNode = ListNode()
            newNode.val = delete_from_heap(heap)
            last.next = newNode
            last = newNode

        return dummyHead.next

if __name__ == "__main__":
    solution = Solution()

    # Create example list of lists
    # convert the list of lists to list of linked lists
    list_of_lists = [[-9,-7,-7],[-6,-4,-1,1],[-6,-5,-2,0,0,1,2],[-9,-8,-6,-5,-4,1,2,4],[-10],[-5,2,3]]

    lists = []

    for i in list_of_lists:
        head = ListNode()
        last = head

        for j in i:
            node = ListNode()
            node.val = j
            last.next = node
            last = node
        
        lists.append(head.next)

    newList = solution.mergeKLists(lists)

    while not(newList == None):
        print(newList.val)
        newList = newList.next