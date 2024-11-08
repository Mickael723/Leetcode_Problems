
if __name__== "__main__":

    weightBudget, numItems = tuple(map(int, input().split()))
    weightList = []
    valueList = []
    count = 0
    while count < numItems:
        weight, value = tuple(map(int, input().split()))
        weightList.append(weight)
        valueList.append(value)
        count += 1


    s = [[-1]*(weightBudget + 1) for i in range(numItems + 1)] #MO: Initialize s array
    
    def knapSack(numItems, budget):
        #MO: Check if this combo has been computed
        if s[numItems][budget] != -1: return s[numItems][budget] 

        if budget == 0 or numItems == 0: return 0
        #MO: If item has a weight larger than the budget, can skip iteration
        if weightList[numItems - 1] > budget:
            currentBest = knapSack(numItems - 1, budget)

        else:
            currentBest = max(knapSack(numItems - 1, budget), knapSack(numItems - 1, budget - weightList[numItems - 1]) + valueList[numItems - 1])
       
        s[numItems][budget] = currentBest #MO: Memoize
        return currentBest
    
    print(knapSack(numItems, weightBudget))
    