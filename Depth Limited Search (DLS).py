graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(node, goal, limit):
    print(node, end=" ")

    if node == goal:
        return True

    if limit <= 0:
        return False

    for neighbor in graph[node]:
        if dls(neighbor, goal, limit - 1):
            return True

    return False

if dls('A', 'E', 2):
    print("\nGoal found")
else:
    print("\nGoal not found")
