import heapq
import math
from collections import defaultdict

if __name__== "__main__":

    # Get input
    num_cities, num_roads = tuple(map(int, input().split()))
    city_selling_prices = []
    adjacency_list = defaultdict(list)
    for i in range(num_cities):
        city_selling_prices.append(int(input()))
    # Using an adjacency list for simplicity
    for i in range(num_roads):
        city_x, city_y, cost = tuple(map(int, input().split()))
        # Need to add each edge twice for bidirectionality
        adjacency_list[city_x].append((city_y, cost))
        adjacency_list[city_y].append((city_x, cost))
    
    # Perform Dijkstra
    tentative_distances = [math.inf] * num_cities
    tentative_distances[0] = 0
    visited_nodes = set()
    queue = []
    heapq.heappush(queue, 0)
    while len(queue) != 0:
        current_node = heapq.heappop(queue)
        visited_nodes.add(current_node)
        for path in adjacency_list[current_node]:
            if path[0] not in visited_nodes:
                tentative_distances[path[0]] = min(tentative_distances[path[0]], 
                                               tentative_distances[current_node] + path[1])
                heapq.heappush(queue, path[0])
    # Calculate the best profit
    profits = []
    for i in range(num_cities):
        profits.append(city_selling_prices[i] - (2 * tentative_distances[i]))
    max_profit = max(profits)
    if max_profit < 0:
        print(0)
    else:
        print(max_profit)


    
    





    
    
    