from copy import deepcopy

symbol_table = {}
OPERATIONS = ["Plus","Times","Equals","If","Set"]

class Expression:
    def __init__(self, tag, args) -> None:
        self.tag = tag
        self.args = args

    def evaluate(self):
        return deepcopy(self)

    def __repr__(self) -> str:
        if self.args == []:
            return str(self.tag)
        else:
            return f"{self.tag}[{",".join(map(repr,self.args))}]"
        
    def __eq__(self, other) -> bool:
        if isinstance(other,Expression):
            if self.__repr__() == other.__repr__():
                return True
        return False

def customSplit(s):
    splitItems = []
    check = 0
    lastCommaPos = 0
    for i, letter in enumerate(s):
        if letter == "," and check == 0:
            splitItems.append(s[lastCommaPos:i])
            lastCommaPos = i+1
        elif letter == "[":
            check += 1
        elif letter == "]":
            check -= 1
    splitItems.append(s[lastCommaPos:])
    return splitItems


def isfloat(s):
    for i in s:
        if not i.isdigit() and i != ".":
            return False
    return True


def parse(s):
    s = customSplit(s)
    for expr in s:
        if "[" in expr:
            j = expr.split("[")
            return Expression(j[0],parse(j[1][:-1]))
        else:
            return Expression(expr,[])


def evaluate(s:str):
    items = s[:-1]
    if items == "":
        items = s
    items = items.split("[",1)
    output = ""
    if len(items) == 1:
        symbol = symbol_table.get(s)
        if symbol == None:
            return s
        else:
            return evaluate(symbol)

    elif items[0] == "Plus":
        toAdd = customSplit(items[1])
        evaluated = []
        allNumbers = True
        for val in toAdd:
            evald = evaluate(val)
            if not evald.isdigit() and not isfloat(evald):
                allNumbers = False
                evaluated.append(evald)
            else:
                try:
                    evaluated.append(int(evald))
                except:
                    evaluated.append(float(evald))
        if allNumbers:
            output = str(sum(evaluated))
        else:
            output = f"{items[0]}["
            for val in evaluated:
                output = output + str(val) + ","
            output = output[:-1] + "]"

    elif items[0] == "Times":
        toMul = customSplit(items[1])
        evaluated = []
        allNumbers = True
        for val in toMul:
            evald = evaluate(val)
            if not evald.isdigit() and not isfloat(evald):
                allNumbers = False
                evaluated.append(evald)
            else:
                try:
                    evaluated.append(int(evald))
                except:
                    evaluated.append(float(evald))
        if allNumbers:
            total = 1
            for val in evaluated:
                total *= val
            output = str(total)
        else:
            output = f"{items[0]}["
            for val in evaluated:
                output = output + str(val) + ","
            output = output[:-1] + "]"

    elif items[0] == "Equals":
        toCheck = customSplit(items[1])
        if len(toCheck) != 2:
            return s
        else:
            if evaluate(toCheck[0]) == evaluate(toCheck[1]):
                return "True"
            return "False"
    elif items[0] == "If":
        toCheck = customSplit(items[1])
        if len(toCheck) != 3:
            return s
        else:
            if evaluate(toCheck[0]) == "True":
                return evaluate(toCheck[1])
            else:
                return evaluate(toCheck[2])
    elif items[0] == "Set":
        toCheck = customSplit(items[1])
        if len(toCheck) != 2:
            return s
        else:
            val = evaluate(toCheck[1])
            if not toCheck[0].isdigit() and toCheck[0] not in OPERATIONS:
                symbol_table.update({toCheck[0]:Expression(val,[]).__repr__()})
            return toCheck[1]
    else:
        toEval = customSplit(items[1])
        output = f"{items[0]}["
        for val in toEval:
            output = output + evaluate(val) + ","
        output = output[:-1] + "]"
    return output




while True:
    expr:Expression = parse(input("ENSEA>>> "))
    print(expr.evaluate())




"""
print(evaluate("Set[x,Plus[2,y]]"))
print(evaluate("Set[y,5]"))
print(evaluate("x"))
"""


"""
minusOne = Expression("-1",[])
b = Expression("b",[])
twoDotThree = Expression("2.3",[])
right = Expression("g", [minusOne,b,twoDotThree])
a = Expression("a",[])
c = Expression("a",[])
expr = Expression("f", [a,right])
"""