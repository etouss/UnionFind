#! /usr/local/bin/python3.4
from PIL import Image
import sys
import UnionFind


class Pixel():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def relation(self, pixel, r):
        if (pixel.y - self.y) ** 2 > r:
            return 2
        elif (self.x - pixel.x) ** 2 + (self.y - pixel.y) ** 2 <= r:
            return 1
        else:
            return 0

    def __repr__(self):
        return "x:" + str(self.x) + "y: " + str(self.y)


def miseEnRelation(union):
    for i, elementA in enumerate(union.tabWork):
        # print(i)ah
        for elementB in union.tabWork[i:]:
            p = elementA.relation(elementB, r)
            if p == 2:
                break
            elif p == 1:
                union.union(elementA, elementB)


def nombreClasse(union, n):
    i = 0
    for element in union.ensRoot:
        if union.nombreFils[element] > n:
            i += 1
    return i


if __name__ == '__main__':
    r = int(sys.argv[2])
    n = int(sys.argv[3])
    im = Image.open(sys.argv[1])
    im = im.convert('1')
    # print(list(im.getdata()))
    # im.save("test.png")
    pixelEns = [Pixel(j % im.size[0], j // im.size[0])
                for j, i in enumerate(list(im.getdata())) if i == 0]

    # print(len(pixelEns))
    union = UnionFind.UnionFind(pixelEns)
    miseEnRelation(union)
    print(nombreClasse(union, n))
