import turtle

mywindow = turtle.Screen()
mywindow.title("Jeux de Cercle")
mywindow.setup(1200, 800)

# -------------Turtles and Variables-------------------

mywindow.tracer(0, 0)

write = turtle.Turtle()
write.hideturtle()
write.penup()
write.goto(200, 170)
write.write("'q' pour quitter", font=('Arial', 18, 'normal'))
write.goto(-70, -230)
write.write('Si vous voulez colorer', font=('Arial', 11, 'normal'))
write.goto(-70, -245)
write.write('seulement un cercle,', font=('Arial', 11, 'normal'))
write.goto(-70, -260)
write.write('click dessus le cercle deux fois', font=('Arial', 11, 'normal'))

xLines = [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25, 26, 27]]
lRLines = [[21], [15, 22], [10, 16, 23], [6, 11, 17, 24], [3, 7, 12, 18, 25], [1, 4, 8, 13, 19, 26],
           [0, 2, 5, 9, 14, 20, 27]]
rLLines = [[27], [20, 26], [14, 19, 25], [9, 13, 18, 24], [5, 8, 12, 17, 23], [2, 4, 7, 11, 16, 22],
           [0, 1, 3, 6, 10, 15, 21]]

Index = -1
layoutList = []
layoutColour = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
layoutRadius = 40
layoutCounter = 1
layoutCoordX1 = 0
layoutCoordY1 = 0
layoutCoordX2 = 0
layoutCoordY2 = 0

circleNumber1 = 0
circleNumber2 = 0

correct = 0
start = 0
end = 0

player = 1


# ------------Functions-------------------

def leave():
    global quitFlag
    quitFlag = True
    mywindow.bye()
    return


def layoutSpawn():
    global Index, layoutList, layoutRadius
    Index += 1
    layoutList.append(turtle.Turtle())
    layoutList[Index].shape('circle')
    layoutList[Index].penup()
    # radius list
    layoutList[Index].turtlesize(4, 4)
    layoutList[Index].color('black')
    layoutList[Index].fillcolor('white')
    return


def endTurn(x, y):
    global player, selectToggle, layoutCounter, circleNumber1, circleNumber2, found, won, start, end, correct
    player *= -1
    # reset and switch player
    layoutCounter = 1
    circleNumber1 = 0
    circleNumber2 = 0
    start = 0
    end = 0
    correct = 0
    found = False
    selectToggle = False
    return


def click(x, y):
    global mousex, mousey, selectToggle
    mousex = x
    mousey = y
    selectToggle = True
    return


def select(t1, r1):
    global player, mousex, mousey, circleNumber1, circleNumber2, layoutCounter, found, selectToggle
    dist = t1.distance(mousex, mousey)
    if dist <= r1:
        # grab the i values of the loop to find which circles
        if player == 1 and layoutColour[i] == 0 and layoutCounter < 3:
            if circleNumber1 == 0 and layoutCounter == 1:
                t1.fillcolor('black')
                circleNumber1 = i
                print('grabs first i')
                layoutCounter += 1
                selectToggle = False
            else:
                circleNumber2 = i
                print("grabs second i")
                layoutCounter += 1
                selectToggle = False
        if player == -1 and layoutColour[i] == 0 and layoutCounter < 3:
            if circleNumber1 == 0 and layoutCounter == 1:
                t1.fillcolor('black')
                circleNumber1 = i
                print('grabs first i')
                layoutCounter += 1
                selectToggle = False
            else:
                circleNumber2 = i
                print("grabs second i")
                layoutCounter += 1
                selectToggle = False
        if layoutCounter == 3:
            color()
            # reset and switch player
            if found is False:
                layoutCounter = 2
            else:
                endTurn(mousex, mousey)
    return


