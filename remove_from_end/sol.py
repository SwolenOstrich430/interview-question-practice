from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr_node = head 
        index_count = 0

        while curr_node is not None: 
            index_count += 1
            curr_node = curr_node.next 

        target_index = index_count - n
        prev_node = None 
        curr_node = head
        i = 0

        while curr_node is not None:
            if i == target_index:
                if prev_node is None:
                    head = head.next
                else: 
                    prev_node.next = curr_node.next 

                break

            prev_node = curr_node 
            curr_node = curr_node.next 
            i += 1

        return head 
        
sol = Solution() 

test_cases = [
    [([1,2,3,4,5], 2), [1, 2, 3, 5]],
    [([1,2,3,4,5], 3), [1, 3, 4, 5]],
    [([1,2,3,4,5], 4), [2, 3, 4, 5]]
]

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    
    head = ListNode(test_case[0][0][0])
    curr_node = head

    for i in range(1, len(test_case[0][0])):
        curr_node.next = ListNode(test_case[0][0][i])
        curr_node = curr_node.next
    
    head = sol.removeNthFromEnd(head, test_case[0][1])
    final_list = []
    
    while head is not None:
        final_list.append(head.val)
        head = head.next

    if final_list != test_case[1]:
        raise # True