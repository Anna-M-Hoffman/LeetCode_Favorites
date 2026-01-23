# DIAMETER OF BINARY TREE
# The diameter is the length of the longest path between any two nodes. 
# The path does not necessarily have to pass through the root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # Global variable keeps track of largest diameter

        def dfs(node): # DFS on left and right subtrees
            if node is None:
                return 0
            left = dfs(node.left) # Recursively goes through left side
            right = dfs(node.right) # Recursively goes through left side
            self.res = max(self.res, left + right) # res updated to heighest 
            # diamter which is the height of the left and right subtrees
            return 1 + max(left, right) # Adds 1 each recursion to the
            # recursively computed heights 
            # (sub-branches which eventually make up the left and right sides)
        dfs(root)
        return self.res

