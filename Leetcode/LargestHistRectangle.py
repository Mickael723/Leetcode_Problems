class Solution:
    def largestRectangleArea(self, heights: list) -> list:
        
        stack = [] # stack[i] = (i, height)
        max_area = 0

        for i, h in enumerate(heights):
            
            extended_i = i

            #While the current prev height in the stack cannot be extended, compute the max area and pop the stack
            while stack and stack[-1][1] > heights[i]:
                prev_i, prev_h = stack.pop()
                width = i - prev_i
                max_area = max(max_area, width * prev_h)
                extended_i = prev_i
                
            #Add element and index to the stack
            stack.append((extended_i, h))
        
        #Clean out the stack by computing the mac area available in the current stack
        for i, h in stack:
            width = len(heights) - i
            max_area = max(max_area, width * h)

        return max_area

if __name__=="__main__":
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))
    print(s.largestRectangleArea([2,4]))