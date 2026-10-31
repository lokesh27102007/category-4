graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

start = 'A'
goal = 'E'

front_start = [start]
front_goal = [goal]

visited_start = {start}
visited_goal = {goal}

while front_start and front_goal:
    node = front_start.pop(0)

    if node in visited_goal:
        print("Path found")
        break

    for neighbor in graph[node]:
        if neighbor not in visited_start:
            visited_start.add(neighbor)
            front_start.append(neighbor)

    node = front_goal.pop(0)

    if node in visited_start:
        print("Path found")
        break

    for neighbor in graph[node]:
        if neighbor not in visited_goal:
            visited_goal.add(neighbor)
            front_goal.append(neighbor)
else:
    print("Path not found")
