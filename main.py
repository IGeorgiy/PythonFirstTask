def printField(field):
    print("  0 1 2")
    for index, value in enumerate(field):
        print(f"{index} {value[0]} {value[1]} {value[2]}")
    return

def makeStep(field, mark) :
    inp = input("Следующий ход, введите ""r"" чтобы начать сначала, введите координаты через запятую (пример: x,y) чтобы сделать ход:")
    if str.lower(inp) == 'r':
        return None
    step = str.split(inp, ',', 2)
    if field[int(step[1])][int(step[0])] == '-':
        field[int(step[1])][int(step[0])] = mark
        return field
    else:
        print("Данные координаты уже заняты! Попробуйте еще раз!")
        return makeStep(field, mark)

def canPlayNext(field):
    for row in field:
        for val in row:
            if val == '-':
                return True
    return False

def getNextMark(currentMark):
    if currentMark == 'x':
        return 'o'
    else:
        return 'x'

continueGame = True
gameField = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
mark = 'x'
while(continueGame):
    printField(gameField)
    gameField = makeStep(gameField, mark)
    mark = getNextMark(mark)

    if gameField is None:
        gameField = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    elif not canPlayNext(gameField):
        decision = input("Поле заполнено! Для продолжения введите 'r' для завершения 'q':")
        if str.lower(decision) == 'r':
            gameField = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        else:
            break