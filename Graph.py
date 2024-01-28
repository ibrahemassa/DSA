from collections import deque

def to_matrix(graph):
    size = len(graph)
    elements = sorted(graph.keys())
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    edges = []
    for element in elements:
        for adjacent in graph[element]:
            edges.append((element, adjacent))
    for edge in edges:
        f_i = elements.index(edge[0])
        s_i = elements.index(edge[1])
        matrix[f_i][s_i] = 1
    return matrix

def dfs(graph, root):
    nodes = sorted(graph.keys())
    stack = [root]
    visited = []
    node = root
    while stack:
        if node not in visited:
            visited.append(node)
        adjacent = sorted(graph[node])
        if set(adjacent).issubset(visited):
            stack.pop()
            if len(stack) > 0:
                node = stack[-1]
            else:
                continue
        else:
            rem = set(adjacent).difference(set(visited))
            first = sorted(rem)[0]
            stack.append(first)
            node = first
    return visited

def bfs(graph, root):
    q = deque([root])
    visited = [root]
    while q:
        node = q.popleft()
        adjacent = graph[node]
        rem = sorted(set(adjacent).difference(set(visited)))
        if len(rem) > 0:
            for elem in rem:
                q.append(elem)
                visited.append(elem)
    return visited

#-----Testing-----#
graph = {}
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'D']
graph['D'] = ['B', 'C']

mat = to_matrix(graph)
print(mat)
print(dfs(graph, 'A'))
print(bfs(graph, 'A'))
