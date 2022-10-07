
# QUESITON 1
#
# On average algorithm two finds the solution quicker. Algo two always finds the solution in 5 steps while algo one can range from anywhere between four and one hundred.
# Since the first algorithm finds the path randomly sometimes it gets lucky and gets the answer in 4 steps on its first random try.
# However if the first algo doesn't find the path on its first random try it will take longer than algo 2.
# So on average algo two is much quicker

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
    steps = 0
    path = []
    currSum = 0
    root = tree
    currNode = tree
    while True:
        steps += 1
        currSum += currNode.value
        path.append(currNode.value)
        if currSum == targetSum:
            return path, steps

        direction = random.randrange(2)
        if direction == 0 and currNode.left:
            currNode = currNode.left
        elif direction == 1 and currNode.right:
            currNode = currNode.right
        elif currNode.right is None and currNode.left is None:
            currNode = root
            currSum = 0
            path = []


# recursivly go down the tree and store than path and sum within each recursive function
# if the sum equals the target sum return the path and stop all over recursive functions
# by making self.targetSumFound = True
class findPathRecursive:
    def __init__(self):
        self.path = ""
        self.targetSumFound = False
        self.steps = 0

    def solve(self, tree, targetSum, runningSum=0, path=""):

        if self.targetSumFound:
            return

        self.steps += 1

        path += str(tree.value) + " "
        runningSum += tree.value

        if runningSum == targetSum:
            self.path = path
            self.targetSumFound = True
            return

        if tree.left is None and tree.right is None:
            return

        if tree.left:
            self.solve(tree.left, targetSum, runningSum, path)
        if tree.right:
            self.solve(tree.right, targetSum, runningSum, path)

        return self.path, self.steps


if __name__ == '__main__':

    path, steps = findPathRandom(tree=node6A, targetSum=27)
    print("\n==== Algo One ====")
    print(
        f"path: {' '.join(str(node) for node in path)}\tsteps: {steps}\tsum: 27")

    print("\n==== Algo Two ====")
    path2, steps2 = findPathRecursive().solve(tree=node6A, targetSum=27)
    print(f"path: {path2}\tsteps: {steps2}\tsum: 27\n")

    # On average algorithm two finds the solution quicker. Algo two always finds the solution in 5 steps while algo one can range from anywhere between four and one hundred.
    # Since the first algorithm finds the path randomly sometimes it gets lucky and gets the answer in 4 steps on its first random try.
    # However if the first algo doesn't find the path on its first random try it will take longer than algo 2.
    # So on average algo two is much quicker

    ANSWER = """
    On average algorithm two finds the solution quicker. 
    Algo two always finds the solution in 5 steps while algo one can range from anywhere between four and one hundred.
    Since the first algorithm finds the path randomly, it sometimes it gets lucky and gets the answer in 4 steps on its first random try.
    However if the first algo doesn't find the path on its first random try it will take longer than algo 2.
    So on average algo two is much quicker
    """
    print(ANSWER)
