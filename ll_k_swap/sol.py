from typing import List, Optional

class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        curr_node = head 
        lead_node = curr_node
        length = 0 

        while curr_node is not None: 
            length += 1
            curr_node = curr_node.next 

        curr_node = head
        memo_arr = []

        while length >= k:
            for _ in range(k):
                memo_arr.append(lead_node.val) 
                lead_node = lead_node.next

            for _ in range(k):
                curr_node.val = memo_arr.pop() 
                curr_node = curr_node.next

            length -= k

        return head
    

test_cases = [
    ([1,2,3,4,5], 2, [2,1,4,3,5]),
    ([1,2,3,4,5], 3, [3,2,1,4,5]),
    ([1,2,3,4,5], 1, [1,2,3,4,5]),
    ([1,2,  3,4,5], 4, [4,3,2,1,5])
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

    head = sol.reverseKGroup(head, test_case[1])
    final_list = []
    
    while head is not None:
        final_list.append(head.val)
        head = head.next

    if final_list != test_case[2]:
        raise # True