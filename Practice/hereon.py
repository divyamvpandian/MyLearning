import math,sys,io,traceback

class InclinationError(Exception):
    pass

class TriangleError(Exception):
    def __init__(self,text,sides):
        super().__init__(text)
        self._sides = sides

    def __str__(self):
        return "'{}' for sides  {}".format(self.args[0],self._sides)

def triarea(a,b,c):
    side = sorted((a,b,c))
    if(side[2] > side[0]+side[1]):
        raise TriangleError("Illegal Triangle",side)
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area

def main():
    inclination(0,4)
    try:
        a = triarea(3,4,5)
        b = triarea(3,4,56)
    except TriangleError as e:
        try:
            print(e, file=sys.stdin)
        except io.UnsupportedOperation as e:
            traceback.print_tb(e.__traceback__)


def inclination(x,y):
    try:
        return math.degrees(math.atan(y/x))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be Vertical") from e

if __name__ == '__main__':
    main()
    print("Fimsehd")