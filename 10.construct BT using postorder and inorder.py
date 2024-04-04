from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(arr, strt, end, value):
    i = 0
    for i in range(strt, end + 1):
        if (arr[i] == value):
            break
    return i


def buildUtil(In, post, inStrt, inEnd, pIndex):

    if (inStrt > inEnd):
        return None

    node = BinaryTreeNode(post[pIndex[0]])
    pIndex[0] -= 1

    if (inStrt == inEnd):
        return node

    iIndex = search(In, inStrt, inEnd, node.data)

    node.right = buildUtil(In, post, iIndex + 1, inEnd, pIndex)
    node.left = buildUtil(In, post, inStrt, iIndex - 1, pIndex)

    return node


def buildTree(post, In, n):
    pIndex = [n - 1]
    return buildUtil(In, post, 0, n - 1, pIndex)




































'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


                

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder, n)
printLevelWise(root)
