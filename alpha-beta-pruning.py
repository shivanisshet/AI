def alpha_beta(node, depth, alpha, beta, maximizing):

    if depth == 0:
        return node

    if maximizing:
        value = float('-inf')

        for child in node:
            value = max(value, alpha_beta(
                child, depth-1, alpha, beta, False))

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in node:
            value = min(value, alpha_beta(
                child, depth-1, alpha, beta, True))

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value


# User input
n = int(input("Enter number of leaf nodes: "))

values = list(map(int, input("Enter leaf node values: ").split()))

tree = []

for i in range(0, n, 2):
    tree.append(values[i:i+2])

result = alpha_beta(tree, 2, float('-inf'),
                    float('inf'), True)

print("Optimal value:", result)