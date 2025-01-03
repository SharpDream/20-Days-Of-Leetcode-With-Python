# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getK(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            prev, curr = None, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = prev
            temp.next = groupNext
            groupPrev = temp

        return dummy.next

    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr if k == 0 else None
