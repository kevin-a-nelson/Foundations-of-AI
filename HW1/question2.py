# Question 2
#
# Both algorithms found the shortest path however A* took longer to find it.
# This is because the F cost of all the nodes is the same since the start and end are on the corners of the graph.
# Because all nodes have the same F cost, no nodes are priotizes over another when finding the path.
# Since there are obstacles, this is not good, since some nodes bring you to the end quicker than others.

# Example input: Matrix ->
#
#  ~  ~  ~  ~  ~  ~  ~  ~  ST
#  ~  #  #  #  #  #  #  #  ~
#  ~  #  ~  ~  ~  ~  ~  #  ~
#  ~  #  ~  #  #  #  ~  #  ~
#  ~  ~  ~  #  ~  ~  ~  #  ~
#  #  #  ~  #  ~  #  #  #  ~
#  EN ~  ~  ~  #  ~  ~  ~  ~
#
# output: Matrix ->
#
# 9  8  7  6  5  4  3  2  1  0
# 10 9  8  7  6  5  4  3  2  1
# 11 10 9  8  7  6  5  4  3  2
# 12 11 10 9  8  7  6  5  4  3
# 13 12 11 10 9  8  7  6  5  4
# 14 13 12 11 10 9  8  7  6  5
# 15 14 13 12 11 10 9  8  7  6
#
# G cost is the distance of a node from the start node.
# Since the start node is ST, the G cost at [0, 8] is 0
# Since [1, 8] is one away from ST its G cost is 1

def getGCosts(nodes):
    startNode = getStartNode(nodes)

    hueristicValues = []
    for rowIdx, row in enumerate(nodes):
        rowValues = []
        for colIdx, _ in enumerate(row):
            rowDiff = abs(rowIdx - startNode[0])
            colDiff = abs(colIdx - startNode[1])
            rowValues.append(rowDiff + colDiff)
        hueristicValues.append(rowValues)
    return hueristicValues


# Example input: Matrix ->
#
#  ~  ~  ~  ~  ~  ~  ~  ~  ST
#  ~  #  #  #  #  #  #  #  ~
#  ~  #  ~  ~  ~  ~  ~  #  ~
#  ~  #  ~  #  #  #  ~  #  ~
#  ~  ~  ~  #  ~  ~  ~  #  ~
#  #  #  ~  #  ~  #  #  #  ~
#  EN ~  ~  ~  #  ~  ~  ~  ~
#
# output: Matrix ->
#
# 15 15 15 15 15 15 15 15 15 15
# 15 15 15 15 15 15 15 15 15 15
# 15 15 15 15 15 15 15 15 15 15
# 15 15 15 15 15 15 15 15 15 15
# 15 15 15 15 15 15 15 15 15 15
# 15 15 15 15 15 15 15 15 15 15
# 15 15 15 15 15 15 15 15 15 15
#
# F cost is the nodes g cost + h cost.
# the G cost at [0, 8] is 0 because it is 0 distance away from ST
# the H cost at [0, 8] is 15 because it is 15 distance away from EN
# Therefore the F cost is 0 + 15 = 15
def getFCosts(nodes):
    HCosts = getHCosts(nodes)
    GCosts = getGCosts(nodes)
    FCosts = []

    for rowIdx, row in enumerate(nodes):
        FCostRow = []
        for colIdx, _ in enumerate(row):
            HCost = HCosts[rowIdx][colIdx]
            GCost = GCosts[rowIdx][colIdx]
            FCostRow.append(HCost + GCost)
        FCosts.append(FCostRow)
    return FCosts


