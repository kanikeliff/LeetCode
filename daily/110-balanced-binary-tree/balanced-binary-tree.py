import math


class Solution(object):
   def isBalanced(self, root):
       """
       :type root: Optional[TreeNode]
       :rtype: bool
       """


       def checkBalance(node):
           if node is None:
               return (0, True)
          
           # Checking left subtree first
           leftHeight, leftBalance = checkBalance(node.left)


           # Checking right subtree after left subtree
           rightHeight, rightBalance = checkBalance(node.right)


           # If either left or right subtree is unbalanced, return unbalanced
           if not leftBalance or not rightBalance:
               return (0, False)


           if abs(leftHeight - rightHeight) > 1:
               return (0, False)


           currHeight = 1 + max(leftHeight, rightHeight)
           return (currHeight, True)
      
       rootHeight, rootBalance = checkBalance(root)
       return rootBalance