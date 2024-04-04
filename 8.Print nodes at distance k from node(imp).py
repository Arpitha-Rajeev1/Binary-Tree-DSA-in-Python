#You are given a Binary Tree of type integer, a target node, and an integer value K.
#Print the data of all nodes that have a distance K from the target node. The order in which they would be printed will not matter.
#Example:
#For a given input tree(refer to the image below):
#1. Target Node: 5
#2. K = 2
#Starting from the target node 5, the nodes at distance K are 7 4 and 1.

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printkDistanceNodeDown(root, k):
    if root is None or k < 0:
        return

    if k == 0:
        print(root.data)
        return

    printkDistanceNodeDown(root.left, k-1)
    printkDistanceNodeDown(root.right, k-1)


def nodesAtDistanceK(root, target, k):
    if root is None:
        return -1

    if root.data == target:
        printkDistanceNodeDown(root, k)
        return 0

    dl = nodesAtDistanceK(root.left, target, k)

    if dl != -1:
        if dl + 1 == k:
            print(root.data)
        else:
            printkDistanceNodeDown(root.right, k-dl-2)
        return 1 + dl

    dr = nodesAtDistanceK(root.right, target, k)
    if dr != -1:
        if (dr+1 == k):
            print(root.data)
        else:
            printkDistanceNodeDown(root.left, k-dr-2)
        return 1 + dr

    return -1






























	


#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

    
def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])

nodesAtDistanceK(root, target, k)
