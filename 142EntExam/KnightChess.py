from collections import deque

def checkValidMove(x, y):
        #Make sure x and y are on the board and not occupied
        if x > 0 and x < 9 and y > 0 and y < 9 and (x,y) not in occupied_coords:
            return True
        return False

if __name__=="__main__":

    #Translate Letters to Numbers
    letter_key = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    #Read Input
    board_num = 0
    while(True):
        occupied_len = int(input())
        if occupied_len == -1:
            break
        board_num += 1
        occupied_spaces = input().split()
        occupied_coords = set()
        for space in occupied_spaces:
            occupied_coords.add((letter_key[space[0]], int(space[1])))

        start_space, end_space = input().split()
        start_coords = letter_key[start_space[0]], int(start_space[1])
        end_coords = letter_key[end_space[0]], int(end_space[1])
        
        #Create Graph
        dx = [-2, -1, 1, 2, -2, -1, 1, 2] #Movements in x direction
        dy = [-1, -2, -2, -1, 1, 2, 2, 1] #Movements in y direction

        queue = deque()
        visited = set()
        solution_found = False #For very specific case where a solution is found when the queue is empty
        queue.append((start_coords, 0))
        while queue:
            coord, counter = queue.popleft()
            visited.add(coord)
            #Check if node is valid
            if not checkValidMove(coord[0],coord[1]):
                continue
            #Check if node is goal
            if coord[0] == end_coords[0] and coord[1] == end_coords[1]:
                 print(f"Board {board_num}: {counter} moves")
                 solution_found = True
                 break
            #Add nodes to queue
            for i in range(len(dx)):
                if (not checkValidMove(coord[0] + dx[i],coord[1] + dy[i])) or (coord[0] + dx[i],coord[1] + dy[i]) in visited:
                    continue
                else:
                    queue.append(((coord[0] + dx[i], coord[1] + dy[i]), counter + 1))
        #Edge Case:End goal unreachable
        if not queue and not solution_found:
            print(f"Board {board_num}: not reachable")
                
    
    