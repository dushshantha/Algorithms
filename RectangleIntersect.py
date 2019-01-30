import collections
Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'hight'))

def intersect_rectangle(R1, R2):

    def is_intersect(R1, R2):
        return (R1.x <= R2.x + R2.width) and (R1.x + R1.width >= R2.x) and (R1.y <= R2.y + R2.hight) and (R1.y + R1.hight >= R2.y)
    
    if not is_intersect(R1, R2):
        return Rectangle(0,0, -1, -1)

    return Rectangle (max(R1.x, R2.x), max(R1.y, R2.y),\
        min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
        min(R1.y + R1.hight, R2.y + R2.hight) - max(R1.y, R2.y))

if __name__ == "__main__":
    r1 = Rectangle(1,2,3,4)
    r2 = Rectangle(3,3,2,4)

    print(intersect_rectangle(r1,r2))
            