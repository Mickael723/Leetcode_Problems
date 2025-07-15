if __name__== "__main__":

    n = int(input())
    sequence = list(map(int, input().split()))
    
    lds_list = [-1] * (n + 1)
    lis_list = [-1] * (n + 1)

    def get_lds(i: int):
        
        #MO: Return memoized value if previously calculated
        if lds_list[i] != -1: return lds_list[i]

        current_best = 1

        #MO: Calculate the lds for every possible dss in the list
        for j in range(i + 1, n):
            if sequence[j] < sequence[i]:
                current_best = max(current_best, 1 + get_lds(j))
        
        #MO: Memoize result
        lds_list[i] = current_best
        return lds_list[i]
    
    def get_lis(i: int):
        
        #MO: Return memoized value if previously calculated
        if lis_list[i] != -1: return lis_list[i]

        current_best = 1

        #MO: Calculate the lis for every possible iss in the list
        for j in range(i):
            if sequence[j] < sequence[i]:
                current_best = max(current_best, 1 + get_lis(j))
        
        #MO: Memoize result
        lis_list[i] = current_best
        return lis_list[i]
    
    #Compute LIS forwards
    for i in range(n):
        get_lis(i)
    #Compute LDS backwards
    for j in range(n-1,-1,-1):
        get_lds(j)

    #Compute the max LUS by comparing compatibale values in both dp arrays
    max_lus = lis_list[0] + lds_list[0] - 1
    for i in range(n):
        if lis_list[i] + lds_list[i] - 1 > max_lus:
            max_lus = lis_list[i] + lds_list[i] - 1

    print(max_lus)