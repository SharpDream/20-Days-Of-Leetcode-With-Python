class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        stk = []
        maxArea = 0

        for index, height in enumerate(heights):
            start = index
            while stk and stk[-1][1] > height:
                index2, height2 = stk.pop()
                maxArea = max(maxArea, height2*(index-index2))
                start = index2
            stk.append((start, height))
    
        for index, height in stk:
            maxArea = max(maxArea, height* (len(heights) - index))

        return maxArea

