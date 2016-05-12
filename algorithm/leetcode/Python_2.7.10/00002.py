#
## https://leetcode.com/problems/add-two-numbers/
#

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        current = head
        carry_over = 0
        while l1 or l2:
            if l1 and l2:
                tmp = l1.val + l2.val + carry_over
                if tmp >= 10:
                    current.val = tmp - 10
                    carry_over = 1
                else:
                    current.val = tmp
                    carry_over = 0
            elif l1:
                tmp = l1.val + carry_over
                if tmp >= 10:
                    current.val = tmp - 10
                    carry_over = 1
                else:
                    current.val = tmp
                    carry_over = 0
            elif l2:
                tmp = l2.val + carry_over
                if tmp >= 10:
                    current.val = tmp - 10
                    carry_over = 1
                else:
                    current.val = tmp
                    carry_over = 0
            else:
                if carry_over == 1:
                    current.val = 1
                    carry_over = 0
                    
                break
               
            if l1:
                l1 = l1.next
                
            if l2:
                l2 = l2.next
            
            if l1 or l2:
                current.next = ListNode(None)
                current = current.next
                
        if carry_over == 1:
            current.next = ListNode(1)
            
        return head
        
        
