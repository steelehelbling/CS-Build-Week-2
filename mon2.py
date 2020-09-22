class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        if l1 == None and l2 == None:
            return None            
        if l1 == None: 
            return l2
        if l2 == None:
            return l1

        addednumber = l1.val + l2.val
        carry = None
        
        if addednumber > 9:
            addednumber = addednumber % 10
            carry = ListNode(1)
            
        newnum = ListNode(addednumber)
        numaker= ListNode(addednumber)
        
        numaker = self.addTwoNumbers(l1.next, l2.next)
            
        newnum.next = self.addTwoNumbers(numaker, carry)
        return newnum 
