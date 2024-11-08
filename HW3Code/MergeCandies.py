import heapq

if __name__== "__main__":
    numCandies = int(input())
    count = 0
    candyBagQueue = []
    while count < numCandies:
        heapq.heappush(candyBagQueue, int(input()))
        count += 1
    candyTotal = 0
    #MO: Pop items from priority queue
    while len(candyBagQueue) >= 2:
        mergedSum = heapq.heappop(candyBagQueue) + heapq.heappop(candyBagQueue)
        candyTotal += mergedSum * 2
        heapq.heappush(candyBagQueue, mergedSum)
    print(candyTotal)

    