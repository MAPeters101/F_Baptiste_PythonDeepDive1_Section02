

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

r1 = Rectangle(10, 20)
print(r1.width)
r1.width = 100
print(r1.width)
print('-'*80)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

r1 = Rectangle(10, 20)
print(r1.area())
print(r1.perimeter())
print('-'*80)







