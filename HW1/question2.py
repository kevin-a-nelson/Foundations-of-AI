

import enum
from platform import node


def getHueristicValues(nodes):
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


def popLowestHeuisticValueNode(queue, hueristicValues):
    minHueisticValue = float('inf')
    minHeuristicValueIdx = -1
    for idx, node in enumerate(queue):
        hueristicValue = hueristicValues[node[0]][node[1]]
        if hueristicValue < minHueisticValue:
            minHeuristicValueIdx = idx
            minHueisticValue = hueristicValue

    return queue.pop(minHeuristicValueIdx)


def getDefaultVisited(nodes):
    rows = len(nodes)
    cols = len(nodes[0])

    visited = []

    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(False)
        visited.append(row)

    return visited


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


def greedyBFS(nodes):
    visited = getDefaultVisited(nodes)
    startNode = getStartNode(nodes)
    hueristicValues = getHueristicValues(nodes)
    queue = [startNode]
    path = []

    while queue:
        currNode = popLowestHeuisticValueNode(queue, hueristicValues)
        path.append(currNode)
        row, col = currNode

        if nodes[row][col] == END:
            break

        visited[row][col] = True
        neighbors = getNeighbors(row, col, nodes, visited)

        for neighbor in neighbors:
            queue.append(neighbor)

    return path


def prettyPrintNodes(nodes):
    for rowIdx, row in enumerate(nodes):
        for colIdx, col in enumerate(row):
            node = nodes[rowIdx][colIdx]
            if type(node) != int:
                continue
            if node < 10:
                node = f"  {node}"
            elif node >= 10:
                node = f" {node}"
            nodes[rowIdx][colIdx] = node

    print("==== LEGEND ====")
    print(f"Obstacle:\t\t{OBSTACLE}")
    print(f"Unexplored Path:\t{PATH}")
    print("================\n")
    for row in nodes:
        print("".join(row))


if __name__ == '__main__':
    OBSTACLE = "  #"
    PATH = "  ~"
    START = "  @"
    END = "   E"

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

    path = greedyBFS(nodes)

    hueristicValues = getHueristicValues(nodes)
    nodesWithPath = nodes
    for idx, node in enumerate(path):
        nodesWithPath[node[0]][node[1]] = idx

    print("\n")
    prettyPrintNodes(nodesWithPath)
    print("\n")
