"""
Both rectangle and 
circle should extend the Shape class
and should calculate their own
area and perimeter. This is called
"polymorphism" because we sent
the same message - "area" - to
both circle and rectangle, but we
got different responses
"""


class Shape:

    def __init__(self):
        pass

    def setChar(self):
        pass


class Rectangle(Shape):

    def __init__(self, bredth, width):
        super().__init__()
        self.bredth = bredth
        self.width = width
        pass

    # get the area of a rectangle
    def area(self):
        pass

    # get the perimeter of a rectangle
    def perimeter(self):
        pass

    # draw a rectangle as a string
    def draw(self, char):
        return (((char * self.bredth) + "\n") * self.width)[:-1]


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        pass

    # get the area of a circle
    def area(self):
        pass

    # get the perimeter of a circle
    def perimeter(self):
        pass

    def diameter(self):
        pass

    # draw a circle as a string
    def draw(self, char):
        diameter = self.diameter()
        radius = diameter / 2 - .5
        r = (radius + .25)**2 + 1
        result = ''
        for i in range(diameter):
            y = (i - radius)**2
            for j in range(diameter):
                x = (j - radius)**2
                if x + y <= r:
                    result += char
                else:
                    result += ' '
            result += '\n'
        return result
        pass


# test if your code works as intended
def tests(tester):
    c = Circle(10)
    r = Rectangle(5, 2)
    tester.set_env(locals())
    tester.ae("c.area()", 314.159, "circle area")
    tester.ae("c.perimeter()", 62.8319, "circle perimeter")
    tester.ae("r.area()", 10, "rectangle area")
    tester.ae("r.perimeter()", 14, "rectangle perimeter")
    tester.ae("r.draw('*')", """*****
*****""", "test draw rectangle")
