
import random


class QItem:
    def __init__(self, row, col, distance):
        self.row = row
        self.col = col
        self.distance = distance

    def __repr__(self):
        return f"QItem({self.row}, {self.col}, {self.distance})"


def getStartNode(nodes):
    global END
    for rowIdx, row in enumerate(nodes):
        for colIdx, col in enumerate(row):
            if col == START:
                return QItem(rowIdx, colIdx, 0)


def goNorth(currNode, nodes, path):
    while currNode.row - 1 >= 0 and nodes[currNode.row - 1][currNode.col] != OBSTICAL:
        currNode.row -= 1
        currNode.distance += 1
        path.append([currNode.row, currNode.col, currNode.distance])
    return currNode


def goSouth(currNode, nodes, path):
    while currNode.row + 1 <= len(nodes) - 1 and nodes[currNode.row + 1][currNode.col] != OBSTICAL:
        currNode.row += 1
        currNode.distance += 1
        path.append([currNode.row, currNode.col, currNode.distance])
    return currNode


def goWest(currNode, nodes, path):
    while currNode.col - 1 >= 0 and nodes[currNode.row][currNode.col - 1] != OBSTICAL:
        currNode.col -= 1
        currNode.distance += 1
        path.append([currNode.row, currNode.col, currNode.distance])
    return currNode


def goEast(currNode, nodes, path):
    while currNode.col + 1 <= len(nodes[0]) - 1 and nodes[currNode.row][currNode.col + 1] != OBSTICAL:
        currNode.col += 1
        currNode.distance += 1
        path.append([currNode.row, currNode.col, currNode.distance])
    return currNode


def getPathHardCoded(nodes):
    currNode = getStartNode(nodes)

    path = []

    goSouth(currNode, nodes, path)
    goWest(currNode, nodes, path)
    goNorth(currNode, nodes, path)
    goEast(currNode, nodes, path)
    goNorth(currNode, nodes, path)
    goWest(currNode, nodes, path)
    goSouth(currNode, nodes, path)
    goWest(currNode, nodes, path)

    return path


def getPathRandomly(nodes):
    # Get cords of the starting node
    path = []
    currNode = getStartNode(nodes)
    direction = ["N", "E", "S", "W"]
    randomNumber = random.randrange(3)
    randomDirection = direction[randomNumber]

    while True:

        if nodes[currNode.row][currNode.col] == END:
            if currNode.distance == 27:
                break
            else:
                path = []
                currNode = getStartNode(nodes)

        randomNumber = random.randrange(4)
        randomDirection = direction[randomNumber]
        if randomDirection == "N":
            goNorth(currNode, nodes, path)
        elif randomDirection == "E":
            goEast(currNode, nodes, path)
        elif randomDirection == "S":
            goSouth(currNode, nodes, path)
        elif randomDirection == "W":
            goWest(currNode, nodes, path)

    return path


if __name__ == '__main__':
    OBSTICAL = 0
    PATH = 1
    START = 2
    END = 3

    nodes = [
        [OBSTICAL, PATH, PATH, PATH, PATH, PATH, PATH, PATH, PATH, START],
        [OBSTICAL, PATH, OBSTICAL, OBSTICAL, OBSTICAL,
            OBSTICAL, OBSTICAL, OBSTICAL, OBSTICAL, PATH],
        [OBSTICAL, PATH, OBSTICAL, PATH, PATH, PATH, PATH, PATH, OBSTICAL, PATH],
        [OBSTICAL, PATH, OBSTICAL, PATH, OBSTICAL,
            OBSTICAL, OBSTICAL, PATH, OBSTICAL, PATH],
        [OBSTICAL, PATH, PATH, PATH, OBSTICAL, PATH, PATH, PATH, OBSTICAL, PATH],
        [OBSTICAL, OBSTICAL, OBSTICAL, PATH, OBSTICAL,
            PATH, OBSTICAL, OBSTICAL, OBSTICAL, PATH],
        [END, PATH, PATH, PATH, OBSTICAL, PATH, PATH, PATH, PATH, PATH],
    ]

    algoOnePath = getPathHardCoded(nodes)
    algoTwoPath = getPathRandomly(nodes)

    print("========== Algorith 1 ==========")
    for node in algoOnePath:
        print(f"x: {node[0]}\ty: {node[1]}\td: {node[2]}")

    print("========== Algorith 2 ==========")
    for node in algoTwoPath:
        print(f"x: {node[0]}\ty: {node[1]}\td: {node[2]}")

    print("\nAlgorithm one takes much less time than algorithm one. Algo One is hard coded to follow the best path, while algo two finds the path randomly.\n")
