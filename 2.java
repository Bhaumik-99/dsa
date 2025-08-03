
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Dummy node to start the result list
        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead;
        int carry = 0;
        
        // Loop through both lists
        while (l1 != null || l2 != null || carry != 0) {
            int x = (l1 != null) ? l1.val : 0;  // value from l1
            int y = (l2 != null) ? l2.val : 0;  // value from l2
            int sum = x + y + carry;

            carry = sum / 10;  // update carry
            current.next = new ListNode(sum % 10);  // store digit
            current = current.next;

            // move to next nodes
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        return dummyHead.next;
    }
}
