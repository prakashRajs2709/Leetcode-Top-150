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
    def maxDepth(self, root: Optional[TreeNode]) -> int: # type: ignore
        def depth(root):
            if not root:
                return 0
            left_height = depth(root.left)
            right_height = depth(root.right)
            return 1+max(left_height,right_height)
        return depth(root)
        
            
            




level_order = [1,None,2]
sol = Solution()
root = TreeNode.build_tree(level_order)
result = sol.maxDepth(root)
print(result)