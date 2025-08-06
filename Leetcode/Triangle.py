class Solution:
    def minimumTotal(self, triangle: list) -> int:

        dp_array = [[float("inf")] * len(triangle[i]) for i in range(len(triangle))]

        #Base Cases initialized
        for i in range(len(triangle[len(triangle) - 1])):
            dp_array[len(triangle) - 1][i] = triangle[len(triangle) - 1][i]
        
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp_array[i][j] = min(triangle[i][j] + dp_array[i+1][j], triangle[i][j] + dp_array[i+1][j+1])

        return dp_array[0][0]

if __name__=="__main__":
    s = Solution()
    print(s.minimumTotal([[-1],[2,3],[1,-1,-3]]))