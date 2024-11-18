if __name__== "__main__":

    n = int(input())
    sequence = list(map(int, input().split()))
    
    lis_list = [-1] * (n + 1)

    def get_lis(i: int):
        
        #MO: Return memoized value if previously calculated
        if lis_list[i] != -1: return lis_list[i]

        current_best = sequence[i]

        #MO: Calculate the lis for every possible iss in the list
        for j in range(i):
            if sequence[j] < sequence[i]:
                current_best = max(current_best, sequence[i] + get_lis(j))
        
        #MO: Memoize result
        lis_list[i] = current_best
        return lis_list[i]

    #MO: Compute LIS for every element in the list
    true_lds = max(get_lis(i) for i in range(n))
    print(true_lds)