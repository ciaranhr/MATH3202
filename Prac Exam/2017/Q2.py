#Stages: Card Draw T

#State : Cards Remaining S

#Action: card position to place in at s

#Value Function: Minimise the expected value of the multiplication

#Data: probability of drawing a card 1/10, 1/9, 1/8, 1/7
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
board = [0, 0,
         0, 0]

B = range(len(board))
C = range(len(cards))
def multiply(board):
    a, b = board[0]*10 + board[1], board[2]*10 + board[3] 
    return a*b

def update_b(pos, val, board):
    b2 = list(board)
    b2[pos] = val
    return b2

#we want V(0, [all cards])
#Base Case V(3) = multiply()

def check_zero(board):
    noZero = False
    for i in board:
        if i:
            noZero = True
        elif not i:
            return False
    return noZero

def num_filled(board):
    total = 0
    for i in board:
        if i:
            total+= 1
    return total

def indexes_filled(board):
    filled = []
    for i in range(len(board)):
        if board[i]:
            filled.append(i)
    return filled


def V(S):
    new_s = list(S)
    if check_zero(S):
        return multiply(S)
    else:
    
    
        return  min(sum(1/(len(cards)-num_filled(S))*V(update_b(p, c, new_s)) for c in cards if c not in new_s) for p in B if p not in indexes_filled(new_s))

print(V(board))
