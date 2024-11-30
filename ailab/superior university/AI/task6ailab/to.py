from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

def bfs(graph, start):
    visited = set() 
    queue = deque([start])  
    
    while queue:
        current = queue.popleft() 
        if current not in visited:
            print(current, end=' ')  
            visited.add(current) 
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)  


graph = {
    '0': ['1', '2'],
    '1': ['3', '4'],
    '2': ['5'],
    '3': [],
    '4': ['5'],
    '5': []
}

print("BFS Traversal:")
bfs(graph, '0')  


def dfs_with_stack(start_node):
    visited = set()  
    stack = [start_node]  
    
    while stack:
        current_node = stack.pop()  
        if current_node not in visited:
            print(current_node.value, end=' ')  
            visited.add(current_node)  
            for neighbor in reversed(current_node.neighbors):
                if neighbor not in visited:
                    stack.append(neighbor) 

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

a.add_neighbor(b)
a.add_neighbor(c)
b.add_neighbor(d)
b.add_neighbor(e)
c.add_neighbor(e)

print("\nDFS Traversal:")
dfs_with_stack(a)  