def color():
    # use the list, find which list both numbers are in, then check if the circles in between are coloublack
    # if not colour them
    global found, player, circlenumber1, circlenumber2, correct, start, end, layoutCounter, selectToggle
    # ------- x -------
    if found is False:
        for k in range(0, len(xLines), 1):
            for j in range(0, len(xLines[k]), 1):
                if xLines[k][j] == circleNumber1:
                    for l in range(0, len(xLines[k]), 1):
                        if xLines[k][l] == circleNumber2:
                            correct = k
                            start = j
                            end = l
                            found = True
                            print(xLines)
                            print(xLines[correct][start], xLines[correct][end])
        if xLines[correct][end] - xLines[correct][start] > 0:
            while xLines[correct][start] < xLines[correct][end] and layoutColour[xLines[correct][start]] == 0:
                if player == 1:
                    layoutList[xLines[correct][start]].fillcolor('black')
                    print(xLines[correct][start])
                else:
                    layoutList[xLines[correct][start]].fillcolor('black')
                    print(xLines[correct][start])
                layoutColour[xLines[correct][start]] = 1
                start += 1
                if xLines[correct][start] == xLines[correct][end] and layoutColour[xLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[xLines[correct][start]].fillcolor('black')
                        print(xLines[correct][start])
                    else:
                        layoutList[xLines[correct][start]].fillcolor('black')
                        print(xLines[correct][start])
                    layoutColour[xLines[correct][start]] = 1
        elif xLines[correct][end] - xLines[correct][start] < 0:
            while xLines[correct][start] > xLines[correct][end] and layoutColour[xLines[correct][start]] == 0:
                if player == 1:
                    layoutList[xLines[correct][start]].fillcolor('black')
                    print(xLines[correct][start])
                else:
                    layoutList[xLines[correct][start]].fillcolor('black')
                    print(xLines[correct][start])
                layoutColour[xLines[correct][start]] = 1
                start -= 1
                if xLines[correct][start] == xLines[correct][end] and layoutColour[xLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[xLines[correct][start]].fillcolor('black')
                        print(xLines[correct][start])
                    else:
                        layoutList[xLines[correct][start]].fillcolor('black')
                        print(xLines[correct][start])
                    layoutColour[xLines[correct][start]] = 1

    # ----------------- Right to Left ------------------
    if found is False:
        for k in range(0, len(rLLines), 1):
            for j in range(0, len(rLLines[k]), 1):
                if rLLines[k][j] == circleNumber1:
                    for l in range(0, len(rLLines[k]), 1):
                        if rLLines[k][l] == circleNumber2:
                            correct = k
                            start = j
                            end = l
                            found = True
                            print(rLLines)
                            print(rLLines[correct][start], rLLines[correct][end])
        if rLLines[correct][end] - rLLines[correct][start] > 0:
            while rLLines[correct][start] < rLLines[correct][end] and layoutColour[rLLines[correct][start]] == 0:
                if player == 1:
                    layoutList[rLLines[correct][start]].fillcolor('black')
                    print(rLLines[correct][start])
                else:
                    layoutList[rLLines[correct][start]].fillcolor('black')
                    print(rLLines[correct][start])
                layoutColour[rLLines[correct][start]] = 1
                start += 1
                if rLLines[correct][start] == rLLines[correct][end] and layoutColour[rLLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[rLLines[correct][start]].fillcolor('black')
                        print(rLLines[correct][start])
                    else:
                        layoutList[rLLines[correct][start]].fillcolor('black')
                        print(rLLines[correct][start])
                    layoutColour[rLLines[correct][start]] = 1
        elif rLLines[correct][end] - rLLines[correct][start] < 0:
            while rLLines[correct][start] > rLLines[correct][end] and layoutColour[rLLines[correct][start]] == 0:
                if player == 1:
                    layoutList[rLLines[correct][start]].fillcolor('black')
                    print(rLLines[correct][start])
                else:
                    layoutList[rLLines[correct][start]].fillcolor('black')
                    print(rLLines[correct][start])
                layoutColour[rLLines[correct][start]] = 1
                start -= 1
                if rLLines[correct][start] == rLLines[correct][end] and layoutColour[rLLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[rLLines[correct][start]].fillcolor('black')
                        print(rLLines[correct][start])
                    else:
                        layoutList[rLLines[correct][start]].fillcolor('black')
                    layoutColour[rLLines[correct][start]] = 1
    # ------------------- Left to Right --------------
    if found is False:
        for k in range(0, len(lRLines), 1):
            for j in range(0, len(lRLines[k]), 1):
                if lRLines[k][j] == circleNumber1:
                    for l in range(0, len(lRLines[k]), 1):
                        if lRLines[k][l] == circleNumber2:
                            correct = k
                            start = j
                            end = l
                            found = True
                            print(lRLines)
                            print(lRLines[correct][start], lRLines[correct][end])
        if lRLines[correct][end] - lRLines[correct][start] > 0:
            while lRLines[correct][start] < lRLines[correct][end] and layoutColour[lRLines[correct][start]] == 0:
                if player == 1:
                    layoutList[lRLines[correct][start]].fillcolor('black')
                    print(lRLines[correct][start])
                else:
                    layoutList[lRLines[correct][start]].fillcolor('black')
                    print(lRLines[correct][start])
                layoutColour[lRLines[correct][start]] = 1
                start += 1
                if lRLines[correct][start] == lRLines[correct][end] and layoutColour[lRLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[lRLines[correct][start]].fillcolor('black')
                        print(lRLines[correct][start])
                    else:
                        layoutList[lRLines[correct][start]].fillcolor('black')
                        print(lRLines[correct][start])
                    layoutColour[lRLines[correct][start]] = 1
        elif lRLines[correct][end] - lRLines[correct][start] < 0:
            while lRLines[correct][start] > lRLines[correct][end] and layoutColour[lRLines[correct][start]] == 0:
                if player == 1:
                    layoutList[lRLines[correct][start]].fillcolor('black')
                    print(lRLines[correct][start])
                else:
                    layoutList[lRLines[correct][start]].fillcolor('black')
                    print(lRLines[correct][start])
                layoutColour[lRLines[correct][start]] = 1
                start -= 1
                if lRLines[correct][start] == lRLines[correct][end] and layoutColour[lRLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[lRLines[correct][start]].fillcolor('black')
                        print(lRLines[correct][start])
                    else:
                        layoutList[lRLines[correct][start]].fillcolor('black')
                        print(lRLines[correct][start])
                    layoutColour[lRLines[correct][start]] = 1
    if found is True:
        layoutColour[circleNumber1] = 1
    return


# -------------Even handlers--------------

map = ['000000000000000',
       '000000000000000',
       '000000000000000',
       '000000000000000',
       '000000010000000',
       '000000101000000',
       '000001010100000',
       '000010101010000',
       '000101010101000',
       '001010101010100',
       '010101010101010',
       '000000000000000',
       '000000000000000',
       '000000000000000',
       '000000000000000']

for i in range(0, 28, 1):
    layoutSpawn()

indexPlace = 0
for j in range(0, 15, 1):
    for i in range(0, 15, 1):
        temp = 0
        xCoord = 40 * (i - 8)
        yCoord = 70 * (8 - j)
        if map[j][i] == '1':
            layoutList[indexPlace].goto(xCoord, yCoord)
            indexPlace += 1

quitFlag = False
selectToggle = False
found = False
won = False

# --------------Listen--------------------

mywindow.listen()

mywindow.onkey(leave, 'q')
mywindow.onclick(click)

# -------------main game loop-------------

while quitFlag is False:
    if selectToggle is True:
        for i in range(0, 28, 1):
            select(layoutList[i], layoutRadius)
    mywindow.update()