# Example input: Matrix ->
#
#  ~  ~  ~  ~  ~  ~  ~  ~  ST
#  ~  #  #  #  #  #  #  #  ~
#  ~  #  ~  ~  ~  ~  ~  #  ~
#  ~  #  ~  #  #  #  ~  #  ~
#  ~  ~  ~  #  ~  ~  ~  #  ~
#  #  #  ~  #  ~  #  #  #  ~
#  EN ~  ~  ~  #  ~  ~  ~  ~
#
# output: Matrix ->
#
# 6  7  8  9  10 11 12 13 14 15
# 5  6  7  8  9  10 11 12 13 14
# 4  5  6  7  8  9  10 11 12 13
# 3  4  5  6  7  8  9  10 11 12
# 2  3  4  5  6  7  8  9  10 11
# 1  2  3  4  5  6  7  8  9  10
# 0  1  2  3  4  5  6  7  8  9
#
# H cost is the nodes distance from the end node.
# [9,0] has a H cost of 15 because it is 15 distance away from EN
def getHCosts(nodes):
    endNode = getEndNode(nodes)

    hueristicValues = []
    for rowIdx, row in enumerate(nodes):
        rowValues = []
        for colIdx, _ in enumerate(row):
            rowDiff = abs(rowIdx - endNode[0])
            colDiff = abs(colIdx - endNode[1])
            rowValues.append(rowDiff + colDiff)
        hueristicValues.append(rowValues)
    return hueristicValues

# Example input: Matrix ->
#
#  ~  ~  ~  ~  ~  ~  ~  ~  ST
#  ~  #  #  #  #  #  #  #  ~
#  ~  #  ~  ~  ~  ~  ~  #  ~
#  ~  #  ~  #  #  #  ~  #  ~
#  ~  ~  ~  #  ~  ~  ~  #  ~
#  #  #  ~  #  ~  #  #  #  ~
#  EN ~  ~  ~  #  ~  ~  ~  ~
#
# Ouput: [0, 8]
#
# Returns the index of the ST node


def getStartNode(nodes):
    for rowIdx, row in enumerate(nodes):
        for colIdx, _ in enumerate(row):
            if nodes[rowIdx][colIdx] == START:
                return [rowIdx, colIdx]


# Example input: Matrix ->
#
#  ~  ~  ~  ~  ~  ~  ~  ~  ST
#  ~  #  #  #  #  #  #  #  ~
#  ~  #  ~  ~  ~  ~  ~  #  ~
#  ~  #  ~  #  #  #  ~  #  ~
#  ~  ~  ~  #  ~  ~  ~  #  ~
#  #  #  ~  #  ~  #  #  #  ~
#  EN ~  ~  ~  #  ~  ~  ~  ~
#
# Ouput: [6, 0]
#
# Returns the index of the EN node
def getEndNode(nodes):
    for rowIdx, row in enumerate(nodes):
        for colIdx, _ in enumerate(row):
            if nodes[rowIdx][colIdx] == END:
                return [rowIdx, colIdx]

# Example Input: [[0, 4], [1, 4], [3, 5]]
# Lets say the cost of the nodes are [1, 3, 1]
#
# Output: [[3,5]] and [[0,4], [3,5]]
#
# Removes the min costs nodes in the queue and puts them in another queue


def removeMinCostNodes(queue, costs):
    minCost = float('inf')
    for idx, node in enumerate(queue):
        cost = costs[node[0]][node[1]]
        if cost < minCost:
            minCost = cost

    minCosts = []
    queueMinCostsRemoved = []
    for idx, node in enumerate(queue):
        cost = costs[node[0]][node[1]]
        if cost == minCost:
            minCosts.append(node)
        else:
            queueMinCostsRemoved.append(node)

    return queueMinCostsRemoved, minCosts


