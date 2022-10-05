

import math
GET_MAX = -1
GET_MIN = 1

# Tree setup
class Tree:
    def __init__(self, value, left=None, right=None, sum=0, path=[]):
        self.left = left
        self.right = right
        self.value = value
        self.sum = sum
        self.path = []


def toggleMode(mode):
    return mode * -1


def minMax(node, mode = -1):

    # if mode equals GET_MAX make it GET_MIN
    # if mode equals GET_MIN make it MIN_MAX
    mode = toggleMode(mode)

    if node.left is None and node.right is None:
        return node.value
    
    if node.left is None:
        return minMax(node.right, mode)
    
    if node.right is None:
        return minMax(node.left, mode)
    
    if mode == GET_MAX:
        maxLeft = minMax(node.left, mode)
        maxRight = minMax(node.right, mode)
        return max(maxLeft, maxRight)
    
    if mode == GET_MIN:
        minLeft = minMax(node.left, mode)
        minRight = minMax(node.right, mode)
        return min(maxLeft, maxRight)
    


    