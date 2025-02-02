t:set = [1,2,3,4]
subsets:set[set] = set()

def partList(t:set):
    if len(subsets) == 0:
        temp:set = {t.pop()}
        subsets.add(temp)
    else:
        copySet = subsets.copy()
        for i in range(len(subsets)):
            tempT:set = t.pop()
            tempCS:set = copySet.pop()
            subsets.add(tempCS.union(tempT))
    if len(t) > 1:
        partList(t)
    return

partList(t)
print(subsets)