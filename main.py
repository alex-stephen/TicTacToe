board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

print('------The selections on the board are as follows------')
print('1 | 2 | 3 \n')
print('4 | 5 | 6 \n')
print('7 | 8 | 9 \n')
print('\n \n')


def playGame(board):
    choice = int(input("Enter 1 to play first or 2 to play second!: "))
    for i in range(0, 9):
        if checkForWin(board) != 0:
            break
        if (i + choice) % 2 == 0:
            aiTurn(board)
        else:
            printBoard(board)
            playerTurn(board)

    checkWinner(board)


def checkWinner(board):
    winner = checkForWin(board)
    if winner == 0:
        printBoard(board)
        print('\n \n')
        print('********Draw********')
    elif winner == -1:
        printBoard(board)
        print('\n \n')
        print('********X Wins********')
    elif winner == 1:
        printBoard(board)
        print('\n \n')
        print('********O Wins********')


def printBoard(board):
    for i in range(0, 9):
        if i != 0 and (i % 3) == 0:
            print('\n')
        if board[i] == 0:
            print('_ ', end=" ")
        if board[i] == 1:
            print('O ', end=" ")
        if board[i] == -1:
            print('X ', end=" ")
    print('\n \n')


def playerTurn(board):
    position = int(input("Enter the position you would like to play: "))
    if board[position - 1] != 0:
        print("This is an invalid move please choose another space!")
        exit(0)
    board[position - 1] = -1


def miniMax(board, player, isMaximizing, alpha, beta):
    status = checkForWin(board)
    if status != 0:
        return status * player
    position = -1

    if isMaximizing:
        tempScore = -100
        for i in range(0, 9):
            if board[i] == 0:
                board[i] = player
                score = -miniMax(board, (player * -1), False, alpha, beta)
                tempScore = max(tempScore, score)
                alpha = max(alpha, tempScore)
                board[i] = 0
                if beta <= alpha:
                    break
        return tempScore
    else:
        tempScore = 100
        for i in range(0, 9):
            if board[i] == 0:
                board[i] = player
                score = -miniMax(board, (player * -1), True, alpha, beta)
                tempScore = max(tempScore, score)
                beta = min(alpha, tempScore)
                board[i] = 0
                if beta <= alpha:
                    break
        return tempScore

    #for i in range(0, 9):
       # if board[i] == 0:
     #      board[i] = player
       #     score = -miniMax(board, (player * -1))
         #   if score > tempScore:
            #    tempScore = score
               # position = i
          #  board[i] = 0
   # if position == -1:
       # return 0
   # return tempScore


def aiTurn(board):
    maximizing = True
    alpha = -100000
    beta = 100000
    position = -1
    tempScore = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -miniMax(board, -1, maximizing, alpha, beta)
            board[i] = 0
            if score > tempScore:
                tempScore = score
                position = i
    board[position] = 1


def checkForWin(board):
    winState = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if (board[winState[i][0]] != 0 and
                board[winState[i][0]] == board[winState[i][1]] and
                board[winState[i][0]] == board[winState[i][2]]):
            return board[winState[i][2]]
    return 0


playGame(board)
