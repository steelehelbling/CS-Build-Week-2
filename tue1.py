class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, number in enumerate(nums):
            n = target - number
            if n in dic:
                return [dic[n], index]
            else:
                dic[number] = index
                