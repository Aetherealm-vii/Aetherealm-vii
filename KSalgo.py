import math

def place_nodes(num_nodes, r_0):
    """
    Generate node positions based on the Krystal Spiral geometry.
    :param num_nodes: Number of nodes to place.
    :param r_0: Initial radius.
    :return: List of node (x, y) coordinates.
    """
    node_positions = []
    for i in range(num_nodes):
        theta = i * 45  # Increment angle by 45 degrees
        r = r_0 * (2 ** (theta / 90))  # Spiral radius formula
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        node_positions.append((x, y))
    return node_positions

# Example Usage
nodes = place_nodes(10, 1)
print(nodes)
