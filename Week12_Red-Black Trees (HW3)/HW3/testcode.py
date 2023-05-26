from redblack_tree import RedBlackTree

# Example test cases to verify your implementation
T = RedBlackTree()

# Test case 1: Test inserting just one element (should be the root)
root = T.insert(100)
T.display()

"""
# Test case 2: Try adding left and right child, (they should be all reds)
T.insert(50)
T.insert(150)
T.display()

# Test case 2: Try adding one more
# This should be recolored.
T.insert(30)
T.display()

# Test case 3: Reconstruction, with left child-left child case 
T.insert(10)
T.display()

# Test case 4: Reconstruction, with left child-right child case 
T.insert(125)
T.insert(140)
T.display()

# Test case 5: Recoloring, then reconstruction
# with right child-right child case
T.insert(175)
T.insert(200)
T.display()

# Test case 6: Recoloring, then propagation to a reconstruction
# with right child-left child case
T.insert(250)
T.display()

node_125 = T.search(125)
print(node_125)
print(T.search(1111))

# Make some random sequence, and check
import random
random.seed()

# make some non-duplicated numbers
numbers = list(range(50))
random.shuffle(numbers)

# iterate through the numbers, and insert them into the tree
T = RedBlackTree()
count = 0
for n in numbers:
    print(f'inserting {n} ...')
    T.insert(n)
    count += 1
    assert(T.search(n) != None), "The inserted item is missing in the tree"
    assert(T._size == count), f"The size of the tree is different from expected number, {T._size}, {count}"
    assert(T.check_tree_property_silent() == True), "The red-black tree property is broken"

# display the tree (if you want)
T.display()

# Check the tree's validity
T.check_tree_property()

# check if the tree is valid
print("> The inorder traverse is equal to the initial list?")
print(T.inorder_traverse() == sorted(numbers))
"""