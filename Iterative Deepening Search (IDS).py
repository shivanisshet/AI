
def DLS(graph, node, goal, depth):
    if node == goal:
        return True

    if depth <= 0:
        return False

    for neighbour in graph[node]:
        if DLS(graph, neighbour, goal, depth - 1):
            return True

    return False


def IDS(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print("Searching at depth:", depth)

        if DLS(graph, start, goal, depth):
            print("Goal found:", goal)
            return True

    print("Goal not found")
    return False


# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Execute IDS
IDS(graph, 'A', 'G', 3)
