class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = set() 
        for n in nums:
            if n not in dic: 
                dic.add(n)
            else:
                return n