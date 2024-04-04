class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def printTree(root):
    if root == None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, end = ':')
    if root.left != None:
        print("L", root.left.data, end = ',')
    if root.right != None:
        print("R", root.right.data)
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def numNodes(root):
    if root == None:
        return 0
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    return 1 + leftCount + rightCount

#get sum of all nodes
def getSum(root):
    if root is None:
        return 0
    leftSum = getSum(root.left)
    rightSum = getSum(root.right)

    return root.data + leftSum + rightSum

#print the BT in preorder form
def preOrder(root):
    if root is None:
        return

    print(root.data, end = ' ')

    preOrder(root.left)
    preOrder(root.right)

#post order
def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end = ' ')

#For a given a binary tree of integers and an integer X,
#find and return the total number of nodes of the given binary tree which are
#having data greater than X.
def countNodesGreaterThanX(root, x, count) :
    if root is None:
        return count
    if root.data > x:
        count += 1
    count = countNodesGreaterThanX(root.left, x, count)
    count = countNodesGreaterThanX(root.right, x, count)
    return count

def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return 1 + max(left, right)

#replace node with depth
#For a given a Binary Tree of integers, replace each of its data with the depth of the tree.
#input: 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
#output: 2 1 2 0 2 1 2 
Root is at depth 0, hence the root data is updated with 0. Replicate the same further going down the in the depth of the given tree.
def changeToDepthTree(root, count=-1):
    if root is None:
        return 0
    count += 1
    changeToDepthTree(root.left, count)
    changeToDepthTree(root.right, count)
    root.data = count
    return root

#For a given Binary Tree of type integer and a number X, find whether a node exists in the tree with data X or not.
def isNodePresent(root, x):
    if root is None:
        return False
    if root.data == x:
        return True
    res1 = isNodePresent(root.left, x)
    if res1:
        return True
    res2 = isNodePresent(root.right, x)
    return res2

#For a given Binary Tree of type integer, print all the nodes without any siblings.
def printNodesWithoutSibling(root):
    if root is None:
        return
    left = root.left
    right = root.right
    if left is not None and right is None:
        print(root.left.data, end=' ')
    if right is not None and left is None:
        print(root.right.data, end=' ')

    printNodesWithoutSibling(root.left)
    printNodesWithoutSibling(root.right)

btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(4)
btn3 = BinaryTreeNode(9)

btn4 = BinaryTreeNode(3)
btn5 = BinaryTreeNode(5)

btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5

printTreeDetailed(btn1)

root = treeInput()
printTreeDetailed(root)
print(numNodes(root))
