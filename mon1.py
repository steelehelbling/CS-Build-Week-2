class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = set() #create a arry of nums that have been seen
        answer = False
        for n in nums:
            if n not in dic: #if you have seen
                # print('true')
                dic.add(n)
            else: 
                answer = True
                # print('false')
        return answer