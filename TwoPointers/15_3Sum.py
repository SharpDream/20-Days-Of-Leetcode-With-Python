class Solution(object):
  def threeSum(self, nums):
      """
      :type nums: List[int]
      :rtype: List[List[int]]
      """
      nums.sort()
      res = []
      for i,x in enumerate(nums):
          if i>0 and x == nums[i-1]:
              continue

          l,r = i+1, len(nums)-1
          while l<r:
              sum3 = x + nums[l] + nums[r]
              if sum3 < 0:
                  l += 1
              elif sum3 > 0:
                  r -= 1
              else:
                  res.append([x, nums[l], nums[r]])
                  l += 1
                  while nums[l] == nums[l-1] and l<r:
                      l += 1
      return res
