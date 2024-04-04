import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def longestPath(root):
    if (root is None):
        return []

    rightvect = longestPath(root.right)

    leftvect = longestPath(root.left)

    if (len(leftvect) < len(rightvect)):
        leftvect.append(root.data)
    else:
        rightvect.append(root.data)

    if len(leftvect) > len(rightvect):
        return leftvect

    return rightvect


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
path = longestPath(root)
for ele in path:
    print(ele)
