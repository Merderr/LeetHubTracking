class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}

        for i, num in enumerate(nums):
            twin = target - num
            if twin in num_dict:
                return [num_dict[twin], i]
            
            num_dict[num] = i
        