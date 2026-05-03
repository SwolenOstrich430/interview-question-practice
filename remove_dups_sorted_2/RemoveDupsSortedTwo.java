import java.util.HashSet;
import java.util.Set;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class RemoveDupsSorted2Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode currNode = head;
        ListNode prevNode = null;
        ListNode placeHolder;
        Set<Integer> hist = new HashSet<>();

        while (currNode != null && currNode.next != null) {
            if (hist.contains(currNode.val)) {
                currNode = prevNode;
                placeHolder = currNode;

                while (placeHolder.next != null && hist.contains(placeHolder.val)) {
                    placeHolder = placeHolder.next;
                }

                prevNode = currNode;
                currNode.next = placeHolder;
                currNode = placeHolder;
            } else {
                hist.add(currNode.val);
                prevNode = currNode;
                currNode = currNode.next;
            }

        }

        return head;
    }
}

class RemoveDupsSorted3Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode currNode = head;
        ListNode lastChange = null;
        ListNode placeHolder;
        Set<Integer> hist = new HashSet<>();

        while (currNode != null && currNode.next != null) {
            if (hist.contains(currNode.val)) {
                placeHolder = currNode;

                while (placeHolder.next != null && hist.contains(placeHolder.val)) {
                    placeHolder = placeHolder.next;
                }

                if (lastChange == null && head.val != placeHolder.val) {
                    head = placeHolder;
                    currNode = head;
                } else if (lastChange == null && head.val == placeHolder.val) {
                    head = null;
                    return head;
                } else {
                    currNode = lastChange;
                    currNode.next = placeHolder;
                    currNode = currNode.next;
                }
            } else {
                hist.add(currNode.val);
                
                if (currNode.next != null && currNode.val != currNode.next.val) {
                    lastChange = currNode;
                }

                currNode = currNode.next;
            }

        }

        return head;
    }
}

class RemoveDupsSorted4Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        } else if (head.next == null) {
            return head;
        } else if (head.next.next == null) {
            return head.val == head.next.val ? null : head;
        }

        ListNode lag = head;
        ListNode lead = lag.next;
        Integer currSkipVal = null;
        ListNode newHead = null;
        ListNode currNode = null;

        while (lead != null) {
            while (lead != null && lag.val == lead.val) {
                if (currSkipVal == null) {
                    currSkipVal = lag.val;
                }

                lag = lead;
                lead = lead.next;
            }

            if (!Integer.valueOf(lag.val).equals(currSkipVal)) {
                if (newHead == null) {
                    newHead = lag;
                    currNode = newHead;
                } else {
                    currNode.next = lag;
                    currNode = currNode.next;
                }
            } else if (currNode != null) {
                currNode.next = null;
            }

            if (lead != null && lead.next == null && lag.val != lead.val) {
                if (currNode == null) {
                    newHead = lead;
                } else {    
                    currNode.next = lead;
                }
            } 

            lag = lead;
            currSkipVal = null;
            if (lead != null) {
                lead = lead.next;
            }
        }
        
        return newHead;
    }
}

public class RemoveDupsSortedTwo {
    public static void main(String[] args) {
        RemoveDupsSorted4Solution sol = new RemoveDupsSorted4Solution();
        // int [] nums = new int[]{1,1,1,2,2,3,3,5};
        // int[] nums = {1, 1, 2, 2};
        // int[] nums = {-1,0,0,0,0,3,3};
        int[] nums = {1,2,3,3,4,4,5};
        ListNode head = new ListNode(nums[0]);
        ListNode currNode = head;

        for (int i = 1; i < nums.length; i++) {
            currNode.next = new ListNode(nums[i]);
            currNode = currNode.next;
        }

        sol.deleteDuplicates(head);
    }
}