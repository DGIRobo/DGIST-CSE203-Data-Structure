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
    def subSearch(self, node, element):
        if node._element > element:
            if node._left != None:
                return self.subSearch(node._left, element)
            else: return node
        elif node._element < element:
            if node._right != None:
                return self.subSearch(node._right, element)
            else: return node
        elif node._element == element:
            return node
        
    # Search for the element in the red-black tree.
    # return: _Node object, or None if it's non-existing
    def search(self, element):
        if self._root == None:
            return None
        else:
            targetNode = self.subSearch(self._root, element)
            if targetNode._element == element:
                return targetNode._element
            else:
                return None

    def isLeft(self, node):
        if node == self._root:
            return False
        elif node._parent._left == node:
            return True
        else: return False
        
    def isRight(self, node):
        if node == self._root:
            return False
        elif node._parent._right == node:
            return True
        else: return False
    
    def isBLACK(self, node):
        if node == None:
            return True
        elif node._color == self._Node.BLACK:
            return True
        else: return False
        
    def singleRot(self, node): # Zig case
        if self.isLeft(node) == True:
            x = node
            T2 = node._right
            y = node._parent
            z = node._parent._parent
            a = x._color
            b = y._color
            x._color = b
            y._color = a
            node._parent = z
            if z != None:
                if z._left == y:
                    z._left = x
                elif z._right == y:
                    z._right = x
            else: self._root = x
            node._right = y
            node._right._parent = x
            node._right._left =T2
            if T2 != None:
                T2._parent = y
            
        elif self.isRight(node) == True:
            y = node
            T2 = node._left
            x = node._parent
            z = node._parent._parent
            a = x._color
            b = y._color
            x._color = b
            y._color = a
            node._parent = z
            if z != None:
                if z._left == x:
                    z._left = y
                elif z._right == x:
                    z._right = y
            else: self._root = y
            node._left = x
            node._left._parent = y
            node._left._right = T2
            if T2 != None:
                T2._parent = x
    
    def trinodeReconstruction(self, node):
        x = node
        y = node._parent
        if (self.isLeft(x) and self.isLeft(y)) or (self.isRight(x) and self.isRight(y)) == True: #Zig-Zig case
            self.singleRot(y)
        elif (self.isLeft(x) and self.isRight(y)) or (self.isRight(x) and self.isLeft(y)) == True: #Zig-Zag case
            self.singleRot(x)
            self.singleRot(x)
    
    def doubleRED(self, node):
        z = node
        v = node._parent
        w = self._sibiling(v)
        if self.isBLACK(w) == True: # Case1
            self.trinodeReconstruction(z)
        elif self.isBLACK(w) == False: # Case2
            v._color = self._Node.BLACK
            w._color = self._Node.BLACK
            if w._parent != self._root:
                w._parent._color = self._Node.RED
                if self.isBLACK(w._parent._parent) == False:
                    self.doubleRED(w._parent)

    def insert(self, element):
        if len(self) == 0:
            self._root = self._Node(element, color=self._Node.BLACK)
            self._size = self._size + 1
        else:
            targetNode = self.subSearch(self._root, element)
            if targetNode._element != element:
                if targetNode._element > element:
                    targetNode._left = self._Node(element, parent=targetNode, color=self._Node.RED)
                    if self.isBLACK(targetNode) == False:
                        self.doubleRED(targetNode._left)
                else:
                    targetNode._right = self._Node(element, parent=targetNode, color=self._Node.RED)
                    if self.isBLACK(targetNode) == False:
                        self.doubleRED(targetNode._right) # recursive double red
                self._size = self._size + 1
            else: raise ValueError('Element already exist.')

    def doubleBLACK(self, parent, direction):
        z = parent
        if direction == 'LEFT': 
            Tlight = z._left 
            Theavy = z._right
        elif direction == 'RIGHT':
            Tlight = z._right
            Theavy = z._left
        if (self.isBLACK(Theavy) == True) and (self.isBLACK(Theavy._left) and self.isBLACK(Theavy._right) == True): # Case2
            if self.isBLACK(z) == False:
                z._color = self._Node.BLACK
                Theavy._color = self._Node.RED
            elif self.isBLACK(z) == True:
                Theavy._color = self._Node.RED
                if z._parent != None:
                    if z._parent._left == z:
                        self.doubleBLACK(z._parent, 'LEFT')
                    elif z._parent._right == z:
                        self.doubleBLACK(z._parent, 'RIGHT')
        elif (self.isBLACK(Theavy) == True) and ((self.isBLACK(Theavy._left) == False) or (self.isBLACK(Theavy._right) == False)): # Case1
            if self.isBLACK(Theavy._right) == False:
                if Theavy._right != None: Theavy._right._color = self._Node.BLACK
                self.trinodeReconstruction(Theavy._right)
            elif self.isBLACK(Theavy._left) == False:
                if Theavy._left != None: Theavy._left._color = self._Node.BLACK
                self.trinodeReconstruction(Theavy._left)
            z._color = self._Node.BLACK
        elif (self.isBLACK(Theavy) == False): # Case3
            self.singleRot(Theavy)
            if z._left == Tlight:
                self.doubleBLACK(z, 'LEFT')
            elif z._right == Tlight:
                self.doubleBLACK(z, 'RIGHT')
                
    def delete(self, element):
        targetNode = self.subSearch(self._root, element)
        if targetNode._element == element:
            answer = targetNode._element
            if targetNode._right == None:
                r = targetNode._left
                v = targetNode
                z = targetNode._parent
                if z == None:
                    self._root = r
                    if r != None: 
                        r._parent = None
                        r._color = self._Node.BLACK
                    self._size = self._size - 1
                elif z._left == v:
                    z._left = r
                    if r != None: r._parent = z
                    self._size = self._size - 1
                    if self.isBLACK(v) == True:
                        self.doubleBLACK(z, 'LEFT')
                elif z._right == v:
                    z._right = r
                    if r != None: r._parent = z
                    self._size = self._size - 1
                    if self.isBLACK(v) == True:
                        self.doubleBLACK(z, 'RIGHT')
            else:
                v = self._successor(targetNode)
                v._element, targetNode._element = targetNode._element, v._element
                if v._left != None:
                    r = v._left
                elif v._right != None:
                    r = v._right
                else: r = None
                z = v._parent
                if z._left == v:
                    z._left = r
                    if r != None: r._parent = z
                    self._size = self._size - 1
                    if self.isBLACK(v) == True:
                        self.doubleBLACK(z, 'LEFT')
                elif z._right == v:
                    z._right = r
                    if r != None: r._parent = z
                    self._size = self._size - 1
                    if self.isBLACK(v) == True:
                        self.doubleBLACK(z, 'RIGHT')
            return answer
        else: return None
        
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