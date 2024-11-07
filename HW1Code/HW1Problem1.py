def findCorrectDoll():
    numSwaps = int(input())
    #last significant position
    lsp = 3
    while numSwaps > 0:
        newPosition = input().split()
        if int(newPosition[1]) == lsp:
            lsp = int(newPosition[0])
        elif int(newPosition[0]) == lsp:
            lsp = int(newPosition[1])
        numSwaps -= 1
    return lsp

def main():
    print(findCorrectDoll())
if __name__=="__main__":
    main()