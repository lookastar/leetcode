#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, last_different = head, head

        if current == None or current.next == None:
            return head

        while current != None:
            current = current.next
            while current != None and current.val == last_different.val:
                current = current.next
            last_different.next = current
            last_different = last_different.next

        return head