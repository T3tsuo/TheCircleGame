import turtle

# -------------P1 and P2 names----------
p1Name = input("What is the first competitor's name?")
p2Name = input("What is the second competitor's name?")

# -------------Turtles and Variables -------------------
mywindow = turtle.Screen()
mywindow.title("Jeux de Cercle")
mywindow.setup(600, 600)

mywindow.tracer(0, 0)

p1 = turtle.Turtle()
p1.penup()
p1.shape('square')
p1.turtlesize(2, 3)
p1.color('red')
p1.goto(-240, 260)

p2 = turtle.Turtle()
p2.penup()
p2.shape('square')
p2.turtlesize(2, 3)
p2.color('green')
p2.goto(240, 260)

write = turtle.Turtle()
write.hideturtle()
write.penup()
write.goto(150, -175)
write.write('If you want to color', font=('Arial', 11, 'normal'))
write.goto(150, -190)
write.write('only one circle', font=('Arial', 11, 'normal'))
write.goto(150, -205)
write.write('tap the circle', font=('Arial', 11, 'normal'))
write.goto(150, -220)
write.write('you want to colour.', font=('Arial', 11, 'normal'))
write.goto(150, -235)
write.write('TWICE.', font=('Arial', 11, 'normal'))
write.goto(-280, -130)
write.write('Tap on the FIRST circle you want to colour.', font=('Arial', 11, 'normal'))
write.goto(-280, -145)
write.write("Then tap on the LAST circle you want to colour.", font=('Arial', 11, 'normal'))
write.goto(-280, -175)
write.write("Press 'q' to quit the game.", font=('Arial', 11, 'normal'))
write.goto(-280, -200)
write.write('Rules: Each player takes turns of coloring at least one circle.', font=('Arial', 11, 'normal'))
write.goto(-280, -215)
write.write('If a player colors more than one circle, they can only color', font=('Arial', 11, 'normal'))
write.goto(-280, -230)
write.write('the circles in the direction they are coloring and', font=('Arial', 11, 'normal'))
write.goto(-280, -245)
write.write('cannot pass other coloured circles.', font=('Arial', 11, 'normal'))
write.goto(-280, -260)
write.write("The person that colors the final circle/circles wins the game.", font=('Arial', 11, 'normal'))
write.goto(-280, -275)
write.write("GOOD LUCK BEATING ME.", font=('Arial', 11, 'normal'))

write.goto(-270, 220)
write.write(p1Name, font=('Arial', 11, 'normal'))
write.goto(210, 220)
write.write(p2Name, font=('Arial', 11, 'normal'))

write.goto(-100, 200)
write.write("Player's Turn :", font=('Arial', 18, 'normal'))

writeTurns = turtle.Turtle()
writeTurns.hideturtle()
writeTurns.penup()
writeTurns.goto(-100, 170)
writeTurns.write(p1Name, font=('Arial', 18, 'normal'))

xLines = [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25, 26, 27]]
lRLines = [[21], [15, 22], [10, 16, 23], [6, 11, 17, 24], [3, 7, 12, 18, 25], [1, 4, 8, 13, 19, 26],
           [0, 2, 5, 9, 14, 20, 27]]
rLLines = [[27], [20, 26], [14, 19, 25], [9, 13, 18, 24], [5, 8, 12, 17, 23], [2, 4, 7, 11, 16, 22],
           [0, 1, 3, 6, 10, 15, 21]]

Index = -1
layoutList = []
layoutColour = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
layoutRadius = 20
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
colorP1 = 0
colorP2 = 0


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
    layoutList[Index].turtlesize(2, 2)
    layoutList[Index].color('black')
    layoutList[Index].fillcolor('white')
    return


