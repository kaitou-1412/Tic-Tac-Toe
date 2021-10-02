theBoard = {
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' ',
}
POS = '123456789'
winner = 'Nobody'


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' +board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' +board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' +board['3'])
    print('\n----------------------\n')


turn = 'X'
turn_number = 9


def gameEnded(theBoard):
    for i in range(1,4):
        if (theBoard[str(3*i - 2)] == theBoard[str(3*i - 1)]) and (theBoard[str(3*i - 1)] == theBoard[str(3*i)]):
            return True
        elif (theBoard[str(i)] == theBoard[str(i + 3)]) and (theBoard[str(i + 3)] == theBoard[str(i + 6)]):
            return True
    if ((theBoard['1'] == theBoard['5']) and (theBoard['5'] == theBoard['9'])) or ((theBoard['3'] == theBoard['5']) and (theBoard['5'] == theBoard['7'])):
        return True
    return False


while True:
    if turn_number <= 0:
        break
    printBoard(theBoard)
    move = input('\nTurn for %s.\nMove on which space?\n\n' % (turn))
    print()
    if move not in POS or theBoard[move] != ' ':
        continue
    theBoard[move] = turn
    if(turn_number <= 5 and gameEnded(theBoard)):
        winner = turn
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    turn_number -= 1

printBoard(theBoard)
print('{} is the Winner!!!\n'.format(winner))
print('----------------------')
