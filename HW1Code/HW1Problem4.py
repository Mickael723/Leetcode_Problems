def countChocoFrogs():
    totalCards = int(input())
    cardCollectionCount = {}
    cardTypes = set()
    #MO: Push new items into the dictionary
    count = 0
    while count < totalCards:
        newCard = int(input())
        if newCard in cardCollectionCount:
            cardCollectionCount[newCard] += 1
        else:
            cardCollectionCount.update({newCard : 1})
            cardTypes.add(newCard)
        count += 1
    
    #MO: Print Items
    sortedCards = sorted(cardTypes)
    for cardType in sortedCards:
        print(str(cardType) + " " + str(cardCollectionCount[cardType]))

def main():
    countChocoFrogs()
if __name__=="__main__":
    main()