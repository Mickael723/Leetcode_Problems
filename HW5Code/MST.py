import math
import heapq
from collections import defaultdict

if __name__== "__main__":

    num_devices, num_connections = tuple(map(int, input().split()))
    # Build graph
    edges = defaultdict(list)
    for i in range(num_connections):
        device_u, device_v, cost = tuple(map(int, input().split()))
        edges[device_u].append((device_v, cost))
        edges[device_v].append((device_u, cost))

    # Run Prim algorithm
    tentative_distance = [math.inf] * num_devices
    tentative_distance[0] = 0
    vertex_from = [0] * num_connections # vertex i just arrived from
    visited_vertices = set()
    queue = []
    heapq.heappush(queue, (0,0)) # push a node with a given priority and a destination
    tree = set()

    while len(tree) < (num_devices):
        _, u = heapq.heappop(queue) 
        tree = tree | {(u, vertex_from[u])} 
        visited_vertices.add(u)
        for neighbor, cost in edges[u]:
            if cost < tentative_distance[neighbor] and neighbor not in visited_vertices:
                tentative_distance[neighbor] = cost
                vertex_from[neighbor] = u
                heapq.heappush(queue, (cost, neighbor))
    
    print(sum(tentative_distance))



    