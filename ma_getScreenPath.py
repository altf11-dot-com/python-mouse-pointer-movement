def getScreenPath():
    screenPath = []
    twoPoints = []
    lineCounter = 0
    f = open("pathway.txt", "r")
    for l in f:
        screenXY = l.strip('\n').split(',')
        screenXY[0] = int(screenXY[0])
        screenXY[1] = int(screenXY[1])
        twoPoints.append(tuple(screenXY))
        if len(twoPoints) == 2:
            screenPath.append(twoPoints)
            twoPoints = []
            twoPoints.append(screenXY)
            lineCounter = 0
    f.close()
    return screenPath

print(getScreenPath())
