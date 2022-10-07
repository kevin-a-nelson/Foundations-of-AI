
# QUESTION 3
#
# The entire right side of the tree after 5 - 2 ( root.right.right is pruned ) is pruned. Since root.right is a min
# and root.right.right.left is 5 we can prune root.right.right since we know that root.right.right will not be less
# than two.

import math
GET_MAX = -1
GET_MIN = 1

# Tree setup


class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    # Display code taken from stack over flow https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

# if mode equals GET_MAX make it GET_MIN
# if mode equals GET_MIN make it MIN_MAX


def toggleMode(mode):
    return mode * -1


def minMax(node, mode=GET_MIN):

    # if mode equals GET_MAX make it GET_MIN
    # if mode equals GET_MIN make it MIN_MAX
    mode = toggleMode(mode)

    if node.left is None and node.right is None:
        return node.key

    # if there is no left node, get the min max of the right node
    if node.left is None:
        rightNode = minMax(node.right, mode)

        if mode == GET_MAX:
            rightNode = max(node.key, rightNode)
        elif mode == GET_MIN:
            rightNode = min(node.key, rightNode)

        node.key = rightNode
        return rightNode

    # if there is no right node, get the min max of the left node
    if node.right is None:
        leftNode = minMax(node.left, mode)

        if mode == GET_MAX:
            leftNode = max(node.key, leftNode)
        elif mode == GET_MIN:
            leftNode = min(node.key, leftNode)

        node.key = leftNode
        return leftNode

    # if right node and left node exist, get the min or max of the two
    if mode == GET_MAX:
        maxLeft = minMax(node.left, mode)
        maxRight = minMax(node.right, mode)
        maxNode = max(maxLeft, maxRight)
        node.key = maxNode
        return maxNode
    elif mode == GET_MIN:
        minLeft = minMax(node.left, mode)
        minRight = minMax(node.right, mode)
        minNode = min(minLeft, minRight)
        node.key = minNode
        return minNode


BEFORE_TITLE = """
=======
Before
=======
"""

AFTER_TITLE = """
=======
After
=======
"""

if __name__ == '__main__':

    # Tree setup
    root = Tree(0)
    nodeL = Tree(5)
    nodeR = Tree(0)

    root.left = nodeL
    root.right = nodeR

    nodeRL = Tree(0)
    nodeRR = Tree(0)

    nodeR.left = nodeRL
    nodeR.right = nodeRR

    nodeRLL = Tree(1)
    nodeRLR = Tree(0)

    nodeRL.left = nodeRLL
    nodeRL.right = nodeRLR

    nodeRRL = Tree(5)
    nodeRRR = Tree(0)

    nodeRR.left = nodeRRL
    nodeRR.right = nodeRRR

    nodeRLRL = Tree(4)
    nodeRLRR = Tree(2)

    nodeRLR.left = nodeRLRL
    nodeRLR.right = nodeRLRR

    nodeRRRR = Tree(3)
    nodeRRRL = Tree(4)

    nodeRRR.right = nodeRRRR
    nodeRRR.left = nodeRRRL

    print(BEFORE_TITLE)
    root.display()
    minMax(root)
    print(AFTER_TITLE)
    root.display()

    # The entire right side of the tree after 5 - 2 ( root.right.right is pruned ) is pruned. Since root.right is a min
    # and root.right.right.left is 5 we can prune root.right.right since we know that root.right.right will not be less
    # than two.

    ANSWER = """
    The entire right side of the tree after 5 - 2 ( root.right.right is pruned ) is pruned. Since root.right is a min
    and root.right.right.left is 5 we can prune root.right.right since we know that root.right.right will not be less
    than two.
        """
    print(ANSWER)
