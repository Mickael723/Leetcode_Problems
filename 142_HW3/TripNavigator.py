import heapq
import math

if __name__=="__main__":

    n, t = map(int, input().split())

    #initialize graph
    graph = [[0] * n for _ in range(n)]

    for row in range(n):
        string = input()
        for i in range(n):
            if string[i] == "-":
                graph[row][i] = 1
            else:
                graph[row][i] = t + 1

    graph[0][0] = 0
    
    #Run dijkstra's algorithm
    distances = [[math.inf for _ in range(n)] for _ in range(n)]
    visited = set()
    settled = set()
    queue = []
    #Nodes inserted to queue as (cost, coordinate pair)
    heapq.heappush(queue, (0, (0, 0)))

    while queue:
        cost, u = heapq.heappop(queue)
        if u in visited:
            continue
        visited.add(u)

        neighbors = []
        neighbors.append((u[0]-1,u[1]))
        neighbors.append((u[0],u[1]-1))
        neighbors.append((u[0]+1,u[1]))
        neighbors.append((u[0],u[1]+1))

        for vertex in neighbors:
            #Check neighbor ranges
            if vertex[0] not in range(0,n) or vertex[1] not in range(0,n):
                continue
            #Push the min distance found
            distances[vertex[0]][vertex[1]] = min(distances[vertex[0]][vertex[1]], 
                                                  cost + graph[vertex[0]][vertex[1]])
            
            heapq.heappush(queue, (distances[vertex[0]][vertex[1]],vertex))
        
    print(distances[n-1][n-1])
            
    
    