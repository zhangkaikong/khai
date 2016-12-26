#coding:utf-8
import math
class Point(object):
    def __init__(self,xValue,yValue):
        self.xValue = xValue
        self.yValue = yValue

class Circle(Point):
    def __init__(self,xValue,yValue,rValue):
        Point.__init__(self,xValue,yValue)
        self.rValue = rValue

    def getArea(self):
        print 'The area of the circle is %d'%(math.pi*self.rValue*self.rValue)

circle = Circle(20,30,27)
circle.getArea()