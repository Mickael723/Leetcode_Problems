#This function recursively searches a grid and memoizes the results of its search
def grid_dfs(i,j, r, c, grid, dp_array):

    if dp_array[i][j] != -1:
        return dp_array[i][j]

    current_slope = grid[i][j]
    max_path = 1  

    #Recursively search adjacent nodes
    if i - 1 in range(r) and grid[i - 1][j] < current_slope:
        max_path = max(max_path, 1 + grid_dfs(i - 1, j, r, c, grid, dp_array))
    if i + 1 in range(r) and grid[i + 1][j] < current_slope:
        max_path = max(max_path, 1 + grid_dfs(i + 1, j, r, c, grid, dp_array))
    if j - 1 in range(c) and grid[i][j - 1] < current_slope:
        max_path = max(max_path, 1 + grid_dfs(i, j - 1, r, c, grid, dp_array))
    if j + 1 in range(c) and grid[i][j + 1] < current_slope:
        max_path = max(max_path, 1 + grid_dfs(i, j + 1, r, c, grid, dp_array))

    dp_array[i][j] = max_path
    return dp_array[i][j]

if __name__=="__main__":

    r, c = map(int, input().split())

    ski_map = [[None for _ in range(c)] for _ in range(r)]

    for i in range(r):
        ski_map[i] = list(map(int, input().split()))

    dp_array = [[-1 for _ in range(c)] for _ in range(r)]

    #Search for longest length chain from all nodes
    curr_max = 0
    for i in range(r):
        for j in range(c):
            curr_max = max(curr_max, grid_dfs(i, j, r, c, ski_map, dp_array))

    print(curr_max)