class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i,x in enumerate(nums):
            diff = target-x
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[x] = i
          
