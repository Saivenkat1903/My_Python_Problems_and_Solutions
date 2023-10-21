''' First time learning object oriented programming and using it in the example of Points in the plane '''

import math

class Point:
    '''going to define a class which moves points and also gives the distance between them'''

    def __init__(self,x=0,y=0):
        '''Automaticallly makes a point at the given coordinates specified, default is (0,0)'''
        self.x=x
        self.y=y

    def move(self,x=None,y=None):
        '''Moves a given point to the specified coordinates'''
        if x==None:
            x=self.x
        if y==None:
            y=self.y
        self.x=x
        self.y=y

    def reset(self):
        '''Resets the point to the origin'''
        self.x=0
        self.y=0

    def distanceBetween(self,point):
        '''Gives back the distance between 2 points'''
        return math.sqrt((self.x-point.x)**2+(self.y-point.y)**2)

p1=Point(1,2)
p2=Point(2,4)
p3=Point()

print("The x coordinate of point1 is "+str(p1.x))
print("The y coordinate of point1 is "+str(p2.y))
p1.move(5)
print("The x coordinate of point1 is now "+str(p1.x)+str(p1.y))
p2.move(4,8)
print("The y coordinate of point2 is "+str(p2.y))

print("The distance between the 2 points is "+str(p1.distanceBetween(p2)))
