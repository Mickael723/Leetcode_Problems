from collections import defaultdict
import heapq
import math
if __name__=="__main__":

    n,m = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(m):
        src_loc, dest_loc, num_bumps, distance = map(int, input().split())
        #Key:source node, Value: destination node, bump_cost, distance
        graph[src_loc].append((dest_loc,num_bumps,distance))
        graph[dest_loc].append((src_loc,num_bumps,distance))
       
    #Run dijkstra's algorithm
    bump_distances = [(math.inf, math.inf) for _ in range(n)]
    bump_distances[0] = (0,0)

    queue = []
     
    #Nodes inserted to queue as (bump_cost, distance, node_id)
    heapq.heappush(queue, (0,0,0))
    while queue:
        u_bump_cost, u_dist, u = heapq.heappop(queue)

        if (u_bump_cost, u_dist) > bump_distances[u]:
            continue
        for neighbor, neighbor_cost, neighbor_dist in graph[u]:
            
            new_cost = u_bump_cost + neighbor_cost
            new_dist = u_dist + neighbor_dist
            #Push the min distance found
            if (new_cost, new_dist) < bump_distances[neighbor]:
                bump_distances[neighbor] = (new_cost, new_dist)
                heapq.heappush(queue, (new_cost, new_dist, neighbor))

    final_bumps, final_dist = bump_distances[n-1]
    print(f"{final_bumps} {final_dist}")
            
    
    
    

