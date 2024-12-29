class Solution:
  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
      res = [0]*len(temperatures)
      stk = []

      for i,t in enumerate(temperatures):
          while stk and stk[-1][0] < t:
              stkT, stkI = stk.pop()
              res[stkI] = (i-stkI)
          stk.append([t, i])

      return res
