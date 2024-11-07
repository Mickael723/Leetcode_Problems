def findTargetStair():
    stairNum = input()
    stairs = []
    # MO: fill in stair list
    n = 0
    while n < int(stairNum):
        stairs.append(int(input()))
        n += 1
    #MO: Search for discrepency
    stairDifferences = []
    heights = {}
    for i in range(len(stairs) - 1):
        difference = stairs[i] - stairs[i + 1]
        if difference not in heights:
            heights[difference] = 1
        else:
            heights[difference] += 1
        stairDifferences.append(difference)

    trueDifference = int(max(zip(heights.values(), heights.keys()))[1])

    for i in range(len(stairDifferences)):
        if stairDifferences[i] != trueDifference and i == 0:
            #Edge case: look at next difference
            if stairDifferences[i + 1] != trueDifference:
                return i + 2
            return i + 1
        if stairDifferences[i] != trueDifference:
            return i + 2    #MO: adjust to position number instead of index
    return -1

def main():
    print(findTargetStair())

if __name__=="__main__":
    main()