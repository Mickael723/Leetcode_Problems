if __name__== "__main__":

    string_a_len, string_b_len = tuple(map(int, input().split()))

    string_a = list(map(int, input().split()))
    string_b = list(map(int, input().split()))

    #MO: Initialize Array
    solutions = [[-1]*(string_b_len + 1) for i in range(string_a_len + 1)]

    solutions[0][0] = 0

    for i in range(1, string_a_len + 1):
        solutions[i][0] = sum(string_a[:i])
    for j in range(1, string_b_len + 1):
        solutions[0][j] = sum(string_b[:j])

    #MO: Iterate backwards: Bottom Up
    for i in range(1, string_a_len + 1):
        for j in range(1, string_b_len + 1):
            #MO: If elements are the same, do nothing
            if string_a[i - 1] == string_b[j - 1]:
                solutions[i][j] = solutions[i - 1][j - 1]
            #MO: If elements are different, take tha minimum edit distance
            else:
                solutions[i][j] = min(
                    solutions[i - 1][j] + string_a[i - 1],      # Insertion
                    solutions[i][j - 1] + string_b[j - 1],      # Deletion
                    solutions[i - 1][j - 1] + abs(string_a[i - 1] - string_b[j - 1])  # Edit
                )

    print(solutions[string_a_len][string_b_len])