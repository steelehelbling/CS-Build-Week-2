class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index, num in enumerate(nums):
                if num == target:
                    return index
        return -1
