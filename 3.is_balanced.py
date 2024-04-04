def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))

#O(n^2) - how? best case is log(n)
def isBalanced(root):
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return False

    ifLeftBalanced = isBalanced(root.left)
    ifRightBalanced = isBalanced(root.right)

    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False

#O(n)
def isBalanced2(root):
    if root == None:
        return 0, True

    lh, isLeftBalanced = isBalanced2(root.left)
    rh, isRightBalanced = isBalanced2(root.right)

    h = 1 + max(lh, rh)
    if lh - rh > 1 or rh - lh > 1:
        return h, False

    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False
