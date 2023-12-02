# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(node, curr_path):
            
            if not node:
                return
            
            if not node.left and not node.right:
                curr_path.append(str(node.val))
                paths.append('->'.join(curr_path))
                curr_path.pop()
                return

            curr_path.append(str(node.val))
            dfs(node.left, curr_path)
            dfs(node.right, curr_path)
            curr_path.pop()


        paths = []
        dfs(root, [])

        return paths