# Example input: nodes =
#  ~  ~  ~  ~  ~  ~  ~  ~  ST
#  ~  #  #  #  #  #  #  #  ~
#  ~  #  ~  ~  ~  ~  ~  #  ~
#  ~  #  ~  #  #  #  ~  #  ~
#  ~  ~  ~  #  ~  ~  ~  #  ~
#  #  #  ~  #  ~  #  #  #  ~
#  EN ~  ~  ~  #  ~  ~  ~  ~
#
#  row = 0
#  col = 0
#
# Ouput: [[1, 0], [0, 1]]
#
# Returns neighboring nodes of input row, col that is not already visited and is a path.
def getNeighbors(row, col, nodes, visited):
    neighbors = []
    if row + 1 <= len(nodes) - 1 and not visited[row + 1][col] and nodes[row + 1][col] != OBSTACLE:
        neighbors.append([row + 1, col])
    if row - 1 >= 0 and not visited[row - 1][col] and nodes[row - 1][col] != OBSTACLE:
        neighbors.append([row - 1, col])
    if col + 1 <= len(nodes[0]) - 1 and not visited[row][col + 1] and nodes[row][col + 1] != OBSTACLE:
        neighbors.append([row, col + 1])
    if col - 1 >= 0 and not visited[row][col - 1] and nodes[row][col - 1] != OBSTACLE:
        neighbors.append([row, col - 1])

    return neighbors


# Example input:
#  ~  ~  ~  ~  ~  ~  ~  ~  ST
#  ~  #  #  #  #  #  #  #  ~
#  ~  #  ~  ~  ~  ~  ~  #  ~
#  ~  #  ~  #  #  #  ~  #  ~
#  ~  ~  ~  #  ~  ~  ~  #  ~
#  #  #  ~  #  ~  #  #  #  ~
#  EN ~  ~  ~  #  ~  ~  ~  ~
#
# output:
#  ~  ~  ~  ~  ~  ~  ~  ~  ST
#  ~  #  #  #  #  #  #  #  ~
#  ~  #  ~  ~  ~  ~  ~  #  ~
#  ~  #  ~  #  #  #  ~  #  ~
#  ~  ~  ~  #  ~  ~  ~  #  ~
#  #  #  ~  #  ~  #  #  #  ~
#  EN ~  ~  ~  #  ~  ~  ~  ~
#
# Returns a copy of nodes.
#
# Usage:
# A = copyNodes(nodes)
# A[0][1] = 5
# nodes is not modified when A is modified
#
# A = nodes
# A[0][1] = 5
# nodes is also modified
def copyNodes(nodes):
    newNodes = []
    for _, row in enumerate(nodes):
        newRow = []
        for _, col in enumerate(row):
            newRow.append(col)
        newNodes.append(newRow)
    return newNodes


# Example Input: nodes =
#  ~  ~  ~  ~  ~  ~  ~  ~  ST
#  ~  #  #  #  #  #  #  #  ~
#  ~  #  ~  ~  ~  ~  ~  #  ~
#  ~  #  ~  #  #  #  ~  #  ~
#  ~  ~  ~  #  ~  ~  ~  #  ~
#  #  #  ~  #  ~  #  #  #  ~
#  EN ~  ~  ~  #  ~  ~  ~  ~
#
# costs =
# 6  7  8  9  10 11 12 13 14 15
# 5  6  7  8  9  10 11 12 13 14
# 4  5  6  7  8  9  10 11 12 13
# 3  4  5  6  7  8  9  10 11 12
# 2  3  4  5  6  7  8  9  10 11
# 1  2  3  4  5  6  7  8  9  10
# 0  1  2  3  4  5  6  7  8  9
#
# output:
#  # 8  7  6  5  4  3  2  1  ST
#  # 9  #  #  #  #  #  #  #  1
#  # 10 #  ~  ~  ~  ~  ~  #  2
#  # 11 #  ~  #  #  #  ~  #  3
#  # 12 13 14 #  ~  ~  ~  #  4
#  # #  #  15 #  ~  #  #  #  5
# EN 18 17 16  # 10 9  8  7  6
#
# returns the path from ST to EN. The numbers represent the order in which the node was explored


def findPathBFS(nodes, costs):
    visited = [[False for col in row] for row in nodes]
    startNode = getStartNode(nodes)
    queue = [startNode]
    path = []

    pathTracker = copyNodes(nodes)

    step = 0

    while queue:
        queue, minCostNodes = removeMinCostNodes(queue, costs)
        for node in minCostNodes:
            path.append(node)
            row, col = node

            if nodes[row][col] == END:
                return pathTracker

            # keep track of order that node was explored unless it is the start node
            if step != 0:
                pathTracker[row][col] = step

            visited[row][col] = True
            neighbors = getNeighbors(row, col, nodes, visited)

            for neighbor in neighbors:
                queue.append(neighbor)

        step += 1

    return pathTracker


