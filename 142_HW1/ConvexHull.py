import math
#Computing convex hull using Jarvis's Algorithm
def convexHull(coordinates: list):

    #Initialize starting point
    start = min(coordinates, key=lambda point: (point[0]))
    hull = []
    hull.append(start)
    previous_point = start

    while True:
        candidate = None
        #Loop through all points
        for point in coordinates:
            if point == previous_point:
                continue
            if candidate is None:
                candidate = point
                continue
            
            #Calculate the cross product to determine if adding the new point moves the polygon in a clockwise direction
            cross_product = ((candidate[0] - previous_point[0]) * (point[1] - previous_point[1]) - 
                                (candidate[1] - previous_point[1]) * (point[0] - previous_point[0]))
            #If points are colinear, add the farthest point to the hull
            if cross_product == 0 and math.dist(previous_point, candidate) < math.dist(previous_point, point):
                candidate = point
            #Moved clockwise with the new point so add it to the hull
            elif cross_product > 0:
                candidate = point

        #End Condition   
        if candidate == start: break

        hull.append(candidate)
        previous_point = candidate

    return hull


if __name__=="__main__":

    coordinates = []
    for i in range(4):
        coordinates.append(tuple(map(int, input().split())))
    
    hull = convexHull(coordinates)

    #Check that its not just a straight line:
    if len(hull) <= 2:
        print(0.0)
    else:
        #Compute area with shoelace formula
        area = 0
        for i in range(len(hull)):
            x1, y1 = hull[i]
            x2, y2 = hull[(i + 1) % len(hull)]
            area += (x1 * y2) - (x2 * y1)
        print(abs(area) / 2)