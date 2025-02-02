class LinkedList():
    def __init__(self, head, tail) -> None:
        self.head = head
        self.tail = tail

def create_empty_linked_list():
    return LinkedList(None,None)

def create_linked_list_head(e):
    return LinkedList(e,None)

def create_linked_list(e, l:LinkedList):
    return LinkedList(e,l)

def is_empty(l:LinkedList):
    return l.head == None

def head(l:LinkedList):
    return l.head

def tail(l:LinkedList):
    return l.tail

def cons(e,l:LinkedList):
    return LinkedList(e,l)

def length(l:LinkedList):
    if l == None:
        return 0
    else:
        return 1 + length(l.tail)

def nth(l:LinkedList,n):
    len_ = length(l)
    if n == 0:
        return l.head
    if n < len_:
        return nth(l.tail, n-1)
    else:
        raise Exception("Out of bounds")

def addLast(e,l:LinkedList):
    if l.tail != None:
        addLast(e,l.tail)
    else:
        l.tail = create_linked_list_head(e)

def reverse(l:LinkedList):
    if l.tail != None:
        return l
    else:
        return addLast(l.head,reverse(l.tail))


def concat(l1,l2):

    pass

def map_():

    pass

def foldLeft():

    pass

def foldALl():

    pass

def exit():

    pass

def mem():

    pass

def sort():

    pass

def toString(l:LinkedList):
    if l.tail != None:
        return f"{l.head}, {toString(l.tail)}"
    return l.head


ll = create_empty_linked_list()
ll.head = 1
ll.tail = create_linked_list_head(2)
ll.tail.tail = create_linked_list_head(3)
addLast(4,ll)
print(toString(ll))
reverse(ll)
print(toString(ll))