def mergeNodes(node1, node2):
    mergedNodes = []
    for rowIdx, row in enumerate(node1):
        mergedRow = node1[rowIdx]
        mergedRow.append("\t")
        mergedRow += node2[rowIdx]
        mergedNodes.append(mergedRow)

    return mergedNodes


def prettyPrintNodes(nodes):
    for rowIdx, row in enumerate(nodes):
        for colIdx, col in enumerate(row):
            node = nodes[rowIdx][colIdx]
            if type(node) != int:
                continue
            if node < 10:
                node = f"{node}  "
            elif node >= 10:
                node = f"{node} "
            nodes[rowIdx][colIdx] = node
    for row in nodes:
        print("".join(row))


def printLegend():
    print("========== LEGEND ==========")
    print(f"Wall:\t\t\t{OBSTACLE}")
    print(f"Unexplored Path:\t{PATH}")
    print(f"Start:\t\t\t{START}")
    print(f"End:\t\t\t{END}")
    print("============================\n")


OBSTACLE = "#  "
PATH = "~  "
START = "ST "
END = "EN "

nodes = [
    [OBSTACLE, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, START],
    [OBSTACLE, PATH, OBSTACLE, OBSTACLE, OBSTACLE,
        OBSTACLE, OBSTACLE, OBSTACLE, OBSTACLE, PATH],
    [OBSTACLE, PATH, OBSTACLE, PATH, PATH, PATH, PATH, PATH, OBSTACLE, PATH],
    [OBSTACLE, PATH, OBSTACLE, PATH, OBSTACLE,
        OBSTACLE, OBSTACLE, PATH, OBSTACLE, PATH],
    [OBSTACLE, PATH, PATH, PATH, OBSTACLE, PATH, PATH, PATH, OBSTACLE, PATH],
    [OBSTACLE, OBSTACLE, OBSTACLE, PATH, OBSTACLE,
        PATH, OBSTACLE, OBSTACLE, OBSTACLE, PATH],
    [END, PATH, PATH, PATH, OBSTACLE, PATH, PATH, PATH, PATH, PATH],
]


if __name__ == '__main__':
    HCosts = getHCosts(nodes)
    GBFSPath = findPathBFS(nodes, costs=HCosts)
    # GBFSPathWithAndHCosts = mergeNodes(GBFSPath, HCosts)

    prettyPrintNodes(GBFSPath)

    print("\n")
    printLegend()
    print("GBFS\t\t\t\tH Cost\n")

    prettyPrintNodes(GBFSPathWithAndHCosts)

    GCosts = getGCosts(nodes)
    FCosts = getFCosts(nodes)
    AStarPath = findPathBFS(nodes, costs=FCosts)

    AStarAndCosts = mergeNodes(AStarPath, HCosts)
    AStarAndCosts = mergeNodes(AStarAndCosts, GCosts)
    AStarAndCosts = mergeNodes(AStarAndCosts, FCosts)

    print("\nA Star\t\t\t\tH Cost\t\t\t\tG Cost\t\t\t\tF Cost\n")
    prettyPrintNodes(AStarAndCosts)
    print("\n")

    # Both algorithms found the shortest path that I found however A* took longer to find it.
    # This is because the F cost of all the nodes is the same since the start and end are on the corners of the graph.
    # Because all nodes have the same F cost, no nodes are priotizes over another when finding the path.
    # Since there are obstacles, this is not good, since some nodes bring you to the end quicker than others.

    ANSWER = """
    Both algorithms found the shortest path that I found however A* took longer to find it. 
    This is because the F cost of all the nodes is the same since the start and end are on the corners of the graph.
    Because all nodes have the same F cost, no nodes are priotizes over another when finding the path.
    Since there are obstacles, this is not good, since some nodes bring you to the end quicker than others. 
    """

    print(ANSWER)
