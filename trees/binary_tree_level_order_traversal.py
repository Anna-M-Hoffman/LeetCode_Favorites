# BINARY TREE LEVEL ORDER TRAVERSAL
# Given a binary tree root, return the level order traversal of it as a nested list, 
# where each sublist contains the values of nodes at a particular level in the tree, 
# from left to right.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        q = collections.deque() # Use a queue data structure
        res = [] # Result array to hold level-specific arrays
        q.append(root) # Begin with root

        while q: # While the queue is not empty
            level = [] # Begin with a level node
            for i in range(len(q)): # For all nodes in the queue
                node = q.popleft() # Remove the leftmost node from the queue
                if node: # If the leftmost node is not null
                    q.append(node.left) # Add the left child to the queue
                    q.append(node.right) # Add the right child to the queue
                    level.append(node.val) # Add the node's value to the level array
            if level: # If the level is not empty
                res.append(level) # Append this level to the result
        return res 
