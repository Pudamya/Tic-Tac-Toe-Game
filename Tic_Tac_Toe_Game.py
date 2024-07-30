board={
    "P1":" ","P2":" ","P3":" ",
    "P4":" ","P5":" ","P6":" ",
    "P7":" ","P8":" ","P9":" "
}

player=1
count_moves=0
win=False

def check_win():
    global win
    
    #Horizontal
    if (all(board[k]=="X" for k in ["P1","P2","P3"])) or (all(board[k]=="X" for k in ["P4","P5","P6"])) or (all(board[k]=="X" for k in ["P7","P8","P9"])):
        print("Player 01 won the game (Horizontal)")
        win=True
        
    if (all(board[k]=="O" for k in ["P1","P2","P3"])) or (all(board[k]=="X" for k in ["P4","P5","P6"])) or (all(board[k]=="X" for k in ["P7","P8","P9"])):
        print("Player 02 won the game (Horizontal)")
        win=True  
        
    #Vertical
    if (all(board[k]=="X" for k in ["P1","P4","P4"])) or (all(board[k]=="X" for k in ["P2","P5","P8"])) or (all(board[k]=="X" for k in ["P3","P6","P9"])):
        print("Player 01 won the game (Vertical)")
        win=True
        
    if (all(board[k]=="O" for k in ["P1","P4","P4"])) or (all(board[k]=="X" for k in ["P2","P5","P8"])) or (all(board[k]=="X" for k in ["P3","P6","P9"])):
        print("Player 01 won the game (Vertical)")
        win=True
        
    #Diagonal
    if (all(board[k]=="X" for k in ["P1","P5","P9"])) or (all(board[k]=="X" for k in ["P3","P5","P7"])):
        print("Player 01 won the game (Diagonal)")
        win=True
        
    if (all(board[k]=="O" for k in ["P1","P5","P9"])) or (all(board[k]=="X" for k in ["P3","P5","P7"])):
        print("Player 01 won the game (Diagonal)")
        win=True    
    

print("**** Tic Tac Toe Game *****")
print()
print("Let's start the game!!!")


while True:
    
    print(board["P1"]+"|"+board["P2"]+"|"+board["P3"])
    print("-|-|-")
    print(board["P4"]+ "|" + board["P5"]+ "|"+ board["P6"])
    print("-|-|-")
    print(board["P7"]+ "|" + board["P8"]+ "|"+ board["P9"])
    
    check_win()
    
    if count_moves==9 or win:
        break
        
    while True:
        if player==1:
            p1=input("Player 01, choose the position: ")
            if (p1.upper() in board) and (board[p1.upper()]==" "):
                board[p1.upper()]="X"
                player=2
                break
            else:
                print("Invalid position")
                continue
        else:
            p2=input("Player 02, choose the position: ")
            if (p2.upper() in board) and (board[p2.upper()]==" "):
                board[p2.upper()]="O"
                player=1
                break
            else:
                print("Invalid position")
                continue
                
                
    count_moves+=1        
