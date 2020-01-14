# moves the mouse pointer from one point to another
# for smooth mouse movement during screen recordings
# first time with comments 7-13-2019 12:03 
# Asus Q324 C:\Users\JLB\Anaconda2\python.exe 11/08/2017  06:41 PM 28,160
# Python 2.7.14 |Anaconda, Inc.| (default, Nov  8 2017, 13:40:45) [MSC v.1500 64 bit (AMD64)] on win32
# usage ma.py [g]
# g = print expose current cursor position
# 7-13-2019 12:03 points are static during initial builds
# working ma_BKP_201907131209.py non-g moves after 3 second delay (\python ma.py)
# working ma_BKP_201907131300.py get, run moves after 3 second delay (\python ma.py [get|run])
# 1301 - adding countdown

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
else
    cmd = sys.argv[1]

if cmd == 'get':
    get_cursor_pos()
elif cmd == 'run':
    countdown(3)
    p1 = [1239,663]
    p2 = [586, 204]
    p3 = [428, 543]
    p4 = [1109,141]
    for p in [[p1,p2], [p2, p3], [p3, p4]]:
        move_two_points(p)
        time.sleep(.25)
else
    print 'usage: python ma.py <command>'
    print '   commands:'
    print '      get     Print current mouse pointer position: x, y'
    print '              redirect output of get to pw.txt'
    print ''
    print '      run     Move the mouse pointer, follows path in pw.txt'
    print '              after 3 second delay'