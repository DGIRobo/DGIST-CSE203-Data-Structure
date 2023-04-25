from linked_tree import LinkedTree
"""
# Example test cases to verify your implementation
T = LinkedTree()

# Test case 1: Test _add_root functionality
print("Test case 1: Add root")
root = T._add_root('A')
print(f"Root: {root.element()}")  # Output: Root: A

# Test case 2: Test _add_child functionality
print("\nTest case 2: Add children")
b = T._add_child(root, 'B')
c = T._add_child(root, 'C')
d = T._add_child(root, 'D')

# Output: Children of A: ['B', 'C', 'D']
print(f"Children of A: {[child.element() for child in T.children(root)]}")

# Test case 3: Test _replace functionality
print("\nTest case 3: Replace element")
T._replace(b, 'B_new')
print(f"New element at B's position: {b.element()}")  # Output: New element at B's position: B_new
print(f"Now Children of A: {[child.element() for child in T.children(root)]}")

# Test case 4: Test _delete non-root functionality
T._delete(b)
print(f"Now Children of A: {[child.element() for child in T.children(root)]}")
T._delete(c)
print(f"Now Children of A: {[child.element() for child in T.children(root)]}")
T._delete(d)
print(f"Now Children of A: {[child.element() for child in T.children(root)]}")

# Test case 5: Test _delete root functionality
T._delete(root)

# Example tree construction

root = T._add_root('A')
b = T._add_child(root, 'B')
c = T._add_child(root, 'C')
d = T._add_child(root, 'D')

b1 = T._add_child(b, 'B1')
b2 = T._add_child(b, 'B2')

T._add_child(b1, 'B11')
T._add_child(b1, 'B12')
T._add_child(b1, 'B13')
T._add_child(b1, 'B14')

T._add_child(b2, 'B21')
T._add_child(b2, 'B22')

c1 = T._add_child(c, 'C1')

T._add_child(d, 'D1')
T._add_child(d, 'D2')
T._add_child(d, 'D3')

T._add_child(c1, "C11")
T._add_child(c1, "C12")
T._add_child(c1, "C13")

for node in T.levelorder():
    print(node.element())
"""
# Test 3
def array2tree(array, childrenMax):
    tree = LinkedTree()
    root = tree._add_root(None)
    positionList = [root]*childrenMax
    for i in range(0, len(array)-1):
        child = tree._add_child(positionList.pop(), None)
        positionList = [child]*childrenMax + positionList
    levelorderlist = []
    for node in tree.levelorder():
        levelorderlist.append(node)
    for match in range(0, len(array)):
        tree._replace(levelorderlist[match], array[match])
    return tree

array1 = []
array2 = ["A"]
array3 = ["A", "B", "C"]
array4 = ["A", "B", "C", "D", "E", "F", "G"]
array5 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
    
TestCase1 = array2tree(array1, 5)
print(f"TestCase1: {[node for node in TestCase1]}") # Expected Output: TestCase1: [None]

TestCase2 = array2tree(array2, 5)
print(f"TestCase2: {[node for node in TestCase2]}") # Expected Output: TestCase2: ['A']

TestCase3 = array2tree(array3, 5)
print(f"TestCase3: {[node for node in TestCase3]}") # Expected Output: TestCase3: ['A', 'B', 'C']

TestCase4 = array2tree(array4, 5)
print(f"TestCase4: {[node for node in TestCase4]}") # Expected Output: TestCase4: ['A', 'B', 'G', 'C', 'D', 'E', 'F']