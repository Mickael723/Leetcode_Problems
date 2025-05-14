

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
    dp_array = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        dp_array[0][i] = dp_array[0][i - 1] + prices[reverse_str[i-1]]
        dp_array[i][0] = dp_array[i - 1][0] + prices[initial_str[i-1]]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            #If elements are the same, do nothing
            if initial_str[i-1] == reverse_str[j-1]:
                dp_array[i][j] = dp_array[i - 1][j - 1]
            #If elements are different, take tha minimum edit distance
            else:
                dp_array[i][j] = min(
                    dp_array[i-1][j] + prices[initial_str[i-1]],      # Left Insertion
                    dp_array[i][j-1] + prices[initial_str[j-1]]         # Right Insertion
                )

    result = 9999999
    i = n 
    j = 0
    while i >= 0:
        result = min(result, dp_array[i][j])
        if i < n:
            result = min(result, dp_array[i + 1][j])
        if i > 0:
            result = min(result, dp_array[i - 1][j])
        i -= 1
        j += 1
    
    print(result)
            

    
        

        