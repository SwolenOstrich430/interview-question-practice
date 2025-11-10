# from types import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initialize start_node to be starting node in new LL
        # this is what we'll return after everything's done
        start_node = ListNode()

        # initialize curr_sum_val var to hold l1.val + l2.val
        curr_sum_val = 0

        # create var to hold curr LL Node (curr_node)
        curr_node = start_node
        # create var to hold the previous LL Node (next_node)
        prev_node = None
        
        # don't mutate l1 and l2 
        l1_nd = l1 
        l2_nd = l2 

        while l1_nd or l2_nd:
            if prev_node and prev_node == curr_node:
                curr_node = ListNode()
                prev_node.next = curr_node

            curr_sum_val = curr_node.val or 0
            
            if l1_nd and l1_nd.val:
                curr_sum_val += l1_nd.val

            if l2_nd and l2_nd.val:
                curr_sum_val += l2_nd.val
            
            # get value from ones place in curr_sum and set to curr_node.val
            curr_node.val = curr_sum_val % 10
            prev_node = curr_node 

            if curr_sum_val > 9:
                curr_node = ListNode()
                curr_node.val = int(curr_sum_val / 10)
                prev_node.next = curr_node

            if l1_nd: 
                l1_nd = l1_nd.next
            if l2_nd:
                l2_nd = l2_nd.next

        return start_node
    

l1 = [1, 2, 3]
l2 = [4, 8, 9, 1]

l1n = ListNode()
l2n = ListNode()

curr_node = l1n 
prev_node = None 

for i in range(len(l1)):
    if i != 0:
        prev_node = curr_node 
        curr_node = ListNode()
        prev_node.next = curr_node

    curr_node.val = l1[i]

curr_node = l2n

for i in range(len(l2)):
    if i != 0:
        prev_node = curr_node 
        curr_node = ListNode()
        prev_node.next = curr_node

    curr_node.val = l2[i]

sol = Solution()
sol.addTwoNumbers(
    l1n, 
    l2n
)