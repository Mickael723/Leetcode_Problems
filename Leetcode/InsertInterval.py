def insert(intervals: list, newInterval: list) -> list:

    updated_intervals = []
    
    inserted = False

    for interval in intervals:
        if interval[1] < newInterval[0]:
            updated_intervals.append(interval)
            continue
        if interval[0] > newInterval[1]:
            if not inserted:
                updated_intervals.append(newInterval)
                inserted = True
            updated_intervals.append(interval)
            continue
        
        newInterval[0] = min(newInterval[0], interval[0])
        newInterval[1] = max(newInterval[1], interval[1])
    
    if not inserted:
        updated_intervals.append(newInterval)
    
    return updated_intervals
        

if __name__=='__main__':
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(insert([[1,3],[6,9]], [2,5]))
    print(insert([], [2,5]))
    print(insert([[1,5]], [2,3]))


        
        

