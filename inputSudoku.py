import os.path

def createBoardFile():
    path = getDirPath() + "/Sudoku Boards"
    currCounter = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))])

    f = open(os.path.join(path, "Board{count}.txt".format(count=currCounter+1)), "w")
    for i in range(0, 9):
        f.write(input())
        f.write('\n')

    f.close()

def getBoardFromFile(filename):
    path = getDirPath() + "/Sudoku Boards/{nameFile}".format(nameFile=filename)
    file = open(path, "r")
    lines = file.readlines()
    board = []
    for line in lines:
        currRow = []
        for val in line:
            if val not in [' ', '\n']:
                currRow.append(val)
        board.append(currRow)
    return board

def getDirPath():
    return os.path.dirname(os.path.abspath(__file__))