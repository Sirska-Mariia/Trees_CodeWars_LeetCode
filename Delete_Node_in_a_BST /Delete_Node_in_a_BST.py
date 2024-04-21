class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if root.val == key:
                if root.left is None and root.right is None:
                    return None
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    root2 = root.right
                    while root2.left is not None:
                        root2 = root2.left
                    root.val = root2.val
                    root.right = self.deleteNode(root.right, root2.val)
        elif root.val > key:
                root.left = self.deleteNode(root.left, key)
        elif root.val < key:
                root.right = self.deleteNode(root.right, key)
        return root
