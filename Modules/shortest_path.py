def selectBestCandidate(distances, visited):
    dist = float('inf')
    next = None
    for i in range(len(distances)):
        if not visited[i] and dist > distances[i]:
            dist = distances[i]
            next = i
    return next, dist

def typeOutput(distances, start):
    output = f'node {start}: ['
    for i in range(len(distances)):
        output += f'{i}:{distances[i]}'
        if i != len(distances) - 1:
            output += ', '
    output += ']\n'
    return output


def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    visited = [False] * n
    actual = start
    visited[actual] = True
    distances[actual] = 0

    for end in graph.get(actual):
        distances[end]=graph.get(actual).get(end).get('weight')

    for _ in range(n-1):
        actual, dist = selectBestCandidate(distances, visited)
        visited[actual] = True
        for end in graph.get(actual):
            if not visited[end]:
                distances[end] = min(distances[actual] + graph.get(actual).get(end).get('weight'), distances[end])

    output = typeOutput(distances, start)
    return output
