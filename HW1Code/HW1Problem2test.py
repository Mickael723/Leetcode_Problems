import fileinput

def getInput():
    inputs = fileinput.input(files=('HW1Code/hw1p2testtext.txt'))

    #targetMatch = (input("First Line:") + input("Second Line:"))
    targetMatch = (next(inputs).strip() + next(inputs).strip())
    i = 0
    fruitMap = []
    while i < 5:
        #fruitMap.append(input("MapInput:"))
        fruitMap.append(next(inputs).strip())
        i += 1
    return targetMatch, fruitMap    
    
def findMatchingFruit(targetMatch: str, fruitMap: list):
    firstPairFound = False
    firstPair = tuple()
    secondPair = tuple()
    row = 0
    column = 0
    while row < 4:
        while column < 5:
            #print("Looking at: " + fruitMap[row][column])
            if (fruitMap[row][column] == targetMatch[0] and fruitMap[row][column + 1] == targetMatch[1] and
                fruitMap[row + 1][column] == targetMatch[2] and fruitMap[row + 1][column + 1] == targetMatch[3]):
                if firstPairFound == False: 
                    firstPair = (row, column)
                    firstPairFound = True
                else: 
                    secondPair = (row, column)
                    return firstPair, secondPair
            column += 1
        column = 0
        row += 1
    return (-1,-1), (-1,-1)

def main():
    targetMatch, fruitMap = getInput()
    print(targetMatch)
    print(fruitMap)
    firstPair, secondPair = findMatchingFruit(targetMatch, fruitMap)
    print(*firstPair)
    print(*secondPair)
    return
if __name__=="__main__":
    main()