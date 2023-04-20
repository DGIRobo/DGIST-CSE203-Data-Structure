from tree import Tree

class LinkedTree(Tree):
    """Linked representation of a general tree structure."""

    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_children' # streamline memory usage

        def __init__(self, element, parent=None, children=None):
            self._element = element # the element of this node
            self._parent = parent # a link towards the parent
            if children == None:
                self._children = []
            else:
                self._children = children # list of links towards children nodes

    #-------------------------- nested Position class --------------------------
    class Position(Tree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    #------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:            # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    #-------------------------- Tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    #-------------------------- public accessors --------------------------    
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        return len(node._children)
    
    def children(self, p):
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size    
    
    #-------------------------- nonpublic mutators --------------------------
    def _add_root(self, e):
        """
        This method places element 'e' at the root of an empty tree and returns the new Position.
        (use self._make_position(node) to pack the Node object into a position.)
        If the tree is not empty, it raises a ValueError with the message 'Root exists'.
        
        :param e: The element to be placed at the root of the tree
        :return: A new Position object representing the root node with the element 'e'
        :raises ValueError: If the tree is not empty, a ValueError is raised with the message 'Root exists'
        """
        raise NotImplementedError('HOMEWORK 2-1')

    def _add_child(self, p, e):
        """
        This method creates a new child node for the given Position 'p' and stores the element 'e'.
        (use self._validate(position) to unpack the node inside the position.)
        It returns the Position of the newly created node (use self._make_position(new_node)).
        
        :param p: The Position object representing the parent node
        :param e: The element to be stored in the new child node
        :return: A new Position object representing the child node with the element 'e'
        """
        raise NotImplementedError('HOMEWORK 2-1')

    def _replace(self, p, e):
        """
        This method replaces the element at the given Position 'p' with the new element 'e'.
        It returns the old element that was replaced.
        
        :param p: The Position object representing the node whose element will be replaced
        :param e: The new element to replace the current element at position 'p'
        :return: The old element that was replaced at position 'p'
        """        
        raise NotImplementedError('HOMEWORK 2-1')

    def _delete(self, p):
        """
        This method deletes the node at the given Position 'p' and returns the element that had been stored at Position 'p'.

        If the position 'p' has any children, a ValueError is raised.

        :param p: The Position object representing the node to be deleted
        :return: The element that was stored at the deleted position 'p'
        :raises ValueError: If the position 'p' has any children, a ValueError is raised
        """
        raise NotImplementedError('HOMEWORK 2-1')