# Applications of Kahn's Algorithm for Topological Sorting
# Course sequencing Management of software dependencies Data processing
from collections import deque

def topological_sort(adj, V):
    # Vector to store indegree of each vertex
    indegree = [0] * V
    for i in range(V):
        for vertex in adj[i]:
            indegree[vertex] += 1

    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        # Decrease indegree of adjacent vertices as the current node is in topological order 
        for adjacent in adj[node]:
            indegree[adjacent] -= 1
            # If indegree becomes 0, push it to the queue
            if indegree[adjacent] == 0:
                q.append(adjacent)

    # Check for cycle
    if len(result) != V:
        print("Graph contains cycle!")
        return []
    return result
    
if __name__ == '__main__':
    n = 6

    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5]]

    adj = [[] for _ in range(n)]

    for edge in edges:
        adj[edge[0]].append(edge[1])

    print("Topological sorting of the graph:", end = " ")
    result = topological_sort(adj, n)

    for vertex in result:
        print(vertex, end = " ")