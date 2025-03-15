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