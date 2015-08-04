from collections import deque
def dfs(graph,start,visited=[]):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(graph,i,visited)
    return visited

def bfs(graph,start):
    visited=[]
    q=deque()
    q.append(start)
    while len(q)>0:
        i=q.popleft()
        if i in visited:
            continue
        visited.append(i)
        for i in graph[i]:
            q.append(i)
    return visited
    
    

graph = {'A': ['B', 'C'],
         'B': ['A', 'D'],
         'C': ['F', 'A'],
         'D': ['B','E'],
         'E': ['D', 'F'],
         'F': ['C', 'E']}

print dfs(graph,'C')
print bfs(graph,'A')
