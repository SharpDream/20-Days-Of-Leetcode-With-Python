class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return

        while len(lists) > 1:
            mergedList = []

            for x in range(0, len(lists), 2):
                l1 = lists[x]
                l2 = lists[x + 1] if (x + 1) < len(lists) else None
                mergedList.append(self.mergeTwoList(l1, l2))
            lists = mergedList

        return lists[0]

    def mergeTwoList(self, l1, l2):

        if not l1 and not l2:
            return

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next
