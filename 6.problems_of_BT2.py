#For a given Binary Tree of type integer, update it with its corresponding mirror image.
def mirrorBinaryTree(root):
    if root is None:
        return

    temp = root.left
    root.left = root.right
    root.right = temp

    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)

    return root

#create and insert duplicate node
#For a given a Binary Tree of type integer, duplicate every node of the tree and attach it to the left of itself.
#The root will remain the same. So you just need to insert nodes in the given Binary Tree.
#Sample Input 1:
#10 20 30 40 50 -1 60 -1 -1 -1 -1 -1 -1
#Sample Output 1:
#10 
#10 30 
#20 30 60 
#20 50 60 
#40 50 
#40 
def insertDuplicateNode(root):
    if root is None:
        return
    insertDuplicateNode(root.left)
    temp = root.left
    root.left = BinaryTreeNode(root.data)
    root.left.left = temp
    insertDuplicateNode(root.right)
    return root

#find maximum and minimum nodes
class Pair:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum


def getMinAndMax(root, pair):
    if root is None:
        return pair

    left = getMinAndMax(root.left, pair)
    right = getMinAndMax(root.right, pair)
    minimum = min(left.minimum, right.minimum, root.data)
    maximum = max(left.maximum, right.maximum, root.data)
    pair.minimum = minimum
    pair.maximum = maximum
    return pair
#this returns object with maximum and minimum data

#print level wise - level order traversal
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
            if curr.left is not None:
                outputQ.put(curr.left)
            if curr.right is not None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ

#print level wise - below code will print in this way
#input: 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
#output:
#5:L:6,R:10
#6:L:2,R:3
#10:L:-1,R:-1
#2:L:-1,R:-1
#3:L:-1,R:9
#9:L:-1,R:-1

def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=':')
            if curr.left is not None:
                outputQ.put(curr.left)
                print('L', end=':')
                print(curr.left.data, end=',')
            elif curr.left is None:
                print('L', end=':')
                print('-1', end=',')

            if curr.right is not None:
                outputQ.put(curr.right)
                print('R', end=':')
                print(curr.right.data, end='')
            elif curr.right is None:
                print('R', end=':')
                print('-1', end='')
            print()

        inputQ, outputQ = outputQ, inputQ
