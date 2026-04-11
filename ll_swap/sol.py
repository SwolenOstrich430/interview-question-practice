from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# would be better to swap the nodes themselves instead of just the values, 
# but this is easier to implement and has the same time complexity  
# do that later
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: 
            return None
        
        next_node = head.next
        curr_node = head

        while curr_node is not None and next_node is not None:
            curr_node.val, next_node.val = next_node.val, curr_node.val
            
            curr_node = next_node.next    
            next_node = curr_node.next if curr_node is not None else None 

        return head


test_cases = [
    ([1,2,3,4], [2,1,4,3]),
    ([1,2,3], [2,1,3]),
    ([1], [1]),
    ([], [])
]

sol = Solution()

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    
    head = ListNode(test_case[0][0])
    curr_node = head

    for i in range(1, len(test_case[0])):
        curr_node.next = ListNode(test_case[0][i])
        curr_node = curr_node.next

    head = sol.swapPairs(head)
    final_list = []
    
    while head is not None:
        final_list.append(head.val)
        head = head.next

    if final_list != test_case[1]:
        raise # True