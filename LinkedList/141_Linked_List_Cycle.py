# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return 

        # Floyd's Tortoise and Hare
        fast, slow = head, head

        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False


