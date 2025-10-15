# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def build_tree(level_order):
        if not level_order or level_order[0] is None:
            return None

        root = TreeNode(level_order[0])
        queue = deque([root])
        i = 1

        while queue and i < len(level_order):
            current = queue.popleft()

            # Left child
            if i < len(level_order) and level_order[i] is not None:
                current.left = TreeNode(level_order[i])
                queue.append(current.left)
            i += 1

            # Right child
            if i < len(level_order) and level_order[i] is not None:
                current.right = TreeNode(level_order[i])
                queue.append(current.right)
            i += 1

        return root
    
    @staticmethod
    def inorder(root):
        if root is None:
            return
        
        TreeNode.inorder(root.left)
        print(root.val)
        TreeNode.inorder(root.right)
    

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        

        root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root


level_order = [4,2,7,1,3,6,9]
root = TreeNode.build_tree(level_order)
sol = Solution()
TreeNode.inorder(root)
root2 = sol.invertTree(root)
print()
TreeNode.inorder(root2)