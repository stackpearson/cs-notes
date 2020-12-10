def csFindAllPathsFromAToB(graph):
    possiblePaths = []
    
    # will need recurison to go through graph
    pathFinder(graph, possiblePaths, 0, [])
    
    return possiblePaths
    
def pathFinder(graph, possiblePaths, currentNode, currentPath):
    currentPath.append(currentNode)
    
    
    # base case - once we've made it through every node in our adj list
    if currentNode >= len(graph) -1:
        possiblePaths.append(currentPath[:])
        currentPath.pop()
        
        return
        
    # base case - node with no neighbors
    # end current path
    if len(graph[currentNode]) == 0:
        return
        
    # iterate through all nodes in our list, recursively build up all branching paths to each neighbor
    for neighbor in graph[currentNode]:
        pathFinder(graph, possiblePaths, neighbor, currentPath)
    # pop the most recently added node to the currently path
    currentPath.pop()