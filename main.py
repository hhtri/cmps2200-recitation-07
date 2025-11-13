from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        current_node = frontier.pop()
        # look at all its neighbors
        for neighbor in graph[current_node]:
            # if this neighbor is new, record it and add to frontier
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)

    return result





def connected(graph):
    # If the graph is empty, then we treat it as connected
    if len(graph) == 0:
        return True
    start = next(iter(graph)) # Pick an arbitrary starting node
    reach = reachable(graph, start) # Find all nodes reachable from that start node
    return len(reach) == len(graph) # The graph is connected if we reached every node





def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            # this node starts a new component
            reachable_nodes = reachable(graph, node)
            visited.update(reachable_nodes)
            count += 1

    return count

