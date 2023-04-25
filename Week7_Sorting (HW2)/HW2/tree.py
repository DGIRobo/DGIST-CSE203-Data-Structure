# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#        Data Structures and Algorithms in Python
#        Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#        John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.    If not, see <http://www.gnu.org/licenses/>.

import collections

class Tree: # Tree의 Abstract Base Class 정의
    """Abstract base class representing a tree structure."""

    #------------------------------- nested Position class -------------------------------
    class Position: # Tree를 구성하는 Node에 접근하기 위한 Position이라는 Class 구현
        """An abstraction representing the location of a single element within a tree.

        Note that two position instaces may represent the same inherent location in a tree.
        Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when testing
        equivalence of positions.
        """

        def element(self): # Position이라는 Class에 정의된 method로 Position에 있는 Node에 접근하여 Node의 element를 가져오는 method. 하지만 이 파일은 Tree의 ABC를 정의하기 때문에 구체적인 구현은 하지 않고 정의가 필요한 method들을 정의만 해둔 상태이다.
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass') # 구체적인 구현 없이 정의가 필요한 method들을 정의만 해둔 상태로 이 Tree의 ABC를 상속하여 Tree를 구체적으로 구현할 때 이 method를 구현해주어야 한다. 구현이 되지 않았을 경우에 대비하여 NotImplementedError를 설정해주었다.

        def __eq__(self, other): # Position이라는 Class에 정의된 method로 어떤 Position과 인자로 받은 node가 동일한 Position 객체인지 판별하여 동일하면 True를 리턴하도록 하는 method. 하지만 이 파일은 Tree의 ABC를 정의하기 때문에 구체적인 구현은 하지 않고 정의가 필요한 method들을 정의만 해주었다.
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass') # 구체적인 구현 없이 정의가 필요한 method들을 정의만 해둔 상태로 이 Tree의 ABC를 상속하여 Tree를 구체적으로 구현할 때 이 method를 구현해주어야 한다. 구현이 되지 않았을 경우에 대비하여 NotImplementedError를 설정해주었다.

        def __ne__(self, other): # Position이라는 Class에 정의된 method로 어떤 Position과 인자로 받은 node가 동일하지 않은 Position 객체인지 판별하여 동일하지 않으면 True를 리턴하도록 하는 method. 하지만 이 파일은 Tree의 ABC를 정의하기 때문에 구체적인 구현은 하지 않고 정의가 필요한 method들을 정의만 해주었다.
            """Return True if other does not represent the same location."""
            return not (self == other)  # not (self == other)의 결과값을 리턴하도록 함으로써 위의 __eq__(self, other) method가 정상적으로 구현되면 해당 method를 이용해서 자동으로 구현되도록 설정해두었다.

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self): # Tree라는 Class에 정의된 method로 Tree의 root에 위치한 node의 position을 리턴하는 method이다. 하지만 이 파일은 Tree의 ABC를 정의하기 때문에 구체적인 구현은 하지 않고 정의가 필요한 method들을 정의만 해주었다.
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass') # 구체적인 구현 없이 정의가 필요한 method들을 정의만 해둔 상태로 이 Tree의 ABC를 상속하여 Tree를 구체적으로 구현할 때 이 method를 구현해주어야 한다. 구현이 되지 않았을 경우에 대비하여 NotImplementedError를 설정해주었다.

    def parent(self, p): # Tree라는 Class에 정의된 method로 Tree에서 position p를 받으면 그 position에 위치한 node의 parent의 position을 리턴하는 method이다. 하지만 이 파일은 Tree의 ABC를 정의하기 때문에 구체적인 구현은 하지 않고 정의가 필요한 method들을 정의만 해주었다.
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass') # 구체적인 구현 없이 정의가 필요한 method들을 정의만 해둔 상태로 이 Tree의 ABC를 상속하여 Tree를 구체적으로 구현할 때 이 method를 구현해주어야 한다. 구현이 되지 않았을 경우에 대비하여 NotImplementedError를 설정해주었다.

    def num_children(self, p): # Tree라는 Class에 정의된 method로 Tree에서 position p를 받으면 그 position에 위치한 node가 가진 children의 총 갯수를 리턴하는 method이다. 하지만 이 파일은 Tree의 ABC를 정의하기 때문에 구체적인 구현은 하지 않고 정의가 필요한 method들을 정의만 해주었다.
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass') # 구체적인 구현 없이 정의가 필요한 method들을 정의만 해둔 상태로 이 Tree의 ABC를 상속하여 Tree를 구체적으로 구현할 때 이 method를 구현해주어야 한다. 구현이 되지 않았을 경우에 대비하여 NotImplementedError를 설정해주었다.

    def children(self, p): # Tree라는 Class에 정의된 method로 Tree에서 position p를 받으면 그 position에 위치한 node의 child들의 position을 차례로 뽑아서 iterative하게 리턴하는 method이다. 하지만 이 파일은 Tree의 ABC를 정의하기 때문에 구체적인 구현은 하지 않고 정의가 필요한 method들을 정의만 해주었다.
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass') # 구체적인 구현 없이 정의가 필요한 method들을 정의만 해둔 상태로 이 Tree의 ABC를 상속하여 Tree를 구체적으로 구현할 때 이 method를 구현해주어야 한다. 구현이 되지 않았을 경우에 대비하여 NotImplementedError를 설정해주었다.

    def __len__(self): # Tree라는 Class에 정의된 method로 Tree가 저장하고 있는 element의 갯수를 리턴하는 method. 하지만 이 파일은 Tree의 ABC를 정의하기 때문에 구체적인 구현은 하지 않고 정의가 필요한 method들을 정의만 해주었다.
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass') # 구체적인 구현 없이 정의가 필요한 method들을 정의만 해둔 상태로 이 Tree의 ABC를 상속하여 Tree를 구체적으로 구현할 때 이 method를 구현해주어야 한다. 구현이 되지 않았을 경우에 대비하여 NotImplementedError를 설정해주었다.

    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p): # Tree라는 Class에 정의된 method로 Tree에서 position p를 받으면 그 position에 위치한 node가 root인지 아닌지 판별하여 root이면 True를 리턴하는 method이다. 
        """Return True if Position p represents the root of the tree."""
        return self.root() == p # self.root() == p의 결과값을 리턴하도록 함으로써 위의 root(self) method가 정상적으로 구현되면 해당 method를 이용해서 자동으로 구현되도록 설정해두었다.

    def is_leaf(self, p): # Tree라는 Class에 정의된 method로 Tree에서 position p를 받으면 그 position에 위치한 node가 leaf인지 아닌지 판별하여 leaf이면 True를 리턴하는 method이다. 
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0 # self.num_children(p) == 0의 결과값을 리턴하도록 함으로써 위의 num_children(self, p) method가 정상적으로 구현되면 해당 method를 이용해서 자동으로 구현되도록 설정해두었다.

    def is_empty(self): # Tree라는 Class에 정의된 method로 Tree에 저장된 element의 갯수가 0개이면 True를 리턴하도록 하는 method이다. 
        """Return True if the tree is empty."""
        return len(self) == 0 # len(self) == 0의 결과값을 리턴하도록 함으로써 위의 __len__(self) method가 정상적으로 구현되면 해당 method를 이용해서 자동으로 구현되도록 설정해두었다.

    def depth(self, p): # Tree라는 Class에 정의된 method로 Tree에서 position p를 받으면 그 position에 위치한 node의 depth(ancestor의 수)를 리턴하는 method이다. 
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p): 
            return 0 # initial case로 root의 depth를 0으로 설정해두었다.
        else: 
            return 1 + self.depth(self.parent(p)) # general case로 p position에 위치한 node는 recursive하게 그 node의 parent의 depth에 +1을 하여 가져오도록 구현되었다. 따라서 위의 parent(self, p) method가 정상적으로 구현되면 해당 method를 이용해서 자동으로 구현되도록 설정해두었다.

    def _height(self, p): # Tree라는 Class에 정의된 method로 position p를 받으면 그 position에 위치한 node의 height를 리턴하는 method이다. 
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0 # initial case로 leaf의 height를 0으로 설정해두었다.
        else:
            return 1 + max(self._height(c) for c in self.children(p)) # general case로 p position에 위치한 node는 recursive하게 그 node의 children 중 하나의 height에 +1을 하여 가져오도록 구현되었다. 따라서 위의 children(self, p) method가 정상적으로 구현되면 해당 method를 이용해서 자동으로 구현되도록 설정해두었다.

    def height(self, p=None): # Tree라는 Class에 정의된 method로 position p를 받으면 그 position에 위치한 node의 height를 리턴하는 method이다. 
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root() # p값이 들어오지 않으면 Tree 자체의 Height를 가져오기 위해 p를 root의 position으로 하고 _height(self, p)를 시행하도록 구현되었다.
        return self._height(p) # p값이 들어오면 그 position에 위치한 node의 height를 리턴하기 위해 위의 _height(self, p)을 그대로 시행하도록 구현되었다. 

    def __iter__(self): # Tree라는 Class에 정의된 method로 Tree를 구성하는 node들의 element를 차례로 뽑아서 iterative하게 리턴하는 method이다.
        """Generate an iteration of the tree's elements."""
        for p in self.positions():     # Tree를 구성하는 node들의 position을 차례로 뽑아서 iterative하게 리턴하는 method인 positions(self)를 사용한다.
            yield p.element()          # Position을 하나하나 받아서 그 Position을 통해 node에 접근하여 element를 추출하여 iterative하게 리턴한다.

    def positions(self): # Tree라는 Class에 정의된 method로 Tree를 구성하는 node들의 position을 차례로 뽑아서 iterative하게 리턴하는 method이다.
        """Generate an iteration of the tree's positions."""
        return self.preorder()         # Tree를 구성하는 node들의 position을 특정 node, 그 node의 child들 순으로 recursive하게 뽑아서 iterative하게 리턴하는 preorder(self) method의 결과를 그대로 리턴한다.

    def preorder(self): # Tree라는 Class에 정의된 method로 Tree를 구성하는 node들의 position을 특정 node, 그 node의 child들 순으로 recursive하게 뽑아서 iterative하게 리턴하는 method이다.
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty(): # Tree가 empty 상태가 아니면 아래의 코드를 실행한다.
            for p in self._subtree_preorder(self.root()): # Tree의 root의 position을 인자로 하여 recursive하게 _subtree_preorder(self, p)를 실행한다.
                yield p # recursive하게 받아온 값들을 iterative하게 리턴한다. 그 결과 subTree를 구성하는 node들의 position을 특정 node, 그 node의 child들 순으로 출력되게 된다.

    def _subtree_preorder(self, p): # Tree라는 Class에 정의된 method로 position p를 받으면 그 position에 위치한 node를 root로 하는 subTree를 구성하는 node들의 position을 특정 node, 그 node의 child들 순으로 recursive하게 뽑아서 iterative하게 리턴하는 method이다.
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p # SubTree에서 우선 인자로 받은 position p 즉 자기 자신을 방문(리턴)한다.
        for c in self.children(p): # 인자로 받은 position p가 가리키는 node가 가진 child들을 하나씩 방문한다.
            for other in self._subtree_preorder(c): # 방문한 child들의 position을 인자로 하여 recursive하게 _subtree_preorder(self, p)를 실행한다.
                yield other # recursive하게 받아온 값들을 iterative하게 리턴한다. 그 결과 subTree를 구성하는 node들의 position을 특정 node, 그 node의 child들 순으로 출력되게 된다.

    def postorder(self): # Tree라는 Class에 정의된 method로 Tree를 구성하는 node들의 position을 특정 node의 child들, 특정 node 순으로 recursive하게 뽑아서 iterative하게 리턴하는 method이다.
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty(): # Tree가 empty 상태가 아니면 아래의 코드를 실행한다.
            for p in self._subtree_postorder(self.root()): # Tree의 root의 position을 인자로 하여 recursive하게 _subtree_postorder(self, p)를 실행한다.
                yield p # recursive하게 받아온 값들을 iterative하게 리턴한다. 그 결과 subTree를 구성하는 node들의 position을 특정 node의 child들, 특정 node 순으로 출력되게 된다.

    def _subtree_postorder(self, p): # Tree라는 Class에 정의된 method로 position p를 받으면 그 position에 위치한 node를 root로 하는 subTree를 구성하는 node들의 position을 특정 node의 child들, 특정 node 순으로 recursive하게 뽑아서 iterative하게 리턴하는 method이다.
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p): # 인자로 받은 position p가 가리키는 node가 가진 child들을 하나씩 방문한다.
            for other in self._subtree_postorder(c): # 방문한 child들의 position을 인자로 하여 recursive하게 _subtree_preorder(self, p)를 실행한다.
                yield other # recursive하게 받아온 값들을 iterative하게 리턴한다. 그 결과 subTree를 구성하는 node들의 position을 특정 node의 child들, 특정 node 순으로 출력되게 된다.
        yield p             # 마지막으로 SubTree에서 인자로 받은 position p 즉 자기 자신을 방문(리턴)한다.
        
    def levelorder(self): # Tree라는 Class에 정의된 method로 Tree를 구성하는 node들의 position을 height가 높은 root node들부터 같은 height를 가지는 node들을 모아서 낮은 height에 있는 leaf들까지 iterative하게 리턴하는 method이다.
        """Generate a levelorder iteration of positions in the tree."""
        """The running time of this level-order traversal should be O(n) """
        class ArrayBasedQueue: # levelorder의 구현을 위해 보조 자료구조로 ArrayBasedQueue를 정의한다.
            def __init__(self): # ArrayBasedQueue를 처음 생성하면 다음의 인스턴스 변수들을 생성한다.
                self._arraySize = 10 # ArrayBasedQueue의 초기 공간은 10 정도로 설정한다. 
                self._L = [None]*self._arraySize # element들이 저장될 ArrayBasedQueue의 초기 공간을 할당한다.
                self._f = 0 # Queue의 첫번째 값을 가리치는 identifier는 초기에 index 0을 가리키도록 한다.
                self._r = 0 # Queue의 마지막번째 값보다 1 큰 index 값을 가리치는 identifier는 초기에 index 0을 가리키도록 한다.
            def size(self): # ArrayBasedQueue에 저장된 element의 갯수를 리턴하는 method를 정의한다.
                return (self._arraySize - self._f + self._r) % self._arraySize # wrapped-around configuration을 고려해서 ArrayBasedQueue의 size를 N-f+r mod N으로 계산한다.
            def resize(self): # 기존에 ArrayBasedQueue에 할당된 공간을 1개 빼고 모두 사용할 경우 Doubling Strategy를 사용해서 ArrayBasedQueue에 새 공간을 할당하는 method를 정의한다.
                self._arraySize = self._arraySize * 2 # ArrayBasedQueue의 공간을 기존 공간의 2배로 설정한다.
                newArray = [None]*self._arraySize # 기존 공간의 2배 크기인 ArrayBasedQueue를 위한 새 공간을 마련한다.
                for i in range(0,self._arraySize//2 - 1):
                    newArray[i] = self._L[(self._f + i) % (self._arraySize//2)] # 기존의 ArrayBasedQueue의 f가 새 공간에서는 0자리에 가도록 하여 값을 옮긴다.
                self._L = newArray # 새로 만들고 값까지 옮긴 새 저장공간을 ArrayBasedQueue로 지정한다.
                self._f = 0 # 새로 할당된 ArrayBasedQueue에서 f는 index 0을 가리키도록 한다.
                self._r = self._arraySize//2 - 1 # 새로 할당된 ArrayBasedQueue에서 r은 기존 ArrayBasedQueue에 할당된 공간의 크기보다 1 작은 값의 index값을 가리키도록 한다.
            def enqueue(self, o): # ArrayBasedQueue의 맨 뒤에 값을 추가하는 method를 정의한다.
                if self.size() == self._arraySize - 1:
                    self.resize() # 만약 ArrayBasedQueue가 Full 상태이면 ArrayBasedQueue를 resize하여 저장공간을 늘린다.
                self._L[self._r] = o # ArrayBasedQueue에서 r이 가리키는 index 공간에 새로 들어온 값을 저장한다.
                self._r = (self._r + 1) % self._arraySize # r값에 +1을 한다. 하지만 r값은 index이기에 ArrayBasedQueue의 size를 넘어갈 수는 없어서 r에 +1을 한 뒤에 mod N 연산을 추가로 해서 wrapped-around configuration으로 이어지도록 만들어 준다.
            def dequeue(self): # ArrayBasedQueue의 맨 앞 값을 추출하는 method를 정의한다.
                value = self._L[self._f] # ArrayBasedQueue에서 f가 가리키는 index 공간에 있는 element를 리턴하기 위해 미리 빼둔다.
                self._L[self._f] = None # 값을 뺐기 때문에 빼진 자리에 None을 할당하여 초기화한다.
                self._f = (self._f + 1) % self._arraySize # f갑에 +1을 한다. 하지만 f값은 index이기에 ArrayBasedQueue의 size를 넘어갈 수는 없어서 f에 +1을 한 뒤에 mod N 연산을 추가로 해서 wrapped-around configuration으로 이어지도록 만들어 준다.
                return value # 빼둔 값을 리턴한다.
        if not self.is_empty(): # Tree가 empty 상태가 아니면 아래의 코드를 실행한다.
            Q = ArrayBasedQueue() # levelorder의 구현을 위해 보조 자료구조로 ArrayBasedQueue를 생성한다.
            Q.enqueue(self.root()) # root의 position을 ArrayBasedQueue에 Enqueue한다.
            for i in range(self._size): # Tree가 저장하고 있는 Element의 수만큼 아래의 작업을 반복한다.
                p = Q.dequeue() # ArrayBasedQueue에 저장된 Tree의 node의 Position들 중 맨 앞의 값을 뺀다.
                for c in self.children(p):
                    Q.enqueue(c) # ArrayBasedQueue에서 뺀 Position이 가리키는 node의 child의 Position들을 하나씩 ArrayBasedQueue의 맨 뒤에 넣는다.
                yield p # ArrayBasedQueue에서 뺀 Position을 iterative하게 리턴한다.