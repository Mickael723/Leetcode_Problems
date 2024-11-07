
def getInput():
    targetMatch = (input() + input())
    i = 0
    fruitMap = []
    while i < 5:
        fruitMap.append(input())
        i += 1
    return targetMatch, fruitMap    
    
def findMatchingFruit(targetMatch: str, fruitMap: list):
    firstPairFound = False
    firstPair = tuple()
    secondPair = tuple()
    row = 0
    column = 0
    # MO: Search 2D array for a match, do not have to search the edges due to the conditions
    while row < 4:
        while column < 5:
            if (fruitMap[row][column] == targetMatch[0] and fruitMap[row][column + 1] == targetMatch[1] and
                fruitMap[row + 1][column] == targetMatch[2] and fruitMap[row + 1][column + 1] == targetMatch[3]):
                #MO: Flag is here to make sure we only stop searching once 2 pairs are found
                if firstPairFound == False: 
                    firstPair = (row, column)
                    firstPairFound = True
                else: 
                    secondPair = (row, column)
                    return firstPair, secondPair
            column += 1
        column = 0
        row += 1
    #MO: Due to conditions this should never be reached but do not want to crash program
    return (-1,-1), (-1,-1)

def main():
    targetMatch, fruitMap = getInput()
    firstPair, secondPair = findMatchingFruit(targetMatch, fruitMap)
    print(*firstPair)
    print(*secondPair)
    return
if __name__=="__main__":
    main()