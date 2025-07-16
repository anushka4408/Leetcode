# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Helper to check if there are at least k nodes to reverse
        def hasKNodes(curr, k):
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1
            return count == k

        # Helper to reverse k nodes and return new head and tail
        def reverseGroup(start, k):
            prev, curr = None, start
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, start  # new head, new tail

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while hasKNodes(group_prev.next, k):
            group_start = group_prev.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next

            next_group_start = group_end.next

            # Reverse current k group
            new_head, new_tail = reverseGroup(group_start, k)

            # Reconnect reversed group with previous part
            group_prev.next = new_head
            new_tail.next = next_group_start

            # Move group_prev forward for next reversal
            group_prev = new_tail

        return dummy.next
