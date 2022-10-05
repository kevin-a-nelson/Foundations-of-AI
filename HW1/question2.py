

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


def getStartNode(nodes):
    for rowIdx, row in enumerate(nodes):
        for colIdx, _ in enumerate(row):
            if nodes[rowIdx][colIdx] == START:
                return [rowIdx, colIdx]


def getEndNode(nodes):
    for rowIdx, row in enumerate(nodes):
        for colIdx, _ in enumerate(row):
            if nodes[rowIdx][colIdx] == END:
                return [rowIdx, colIdx]


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


def copyNodes(nodes):
    newNodes = []
    for _, row in enumerate(nodes):
        newRow = []
        for _, col in enumerate(row):
            newRow.append(col)
        newNodes.append(newRow)
    return newNodes


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
    GBFSPathWithAndHCosts = mergeNodes(GBFSPath, HCosts)

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
