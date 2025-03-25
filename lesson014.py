

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

print(str(r1))
print(hex(id(r1)))
print()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def to_string(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

r1 = Rectangle(10, 20)
print(str(r1))
print(hex(id(r1)))
print(r1.to_string())
print('-'*80)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

r1 = Rectangle(10, 20)
print(str(r1))
print(r1)
print()

l = [1,2,3]
print(str(l))
print(l)
print('-'*80)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

r1 = Rectangle(10, 20)
print(str(r1))
print(r1)
print(repr(r1))
print('-'*80)

r2 = Rectangle(10, 20)
print(r1 is not r2)
print(r1 == r2)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height
        #return (self.width, self.height) == (other.width, other.height)

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
print(r1 is not r2)
print(r1 == r2)
print('-'*80)

#print(r1 == 100)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
print(r1 == r2)
print(r1 == 100)
print('-'*80)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(10, 20)
r2 = Rectangle(100, 200)
print(r1 < r2)
print(r2 < r1)
print(r2 > r1)
#print(r1 <= r2)
print('-'*80)

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        else:
            self._width = width

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False

r1 = Rectangle(10, 20)
#print(r1.width)
r1.width = -100
print(r1.width)
print(r1._width)
print(r1.get_width())
print(r1)

#r1.set_width(-10)
r1.set_width(100)
print(r1)









print('-'*80)










