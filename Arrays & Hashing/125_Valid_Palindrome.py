# you can also use isalnum() inbuild func

class Solution(object):
  def isPalindrome(self, s):
      """
      :type s: str
      :rtype: bool
      """
      l,r = 0, len(s)-1
      while l<r:
          while l<r and not self.isalnum(s[l]):
              l += 1
          while r>l and not self.isalnum(s[r]):
              r -= 1
          if s[l].lower() != s[r].lower():
              return False
          l,r = l+1, r-1
      return True

  def isalnum(self, char):
      return ((ord("A") <= ord(char) <= ord("Z")) or
              (ord("a") <= ord(char) <= ord("z")) or
              (ord("0") <= ord(char) <= ord("9")))