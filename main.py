class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r


class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__()
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Triangle(Shape):
    def __init__(self, a, b, c, h):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def area(self):
        return 0.5 * self.a * self.h

    def perimeter(self):
        return self.a + self.b + self.c


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5, 2.5)
]

for s in shapes:
    print(type(s).__name__, "area:", s.area(), "perimeter:", s.perimeter())
