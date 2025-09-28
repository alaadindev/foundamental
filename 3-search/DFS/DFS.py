def DFS(graph, origin):
    visited = set()
    stack = [origin]
    result = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            result.append(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                stack.append(neighbor)

    return result
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 5],
    5: [4]
}
print(DFS(graph, 0))