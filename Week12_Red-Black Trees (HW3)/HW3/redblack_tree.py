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

    def subSearch(self, node, element):
        if node._element == None:
            return node
        elif node._element > element:
            return self.subSearch(node._left, element)
        elif self._root._element < element:
            return self.subSearch(node._right, element)
        elif node._element == element:
            return node
        
    # Search for the element in the red-black tree.
    # return: _Node object, or None if it's non-existing
    def search(self, element):
        if self._root._element > element:
            targetNode = self.subSearch(self._root._left, element)
            if targetNode._element == None:
                return None
            else: return targetNode
        elif self._root._element < element:
            targetNode = self.subSearch(self._root._right, element)
            if targetNode._element == None:
                return None
            else: return targetNode
        elif self._root._element == element:
            return self._root
        
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
        
    def singleRot(self, node): # Zig case
        if self.isLeft(node) == True:
            node._parent, node._right, node._parnet._left, node._parent._parent = node._parent._parent, node._parent, node._right, node._parnet._left
        elif self.isRight(node) == True:
            node._parent, node._right, node._parnet._left, node._parent._parent = node._right, node._parnet._left, node._parent._parent, node._parent
    
    def trinodeReconstruction(self, node):
        x = node
        y = node._parent
        z = y._parent
        if (self.isLeft(x) and self.isLeft(y)) or (self.isRight(x) and self.isRight(y)) == True: #Zig-Zig case
            self.singleRot(y)
        elif (self.isLeft(x) and self.isRight(y)) or (self.isRight(x) and self.isLeft(y)) == True: #Zig-Zag case
            self.singleRot(x)
            self.singleRot(y)
    
    def doubleRED(self, node):
        z = node
        v = node._parent
        w = self._sibiling(v)
        if w._color == self._Node.BLACK: # Case1
            self.trinodeReconstruction(z)
        elif w._color == self._Node.RED: # Case2
            w._color = self._Node.BLACK
            if w._parent != self._root:
                w._parent.color = self._Node.RED
        if w._parent._color == self._Node.RED:
                    self.doubleRED(targetNode)

    def insert(self, element):
        if len(self) == 0:
            self._root = self._Node(element, color=self._Node.BLACK)
            self._root._left = self._Node(None, parent=self._root, color=self._Node.BLACK)
            self._root._right = self._Node(None, parent=self._root, color=self._Node.BLACK)
            self._size = self._size + 1
        else:
            targetNode = self.search(element)
            if targetNode._element == None:
                targetNode._element = element
                targetNode._left = self._Node(None, parent=targetNode, color=self._Node.BLACK)
                targetNode._right = self._Node(None, parent=targetNode, color=self._Node.BLACK)
                targetNode._color = self._Node.RED
                self._size = self._size + 1
                if targetNode._parent._color == self._Node.RED:
                    self.doubleRED(targetNode)
            else:
                raise ValueError('Element already exist.')

    def delete(self, element):
        ## IMPLEMENT
        pass

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