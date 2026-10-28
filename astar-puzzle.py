import heapq

def h(s, goal):
    return sum(s[i] != 0 and s[i] != goal[i]
               for i in range(9))

def neighbors(s):
    z = s.index(0)
    r, c = divmod(z, 3)
    result = []

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            t = list(s)
            t[z], t[j] = t[j], t[z]
            result.append(tuple(t))
    return result

def astar(start, goal):
    pq = [(h(start, goal), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, s = heapq.heappop(pq)

        if g != cost[s]:
            continue

        if s == goal:
            path = []
            while s is not None:
                path.append(s)
                s = parent[s]
            return path[::-1]

        for t in neighbors(s):
            ng = g + 1
            if ng < cost.get(t, float('inf')):
                cost[t] = ng
                parent[t] = s
                heapq.heappush(pq, (ng + h(t, goal), ng, t))
    return None

def get_state(msg):
    while True:
        try:
            s = tuple(map(int, input(msg).split()))
            if len(s) == 9 and sorted(s) == list(range(9)):
                return s
            print("Enter numbers 0 to 8 exactly once.")
        except ValueError:
            print("Enter valid integers.")

start = get_state("Enter initial state: ")
goal = get_state("Enter goal state: ")

path = astar(start, goal)

if path:
    for i, s in enumerate(path):
        print("Step", i)
        for j in range(0, 9, 3):
            print(*s[j:j+3])
        print()
    print("Total moves:", len(path) - 1)
else:
    print("No solution exists.")