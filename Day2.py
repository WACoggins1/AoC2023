from enum import Enum

#if bag only contains 12 red, 13 green, and 14 blue, which games are possible?
#game 1: 5 red (yes)
#game 3: 20 red (no)
#what is sum of possible game IDs?

class Color(Enum):
    RED = 12
    GREEN = 13
    BLUE = 14


day2 = open("AdventDay2_2023.txt").read().splitlines()

gameSum = 0
powerSum = 0

for k in day2:

    isPossible = True
    minRed = 0
    minBlue = 0
    minGreen = 0

    #remove new line characters
    k = k.strip()

    #hold game number
    phase1 = k.split(":")
    gameNum = phase1[0].split(" ")

    #store
    sets = phase1[1].split(";")

    for set in sets:
        cubes = set.split(",")

        for cube in cubes:

            cubeData = cube.split(" ")
            cubeData.remove('')


            match cubeData[1]:

                case 'blue':
                    if(int(cubeData[0]) > minBlue):
                        minBlue = int(cubeData[0])
                    if(int(cubeData[0]) > Color.BLUE.value):
                        isPossible = False

                case 'green':
                    if(int(cubeData[0]) > minGreen):
                        minGreen = int(cubeData[0])
                    if(int(cubeData[0]) > Color.GREEN.value):
                        isPossible = False

                case 'red':
                    if(int(cubeData[0]) > minRed):
                        minRed = int(cubeData[0])
                    if(int(cubeData[0]) > Color.RED.value):
                        isPossible = False

    powerSum = powerSum + (minRed*minBlue*minGreen)

    if isPossible:
        gameSum = gameSum + int(gameNum[1])

print("Possible Game Sum: ", gameSum)
print("Power set sum: ", powerSum)
