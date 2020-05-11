from math import sqrt


class Point2D:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def translate(self, dx, dy):
        self.translatex(dx)
        self.translatey(dy)


    def translatex(self, dx):
        # Put code here that moves self.__x by dx units
        self.translatex(dx)

    def translatey(self, dy):
        # Put code here that moves self.__y by dy units
        self.translatey(dy)

    def scale(self, sx, sy):
        self.scalex(sx)
        self.scaley(sy)


    def scalex(self, sx):
        # Put code here that scales self.__x by multipying it by sx units
        self.scalex(sx)

    def scaley(self, sy):
        # Put code here that scales self.__y by multipying it by sy units
        self.scaley(sy)

    def distance(self, other):
        if not isinstance(other, Point2D):
            return 0.0

        x = self.getx() - other.getx()
        y = self.gety() - other.gety()

        # Change the 0.0 below to the distance formula sqrt(x ** 2 + y ** 2)
        return sqrt(x ** 2 + y ** 2)