class Solution(object):
  def groupAnagrams(self, strs):
      """
      :type strs: List[str]
      :rtype: List[List[str]]
      """
      result = defaultdict(list)

      for string in strs:
          count = [0]*26
          for char in string:
              count[ord(char) - ord("a")] += 1
          key = tuple(count)
          result[key].append(string)
      return list(result.values())


