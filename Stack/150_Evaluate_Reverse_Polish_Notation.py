# This code dose not run properly on below python3
# cz of int(b/a) on line 21 it can be used b//a to avoid the error on below python3


class Solution(object):
  def evalRPN(self, tokens):
      """
      :type tokens: List[str]
      :rtype: int
      """
      stk = []
      for char in tokens:
          if char == "+": stk.append(stk.pop() + stk.pop())
          elif char == "*": stk.append(stk.pop() * stk.pop())

          elif char == "-": 
              a,b = stk.pop(), stk.pop()
              stk.append(b-a)
          elif char == "/":
              a,b = stk.pop(), stk.pop()
              stk.append(int(b/a))

          else: stk.append(int(char))
      return stk[0]