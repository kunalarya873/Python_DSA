# BFS
graph = {
    '5': ['4', '3', '2'],
    '4': ['5', '2', '3'],
    '3': ['2', '4', '5', '1'],
    '2': ['4', '5', '3', '1'],
    '1': ['3', '2']
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("output of bfs")
bfs(visited, graph, '5')
print()


# DFS

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': ['9'],
    '4': ['9'],
    '8': ['9'],
    '9': []
}
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print('dfs output')
dfs(visited, graph, '5')
print()