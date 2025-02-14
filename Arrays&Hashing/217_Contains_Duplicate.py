class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
        