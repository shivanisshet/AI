# 8 Puzzle using Iterative Deepening Search (IDS)
# 0 represents the blank space


# Generate possible positions of blank space
def get_moves(state):

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = []

    # Move Up
    if row > 0:
        moves.append(zero - 3)

    # Move Down
    if row < 2:
        moves.append(zero + 3)

    # Move Left
    if col > 0:
        moves.append(zero - 1)

    # Move Right
    if col < 2:
        moves.append(zero + 1)

    return moves


# Move blank space
def make_move(state, new_zero):

    zero = state.index(0)

    new_state = list(state)

    new_state[zero], new_state[new_zero] = \
        new_state[new_zero], new_state[zero]

    return tuple(new_state)


# Depth Limited DFS
def depth_limited_dfs(state, goal, depth, path):

    # Goal found
    if state == goal:
        return path

    # Depth limit reached
    if depth == 0:
        return None

    # Try all possible moves
    for new_zero in get_moves(state):

        new_state = make_move(state, new_zero)

        # Avoid states already present in current path
        if new_state not in path:

            result = depth_limited_dfs(
                new_state,
                goal,
                depth - 1,
                path + [new_state]
            )

            if result is not None:
                return result

    return None


# Iterative Deepening Search
def ids(start, goal, max_depth):

    for depth in range(max_depth + 1):

        print("Searching at depth:", depth)

        solution = depth_limited_dfs(
            start,
            goal,
            depth,
            [start]
        )

        if solution is not None:
            return solution

    return None


# Display solution
def display_solution(solution):

    if solution is None:
        print("\nNo solution found.")
        return

    print("\nSolution found!")
    print("Number of moves:", len(solution) - 1)

    for i, state in enumerate(solution):

        print("\nStep", i)

        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

print("================================")
print("     8 PUZZLE USING IDS")
print("================================")

print("\nEnter Initial State")
print("Use 0 for blank space.")

start = tuple(
    map(int, input("Enter 9 numbers: ").split())
)

print("\nEnter Goal State")

goal = tuple(
    map(int, input("Enter 9 numbers: ").split())
)

max_depth = int(
    input("\nEnter maximum depth: ")
)


# Run IDS
solution = ids(
    start,
    goal,
    max_depth
)


# Display result
display_solution(solution)