def endTurn(x, y):
    global player, selectToggle, layoutCounter, circleNumber1, circleNumber2, found, won, start, end, correct, colorP2, colorP1
    player *= -1
    won = True
    for i in range(0, len(layoutColour), 1):
        if layoutColour[i] == 0:
            won = False
    if won is True:
        for k in range(0, len(layoutList), 1):
            layoutList[k].hideturtle()
        for i in range(0, len(layoutColour), 1):
            if layoutColour[i] == 1:
                colorP1 += 1
            elif layoutColour[i] == -1:
                colorP2 += 1
        if player == -1:
            write.clear()
            writeTurns.clear()
            writeTurns.goto(-100, 170)
            writeTurns.write(p1Name, font=('Arial', 18, 'normal'))
            write.goto(-100, 150)
            write.write('WINS', font=('Arial', 18, 'normal'))
        else:
            write.clear()
            writeTurns.clear()
            writeTurns.goto(-100, 170)
            writeTurns.write(p2Name, font=('Arial', 18, 'normal'))
            write.goto(-100, 150)
            write.write('WINS', font=('Arial', 18, 'normal'))
        write.goto(-100, 130)
        write.write(p1Name, font=('Arial', 11, 'normal'))
        write.goto(-100, 115)
        write.write('coloured:', font=('Arial', 11, 'normal'))
        write.goto(-30, 115)
        write.write(colorP1, font=('Arial', 11, 'normal'))
        write.goto(-10, 115)
        write.write('circles', font=('Arial', 11, 'normal'))
        write.goto(-100, 85)
        write.write(p2Name, font=('Arial', 11, 'normal'))
        write.goto(-100, 70)
        write.write('coloured:', font=('Arial', 11, 'normal'))
        write.goto(-30, 70)
        write.write(colorP2, font=('Arial', 11, 'normal'))
        write.goto(-10, 70)
        write.write('circles', font=('Arial', 11, 'normal'))
    elif player == 1:
        writeTurns.clear()
        writeTurns.goto(-100, 170)
        writeTurns.write(p1Name, font=('Arial', 18, 'normal'))
    else:
        writeTurns.clear()
        writeTurns.goto(-100, 170)
        writeTurns.write(p2Name, font=('Arial', 18, 'normal'))
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
                t1.fillcolor('red')
                circleNumber1 = i
                layoutCounter += 1
                selectToggle = False
            else:
                circleNumber2 = i
                layoutCounter += 1
                selectToggle = False
        if player == -1 and layoutColour[i] == 0 and layoutCounter < 3:
            if circleNumber1 == 0 and layoutCounter == 1:
                t1.fillcolor('green')
                circleNumber1 = i
                layoutCounter += 1
                selectToggle = False
            else:
                circleNumber2 = i
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
    # use the list, find which list both numbers are in, then check if the circles in between are coloured
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
        if xLines[correct][end] - xLines[correct][start] > 0:
            while xLines[correct][start] < xLines[correct][end] and layoutColour[xLines[correct][start]] == 0:
                if player == 1:
                    layoutList[xLines[correct][start]].fillcolor('red')
                    layoutColour[xLines[correct][start]] = 1
                else:
                    layoutList[xLines[correct][start]].fillcolor('green')
                    layoutColour[xLines[correct][start]] = -1
                start += 1
                if xLines[correct][start] == xLines[correct][end] and layoutColour[xLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[xLines[correct][start]].fillcolor('red')
                        layoutColour[xLines[correct][start]] = 1
                    else:
                        layoutList[xLines[correct][start]].fillcolor('green')
                        layoutColour[xLines[correct][start]] = -1
        elif xLines[correct][end] - xLines[correct][start] < 0:
            while xLines[correct][start] > xLines[correct][end] and layoutColour[xLines[correct][start]] == 0:
                if player == 1:
                    layoutList[xLines[correct][start]].fillcolor('red')
                    layoutColour[xLines[correct][start]] = 1
                else:
                    layoutList[xLines[correct][start]].fillcolor('green')
                    layoutColour[xLines[correct][start]] = -1
                start -= 1
                if xLines[correct][start] == xLines[correct][end] and layoutColour[xLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[xLines[correct][start]].fillcolor('red')
                        layoutColour[xLines[correct][start]] = 1
                    else:
                        layoutList[xLines[correct][start]].fillcolor('green')
                        layoutColour[xLines[correct][start]] = -1

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
        if rLLines[correct][end] - rLLines[correct][start] > 0:
            while rLLines[correct][start] < rLLines[correct][end] and layoutColour[rLLines[correct][start]] == 0:
                if player == 1:
                    layoutList[rLLines[correct][start]].fillcolor('red')
                    layoutColour[rLLines[correct][start]] = 1
                else:
                    layoutList[rLLines[correct][start]].fillcolor('green')
                    layoutColour[rLLines[correct][start]] = -1
                start += 1
                if rLLines[correct][start] == rLLines[correct][end] and layoutColour[rLLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[rLLines[correct][start]].fillcolor('red')
                        layoutColour[rLLines[correct][start]] = 1
                    else:
                        layoutList[rLLines[correct][start]].fillcolor('green')
                        layoutColour[rLLines[correct][start]] = -1
        elif rLLines[correct][end] - rLLines[correct][start] < 0:
            while rLLines[correct][start] > rLLines[correct][end] and layoutColour[rLLines[correct][start]] == 0:
                if player == 1:
                    layoutList[rLLines[correct][start]].fillcolor('red')
                    layoutColour[rLLines[correct][start]] = 1
                else:
                    layoutList[rLLines[correct][start]].fillcolor('green')
                    layoutColour[rLLines[correct][start]] = -1
                start -= 1
                if rLLines[correct][start] == rLLines[correct][end] and layoutColour[rLLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[rLLines[correct][start]].fillcolor('red')
                        layoutColour[rLLines[correct][start]] = 1
                    else:
                        layoutList[rLLines[correct][start]].fillcolor('green')
                        layoutColour[rLLines[correct][start]] = -1

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
        if lRLines[correct][end] - lRLines[correct][start] > 0:
            while lRLines[correct][start] < lRLines[correct][end] and layoutColour[lRLines[correct][start]] == 0:
                if player == 1:
                    layoutList[lRLines[correct][start]].fillcolor('red')
                    layoutColour[lRLines[correct][start]] = 1
                else:
                    layoutList[lRLines[correct][start]].fillcolor('green')
                    layoutColour[lRLines[correct][start]] = -1
                start += 1
                if lRLines[correct][start] == lRLines[correct][end] and layoutColour[lRLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[lRLines[correct][start]].fillcolor('red')
                        layoutColour[lRLines[correct][start]] = 1
                    else:
                        layoutList[lRLines[correct][start]].fillcolor('green')
                        layoutColour[lRLines[correct][start]] = -1
        elif lRLines[correct][end] - lRLines[correct][start] < 0:
            while lRLines[correct][start] > lRLines[correct][end] and layoutColour[lRLines[correct][start]] == 0:
                if player == 1:
                    layoutList[lRLines[correct][start]].fillcolor('red')
                    layoutColour[lRLines[correct][start]] = 1
                else:
                    layoutList[lRLines[correct][start]].fillcolor('green')
                    layoutColour[lRLines[correct][start]] = -1
                start -= 1
                if lRLines[correct][start] == lRLines[correct][end] and layoutColour[lRLines[correct][start]] == 0:
                    if player == 1:
                        layoutList[lRLines[correct][start]].fillcolor('red')
                        layoutColour[lRLines[correct][start]] = 1
                    else:
                        layoutList[lRLines[correct][start]].fillcolor('green')
                        layoutColour[lRLines[correct][start]] = -1
    if found is True:
        if player == 1:
            layoutColour[circleNumber1] = 1
        else:
            layoutColour[circleNumber1] = -1
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
        xCoord = 20 * (i - 8)
        yCoord = 35 * (8 - j)
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
