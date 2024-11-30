Graph_nodes = {
    "A": [("B", 6), ("F", 3)],
    "B": [("C", 3), ("D", 2)],
    "C": [("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 8)],
    "E": [("I", 5), ("J", 5)],
    "F": [("G", 1), ("H", 7)],
    "G": [("I", 3)],
    "H": [("I", 2)],
    "I": [("E", 5), ("J", 3)],
}

def get_neighbors(v):
    # Return neighbors of node v, or None if not found
    return Graph_nodes.get(v, None)

def h(n):
    # Heuristic distances
    H_dist = {
        "A": 10,
        "B": 8,
        "C": 5,
        "D": 7,
        "E": 3,
        "F": 6,
        "G": 5,
        "H": 3,
        "I": 1,
        "J": 0
    }
    return H_dist.get(n, float('inf'))  # Default to inf if no heuristic for node

def A_star_algo(start_node, stop_node):
    open_set = {start_node}  # Open set is initialized with the start node
    closed_set = set()  # Closed set is empty at the 


