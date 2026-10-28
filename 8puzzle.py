
def get_moves(state):

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = []

  
    if row > 0:
        moves.append(zero - 3)

  
    if row < 2:
        moves.append(zero + 3)

  
    if col > 0:
        moves.append(zero - 1)


    if col < 2:
        moves.append(zero + 1)

    return moves


def make_move(state, new_zero):

    zero = state.index(0)

    new_state = list(state)

    new_state[zero], new_state[new_zero] = \
        new_state[new_zero], new_state[zero]

    return tuple(new_state)



def depth_limited_dfs(state, goal, depth, path):


    if state == goal:
        return path

  
    if depth == 0:
        return None

  
    for new_zero in get_moves(state):

        new_state = make_move(state, new_zero)

      
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



solution = ids(
    start,
    goal,
    max_depth
)


display_solution(solution)
