import math

# Define a simple Node class for demonstration purposes
class Node:
    def __init__(self, value=None, children=None):
        self.value = value  # heuristic value if leaf node
        self.children = children or []  # list of child nodes

    def is_terminal(self):
        # Node is terminal if it has no children
        return len(self.children) == 0

    def evaluate(self):
        # Return heuristic value for terminal nodes
        return self.value

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    # Base case: if depth is 0 or node is terminal, return its heuristic value
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        value = -math.inf
        for child in node.children:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                # Beta cut-off
                break
        return value
    else:
        value = math.inf
        for child in node.children:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                # Alpha cut-off
                break
        return value


# Example usage:
# Constructing a sample game tree manually (leaf nodes have heuristic values)
leaf1 = Node(value=3)
leaf2 = Node(value=5)
leaf3 = Node(value=6)
leaf4 = Node(value=9)
leaf5 = Node(value=1)
leaf6 = Node(value=2)
leaf7 = Node(value=0)
leaf8 = Node(value=-1)

# Intermediate nodes with children
node1 = Node(children=[leaf1, leaf2])
node2 = Node(children=[leaf3, leaf4])
node3 = Node(children=[leaf5, leaf6])
node4 = Node(children=[leaf7, leaf8])

# Root node with children
root = Node(children=[node1, node2, node3, node4])

# Run alpha-beta pruning algorithm on this tree
optimal_value = alpha_beta(root, depth=3, alpha=-math.inf, beta=math.inf, maximizing_player=True)
print("Optimal value (with Alpha-Beta Pruning):", optimal_value)

