class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        # Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        
        # Reverse the second part of the list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second = prev
        first = head
        
        # Merge the two halves
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2