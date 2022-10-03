
import random


# Tree setup
class Tree:
    def __init__(self, value, left=None, right=None, sum=0, path=[]):
        self.left = left
        self.right = right
        self.value = value
        self.sum = sum
        self.path = []


node6A = Tree(6)
node9A = Tree(9)
node5A = Tree(5)
node3A = Tree(3)
node3B = Tree(3)
node5B = Tree(5)
node9B = Tree(9)
node7A = Tree(7)
node9C = Tree(9)


node6A.right = node9A
node6A.left = node5B

node9A.right = node5A
node9A.left = node3B

node5A.right = node3A

node5B.left = node9B

node9B.left = node9C
node9B.right = node7A


# randomly go left/right untill you hit a leaf or the sum of the path is 27
# if you hit a leaf and the sum is not 27 go back to the root.
def findPathRandom(tree, targetSum):
    path = []
    currSum = 0
    root = tree
    currNode = tree
    while True:
        currSum += currNode.value
        path.append(currNode.value)
        if currSum == targetSum:
            return path

        direction = random.randrange(2)
        if direction == 0 and currNode.left:
            currNode = currNode.left
        elif direction == 1 and currNode.right:
            currNode = currNode.right
        elif currNode.right is None and currNode.left is None:
            currNode = root
            currSum = 0
            path = []


class findPathRecursive:
    def __init__(self):
        self.path = ""

    def solve(self, tree, targetSum, runningSum=0, path=""):
        path += str(tree.value) + " "
        runningSum += tree.value

        if runningSum == targetSum:
            self.path = path
            return

        if tree.left is None and tree.right is None:
            return

        if tree.left:
            self.solve(tree.left, targetSum, runningSum, path)
        if tree.right:
            self.solve(tree.right, targetSum, runningSum, path)

        return self.path


if __name__ == '__main__':
    path = findPathRandom(tree=node6A, targetSum=27)
    print("\n==== Algo One ====")
    print(f"path: {' '.join(str(node) for node in path)}\tsum: 27")

    print("\n==== Algo Two ====")
    path2 = findPathRecursive().solve(tree=node6A, targetSum=27)
    print(f"path: {path2}\tsum: 27\n")
