# Lab #5
# Due Date: 10/22/2021, 11:59PM 
# REMINDERS: 
#        The work in this assignment must be your own original work and must be completed alone.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x.insert(11)
        >>> x.insert(2)
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> x.getMin
        Node(2)
        >>> x.getMax
        Node(11)
        >>> 67 in x
        False
        >>> 9.5 in x
        True
        >>> x.isEmpty()
        False
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
        >>> new_tree = x.mirror()
        11 : 10 : 9.5 : 9 : 7 : 5 : 4 : 2 : 
        >>> new_tree.root.right
        Node(4)
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
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
    
    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)         


    def mirror(self):
        # Creates a new BST that is a mirror of self: Elements greater than the root are on the left side, and smaller values on the right side
        # Do NOT modify any given code
        if self.root is None:
            return None
        else:
            newTree = BinarySearchTree()
            newTree.root = self._mirrorHelper(self.root)
            newTree.printInorder
            return newTree
        




    def isEmpty(self):
        return self.root == None #if theres no root, that means the tree is empty



    def _mirrorHelper(self, node):
        
        
        if node == None: #base case
            return None
        else:
            nn = Node(node.value)
            nn.left = self._mirrorHelper(node.right) #set left equal to right
            nn.right = self._mirrorHelper(node.left) #set right equal to left
            return nn




    @property
    def getMin(self): 

        if self.isEmpty():
            return None
        else:
            root = self.root   #gets the left most node since that will be of greatest value
            while root.left != None:
                root = root.left
            return root



    @property
    def getMax(self): 

        if self.isEmpty():
            return None
        else:
            root = self.root #gets the right most node since that will be of greatest value
            while root.right != None:
                root = root.right
                return root




    def __contains__(self,value):
        
        curr = self.root
        while curr != None:
            if value > curr.value: #if input value greater than the current value
                curr = curr.right
            elif value == curr.value: #if it is equal to the current value, it contains it
                return True
            else:
                curr = curr.left
        return False


    def getHeight(self, node):
        
        if node == None:
            return 0
        elif node.right == None and node.left == None:
            return 0
        if self.getHeight(node.right) > self.getHeight(node.left): 
            return 1 + self.getHeight(node.right) #if the right node greater than left, add to height of right
        else:
            return 1 + self.getHeight(node.left) #if the left node greater than right, add to height of left

        



