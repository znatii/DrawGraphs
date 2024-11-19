from collections import deque


def dfs_aux(graph, v, visited):
    sol = []
    visited[v] = True
    q = deque()
    q.append(v)
    while q:
        aux = q.pop()
        sol.append(aux)
        for adj in graph[aux]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)


    return sol

def dfs(graph):
    n = len(graph)
    visited = [False] * n
    sol = []

    for v in range(n):
        if not visited[v]:
            sol.extend(dfs_aux(graph, v, visited))
    return sol

def bfs_aux(graph, v, visited):
    sol = []
    visited[v] = True
    q = deque()
    q.append(v)

    while q:
        aux = q.popleft()
        sol.append(aux)
        for adj in graph[aux]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)

    return sol

def bfs(graph):
    n = len(graph)
    visited = [False] * n
    sol = []
    for v in range(n):
        if not visited[v]:
            sol.extend(bfs_aux(graph, v, visited))
    return sol