from collections import defaultdict

if __name__=="__main__":

    n,m = map(int, input().split())

    family = defaultdict(list)
    traitors = set()

    family[0] = []

    for i in range(1,n):
        parent_val = int(input())
        family[parent_val].append(i)
        family[i].append(parent_val)
        

    for i in range(m):
        traitor = int(input())
        traitors.add(traitor)

    longest_chain = 0
    queue = []
    nodes_seen = set()

    #Run bfs on the tree
    def bfs(root):
        queue.append(root)
        this_chain = 0
        while(queue):
            current_node = queue.pop()
            if current_node in nodes_seen or current_node in traitors:
                    continue
            nodes_seen.add(current_node)
            this_chain += 1 #Add to the chain of this tree
            
            for elem in family[current_node]:
                if elem not in traitors and elem not in nodes_seen:
                    queue.append(elem)
                    
        return this_chain
    
    for node in range(n):
        if node not in nodes_seen and node not in traitors:
            longest_chain = max(longest_chain, bfs(node))
    
    print(longest_chain)
    
    
    
    