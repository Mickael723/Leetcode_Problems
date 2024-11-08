if __name__== "__main__":

    n = int(input())
    sequence = list(map(int, input().split()))
    
    lds_list = [-1] * (n + 1)

    def get_lds(i: int):
        
        #MO: Return memoized value if previously calculated
        if lds_list[i] != -1: return lds_list[i]

        current_best = 1

        #MO: Calculate the lds for every possible dss in the list
        for j in range(i):
            if sequence[j] > sequence[i]:
                current_best = max(current_best, 1 + get_lds(j))
        
        #MO: Memoize result
        lds_list[i] = current_best
        return lds_list[i]

    #MO: Compute LDS for every element in the list
    true_lds = max(get_lds(i) for i in range(n))
    print(true_lds)
    

        
    
    
         




    
