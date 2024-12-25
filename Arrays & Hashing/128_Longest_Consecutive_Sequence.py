class Solution(object):
  def longestConsecutive(self, nums = [100,4,200,1,3,2]):
      """
      :type nums: List[int]
      :rtype: int
      """
      nums = set(nums)
      longest = 0
      for n in nums:
          if n-1 not in nums:
              length = 1
              while (length+n) in nums:
                  length += 1
              longest = max(length, longest)
      return longest

