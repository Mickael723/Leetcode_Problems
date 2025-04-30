import math

if __name__=="__main__":

    #This function uses a tree traversal to check all the geometric conditions of x and y to determine if its a possible spot
    def check_coords(x,y,n_window_x_coords,s_window_x_coords, c1, c2, rx, ry):
        
        #Condition 1: Simply check that x,y is a greater distance than c1 and shorter than c2 from radiator
        distance = math.dist([x,y], [rx,ry])
        if distance < c1 or distance > c2:
            #print(f"{x},{y} failed condition 1!")
            return False

        #Condition 2:
        #Check that x and y fall in between two boundaries by using y to compute the x boundary
        left_boundary = (n_window_x_coords[0] + (s_window_x_coords[0] - n_window_x_coords[0]) * ((500 - y)/500)) 
        right_boundary = (n_window_x_coords[1] + (s_window_x_coords[1] - n_window_x_coords[1]) * ((500 - y)/500)) 

        #Check the boundaries
        if x < left_boundary or x > right_boundary:
            #print(f"{x},{y} failed condition 2!")
            return False
        
        #Condition 3: Check that x and y fall into the predetermined viewing area of the TV

        #First y is not directly in front of the TV
        if y < 300 and y > 200:
            #print(f"{x},{y} failed condition 3, in front of tv!")
            return False
        #Then x is not on the wrong side of the angle
        if x > 300:
            if (y >= (800 - x)) or (y <= (x - 300)):
                #print(f"{x},{y} failed condition outside of angle!")
                return False

        #All conditions met therefore. coordinates are good
        return True

        
    c1,c2,rx,ry = map(int, input().split())
    s, n = map(int, input().split())
    n_window_x_coords = (n, n+100)
    s_window_x_coords = (s, s+100)

    num_queries = int(input())

    for i in range(num_queries):
        x,y = map(int, input().split())
        ans = check_coords(x,y,n_window_x_coords,s_window_x_coords,c1,c2,rx,ry)
        if ans == True:
            print("yes")
        else:
            print("no")
