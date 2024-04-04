def buildTreeFromPreIn(pre, inorder):
    if len(pre) == 0:
        return None

    rootData = pre[0]
    root = BinaryTreeNode(rootData)
    rootIndexInInorder = -1

    for i in range(0, len(inorder)):
        if inorder[i] == rootData:
            rootIndexInInorder = i
            break
    if rootIndexInInorder == -1:
        return None

    leftInorder = inorder[0:rootIndexInInorder]
    rigthInorder = inorder[rootIndexInInorder + 1:]

    lenLeftSubtree = len(leftInorder)

    leftPreorder = pre[1:lenLeftSubtree + 1]
    rightPreorder = pre[lenLeftSubtree + 1:]

    leftChild = buildTreeFromPreIn(leftPreorder, leftInorder)
    rightChild = buildTreeFromPreIn(rightPreorder, rightInorder)

    root.left = leftChild
    root.right = rightChild

    return root
        
#algorithm
    1. find the root -> preorder[0]
    2. find inorder of both left and right subtree
    3. find preorder of left and right subtree
    4. use recursion to build left and right subtree
    5. connect root with both
