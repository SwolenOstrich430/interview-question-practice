import java.util.ArrayList;


class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class ReverseLLIISolution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ArrayList<ListNode> nodes = new ArrayList<>();
        ListNode currNode = head;
        int finalIdx = 0;

        while (currNode != null && finalIdx <= right) {
            nodes.add(currNode);
            currNode = currNode.next;
            finalIdx++;
        }

        while (left < right) {
            right--;

            if (left == 0) {
                head = nodes.get(right);
                head.next = nodes.get(left + 1);
            } else {
                nodes.get(left - 1).next = nodes.get(right);
                nodes.get(right).next = nodes.get(left + 1);
            }

            if (nodes.get(right).next == null || right >= nodes.size()) {
                nodes.get(right - 1).next = nodes.get(left);
                nodes.get(left).next = null;
            } else {
                nodes.get(right - 1).next = nodes.get(left);
                nodes.get(left).next = nodes.get(right);
            }

            left++;
        }

        return head;
    }
}

public class ReverseLLII {
    public static void main(String[] args) {
        ReverseLLIISolution sol = new ReverseLLIISolution();
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        int left = 2;
        int right = 4;
        System.out.println(sol.reverseBetween(head, left, right));
    }
}