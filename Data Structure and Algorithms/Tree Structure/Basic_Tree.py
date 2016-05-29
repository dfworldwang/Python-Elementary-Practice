
class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    # recursive function to traverse it 
    def __repr__(self, level = 0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

# family tree
tree = node("grandmother", [
    node("daughter", [
        node("granddaughter"),
        node("grandson")]),
    node("son", [
        node("granddaughter"),
        node("grandson")])
    ]);

print(tree)
