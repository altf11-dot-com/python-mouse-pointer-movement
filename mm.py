# moves the mouse pointer along a path described in pw.txt
# for smooth mouse movement during screen recordings
# format of pw.txt: x,y\n x,y\n
# https://github.com/altf11-dot-com/python-mouse-pointer-movement
# http://altf11.com

import win32api 
import time
import sys

def countdown(secs):
    for i in range(secs):
        print "running path in ", secs - i
        time.sleep(1)

def get_cursor_pos():
    x, y = win32api.GetCursorPos()
    print str(x) + ',' + str(y)


def move_two_points(points):
    pointA, pointB = points[0], points[1]
    stops = 90.0
    clr = 10
    win32api.SetCursorPos(pointA)
    x, y = pointA[0], pointA[1]
    for i in range(int(stops)):
        x = pointA[0] + int((i/stops) * (pointB[0] - pointA[0]))
        y = pointA[1] + int((i/stops) * (pointB[1] - pointA[1]))
        win32api.SetCursorPos((x,y))
        time.sleep(1.25/stops)
    win32api.SetCursorPos(pointB)
    # to hide the cursor trails
    for i in range(int(clr)):
        win32api.SetCursorPos((x,y))
        time.sleep(.50/clr)

def getScreenPath():
    screenPath = []
    twoPoints = []
    lineCounter = 0
    f = open("pw.txt", "r")
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

if len(sys.argv) == 1:
    cmd = ''
else:
    cmd = sys.argv[1]

if cmd == 'get':
    get_cursor_pos()
elif cmd == 'run':
    countdown(3)
    for p in getScreenPath():
        move_two_points(p)
        time.sleep(.25)
else:
    print 'usage: python ma.py <command>'
    print '   commands:'
    print '      get     Print current mouse pointer position: x, y'
    print '              redirect output of get to pw.txt'
    print ''
    print '      run     Move the mouse pointer, follows path in pw.txt'
    print '              after 3 second delay'