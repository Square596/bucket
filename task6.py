import math


def sign(x):
    return int(x>0) - int(x<0)


class Point:
    """
    This class defines a 2D vector in radial coordinates.

    Keep in mind that a null vector has an angle of 0 by default.
    Angles are measured in degrees from -180 to +180.
    """

    def __init__(self, r: float, phi: float):
        if not (isinstance(r, int | float) and  isinstance(phi, int | float)):
            raise TypeError('Incorrect type! Please, enter arguments of type int or float')

        if r < 0:
            raise ValueError('Incoorect value of "r"! It should be positive number.')
        self.r = r
        if r == 0:
            self.phi = 0
        else:
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
    def from_carthesian(cls, x: float, y: float):
        if not (isinstance(x, int | float) and  isinstance(y, int | float)):
            raise TypeError('Incorrect type! Please, enter arguments of type int or float')

        if x == 0:
            return cls(r=y, phi=90*sign(y))
        else:
            return cls(r=(x**2 + y**2)**0.5, phi=math.degrees(math.atan2(y, x)))

    def __add__(self, other):
        if not isinstance(other, Point):
            raise NotImplementedError('Unsupported type!')

        return Point.from_carthesian(x=( other.r * math.cos(math.radians(other.phi)) + self.r * math.cos(math.radians(self.phi)) ),
                                     y=( other.r * math.sin(math.radians(other.phi)) + self.r * math.sin(math.radians(self.phi)) ))

    def __neg__(self):
        return Point(r=self.r, phi=self.phi+180)

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise NotImplementedError('Unsupported type!')

        return self + (-other)

    def __eq__(self, other):
        if not isinstance(other, Point):
            raise NotImplementedError('Unsupported type!')

        return self.r == other.r and self.phi == other.phi


p1 = Point(1, 120)
p2 = Point(1, 480)

print(p1 == p2)  # True
