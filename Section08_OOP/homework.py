from math import sqrt

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        part1 = (self.coor2[0] - self.coor1[0])**2
        part2 = (self.coor2[1] - self.coor1[1])**2
    
        # solution - tuple unpacking
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        # return ((self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0]))
        # return sqrt(part2 + part1)
        return ((x2-x1) ** 2 + (y2-y1) ** 2)**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return (y2-y1) / (x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

print(f'distance {li.distance()}')

print(f'slope {li.slope()}')

class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        pass
    
    def volume(self):
        return 3.14 * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * 3.14 * self.radius * self.height + 2 * 3.14 * (self.radius ** 2)

c = Cylinder(2,3)

print(f'Volume is {c.volume()}')
print(f'Surface Area is {c.surface_area()}')
