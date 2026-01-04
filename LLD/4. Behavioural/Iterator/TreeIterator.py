class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.stk = []
        self.push(root)

    def push(self, root):
        while root:
            self.stk.append(root)
            root = root.left

    def next(self) -> int:
        tmp = self.stk.pop()
        self.push(tmp.right)
        return tmp.val

    def hasNext(self) -> bool:
        return self.stk


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(-1)
    root.right = TreeNode(5)
    root.left.right = TreeNode(0)
    root.left.left = TreeNode(-5)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)

    treeIter = BSTIterator(root)
    while treeIter.hasNext():
        print(treeIter.next())
