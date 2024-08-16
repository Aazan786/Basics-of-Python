class Point:
    Azan = "White Guy" # Class attributes  and Class Methods are Associated with class. They Are called with class referance. 
    

    def __init__(self, x=0, y=0): # Instance Methods
        self.x = x # Instance attributes
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    # def __str__(self):
    #     return f" ({self.x} {self.y})"


    def __pow__(self, other):
        x = self.x ** other.x
        y = self.y ** other.y
        return Point(x, y)

Point.Azan = "Handsome"
p1 = Point(2, 3)
p2 = Point(2, 3)
print(p1.Azan)
print(Point.Azan)
print(p1 ** p2)
print(p1)

# Output: (3,5)
