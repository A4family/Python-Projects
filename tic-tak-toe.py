def sum(a,b,c):
    return a + b + c

def printBoard(xState,yState):
    zero = 'X' if xState[0] else ('0' if yState[0] else 0 )
    one = 'X' if xState[1] else ('0' if yState[1] else 1 )
    two = 'X' if xState[2] else ('0' if yState[2] else 2 )
    three = 'X' if xState[3] else ('0' if yState[3] else 3 )
    four = 'X' if xState[4] else ('0' if yState[4] else 4 )
    five = 'X' if xState[5] else ('0' if yState[5] else 5 )
    six = 'X' if xState[6] else ('0' if yState[6] else 6 )
    seven = 'X' if xState[7] else ('0' if yState[7] else 7 )
    eight = 'X' if xState[8] else ('0' if yState[8] else 8 )
    print(f"{zero} | {one} | {two}")
    print(f"-----------")
    print(f"{three} | {four} | {five}")
    print(f"------------")
    print(f"{six} | {seven} | {eight}")
    pass

def checkWin(xState,yState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]]) == 3):
            print('x won the match')
            return 1
        if(sum(yState[win[0]],yState[win[1]],yState[win[2]]) == 3):
            print("0 won the match")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    yState = [0,0,0,0,0,0,0,0,0]
    turn = 1     
    print("Welcome")
    print("X's chance")
    while True:
        printBoard(xState,yState)
        if(turn == 1):
            print("X's Turn")
            value = int(input("Please enter a value"))
            xState[value] = 1
        else:
            print("0's Chance")
            value = int(input("Please Enter a value"))
            yState[value] = 1
        cwin =checkWin(xState,yState)
        if(cwin != -1):
            break
        turn = 1 - turn