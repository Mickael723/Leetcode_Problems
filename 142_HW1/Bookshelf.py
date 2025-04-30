if __name__=="__main__":
    n, k = map(int, input().split())
    book_widths = []

    #Fill in array
    for i in range(n):
        book_widths.append(int(input()))

    #Set bounds
    lower = max(book_widths)
    upper = sum(book_widths)
    curr_best = upper

    #This function checks if you can solve the problem with length 'middle'
    def is_feasible(book_widths, middle, k):
        curr_shelves = 1
        sum = 0
        for width in book_widths:
            sum += width
            if sum <= middle:
                continue
            else:
                curr_shelves += 1
                if curr_shelves > k:
                    return False
                sum = width
        return True

    #Perform Binary Search to find the optimal solution
    while(lower <= upper):
        middle = (upper + lower) // 2
        if is_feasible(book_widths, middle, k):
            curr_best = middle
            upper = middle - 1
        else:
            lower = middle + 1
    
    print(curr_best)
        
