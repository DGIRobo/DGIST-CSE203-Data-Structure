from tree import Tree

class LinkedTree(Tree): # Tree의 Abstract Base Class를 상속받아서 LinkedTree라는 구체적인 Tree의 속성과 method 구현
    """Linked representation of a general tree structure."""

    #-------------------------- nested _Node class --------------------------
    class _Node: # Tree에서 element를 저장하고, parent와 children의 position을 저장하고 있는 _Node라는 객체 정의
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_children' # _Node라는 객체는 _element와 _parent, _children이라는 속성이 pair를 이루며 저장되어 있는 객체로 설정

        def __init__(self, element, parent=None, children=None): # _Node는 element, parent, children값을 받아 생성되도록 되어 있지만 parent나 children은 따로 주어지지 않으면 None으로 두고 생성하도록 함. 
            self._element = element # 받은 element값을 node의 _element라는 속성에 저장하도록 함.
            self._parent = parent # 받은 parent라는 해당 node의 parent node를 node의 _parent라는 속성에 저장하도록 함.
            if children == None: 
                self._children = [] # children은 이론적으로 무한정 가질수 있지만 node가 생성될 시 주어지지 않으면 해당 node의 children node들을 모아둘 빈 리스트를 만들어두도록 한다.
            else:
                self._children = children # node가 생성될 시 해당 node의 children node가 될 node들을 모아만든 list가 children이라는 인자로 주어지면 해당 리스트를 node의 _children이라는 속성에 저장하도록 함.

    #-------------------------- nested Position class --------------------------
    class Position(Tree.Position): # Tree를 구성하는 Node에 접근하기 위한 Position이라는 Class 구현
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node): # Position은 해당 Position이 어떤 Tree를 지칭하는 Position인지를 구분하기 위한 container라는 값과 어떤 node를 지칭하는 Position인지를 구분하기 위한 node라는 값을 받아 생성되도록 되어 있다.
            """Constructor should not be invoked by user."""
            self._container = container # 어떤 Tree를 지칭하는 Position인지를 구분하기 위한 container라는 값을 받아 Position의 _container라는 속성에 저장하도록 함.
            self._node = node # 어떤 node를 지칭하는 Position인지를 구분하기 위한 node라는 값을 받아 Position의 _node라는 속성에 저장하도록 함.

        def element(self): # Position이라는 Class에 정의된 method로 Position에 있는 Node에 접근하여 Node의 element를 가져오는 method.
            """Return the element stored at this Position."""
            return self._node._element # Position이 가리키는 node에 접근하여 _element라는 속성을 반환하도록 한다.

        def __eq__(self, other): # Position이라는 Class에 정의된 method로 어떤 Position과 인자로 받은 node가 동일한 Position 객체인지 판별하여 동일하면 True를 리턴하도록 하는 method.
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node #비교하고자 하는 Position의 type과 그 Position이 가리키는 node가 인자로 받은 Position의 type과 그 인자로 받은 Position이 가리키는 node와 각각 같으면 True 둘 중 하나라도 다를 시 False를 리턴하도록 한다.

    #------------------------------- utility methods -------------------------------
    def _validate(self, p): # 입력된 position값이 position 객체가 맞는지, 해당 Tree를 가리키는 position이 맞는지, 삭제된 node의 position이 아닌지 판별하고 어떤 경우에도 해당하지 않는 경우 입력된 position값이 가리키는 node를 반환하는 method
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type') # 들어온 p값이 position 객체가 아니면 p가 position 객체가 아니라는 TypeError 출력
        if p._container is not self:
            raise ValueError('p does not belong to this container') # 들어온 p값이 self가 지칭하는 Tree에서 사용되는 Position값이 아닐 때, 해당 Tree에 해당 position을 가진 node가 없다는 ValueError 출력
        if p._node._parent is p._node:            # convention for deprecated nodes
            raise ValueError('p is no longer valid') # 들어온 p값이 이미 삭제된 node를 지칭할 경우 해당 position값은 더이상 사용할 수 없다는 ValueError 출력
        return p._node # 아무런 문제가 없는 position값인 경우 입력된 position값이 가리키는 node를 반환

    def _make_position(self, node): # 입력된 node의 position 객체를 만들어 반환하는 method.
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None # 입력된 node가 None이면 Position 객체가 아닌 None을 리턴하고, 입력된 node가 있으면 그 node를 지칭하는 Position 객체를 생성하여 그 Position 객체를 리턴함.

    #-------------------------- Tree constructor --------------------------
    def __init__(self): # LinkedTree라는 객체가 생성되면 해당 객체가 다음의 두가지 속성을 가지도록 함.
        """Create an initially empty binary tree."""
        self._root = None # 해당 객체, 처음 만들어진 LinkedTree는 _root라는 속성을 가지고 처음에는 어떤 node도 없기 때문에 초기값은 None으로 지정함.
        self._size = 0 # 해당 객체, 처음 만들어진 LinkedTree는 _size라는 속성을 가지고 처음에는 어떤 node도 없기 때문에 초기값은 0으로 지정함.

    #-------------------------- public accessors --------------------------    
    def root(self): # Tree라는 Class에 정의된 method로 Tree의 root에 위치한 node의 position을 리턴하는 method이다. 
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root) # Tree의 ABC에서는 구체적으로 구현하지 않았지만 여기에서는 Tree의 root node의 position 객체를 만들어서 리턴하도록 구체적으로 구현되어 있다.

    def parent(self, p): # Tree라는 Class에 정의된 method로 Tree에서 position p를 받으면 그 position에 위치한 node의 parent의 position을 리턴하는 method이다. 
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p) # 우선 입력받은 position 객체 p가 타당한 position 객체인지 확인한다.
        return self._make_position(node._parent) # Tree의 ABC에서는 구체적으로 구현하지 않았지만 여기에서는 입력받은 position p가 가리키는 node의 parent node의 position 객체를 만들어서 리턴하도록 구체적으로 구현되어 있다.

    def num_children(self, p): # Tree라는 Class에 정의된 method로 Tree에서 position p를 받으면 그 position에 위치한 node가 가진 children의 총 갯수를 리턴하는 method이다. 
        """Return the number of children of Position p."""
        node = self._validate(p) # 우선 입력받은 position 객체 p가 타당한 position 객체인지 확인한다.
        return len(node._children) # Tree의 ABC에서는 구체적으로 구현하지 않았지만 여기에서는 입력받은 position p가 가리키는 node의 children들의 position들을 담고 있는 _children이라는 속성(리스트 자료형이다.)에 접근해서 그 리스트의 속성을 리턴하는 것으로 그 position p에 위치한 node가 가진 children의 총 갯수를 리턴한다.
    
    def children(self, p): # Tree라는 Class에 정의된 method로 Tree에서 position p를 받으면 그 position에 위치한 node의 child들의 position을 차례로 뽑아서 iterative하게 리턴하는 method이다.
        node = self._validate(p) # 우선 입력받은 position 객체 p가 타당한 position 객체인지 확인한다.
        for child in node._children:
            yield self._make_position(child) # Tree의 ABC에서는 구체적으로 구현하지 않았지만 여기에서는 입력받은 position p가 가리키는 node의 children들의 position들을 담고 있는 _children이라는 속성(리스트 자료형이다.)에 접근해서 그 리스트의 값을 하나씩 빼서 리턴하는 것으로 그 position p에 위치한 node가 가진 children을 iterative하게 리턴한다.

    def __len__(self): # Tree라는 Class에 정의된 method로 Tree가 저장하고 있는 element의 갯수를 리턴하는 method.
        """Return the total number of elements in the tree."""
        return self._size # LinkedTree라는 객체의 속성인 _size(integer 값)에 접근해서 해당 값을 리턴한다. 해당 값은 add시 +1이 되고 delete시 -1이 되는 식으로 따로 관리된다.
    
    #-------------------------- nonpublic mutators --------------------------
    def _add_root(self, e): # Tree라는 Class에 정의된 method로 Tree의 root node에 들어갈 element e를 받아 Tree의 root node를 생성하고 root node의 position을 리턴하는 method이다.
        """
        This method places element 'e' at the root of an empty tree and returns the new Position.
        (use self._make_position(node) to pack the Node object into a position.)
        If the tree is not empty, it raises a ValueError with the message 'Root exists'.
        
        :param e: The element to be placed at the root of the tree
        :return: A new Position object representing the root node with the element 'e'
        :raises ValueError: If the tree is not empty, a ValueError is raised with the message 'Root exists'
        """
        if self.is_empty() == False: raise ValueError('Root exists') # Tree에 이미 값이 들어가 있는 상태이면 root가 이미 존재하므로 Error를 출력한다.
        self._root = self._Node(e) # LinkedTree라는 객체의 속성인 _root에 접근해서 해당 값에 root가 될 node를 만들어 할당한다.
        self._size += 1 # LinkedTree라는 객체에 새 node를 1개 만들어 자료를 저장했으므로 _size(integer 값)에 접근해서 해당 값을 +1 한다.
        return self._make_position(self._root) # _make_position method를 통해 새로 만든 root node의 position을 만들어 리턴한다.

    def _add_child(self, p, e): # Tree라는 Class에 정의된 method로 Tree의 p라는 position에 있는 node에 접근해서 그 node의 child node를 새로 생성하고 그 child node의 element로 e를 저장한 뒤, 새로 생성한 node의 position을 리턴하는 method이다.
        """
        This method creates a new child node for the given Position 'p' and stores the element 'e'.
        (use self._validate(position) to unpack the node inside the position.)
        It returns the Position of the newly created node (use self._make_position(new_node)).
        
        :param p: The Position object representing the parent node
        :param e: The element to be stored in the new child node
        :return: A new Position object representing the child node with the element 'e'
        """
        targetNode = self._validate(p) # 우선 입력받은 position 객체 p가 타당한 position 객체인지 확인하고 문제가 없다면 해당 position의 node를 받는다.
        newChild = self._Node(e, targetNode) # element를 e로 하고 parent를 p position에 위치한 node로 하는 새 node를 생성한다.
        targetNode._children.append(newChild) # 생성한 node를 p position에 위치한 node의 _children 속성에 추가하여 새로 생성한 node가 p position에 위치한 node의 child임을 설정한다.
        self._size += 1 # LinkedTree라는 객체에 새 node를 1개 만들어 자료를 저장했으므로 _size(integer 값)에 접근해서 해당 값을 +1 한다.
        return self._make_position(targetNode._children[-1]) # _make_position method를 통해 새로 만든 node의 position을 만들어 리턴한다.

    def _replace(self, p, e): # Tree라는 Class에 정의된 method로 Tree의 p라는 position에 있는 node에 접근해서 그 node의 element를 새 element e로 바꾸고 저장되어 있던 기존 element를 리턴하는 method이다. 
        """
        This method replaces the element at the given Position 'p' with the new element 'e'.
        It returns the old element that was replaced.
        
        :param p: The Position object representing the node whose element will be replaced
        :param e: The new element to replace the current element at position 'p'
        :return: The old element that was replaced at position 'p'
        """        
        targetNode = self._validate(p) # 우선 입력받은 position 객체 p가 타당한 position 객체인지 확인하고 문제가 없다면 해당 position의 node를 받는다.
        oldElement = targetNode._element # position p에 위치한 node에 접근해서 그 node의 기존 element를 받아서 다른 곳에 저장해둔다.
        targetNode._element = e # position p에 위치한 node의 element를 입력받은 인자 e로 바꾼다.
        return oldElement # 미리 다른 곳에 저장해두었던 node의 기존 element를 리턴한다.

    def _delete(self, p): # Tree라는 Class에 정의된 method로 Tree의 p라는 position에 있는 node에 접근해서 그 node를 제거하고 저장되어 있던 element를 리턴하는 method이다. 
        """
        This method deletes the node at the given Position 'p' and returns the element that had been stored at Position 'p'.

        If the position 'p' has any children, a ValueError is raised.

        :param p: The Position object representing the node to be deleted
        :return: The element that was stored at the deleted position 'p'
        :raises ValueError: If the position 'p' has any children, a ValueError is raised
        """
        if self.num_children(p) != 0: raise ValueError # Tree의 p라는 position에 있는 node가 제거 가능하려면 그 node는 children을 가지면 안되기 때문에 해당 node가 children을 가지면 ValueError를 출력한다.
        removedElement = p.element() # position p에 위치한 node에 접근해서 그 node의 기존 element를 받아서 다른 곳에 저장해둔다.
        if p._node == self._root:
            self._root = None # position p에 위치한 node가 root node이면 LinkedTree라는 객체의 속성인 _root에 접근해서 해당 값에 None을 할당한다.
        else: 
            p._node._parent._children.remove(p._node) # position p에 위치한 node가 root node가 아니면 그 node의 parent node에 접근해서 parent node의 _children 속성에서 삭제대상인 node를 제거한다.
        p._node._parent = p._node # 제거되어 Garbage Data가 된 Node는 Node의 _parent 속성이 자기 자신을 가리키도록 만들어주어야 하므로, 이를 구현하였다.
        self._size -= 1 # LinkedTree라는 객체에 있던 node를 1개 제거했으므로 _size(integer 값)에 접근해서 해당 값을 -1 한다.
        return removedElement # 미리 다른 곳에 저장해두었던 제거된 node의 element를 리턴한다.
            