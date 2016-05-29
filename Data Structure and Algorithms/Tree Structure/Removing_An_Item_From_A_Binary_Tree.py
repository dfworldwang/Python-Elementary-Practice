
class binarynode(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def highest(self):
        if self.right != None:
            return self.right.highest()
        else:
            return self.value

    def lowest(self):
        if self.left != None:
            return self.left.lowest()
        else:
            return self.value

    def delete(self, value):
        if value == self.value:
            if self.left != None:

                # We now want to delete the highest value from the left subtree,
                # and make the value of the deleted node equal to that value,
                # and to delete the highest value from the left.
                self.value = self.left.highest()
                self.left.delete(self.value)

            elif self.right != None:

                # Similarly, we want the lowest value from the right subtree
                # if we are forced to go that way.
                self.value = self.right.lowest()
                self.right.delete(self.value)
            else:
                return None
        else:
            if value < self.value and self.left != None:
                self.left = self.left.delete(value)
            if value > self.value and self.right != None:
                self.right = self.right.delete(value)
            return self

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
        binarynode(3)),
    binarynode(6,
        binarynode(5),
        binarynode(7)))

# delete the number 2 from the binary tree
# before deletion
print(my_binary.search(2))

my_binary.delete(2)

# after the deletion
print(my_binary.search(2))
    
