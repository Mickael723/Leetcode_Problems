if __name__ == "__main__":

    # Initialize
    total_stair_len = int(input())
    stair_heights = []
    for i in range(total_stair_len):
        stair_heights.append(int(input()))
    
    height_diffs = []
    for i in range(total_stair_len - 1):
        height_diffs.append(stair_heights[i] - stair_heights[i + 1])
    
    # Get most common elem
    height_mode = max(set(height_diffs), key=height_diffs.count)

    found = False
    #Check heights to find problem index
    for i in range(len(height_diffs) - 1):
        if height_diffs[i] != height_mode:
            #Case 1: Bad stair is in middle of list
            if height_diffs[i + 1] != height_mode:
                print(i + 2)
                found = True
                break
            #Case 2: Bad stair is first in list
            elif (height_diffs[i + 1] == height_mode) and i == 0:
                print(i + 1)
                found = True
                break
    #Case 3: Bad stair is last in list
    if found == False:
        print(total_stair_len)
        
    

    
