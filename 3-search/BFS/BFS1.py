
def BFS(arr):
    vertices_number = len(arr)
    result = []
    visited = [False] * vertices_number
    origin = 0
    from collections import deque

    que = deque()
    visited[origin] = True
    que.append(origin)

    while que:
        current = que.popleft()
        result.append(current)

        for vertice in arr[current]:
            if not visited[vertice]:
                visited[vertice] = True
                que.append(vertice)
    return result

print(BFS([[1,2], [0,2,3], [0,4], [1,4], [2,3]]))