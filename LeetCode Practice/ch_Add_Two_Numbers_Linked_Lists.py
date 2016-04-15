
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

    def getValue(self):
        current = self.head
        valuepool = ()
        while current:
            valuepool = valuepool + (current.get_data(), )
            current = current.get_next()
        return valuepool    

class Solution(object):
    def addTwoNumbers(self, l1, t1, l2, t2):
        Sumpool = [0, 0, 0]
        t1 = l1.getValue()
        t2 = l2.getValue()

        t1 = list(t1)                           # transfer tuple to list
        t2 = list(t2)
        print(t1, t2)
        print(t1[0], t1[1], t1[2])
        for index, var in enumerate(t1):        # iterate each element in the list
            print(index, var)

        for i in range(0, 3):
            if t1[i] + t2[i] >= 10:
                Sumpool[i] = 0                  # can't plus 1 to next Sumpool element
            else:
                Sumpool[i] = t1[i] + t2[i]
        
        print(Sumpool)
        


list1 = LinkedList()
list2 = LinkedList()
tuple1 = ()
tuple2 = ()

List1Data = (2, 4, 3)
List2Data = (5, 6, 4)

for i in List1Data:
    list1.insert(i)

for i in List2Data:
    list2.insert(i)

s = Solution()
s.addTwoNumbers(list1, tuple1, list2, tuple2)

