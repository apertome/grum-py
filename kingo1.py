#!/usr/bin/python

from graphics import *
import random
import json
import math


##def displayGrid(lifegrid):


def main():
    win = GraphWin("TestingWindow", 1000, 1000)
    win.setBackground(color_rgb(0, 0, 0))
    c1speed, c1chasespeed = 2, 1.1
    c2speed, c2escapespeed = 3, 1

    #show a thing in the center
    gs = Point(win.width/2,win.height/2)
    cs = Circle(gs, 10)
    cs.setFill(color_rgb(100,100,100))
    cs.draw(win)


    ## c1 is chasing c2

    sx1, sy1 = (random.randrange(0, win.width), random.randrange(0, win.height))
    g1 = Point(sx1,sy1)
    c1 = Circle(g1, 5)
    c1.setFill(color_rgb(20,90, 130))
    c1.draw(win)

    sx2, sy2 = (random.randrange(0, win.width), random.randrange(0, win.height))
    g2 = Point(sx2,sy2)
    c2 = Circle(g2,2)
    c2.setFill(color_rgb(200,0,0))
    c2.draw(win)
##    g1.setOutline(color_rgb(20,98,200))
##    g1.draw(win)

    dataObj = {}
    records = 0


    while c1.getCenter().getX() > 0 and c1.getCenter().getX() < win.width and \
          c1.getCenter().getY() > 0 and c1.getCenter().getY() < win.height and records < 1000:

	c1obj = {}
	c2obj = {}
	c1obj['radius'] = 5
	c2obj['radius'] = 2

	c1obj['color'] = [20, 90, 130]
	c2obj['color'] = [200, 0, 0]

	c1obj['center'] = c1.getCenter().getX(), c1.getCenter().getY()
	c2obj['center'] = c2.getCenter().getX(), c2.getCenter().getY()


        if c2.getCenter().getX() < c1.getCenter().getX():
            x_off = -c1chasespeed
        if c2.getCenter().getX() > c1.getCenter().getX():
            x_off = c1chasespeed
        if c2.getCenter().getY() < c1.getCenter().getY():
            y_off = -c1chasespeed
        if c2.getCenter().getY() > c1.getCenter().getY():
            y_off = c1chasespeed

        if c2.getCenter().getX() < win.width / 2:
            x2_off = c2escapespeed
        if c2.getCenter().getX() > win.width / 2:
            x2_off = -c2escapespeed
        if c2.getCenter().getY() < win.height / 2:
            y2_off = c2escapespeed
        if c2.getCenter().getY() > win.height / 2:
            y2_off = -c2escapespeed

	c1obj['off'] = [x_off, y_off]
	c2obj['off'] = [x2_off, y2_off]

        x2,y2 = (random.randrange(-c2speed,c2speed), random.randrange(-c2speed,c2speed))
        x,y = (random.randrange(-c1speed,c1speed), random.randrange(-c1speed,c1speed))

        x = x+x_off
        y = y+y_off
        x2 = x2+x2_off
        y2 = y2+y2_off

	dataObj['c1'] = {}
	dataObj['c2'] = {}
	dataObj['c1'] = c1obj
	dataObj['c2'] = c2obj
	dataObj['c1c2dist'] = math.sqrt( ( x2 - x ) ** 2 + ( y2 - y ) ** 2 )

	#for x in dataObj.keys():
	#    print x +" => " + dataObj[x]
	#print(json.dumps(dataObj, indent = 4))
	print(json.dumps(dataObj))


        c2.move(x2,y2)
        c1.move(x,y)
        #time.sleep(.07)
	records += 1



    win.getMouse()
    win.close()

main()
