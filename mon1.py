class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arry = []
        answer = False
        for n in nums:
            if n not in arry: 
                # print('true')
                arry.append(n) 
            else: 
                answer = True
                # print('false')
        return answer