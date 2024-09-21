from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        sorted_list = dummy

        while list1 and list2:
            if list1.val < list2.val:
                sorted_list.next = list1
                list1 = list1.next
            else:
                sorted_list.next = list2
                list2 = list2.next

            sorted_list = sorted_list.next

        if list1:
            sorted_list.next = list1
        elif list2:
            sorted_list.next = list2

        return dummy.next
