
class binarynode(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    # checking whether some value 'x' is in the binary tree
    def search(self, value):
        # returns True if value is in the tree
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
my_binary = binarynode(6,
    binarynode(4,
        binarynode(3),
        binarynode(5)),
    binarynode(8,
        binarynode(7),
        binarynode(9)))

print(my_binary.search(3), my_binary.search(7), my_binary.search(10))
