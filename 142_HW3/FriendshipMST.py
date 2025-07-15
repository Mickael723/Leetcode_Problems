import heapq
import math

if __name__=="__main__":

    r,c = map(int, input().split())

    graph = [[0] * c for _ in range(r)]

    for row in range(r):
        graph[row] = list(map(int, input().split()))
    
    
    #Run Prims Algorithm
    distances = [[math.inf for _ in range(c)] for _ in range(r)]
    mst_cost = 0
    visited = set()
    queue = []
    #Nodes inserted to queue as (cost, coordinate pair)
    heapq.heappush(queue, (0, (0, 0)))

    while queue:
        cost, u = heapq.heappop(queue)
        if u in visited:
            continue
        visited.add(u)
        
        mst_cost += cost

        neighbors = []
        neighbors.append((u[0]-1,u[1]))
        neighbors.append((u[0],u[1]-1))
        neighbors.append((u[0]+1,u[1]))
        neighbors.append((u[0],u[1]+1))

        for vertex in neighbors:
            #Check neighbor ranges
            if vertex[0] not in range(0,r) or vertex[1] not in range(0,c):
                continue
            #Compute the cheapest cost to create the new edge
            edge_cost = min(graph[u[0]][u[1]], graph[vertex[0]][vertex[1]])
            if edge_cost < distances[vertex[0]][vertex[1]] and vertex not in visited:
                distances[vertex[0]][vertex[1]] = edge_cost
                heapq.heappush(queue, (edge_cost,vertex))

    #Print total cost
    print(mst_cost)

