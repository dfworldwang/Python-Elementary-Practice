
class binarynode(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    # insert an item into the binary tree
    # If there is no subtree in the appropriate direction,
    # then we simply create a new subtree in the correct direction
    # with it's root as our item, and no sub children
    def insert(self, item):
        if self.value == item:
            return # we do nothing because the item is already here
        else:
            if item < self.value:
                if self.left != None:
                    self.left.insert(item)
                else:
                    self.left = binarynode(item)
            else:
                if self.right != None:
                    self.right.insert(item)
                else:
                    self.right = binarynode(item)

    def search(self, value): # returns True if value is in the tree
        if self.value == value:
            return True
        else:
            if value < self.value:
                if self.left != None:
                    return self.left.search(value)
                else:
                    return False
            else:
                if self.right != None:
                    return self.right.search(value)
                else:
                    return False

# a binary tree data
my_binary = binarynode(4,
    binarynode(2,
        binarynode(1),
        None),
    binarynode(6,
        binarynode(5),
        binarynode(7)))

# insert the number 3 into the binary tree

# before insertion
print(my_binary.search(3))

my_binary.insert(3)

# after the insertion
print(my_binary.search(3))
