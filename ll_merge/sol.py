from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr_node = None 
        new_head = None 

        while len([node for node in lists if node is not None]) > 0:
            min_val = next(filter(None, lists), None).val

            for _list in lists:
                if _list is None: 
                    continue 

                if _list.val < min_val:
                    min_val = _list.val 

            for i in range(len(lists)):
                if lists[i] is None or lists[i].val > min_val: 
                    continue 

                if new_head is not None:
                    curr_node.next = ListNode(lists[i].val, None)
                    curr_node = curr_node.next
                else:
                    new_head = ListNode(min_val, None)
                    curr_node = new_head
                    
                lists[i] = lists[i].next

        return new_head 


test_cases = [
    ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
    ([], []),
    ([[]], [])
]

sol = Solution()
i = 0

for test_case in test_cases:
    # print(f"test_case[0]: {test_case[0]}")
    # print(f"test_case[1]: {test_case[1]}")
    # print(f"sol.mergeKLists(test_case[0]): {sol.mergeKLists(test_case[0])}")

    lists = []

    for _list in test_case[0]:
        head = ListNode(_list[0])
        curr_node = head
        
        for i in range(1, len(_list)):
            curr_node.next = ListNode(_list[i])
            curr_node = curr_node.next
        
        lists.append(head)

    if sol.mergeKLists(lists).sort() != test_case[1].sort():
        raise # True