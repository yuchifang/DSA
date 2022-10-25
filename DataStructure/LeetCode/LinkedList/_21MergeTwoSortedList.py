# https://leetcode.com/problems/merge-two-sorted-lists/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        anwser = listNode
        while list1 or list2:
            item1=list1.next
            item2=list2.next
            if item1> item2:
                anwser.val = item2 



# list1 =
# list2 = 
'''
list1.next = []
'''
