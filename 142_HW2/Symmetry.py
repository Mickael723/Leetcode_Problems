
if __name__=="__main__":
    n, k = map(int, input().split())

    #Create dictionary of prices
    prices = {}
    first_letter = ord('a')
    for i in range(k):
        prices[chr(first_letter + i)] = int(input())
    
    initial_str = input()

    #Initialize dp array
    dp_array = [[0] * (n) for _ in range(n)]
    
    #Iteratively search each subsequence from i to j
    for length in range(2,n+1):
        for i in range(n - length + 1):
            j = i  + length - 1 #Get the end of the subsequence

            #If elements are the same, do nothing
            if initial_str[i] == initial_str[j]:
                dp_array[i][j] = dp_array[i + 1][j - 1]
            #If elements are different, take tha minimum edit distance
            else:
                dp_array[i][j] = min(
                    dp_array[i+1][j] + prices[initial_str[i]],      # Insert string[i] 
                    dp_array[i][j-1] + prices[initial_str[j]],         # Insert string[j] 
                )

    for list in dp_array:
        print(list)
    print(dp_array[0][n-1])
            

    
        

        