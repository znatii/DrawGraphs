
def updateComponents(connected_components, new_id, old_id):
    for i in range(len(connected_components)):
        if connected_components[i] == old_id:
            connected_components[i] = new_id

def sortCandidates(edges):
    candidates = []

    visited = [False] * len(edges)
    for i in range(len(edges)):
        for j in (edges.get(i)):
            if not visited[j]:
                candidates.append((i, j, edges.get(i).get(j).get('weight')))
        visited[i] = True
    candidates = sorted(candidates, key=lambda x: x[2])
    return candidates


def kruskal (number_nodes, edges):
    connected_components = list(range(number_nodes))
    candidates = sortCandidates(edges)
    #candidates = sorted(edges, key = lambda x : x[2])
    weight_total = 0
    edges = []

    count = number_nodes - 1
    i = 0
    while count > 0 and i < len(candidates):
        n1, n2, weight = candidates[i]
        if connected_components[n1] != connected_components[n2]:
            updateComponents(connected_components, connected_components[n1], connected_components[n2])
            edges.append((n1, n2, weight))
            weight_total += weight
            count -= 1
        i += 1
    return weight_total, edges

def selectBestCandidate(candidates, visited):
    weight = 0x3f3f3f3f
    next = 0
    for i in range(len(candidates)):
        if not visited[i] and weight > candidates[i]:
            weight = candidates[i]
            next = i
    return next, weight

def prim (graph):
    n = len(graph)
    actual = 0
    visited = [False]*n
    candidates = [0x3f3f3f3f] * n
    visited[actual] = True
    nodes = []
    nodes.append(actual)
    weight_total = 0

    for end in graph.get(actual):
        candidates[end] = graph.get(actual).get(end).get('weight')


    for _ in range (1, n):
        actual, cost = selectBestCandidate(candidates, visited)
        weight_total += cost
        nodes.append(actual)
        visited[actual] = True
        for end in graph.get(actual):
            if not visited [end]:
                candidates[end] = min(candidates[end], graph.get(actual).get(end).get('weight'))

    return weight_total, nodes