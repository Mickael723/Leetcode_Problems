import heapq
import math
from collections import defaultdict
 
if __name__ == "__main__":
 
    # Get input
    num_cities, num_roads = map(int, input().split())
    city_selling_prices = [int(input()) for _ in range(num_cities)]
 
    # Using adjacency list
    adjacency_list = {}  # Default dict of lists for edges
 
    # Count the number of edges out of each node
    for _ in range(num_roads):
        city_x, city_y, cost = map(int, input().split())
        if city_x not in adjacency_list:
            adjacency_list[city_x] = []
        if city_y not in adjacency_list:
            adjacency_list[city_y] = []
        adjacency_list[city_x].append((city_y, cost))
        adjacency_list[city_y].append((city_x, cost))
 
    # Perform Dijkstra
    tentative_distances = [math.inf] * num_cities
    tentative_distances[0] = 0
    queue = []
    visited_nodes = [False] * num_cities # Not a set because memory lol
    heapq.heappush(queue, (0,0)) # distance and node
 
    while queue:
        u_cost, u = heapq.heappop(queue)
        if visited_nodes[u]:
            continue
        visited_nodes[u] = True
        for neighbor, cost in adjacency_list[u]:
            if visited_nodes[neighbor]:
                continue
            new_distance = u_cost + cost
            if new_distance < tentative_distances[neighbor]:
                tentative_distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
        del adjacency_list[u] # Clean up nodes we don't need bc strict af memory
 
    # Calculate the best profit
    max_profit = 0
    for i in range(num_cities):
        profit = city_selling_prices[i] - 2 * tentative_distances[i]
        max_profit = max(max_profit, profit)
 
    print(max(0, max_profit))