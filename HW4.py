# HW4
# Due Date: 11/05/2021, 11:59PM
# REMINDER: 
#       The work in this assignment must be your own original work and must be completed alone.
#       You might add additional methods to encapsulate and simplify the operations, but they must be
#       thoroughly documented


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
        >>> x.insert('mom')  
        >>> x.insert('omm') 
        >>> x.insert('mmo') 
        >>> x.root          
        Node({'mmo': ['mom', 'omm', 'mmo']})
        >>> x.insert('sat')
        >>> x.insert('kind')
        >>> x.insert('ats') 
        >>> x.root.left
        Node({'ast': ['sat', 'ats']})
        >>> x.root.right is None
        True
        >>> x.root.left.right
        Node({'dikn': ['kind']})
    '''

    def __init__(self):
        self.root = None


    # Modify the insert and _insert methods to allow the operations given in the PDF
    def insert(self, value):
        if self.root is None:
            mydict = {}
            nvalue = sorted(value) #sorts the letters into an alphabetical list
            joinedstr = "".join(nvalue) #takes the list and makes it a string again
            mydict[joinedstr] = []
            mydict[joinedstr].append(value) #adds the value to the dictionary
            self.root=Node(mydict)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        mydict = {}
        nvalue = sorted(value) 
        joinedstr = "".join(nvalue) #same methods as above
        mydict[joinedstr] = []
        mydict[joinedstr].append(value)
        if joinedstr in node.value:
            node.value[joinedstr].append(value)
        else: 
            if joinedstr < list(sorted(node.value.keys()))[0]:
                if(node.left==None):
                    node.left = Node(mydict) #satisfies left node conditions
                else:
                    self._insert(node.left, value)
            else:   
                if(node.right==None):
                    node.right = Node(mydict)
                else:
                    self._insert(node.right, value) #satisfies right node conditions


    def isEmpty(self):
        return self.root == None

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

    



class Anagrams:
    '''
        # Verify class has _bst attribute  
        >>> x = Anagrams(5)
        >>> '_bst' in x.__dict__    
        True
        >>> isinstance(x.__dict__.get('_bst'), BinarySearchTree)
        True
        >>> x = Anagrams(5)
        >>> x.create('words_small.txt')
        >>> x.getAnagrams('tap')
        'No match'
        >>> x.getAnagrams('arm')
        'No match'
        >>> x.getAnagrams('rat')
        ['art', 'tar', 'rat']
        >>> x._bst.printInorder
        {'a': ['a']} : {'adns': ['ands', 'sand']} : {'ahms': ['sham', 'hams']} : {'amt': ['tam', 'mat']} : {'arst': ['arts', 'rats', 'star']} : {'arsty': ['artsy']} : {'art': ['art', 'tar', 'rat']} : 
    '''
    
    def __init__(self, word_size):

        self.word_size = word_size
        self._bst = BinarySearchTree()




    def create(self, file_name):
        with open(file_name) as f: #opens file
            contents = f.readlines()
            for i in contents:
                i = i.strip() 
                if len(i) != 0 and len(i) <= self.word_size: #if it is filled and less than or equal to the given word size inserts into tree
                    self._bst.insert(i)


 


    def getAnagrams(self, word):
        nvalue = sorted(word)
        jstr = "".join(nvalue)
        node = self._bst.root
        while node:
            if jstr in node.value:   #if the word is in the tree 
                return node.value[jstr]
            else:
                if jstr > list(node.value.keys())[0]: #if the word value greater --> right node
                    node = node.right
                else:                                 #if the word value less --> left node
                    node = node.left
        return "No match" 



