import math

class Point:
    def __init__(self, r=None, phi=None):

        if r is None or phi is None:
            raise TypeError('Missing required argument!')

        if not( type(r) is int or type(r) is float or type(phi) is int or type(phi) is float ):
            raise TypeError('Incorrect type! Please, enter type float or int')

        self.r = r
        if r == 0:
            self.phi = 0

        phi_without_period = phi - 360*(phi//360)
        if -360 <= phi_without_period <= -180:
            self.phi = phi_without_period+360
        elif -180 < phi_without_period <= 180:
            self.phi = phi_without_period
        elif 180 < phi_without_period <= 360:
            self.phi = phi_without_period - 360


    def __str__(self):
        return 'r = ' + str(round(self.r, 2)) + ', phi = ' + str(round(self.phi, 2))

    def __repr__(self):
        return 'Point('+str(round(self.r, 2))+', '+str(round(self.phi,2))+')'

    @classmethod
    def from_carthesian(cls, x=None, y=None):

        if x is None or y is None:
            raise TypeError('Missing required argument!')

        if not( type(x) is int or type(x) is float or type(y) is int or type(y) is float ):
            raise TypeError('Incorrect type! Please, enter type float or int')

        if x == 0:
            return cls(r=y, phi=90)
        else:
            return cls(r=(x**2 + y**2)**0.5, phi=math.degrees(math.atan2(y, x)))

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError('Unsupported type!')

        return Point.from_carthesian(x=( other.r * math.cos(math.radians(other.phi)) + self.r * math.cos(math.radians(self.phi)) ), y=( other.r * math.sin(math.radians(other.phi)) + self.r * math.sin(math.radians(self.phi)) ))

    def __neg__(self):
        return Point(r=self.r, phi=self.phi+180)

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise TypeError('Unsupported type!')

        return self + (-other)

p1 = Point(r=1, phi=0)
p2 = Point(r=1, phi=90)
p3 = p1 + p2
# p3 — точка с r = 1.41 (примерно) и phi = 45
print(repr(p3))  # Point(1, 10)
