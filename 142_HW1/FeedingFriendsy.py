import heapq
import sys

if __name__=="__main__":

    t,n,m = map(int, sys.stdin.readline().split())

    #Use a generator to read in events directly and yield them when done with them
    def generate_events():
        for _ in range(n):
            start, end, glowing = map(int, sys.stdin.readline().split())
            points = 3 if glowing == 1 else 1
            yield (start, points, 0)  
            yield (end + 1, -points, 0)  

        for _ in range(m):
            start, end, glowing = map(int, sys.stdin.readline().split())
            points = 3 if glowing == 1 else 1
            yield (start, points, 1)  
            yield (end + 1, -points, 1)  

    #Sort events using generator
    events = sorted(generate_events())

    upper_active_points = 0
    lower_active_points = 0
    point_total = 0
    last_position = 0

    # Process events directly
    for position, change, layer in events:
        # Calculate points for the range between the last position and the current position
        if last_position != position:
            point_total += max(upper_active_points, lower_active_points) * (position - last_position)
            last_position = position

        # Update active points for the respective layer
        if layer == 0:
            upper_active_points += change
        else:
            lower_active_points += change

    print(point_total)
    