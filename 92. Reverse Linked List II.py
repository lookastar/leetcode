from locale import currency
from typing import Optional
from warnings import formatwarning
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        rearN = ListNode # next = None
        curri = 1
        currN = head
        forwN = currN.next

        while curri <= right:

            if curri > left:
                currN.next = rearN
            elif curri == left:
                L = currN
                L_1 = rearN
            rearN = currN
            currN = forwN
            if forwN:
                forwN = forwN.next
            curri += 1

        L_1.next = rearN
        L.next = currN
        
        if left == 1:
            return rearN
        else:
            return head