class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        # solution #1
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        # Time (test): 23 ms
        return sorted(s) == sorted(t)
        
        # solution #2
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Time (test): 27 ms
        # return Counter(s) == Counter(t)
        
        # solution #3
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Time (test): 23 ms
        # s_dict, t_dict = {}, {}
        # for i in range(len(s)):
        #     s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        #     t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        # for x in s_dict:
        #     if s_dict[x] != t_dict.get(x, 0):
        #         return False
        # return True
