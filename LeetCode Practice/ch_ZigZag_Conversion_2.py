
def cond(condition):
    if condition:
        condition = False
        return condition
    else:
        condition = True
        return condition
    

def convert(s, nRows):
    if nRows == 1:
        return s

    array = []
    step = 2 * nRows - 2
    i = 0
    
    for i in range(0, nRows):
        if i == 0 or i == nRows - 1:
            j = i
            while j < len(s):
                array.append(s[j])
                j = j + step
        else:
            j = i
            flag = True
            step1 = 2 * (nRows - 1 - i)
            step2 = step - step1
            while j < len(s):
                array.append(s[j])
                if flag:
                    j = j + step1
                else:
                    j = j + step2

                cond(flag)

        # Review this algorithm later, not understanding too much.

    return array


string = "PAYPALISHIRING"
ConvertString = convert(string, 3)
print(ConvertString)
