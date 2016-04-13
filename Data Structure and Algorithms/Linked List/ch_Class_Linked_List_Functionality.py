
# Source: Online Reference

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        # when the delete method reaches the node it wants to delete,
        # it looks at the last node it visited (the 'previous' node),
        # and resets that previous node's pointer so that,
        # rather than pointing to the soon-to-be-deleted node,
        # it will point to the next node in line.

    def printnode(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()

link = LinkedList()
ListData = (10, 20, 30, 40, 50)

for i in ListData:
    link.insert(i)              # Problem: 'int' object is not iterable.  occurs

print(link.size())    

link.printnode()
