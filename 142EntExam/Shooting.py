import math
if __name__=="__main__":

    #Initialize
    rounds = int(input())
    score = 0
    
    for i in range(rounds):
        x, y = tuple(map(float, input().split()))
        # Calculate Distance
        distance_from_center = math.sqrt((x ** 2) + (y ** 2))

        #Check if shot missed:
        if distance_from_center > 1:
            points = 0
        else:
        #Calculate Points
            points = math.ceil((1 - distance_from_center) * 10)
        score = score + points
    
    print(score)