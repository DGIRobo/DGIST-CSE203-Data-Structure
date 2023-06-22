class RedBlackTree():
    # Node class - DO NOT MODIFY
    class _Node:
        RED = object()
        BLACK = object()
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right', '_color' # streamline memory usage

        def __init__(self, element, parent=None, left=None, right=None, color=RED):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            self._color = color

    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size
    
    # Search for the element in the sub red-black tree whose root is given node.
    # return: _Node object whose element is given element if it's existing, or _Node object whose element is not given element and one of its children is None if it's non-existing
    def subSearch(self, node, element): # receive root node of the sub red-black tree and element to search 
        if node._element > element: # if given node's element is bigger than element to search
            if node._left != None: # and if given node's left child is not none
                return self.subSearch(node._left, element) # do subsearch again at the sub red-black tree whose root is given node's left child with given element to search.
            else: return node # if given node's left child is none then return the current node's position
        elif node._element < element: # if given node's element is smaller than element to search
            if node._right != None: # and if given node's right child is not none
                return self.subSearch(node._right, element) # do subsearch again at the sub red-black tree whose root is given node's right child with given element to search.
            else: return node # if given node's right child is none then return the current node's position
        elif node._element == element: # if given node's element is equal to element to search
            return node # return the current node's position
        
    # Search for the element in the red-black tree.
    # return: found _Node object's element if it is existing, or None if it's non-existing
    def search(self, element): # receive element to search 
        if self._root == None: # if root is none then this RB tree is empty
            return None # so return none
        else: # if root is not none
            targetNode = self.subSearch(self._root, element) # then do subsearch at the sub red-black tree whose root is root node with given element to search.
            if targetNode._element == element: # if the element of the result node of subsearch is equal to element to search
                return targetNode._element # return the element of the result node of subsearch
            else: # if the element of the result node of subsearch is not equal to element to search
                return None # then there is not finding element. so return None
    
    # Discriminate if the given node is a left child
    # return: True if the given node is a left child, False if the given node is not a left child
    def isLeft(self, node): # receive node to Discriminate
        if node == self._root: # if given node is root
            return False # then it is not left node, so return False
        elif node._parent._left == node: # if given node's parent's left link is connected to given node
            return True # then given node is left node, so return True
        else: return False # otherwise return False
    
    # Discriminate if the given node is a right child
    # return: True if the given node is a right child, False if the given node is not a right child
    def isRight(self, node): # receive node to Discriminate
        if node == self._root: # if given node is root
            return False # then it is not right node, so return False
        elif node._parent._right == node: # if given node's parent's right link is connected to given node
            return True # then given node is right node, so return True
        else: return False # otherwise return False
    
    # Discriminate if the given node's color is black
    # return: True if the given node's color is black, False if the given node's color is red
    def isBLACK(self, node): # receive node to Discriminate
        if node == None: # if node is none node 
            return True # then consider that's color is black, so return True
        elif node._color == self._Node.BLACK: # if node's color is black
            return True # then return true
        else: return False # otherwise that's color is red, so return False
        
    # Make single rotation reconstruction of the RB tree Based on the given node
    # return: there is no return value, only reconstruction the RB tree
    def singleRot(self, node): # Zig case
        if self.isLeft(node) == True: # if given node is left child
            x = node # set given node as x
            T2 = node._right # set given node's right child as T2
            y = node._parent # set given node's parent as y
            z = node._parent._parent # set given node's grandparent as z
            a = x._color # set x's color as a
            b = y._color # set y's color as b
            x._color = b # change x's color to y's
            y._color = a # change y's color to x's
            node._parent = z # change given node's parent to z
            if z != None: # if y was not root node
                if z._left == y: # then if z node's left node is y
                    z._left = x # change z node's left node to x
                elif z._right == y: # if z node's right node is y
                    z._right = x # change z node's right node to x
            else: self._root = x # if y was root node then change root node to x
            node._right = y # change given node's right child to y
            node._right._parent = x # change given node's right child's parent to x
            node._right._left =T2 # change given node's right child's left child to T2
            if T2 != None: # if T2 isnot none
                T2._parent = y # then have to change T2's parent to y
            
        elif self.isRight(node) == True: # if given node is right child
            y = node # set given node as y
            T2 = node._left # set given node's left child as T2
            x = node._parent # set given node's parent as x
            z = node._parent._parent # set given node's grandparent as z
            a = x._color # set x's color as a
            b = y._color # set y's color as b
            x._color = b # change x's color to y's
            y._color = a # change y's color to x's
            node._parent = z # change given node's parent to z
            if z != None: # if x was not root node
                if z._left == x: # then if z node's left node is x
                    z._left = y # change z node's left node to y
                elif z._right == x: # if z node's right node is x
                    z._right = y # change z node's right node to y
            else: self._root = y # if x was root node then change root node to y
            node._left = x # change given node's left child to x
            node._left._parent = y # change given node's left child's parent to y
            node._left._right = T2 # change given node's left child's right child to T2
            if T2 != None: # if T2 isnot none
                T2._parent = x # then have to change T2's parent to x
    
    # Make trinode reconstruction of the RB tree Based on the given node
    # return: there is no return value, only reconstruction the RB tree
    def trinodeReconstruction(self, node):
        x = node # set given node as x
        y = node._parent # set given node's parent as y
        if (self.isLeft(x) and self.isLeft(y)) or (self.isRight(x) and self.isRight(y)) == True: # if x, y, y's parent is in Zig-Zig case
            self.singleRot(y) # do single rotation at position y
        elif (self.isLeft(x) and self.isRight(y)) or (self.isRight(x) and self.isLeft(y)) == True: # if x, y, y's parent is in Zig-Zag case
            self.singleRot(x) # do single rotation at position x
            self.singleRot(x) # after that do sigle rotation again at position x
    
    # Fix double red conditions due to insertion
    # return: there is no return value, only fixing the double red condition of the RB tree
    def doubleRED(self, node):
        z = node # set given node as z
        v = node._parent # set given node's parent as v
        w = self._sibiling(v) # set v's sibiling as w
        if self.isBLACK(w) == True: # Case1: if w is black, this is reconstruction case
            self.trinodeReconstruction(z) # do trinode reconstruction based on the node z
        elif self.isBLACK(w) == False: # Case2: if w is red, this is recoloring case
            v._color = self._Node.BLACK # change v's color to black
            w._color = self._Node.BLACK # change w's color to black
            if w._parent != self._root: # if w's parent is not root
                w._parent._color = self._Node.RED # change w's parent's color to red
                if self.isBLACK(w._parent._parent) == False: # if w's grand parent's color is red
                    self.doubleRED(w._parent) # then this is in double red condition based on w's parent position, so fix it using recursion of double red function.
    
    # Inserting the new node whose element is given element
    # return: there is no return value, only inserting the new node whose element is given element to the RB tree
    def insert(self, element):
        if len(self) == 0: # if tree is empty
            self._root = self._Node(element, color=self._Node.BLACK) # then new node of given element have to insert to root position
            self._size = self._size + 1 # after successful insertion, have to plus the 1 to the size of the tree
        else: # if tree is not empty
            targetNode = self.subSearch(self._root, element) # do subsearch at the sub red-black tree whose root is root node with given element to search.
            if targetNode._element != element: # if the RB tree does not have the node of given element
                if targetNode._element > element: # if new element have to insert at the left child position of result node of subsearch operation
                    targetNode._left = self._Node(element, parent=targetNode, color=self._Node.RED) # insert new node whose element is given element and whose color is red to the left child position of result node of subsearch operation
                    if self.isBLACK(targetNode) == False: # if inserted node's parent's color is red
                        self.doubleRED(targetNode._left) # this is in double red condition based on inserted node's position, so fix it using double red function. 
                else: # if new element have to insert at the right child position of result node of subsearch operation
                    targetNode._right = self._Node(element, parent=targetNode, color=self._Node.RED) # insert new node whose element is given element and whose color is red to the right child position of result node of subsearch operation
                    if self.isBLACK(targetNode) == False: # if inserted node's parent's color is red
                        self.doubleRED(targetNode._right) # this is in double red condition based on inserted node's position, so fix it using double red function.
                self._size = self._size + 1 # after successful insertion, have to plus the 1 to the size of the tree
            else: raise ValueError('Element already exist.') # if the RB tree has already the node of given element, raise Element already exist Error
    
    # Fix double black conditions due to deletion
    # return: there is no return value, only fixing the double black condition of the RB tree
    def doubleBLACK(self, parent, direction):
        z = parent # set given node as z
        if direction == 'LEFT': # if given direction hint is left, this means double black point is left child of z
            Tlight = z._left # then set z's left child as Tlight
            Theavy = z._right # set z's right child as Theavy
        elif direction == 'RIGHT': # if given direction hint is right, this means double black point is right child of z
            Tlight = z._right # then set z's right child as Tlight
            Theavy = z._left # set z's left child as Theavy
        if (self.isBLACK(Theavy) == True) and (self.isBLACK(Theavy._left) and self.isBLACK(Theavy._right) == True): # Case2: Theavy's color is black and Theavy's children's color is all black
            if self.isBLACK(z) == False: # if z's color is red
                z._color = self._Node.BLACK # change z's color to black
                Theavy._color = self._Node.RED # change Theavy's color to red, after this double black condition is fixed
            elif self.isBLACK(z) == True: # if z's color is black
                Theavy._color = self._Node.RED # change Theavy's color to red, after this double black condition is propagate to z node
                if z._parent != None: # if z is not root node
                    if z._parent._left == z: # if z is left child
                        self.doubleBLACK(z._parent, 'LEFT') # this is in double black condition based on z node's position(z node's parent's left child's position), so fix it using double black function. 
                    elif z._parent._right == z: # if z is right child
                        self.doubleBLACK(z._parent, 'RIGHT') # this is in double black condition based on z node's position(z node's parent's right child's position), so fix it using double black function. 
        elif (self.isBLACK(Theavy) == True) and ((self.isBLACK(Theavy._left) == False) or (self.isBLACK(Theavy._right) == False)): # Case1: Theavy's color is black and Theavy's one of the children is red node
            if self.isBLACK(Theavy._right) == False: # if Theavy's right child's color is red
                if Theavy._right != None: Theavy._right._color = self._Node.BLACK # if Theavy's right child is not None, change its color to black
                self.trinodeReconstruction(Theavy._right) # do trinode reconstruction based on the Theavy's right child
            elif self.isBLACK(Theavy._left) == False: # if Theavy's left child's color is red
                if Theavy._left != None: Theavy._left._color = self._Node.BLACK # if Theavy's left child is not None, change its color to black
                self.trinodeReconstruction(Theavy._left) # do trinode reconstruction based on the Theavy's left child
            z._color = self._Node.BLACK # change z's color to black
        elif (self.isBLACK(Theavy) == False): # Case3: Theavy's color is red
            self.singleRot(Theavy) # do single rotation based on Theavy position
            if z._left == Tlight: # if Tlight is left child
                self.doubleBLACK(z, 'LEFT') # this is in double black condition based on z node's position(z node's parent's left child's position), so fix it using double black function. 
            elif z._right == Tlight: # if Tlight is right child
                self.doubleBLACK(z, 'RIGHT') # this is in double black condition based on z node's position(z node's parent's right child's position), so fix it using double black function. 
    
    # Delete the node of given element is exist
    # return: deleted node's element if the node of given element is exist, none if the node of given element is not exist.
    def delete(self, element):
        targetNode = self.subSearch(self._root, element) # do subsearch at the sub red-black tree whose root is root node with given element to search.
        if targetNode._element == element: # if the node whose element is given element is exist in the RB tree
            answer = targetNode._element # save the return value in advance
            if targetNode._right == None: # if the node whose element is given element have none node at right child position
                r = targetNode._left # set left child of the node whose element is given element as r
                v = targetNode # set the node whose element is given element as v
                z = targetNode._parent # set the parent of the node whose element is given element as z
                if z == None: # if the node whose element is given element is root
                    self._root = r # change the root to r
                    if r != None: # if r is not none node
                        r._parent = None # change r's parent to none
                        r._color = self._Node.BLACK # change r's color to black
                    self._size = self._size - 1 # after successful deletion, have to minus the 1 to the size of the tree
                elif z._left == v: # if v is left child of z
                    z._left = r # change z's left child to r
                    if r != None: r._parent = z # if r is not none node, then change r's parent to z
                    self._size = self._size - 1 # after successful deletion, have to minus the 1 to the size of the tree
                    if self.isBLACK(v) == True: # if v's color was black
                        self.doubleBLACK(z, 'LEFT') # this is in double black condition based on z node's position(z node's parent's left child's position), so fix it using double black function. 
                elif z._right == v: # if v is right child of z
                    z._right = r # change z's right child to r
                    if r != None: r._parent = z # if r is not none node, then change r's parent to z
                    self._size = self._size - 1 # after successful deletion, have to minus the 1 to the size of the tree
                    if self.isBLACK(v) == True: # if v's color was black
                        self.doubleBLACK(z, 'RIGHT') # this is in double black condition based on z node's position(z node's parent's right child's position), so fix it using double black function. 
            else: # if right child of the node whose element is given element is not none node
                v = self._successor(targetNode) # find successor node of the node whose element is given element, and set that successor node as v
                v._element, targetNode._element = targetNode._element, v._element # swap element between v and the node whose element is given element
                if v._left != None: # if v's left child is not none node
                    r = v._left # set v's left child as r
                elif v._right != None: # if v's right child is not none node
                    r = v._right # set v's right child as r
                else: r = None # if v's children are none nodes, then set none as r
                z = v._parent # set v's parent as z
                if z._left == v: # if v is left child of z
                    z._left = r # then change z's left child to r
                    if r != None: r._parent = z # if r is not none node, then change r's parent to z
                    self._size = self._size - 1 # after successful deletion, have to minus the 1 to the size of the tree
                    if self.isBLACK(v) == True: # if v's color was black
                        self.doubleBLACK(z, 'LEFT') # this is in double black condition based on z node's position(z node's parent's left child's position), so fix it using double black function. 
                elif z._right == v: # if v is right child of z
                    z._right = r # then change z's right child to r
                    if r != None: r._parent = z # if r is not none node, then change r's parent to z
                    self._size = self._size - 1 # after successful deletion, have to minus the 1 to the size of the tree
                    if self.isBLACK(v) == True: # if v's color was black
                        self.doubleBLACK(z, 'RIGHT') # this is in double black condition based on z node's position(z node's parent's right child's position), so fix it using double black function. 
            return answer # return pre-stored return value
        else: return None # if the node whose element is given element is not exist in the RB tree, Return none
        
    # BONUS FUNCTIONS -- use them freely if you want
    def _is_black(self, node):
        return node == None or node._color == self._Node.BLACK

    def _successor(self, node):
        successor = node._right
        while successor._left != None:
            successor = successor._left
        return successor

    def _sibiling(self, node):
        parent = node._parent

        if parent._left == node:
            return parent._right
        else:
            return parent._left

    # Supporting functions -- DO NOT MODIFY BELOW
    def display(self):
        print('--------------')
        self._display(self._root, 0)
        print('--------------')

    def _display(self, node, depth):
        if node == None:
            return

        if node._right != None:
            if node._right._parent != node:
                print("parent-child error - ", node._element, node._right._element)
            self._display(node._right, depth+1)

        if node == self._root:
            symbol = '>'
        else:
            symbol = '*'

        if node._color == self._Node.RED:
            colorstr = 'R'
        else:
            colorstr = 'B'
        print(f'{"    "*depth}{symbol} {node._element}({colorstr})')
        if node._left != None:
            if node._left._parent != node:
                print("parent error - ", node._element, node._left._element)
            self._display(node._left, depth+1)

    def inorder_traverse(self):
        return self._inorder_traverse(self._root)

    def _inorder_traverse(self, node):
        if node == None:
            return []
        else:
            return self._inorder_traverse(node._left) + [node._element] + self._inorder_traverse(node._right)

    def check_tree_property_silent(self):
        if self._root == None:
            return True

        if not self._check_parent_child_link(self._root):
            print('Parent-child link is violated')
            return False
        if not self._check_binary_search_tree_property(self._root):
            print('Binary search tree property is violated')
            return False
        if not self._root._color == self._Node.BLACK:
            print('Root black property is violated')
            return False
        if not self._check_double_red_property(self._root):
            print('Internal property is violated')
            return False
        if self._check_black_height_property(self._root) == 0:
            print('Black height property is violated')
            return False
        return True

    def check_tree_property(self):
        if self._root == None:
            print('Empty tree')
            return

        print('Checking binary search tree property...')
        self._check_parent_child_link(self._root)
        self._check_binary_search_tree_property(self._root)
        print('Done')

        print('Checking root black property...')
        print(self._root._color == self._Node.BLACK)
        print('Done')

        print('Checking internal property (=no double red)...')
        self._check_double_red_property(self._root)
        print('Done')

        print('Checking black height property...')
        self._check_black_height_property(self._root)
        print('Done')

    def _check_parent_child_link(self, node):
        if node == None:
            return True

        test_pass = True

        if node._right != None:
            if node._right._parent != node:
                print("parent-child error - ", node._element, node._right._element)
            test_pass = test_pass and self._check_parent_child_link(node._right)
        if node._left != None:
            if node._left._parent != node:
                print("parent error - ", node._element, node._left._element)
            test_pass = test_pass and self._check_parent_child_link(node._left)

        return test_pass

    def _check_binary_search_tree_property(self, node):
        if node == None:
            return True

        test_pass = True

        if node._left != None:
            if node._left._element > node._element:
                print("Binary search tree property error - ", node._element, node._left._element)
                return False
            test_pass = test_pass and self._check_binary_search_tree_property(node._left)

        if node._right != None:
            if node._right._element < node._element:
                print("Binary search tree property error - ", node._element, node._right._element)
                return False
            test_pass = test_pass and self._check_binary_search_tree_property(node._right)

        return test_pass

    def _check_double_red_property(self, node):
        if node == None:
            return True

        test_pass = True

        if node._color == self._Node.RED:
            if node._left != None:
                if node._left._color == self._Node.RED:
                    print("Double red property error - ", node._element, node._left._element)
                    return False
            if node._right != None:
                if node._right._color == self._Node.RED:
                    print("Double red property error - ", node._element, node._right._element)
                    return False

        if node._left != None:
            test_pass = test_pass and self._check_double_red_property(node._left)
        if node._right != None:
            test_pass = test_pass and self._check_double_red_property(node._right)

        return test_pass


    def _check_black_height_property(self, node):
        if node == None:
            return 1

        left_height = self._check_black_height_property(node._left)
        right_height = self._check_black_height_property(node._right)

        if left_height != right_height:
            print("Black height property error - ", node._element, left_height, right_height)
            return 0

        if node._color == self._Node.BLACK:
            return left_height + 1
        else:
            return left_height