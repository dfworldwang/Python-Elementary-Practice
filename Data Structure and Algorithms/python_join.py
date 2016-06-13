


li = ['my', 'name', 'is', 'bob']

# Concatenate the elements of list with blank
print(' '.join(li))

print('..'.join(li))


class Foo():
    def __init__(self):
        self.name = [{"Susan": ("Boyle", 50, "alive")}, {"Albert": ("Speer", 106, "dead")}]

    def __str__(self):
        ret_str = ""
        for d in self.name:
            for k in d:
                ret_str += "".join([k, " ", d[k][0], " is ", str(d[k][1]),
                                    " and ", d[k][2], ". "])

        return ret_str

foo = Foo()
print(foo)

