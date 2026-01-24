# VALID BINARY SEARCH TREE

# Return true if it is a valid binary search tree, otherwise return false.

# A valid binary search tree satisfies the following constraints:

# 1. The left subtree of every node contains only nodes with keys less 
# than the node's key.
# 2. The right subtree of every node contains only nodes with keys greater 
# than the node's key.
# 3. Both the left and right subtrees are also binary search trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, left, right):
            # A null node does not make the BST invalid
            if node is None:
                return True
            # Not a valid BST if left is greater than or right is less than parent node
            if not (node.val > left and node.val < right):
                return False
            # Recursively check right and left sides of the tree
            return (isValid(node.left, left, node.val) and
            isValid(node.right, node.val, right))
            
        # Begin the function with the root and the left being the lowest value and right the highest    
        return isValid(root, float("-inf"), float("inf"))
            
