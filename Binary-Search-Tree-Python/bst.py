class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    

    def isEmpty(self):
    # YOUR CODE STARTS HERE
        return self.root is None
    

    @property
    def getMin(self): 
    # YOUR CODE STARTS HERE
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value


    @property
    def getMax(self): 
    # YOUR CODE STARTS HERE   
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value
        



    def __contains__(self,value):
    # YOUR CODE STARTS HERE    
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            elif current.value == value:
                return True
        return False


    def getHeight(self, node):
    # YOUR CODE STARTS HERE    
        if node is None:
            return -1
        lhs = self.getHeight(node.left)
        rhs = self.getHeight(node.right)
        return max(lhs, rhs) + 1


    def get_numLeaves(self): # Do not modify this method
        return self._get_numLeaves_helper(self.root)


    def _get_numLeaves_helper(self, node):
    # YOUR CODE STARTS HERE
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._get_numLeaves_helper(node.left) + self._get_numLeaves_helper(node.right)

    @property
    def isBalanced(self):  # Do not modify this method
        return self.isBalanced_helper(self.root)
    
    
    def isBalanced_helper(self, node):
    # YOUR CODE STARTS HERE
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        lhs = self.getHeight(node.left)
        rhs = self.getHeight(node.right)
        if abs(lhs - rhs) > 1:
            return False
        return self.isBalanced_helper(node.left) and self.isBalanced_helper(node.right)


