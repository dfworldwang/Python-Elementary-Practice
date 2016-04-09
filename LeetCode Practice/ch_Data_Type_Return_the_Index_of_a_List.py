
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.

                                # Beware of 4 and "4", they are different
                                # one is number, the other is String
list1 = [1, 2, 3]               # first list
list2 = [4, 5, 6]               # second list
list3 = [list1, list2]          # merge to two dimension
print(list3)

print([4, 5, 6].index(4))

if 4 + 6 == 10:
    print(list2.index(4))       # index(): show the index of the item in a List
    print(list2.index(6))

def twoSum(num1, num2, target):
    if (num1 + num2 == target):
        global a, b                 # there are Global variable and
                                    # Local variable effects.
        a = list2.index(num1)
        b = list2.index(num2)
        return a, b
    else:
        print("two Sum Error. Retry to choose two correct Nums.");

c, d = twoSum(4, 5, 9)
print(c, d)

    
