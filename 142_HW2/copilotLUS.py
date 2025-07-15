if __name__ == "__main__":

    n = int(input())
    sequence = list(map(int, input().split()))
    
    #initialize dp arrays
    lds_list = [1] * n  # LDS starting at each index
    lis_list = [1] * n  # LIS ending at each index

    #Compute LIS for every element forwards
    for i in range(n):
        for j in range(i):
            if sequence[j] < sequence[i]:
                lis_list[i] = max(lis_list[i], lis_list[j] + 1)

    #Compute LDS for every element backwards
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if sequence[j] < sequence[i]:
                lds_list[i] = max(lds_list[i], lds_list[j] + 1)

    # Find the maximum LUS by combining LIS and LDS for all peaks
    max_lus = 0
    for i in range(n):
        max_lus = max(max_lus, lis_list[i] + lds_list[i] - 1)

    print(lis_list)
    print(lds_list)
    print(max_lus)