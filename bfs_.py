#!/user/bin/python3
"""
Breadth-first search is a search in python,
is algorithm used to traverse a graph or a tree.
"""


graph = {
  '5': ['3', '7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': []
}

visited = []
queue = []


def breast_first_search(visited, graph, node):
    """
    Traves a tree looking for empty nodes

    Args:
        visited: list of visited nodes in graph.
        graph: dictionary of tree.
        node: Head of the tree.
    """
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


print("Following is the Breadth-First Search")
breast_first_search(visited, graph, '5')
