#node with largest data
def largestData(root):
    if root == None:
        return -1
    leftLargest = largestData(root.left)
    rightLargest = largestData(root.right)
    largest = max(leftLargest, rigthLargest, root.data)
    return largest

#no of leaf nodes
def no(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    numLeafLeft = no(root.left)
    numLeafRight = no(root.rigth)
    return numLeafLeft + numLeafRight

#print nodes at depth k
def printd(root, k):
    if root == None:
        return
    if k == 0:
        print(root.data)
        return
    printd(root.left, k - 1)
    printd(root.right, k - 1)

def printv2(root, k, d = 0):
    if root == None:
        return
    if k == d:
        print(root.data)
        return
    printv2(root.left, k, d + 1)
    printv2(root.right, k, d + 1)

#remove leaf nodes
def removeLeafNodes(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left = removeLeafNodes(root.left)
    root.right = removeLeafNodes(root.right)
    return root
