from redblack_tree import RedBlackTree

# Preparing a tree for the test
T = RedBlackTree()

"""
T.insert(50)
T.insert(150)
T.insert(30)
T.insert(10)
T.insert(125)
T.insert(140)
T.insert(175)
T.insert(200)
T.insert(250)
T.display()


# make your own test cases for all the deletion cases.
T.delete(150)
T.delete(200)
T.delete(175)
T.display()

T.delete(250)
T.display()
"""
#-----------------------------------------------------------------------------------------------------------------
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

T.display()
random.shuffle(numbers)
for n in numbers:
    print(f'deleting {n} ...')
    T.delete(n)
    count -= 1
    T.display()
    assert(T.search(n) == None), "The deleted item is still remaining in the tree"
    assert(T._size == count), f"The size of the tree is different from expected number, {T._size}, {count}"
    assert(T.check_tree_property_silent() == True), "The red-black tree property is broken"
    
    if T.check_tree_property_silent() == False:
        print("Error: the tree property is violated after inserting", n)
        break


# display the tree (should be empty at this point)
T.display()