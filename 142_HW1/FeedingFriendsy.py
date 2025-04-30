if __name__=="__main__":

    t,n,m = tuple(map(int, input().split()))

    upper_intervals = []
    lower_intervals = []

    #Create list of intervals
    for i in range(n):
        upper_intervals.append(tuple(map(int, input().split())))
    max_upper = max(triple[1] for triple in upper_intervals)
    for j in range(m):
        lower_intervals.append(tuple(map(int, input().split())))
    max_lower = max(triple[1] for triple in lower_intervals)

    #Compute the length of the sweepline arrays
    max_interval = max(max_lower,max_upper)
    upper_pos_points = [0] * (max_interval + 1)
    lower_pos_points = [0] * (max_interval + 1)

    #Fill every element in the arrays to decide how many points to add per interval
    for triple in upper_intervals:
        for x in range(triple[0],triple[1] + 1):
            if triple[2] == 1:
                upper_pos_points[x] = 3
            else:
                upper_pos_points[x] = 1
    for triple in lower_intervals:
        for x in range(triple[0],triple[1] + 1):
            if triple[2] == 1:
                lower_pos_points[x] = 3
            else:
                lower_pos_points[x] = 1   
    
    #Sweep through both array simultaneously to compute the max # of points we can get
    point_total = 0
    for i in range(len(upper_pos_points)):
        point_total += max(upper_pos_points[i],lower_pos_points[i])
    print(point_total)
    