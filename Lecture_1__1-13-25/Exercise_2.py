L:list[chr] = ["S","a","n","t","a","o","s","c","i","l","l","a","t","e","m","y","m","e","t","a","l","l","i","c","s","o","n","a","t","a","s"]
L:list[chr] = ["S","a","t","a","n","o","s","c","i","l","l","a","t","e","m","y","m","e","t","a","l","l","i","c","s","o","n","a","t","a","s"]
def IsPalindrome(seq):
    start = 0 
    end = len(seq)-1
    if check(seq,start,end):
        print("It is a Palindrome")
    else:
        print("It is NOT a Palindrome")

def check(seq,start,end):
    if start+1 >= end:
        return True

    if seq[start].lower() != seq[end].lower():
        return False
    else:
        return check(seq,start+1,end-1)

IsPalindrome(L)