#! /usr/local/bin/python3.4
from PIL import Image
import sys


class Pixel():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pere = self

    def root(self):
        if(self == self.pere):
            return self
        else:
            self.pere = self.pere.root()
            return self.pere

    def find(self, v):
        return (self.root() == v.root())

    def union(self, v):
        rootU = self.root()
        rootV = v.root()
        if not(rootU == rootV):
            if nombreFils[rootU] > nombreFils[rootV]:
                rootV.pere = rootU
                ensRoot.remove(rootV)
                nombreFils[rootU] += nombreFils[rootV]
            else:
                rootU.pere = rootV
                ensRoot.remove(rootU)
                nombreFils[rootV] += nombreFils[rootU]


    def relation(self, pixel, r):
        if (pixel.y - self.y) ** 2 > r:
            return 2
        elif (self.x - pixel.x) ** 2 + (self.y - pixel.y) ** 2 <= r:
            return 1
        else:
            return 0

    def __repr__(self):
        return "x:" + str(self.x) + "y: " + str(self.y)


def miseEnRelation(pixelEns):
    for i, elementA in enumerate(pixelEns):
        for elementB in pixelEns[i:]:
            p = elementA.relation(elementB, r)
            if p == 2:
                break
            elif p == 1:
                elementA.union(elementB)


def nombreClasse(ensRoot,n):
    i = 0
    for element in ensRoot:
        if nombreFils[element] > n:
            i += 1
    return i



if __name__ == '__main__':
    r = int(sys.argv[2])
    n = int(sys.argv[3])
    im = Image.open(sys.argv[1])
    im = im.convert('1')
    pixelEns = [Pixel(j % im.size[0], j // im.size[0])
                for j, i in enumerate(list(im.getdata())) if i == 0]

    nombreFils = {element: 1 for element in pixelEns}
    ensRoot = set(pixelEns)
    miseEnRelation(pixelEns)
    print(nombreClasse(ensRoot,n))
