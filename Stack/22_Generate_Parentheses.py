class Solution:
def generateParenthesis(self, n: int) -> list[str]:
    # ( -> while open < n:
    # ) -> while close < open
    # valid () -> open=close=n
    res = []
    stk = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            return res.append("".join(stk))

        if openN < n:
            stk.append("(")
            backtrack(openN+1, closedN)
            stk.pop()

        if closedN<openN:
            stk.append(")")
            backtrack(openN, closedN+1)
            stk.pop()

    backtrack(openN=0, closedN=0)

    return res
