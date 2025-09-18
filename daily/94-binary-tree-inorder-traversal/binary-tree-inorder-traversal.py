# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        visited=[]
        def check_node(root):
            if not root:
                return 
            
            most_leftTree_check= check_node(root.left)
            visited.append(root.val)
            most_rightTree_check= check_node(root.right)

        check_node(root)
        return visited 
