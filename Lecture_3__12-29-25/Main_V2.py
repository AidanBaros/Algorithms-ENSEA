from copy import deepcopy

symbol_table = {}
OPERATIONS = ["Plus","Times","Equals","If","Set","Function","Apply"]

class Expression:
    def __init__(self, tag, args) -> None:
        self.tag:str = tag
        self.args:list[Expression] = args

    def evaluate(self) -> str:
        evaluated:list[Exception] = []
        if len(self.args) == 0:
            return symbol_table.get(self.tag).evaluate() if self.tag in symbol_table else self
        if self.tag == "If":
            if len(self.args) != 3:
                return self
            else:
                if self.args[0].evaluate() == "True":
                    return self.args[1].evaluate()
                return self.args[2].evaluate()
        elif self.tag == "Set":
            if len(self.args) != 2:
                return self
            else:
                if not self.args[0].tag.isdigit() and self.args[0] not in OPERATIONS:
                    symbol_table.update({self.args[0].tag:self.args[1]})
                    return self.args[1]
                else:
                    return self
        elif self.tag == "Function":
            return deepcopy(self)
        elif self.tag == "Apply":
            if len(self.args) != 2:
                return self
            else:
                newExpr:Expression = self.args[0].evaluate()
                newVal = self.args[1]

                toChange = newExpr.args[1]
                toEval = toChange.substitute(newExpr.args[0], newVal)
                
                return toEval.evaluate()
        for arg in self.args:
            evaluated.append(arg.evaluate())
        if self.tag == "Plus":
            total = 0
            for evald in evaluated:
                try:
                    total += int(evald.tag)
                except:
                    try:
                        total += float(evald.tag)
                    except:
                        return self
            return Expression(str(total),[])
        elif self.tag == "Times":
            total = 1
            for evald in evaluated:
                if evald.tag.isdigit():
                    total *= int(evald.tag)
                elif isfloat(evald.tag):
                    total *= float(evald.tag)
                else:
                    return self
            return Expression(str(total),[])
        elif self.tag == "Equals":
            if len(self.args) != 2:
                return self
            else:
                if evaluated[0] == evaluated[1]:
                    return "True"
                return "False"
        else:
            return deepcopy(self)
        
    def substitute(self, expr1, expr2):
        if self == expr1:
            return expr2
        else:
            return Expression(self.tag,[arg.substitute(expr1, expr2) for arg in self.args])
        
    def __repr__(self) -> str:
        if self.args == []:
            return str(self.tag)
        else:
            return self.tag + '[' + ','.join([str(arg) for arg in self.args]) + ']'
        
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
    items = customSplit(s)
    expressionList = []
    for expr in items:
        if "[" in expr:
            subitems = expr.split("[",1)
            expressionList.append(Expression(subitems[0],parse(subitems[1][:-1])))
        else:
            expressionList.append(Expression(expr,[]))
    if len(items) == 1:
        return expressionList[0]
    return expressionList

"""
Fibo
Set[Fibo,Function[n,If[Equals[n,Times[n,n]],1,Plus[Apply[Fibo,Plus[n,-1]],Apply[Fibo,Plus[n,-2]]]]]]
"""

while True:
    expr:Expression = parse(input("ENSEA>>> "))
    print(expr.evaluate())