class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None 

        i = 0 
        length = 0
        end = None 
        curr_node = head 
        prev_node = None 

        while curr_node is not None:
            curr_node = curr_node.next
            length += 1

        curr_node = head

        while i < k % length:
            while curr_node.next is not None:
                prev_node = curr_node
                curr_node = curr_node.next 

            if prev_node is not None:
                prev_node.next = None 
                curr_node.next = head

            head = curr_node 
            i += 1

        return head 
