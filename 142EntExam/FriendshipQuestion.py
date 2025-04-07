if __name__=="__main__":

    #Initialize
    n = int(input())
    original_ans = str(input())
    test_ans = str(input())

    #Initialize DP array
    dp_array = [[-1] * (n + 1) for i in range(n + 1)]

    dp_array[0][0] = 0

    for i in range(1, n + 1):
        dp_array[i][0] = i
    for j in range(1, n + 1):
        dp_array[0][j] = j 

    #Try Combinations
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            #Chars are the same
            if original_ans[i-1] == test_ans[j-1]:
                dp_array[i][j] = dp_array[i-1][j-1]
            #Chars are different
            else:
                dp_array[i][j] = min(dp_array[i-1][j] + 1, #Insert
                                     dp_array[i][j-1] + 1, #Delete
                                     dp_array[i-1][j-1] + 1 #Edit
                                     )
    
    print(dp_array[n][n])