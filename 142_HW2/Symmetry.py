
if __name__=="__main__":
    n, k = map(int, input().split())

    #create dictionary of prices
    prices = {}
    first_letter = ord('a')
    for i in range(k):
        prices[chr(first_letter + i)] = int(input())
    
    initial_str = input()
    reverse_str = initial_str[::-1]

    #initialize dp array
    dp_array = [[-1] * (n + 1) for _ in range(n + 1)]
    dp_array[0][0] = 0
    for i in range(1, n+1):
        dp_array[0][i] = 0
        dp_array[i][0] = 0
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            #If elements are the same, do nothing
            if initial_str[i-1] == reverse_str[j-1]:
                dp_array[i][j] = dp_array[i - 1][j - 1]
            #If elements are different, take tha minimum edit distance
            else:
                dp_array[i][j] = min(
                    dp_array[i-1][j] + prices[initial_str[i-1]],      # Insert string[i] 
                    dp_array[i][j-1] + prices[initial_str[n - j]],         # Insert string[j] 
                )

    # for list in dp_array:
    #     print(list)
    print(dp_array[n][n])
            

    
        

        