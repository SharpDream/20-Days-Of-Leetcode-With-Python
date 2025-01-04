"""
Time Complexity: 0(mlogn)
Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        for x in matrix:
            find = self.binarysearch(x, target)
            if find:
                return True
        return False


    def binarysearch(self, li, target):

        l, r = 0, len(li) - 1

        while l<=r:
            mid = l + ((r-l)//2)
            if li[mid] < target:
                l = mid+1
            elif li[mid] > target:
                r = mid-1
            else:
                return True
        return False

"""


"""
Time Complexity: 0(logmn)
Space Complexity: O(1)
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows-1
        while top<=bot:
            mid = (top+bot)//2
            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bot = mid-1
            else:
                break

        if not (top<=bot):
            return False
        

        li = (top+bot)//2
        l, r = 0, cols -1
        while l<=r :
            mid = (l+r)//2
            if target > matrix[li][mid]:
                l = mid+1
            elif target < matrix[li][mid]:
                r = mid-1
            else:
                return True

        return False

