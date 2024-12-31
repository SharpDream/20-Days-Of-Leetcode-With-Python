class Solution(object):
  def topKFrequent(self, nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: List[int]
      """
      # Time complexity: o(n+k)

      hashmap = {}
      for num in nums:
          hashmap[num] = 1 + hashmap.get(num, 0)

      max_freq = max(hashmap.values())
      freq = [[] for _ in range(max_freq + 1)]
      for num,count in hashmap.items():
          freq[count].append(num)

      res = []
      for i in range(len(freq)-1, 0, -1):
          for n in freq[i]:
              res.append(n)
              if len(res) == k:
                  return res
