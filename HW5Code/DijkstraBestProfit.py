import heapq
import math
from collections import deque

if __name__== "__main__":

    # Get input
    num_cities, num_roads = tuple(map(int, input().split()))
    city_selling_prices = []
    for i in range(num_cities):
        city_selling_prices.append(int(input()))

    # Using an edge list for simplicity
    edges = []
    for i in range(num_roads):
        city_x, city_y, cost = tuple(map(int, input().split()))
        # Need to add each edge twice for bidirectionality
        edges.append((city_x, city_y, cost))
        edges.append((city_y, city_x, cost))
    edges.sort()

    # Perform Dijkstra
    tentative_distances = [math.inf] * num_cities
    tentative_distances[0] = 0
    visited_nodes = set()
    queue = []
    edges = deque(edges)
    heapq.heappush(queue, 0)
    while len(queue) != 0:
        current_node = heapq.heappop(queue)
        visited_nodes.add(current_node)
        for city_x, city_y, cost in edges:
            if current_node == city_x and city_y not in visited_nodes:
                tentative_distances[city_y] = min(tentative_distances[city_y], 
                                               tentative_distances[city_x] + cost)
                heapq.heappush(queue, city_y)
        edges.popleft() # Shorten the list of edges to parse through on the next run
 
    # Calculate the best profit
    max_profit = 0
    for i in range(num_cities):
        profit = city_selling_prices[i] - 2 * tentative_distances[i]
        max_profit = max(max_profit, profit)
 
    print(max(0, max_profit))