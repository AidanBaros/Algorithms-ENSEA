#N = int(input("Enter the number of queens\n - "))
N = 5

board = [[0]*N for _ in range(N)]

#checkBoard = [[0]*N for _ in N]

def is_attack(xMain, yMain):
    if board[yMain][xMain] == 1:
        return True
    
    for h in range(N):
        if board[yMain][h] == 1 and h != xMain:
            return True
    for h in range(N):
        if board[h][xMain] == 1 and h != yMain:
            return True
        
    x:int = xMain
    y:int = yMain
    if x <= y:
        y = y-x
        x = x-x
    else:
        x = x-y
        y = y-y

    for h in range(N):
        if x+h >= N or y+h >= N:
            break
        if board[y+h][x+h] == 1 and x+h != xMain and y+h != yMain:
            return True
    
    x = xMain
    y = yMain
    if x <= y:
        y = y+x
        x = x-x
        if x > N-1:
            y += x%(N-1)
            x -= y
        elif y > N-1:
            x += y%(N-1)
            y -= x
        for h in range(N):
            if x+h >= N or y-h >= N:
                break
            if board[y-h][x+h] == 1 and x+h != xMain and y-h != yMain:
                return True
    else:
        x = x+y
        y = y-y
        if x > N-1:
            y += x%(N-1)
            x -= y
        elif y > N-1:
            x += y%(N-1)
            y -= x
        for h in range(N):
            if x-h >= N or y+h >= N:
                break
            if board[y+h][x-h] == 1 and x-h != xMain and y+h != yMain:
                return True
    return False

def find_queens(n):
    for i in range(n):
        if place_queens(i,0,n):
            return board
    return [[]]

def place_queens(x,y,n):
    board[y][x] = 1
    if y >= n-1:
        return True
    
    for i in range(n):
        if not is_attack(i, y+1):
            if place_queens(i,y+1,n):
                return True
    board[y][x] = 0            
    return False

find_queens(N)
for i in board:
    print(i)
