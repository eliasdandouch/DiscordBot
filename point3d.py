from graphics.point2d import Point2D
from math import sqrt

class Point3D(Point2D):

    def __init__(self, x=0, y=0, z=0):
        Point2D.__init__(self, x, y)
        self.__z = z

    def getz(self):
        return self.__z

    def translate(self, dx, dy, dz):
        Point2D.translate(self, dx, dy)
        self.translatez(dz)

    def translatez(self, dz):
        # Put code here that moves self.__z by dz units
        self.translatez(dz)

    def scale(self, sx, sy, sz):
        Point2D.scale(self, sx, sy)
        self.scalez(sz)

    def scalez(self, sz):
        # Put code here that scales self.__z by multipying it by sz units
        self.scalez(sz)

    def distance(self, other):
        x = self.__x - other.__x
        y = self.__y - other.__y
        z = self.__z - other.__z

        # Change the 0.0 below to the distance formula sqrt(x ** 2 + y ** 2 + z ** 2)
        return sqrt(x ** 2 + y ** 2 + z ** 2)