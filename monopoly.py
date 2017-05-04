##Author: Timothy WIlliams
#
##Date: 3/2/2017
#
##Finds the most visited spaces on a monopoly board.

import random

inRow = 0 #how many doubles in a row

#keeps track of how many times a space was visited (40 spaces)
pos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
#tracks current position on the board
curPos = 0

progress = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

#will draw a card from chance or community chest
def chance():
    na = ("%r", 0)
    switch = {
        0: ("%a", 24),
        1: ("%a", 16),
        2: ("%a", 39),
        3: ("%a", 5),
        4: ("%a", 10),
        5: ("%a", 0),
        6: ("%r", -3),
        }
    return switch.get(random.randint(0, 16), na)
def communityChest():
    na = ("%r", 0)
    switch = {
        0: ("%a", 10),
        1: ("%a", 0),
    }
    return switch.get(random.randint(0, 16), na)

#rolls the dice
def rollDice(inRow):
    i = random.randint(1, 6)
    j = random.randint(1, 6)
    if i == j:
        inRow += 1
    else:
        inRow = 0
    out = [("%r", (i + j)), inRow]
    return out

#moves the current position around the board
def move(rollIn, curPos):
    if rollIn[0] == "%r":
        return (rollIn[1] + curPos)%40
    elif rollIn[0] == "%a":
        return rollIn[1]
    

#to actually roll the dice and move
print("Starting")
iterations = 10000000
for i in range(0, iterations):
    if (i / 100000) in progress: print(str(int(i / (iterations / 100))) + "%")
    rollOut, inRow = rollDice(inRow)
    if inRow == 3 or curPos == 30: #if 3 doubles were rolled in a row or landed on go to jail
        inRow = 0
        curPos = move(("%a", 10), curPos)
        pos[curPos] += 1
    else:
        curPos = move(rollOut, curPos)
        pos[curPos] += 1
    if curPos == 7 or curPos == 22 or curPos == 36: #checks if on chance
        temp = curPos #saves the current position to avoid double counting the same position
        curPos = move(chance(), curPos)
        if curPos != temp:
            pos[curPos] += 1
            if curPos == 10:
                inRow = 0
    if curPos == 2 or curPos == 17 or curPos == 33: #checks if on community chest
        temp = curPos #saves the current position
        curPos = move(communityChest(), curPos)
        if curPos != temp:
            pos[curPos] += 1
            if curPos == 10:
                inRow = 0

#printing results
print("100%\nPrinting Results")
allRolls = sum(pos)

print()
print("Distrobution of most visited positions on board (raw):")
for i in range(0, 40):
    print("Square " + str(i) + ": " + str(pos[i]))
print()
print("Distrobution of most visited positions on board (percent):")
for i in range(0, 40):
    print("Square " + str(i) + ": " + str((pos[i] / allRolls) * 100) + "%")

#rank the spaces (most to least visited) then print results
rankPos = sorted(pos, reverse=True)
print()
print("Ranked distrobution of most visited positions on board (percent):")
for i in rankPos:
    print("Square " + str(pos.index(i)) + ": " + str((i / allRolls) * 100) + "%")

print()
print("End")
