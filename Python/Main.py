#! /usr/local/bin/python3.4
from PIL import Image
import sys


class Pixel():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pere = self
        self.taille = 1

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
            if rootU.taille > rootV.taille:
                rootV.pere = rootU
                ensRoot.remove(rootV)
                rootU.taille += rootV.taille
            else:
                rootU.pere = rootV
                ensRoot.remove(rootU)
                rootV.taille += rootU.taille

    def relation(self, pixel, r):
        if (self.x - pixel.x) ** 2 + (self.y - pixel.y) ** 2 <= r:
            return 1
        else:
            return 3

    def __repr__(self):
        return "x:" + str(self.x) + "y: " + str(self.y)


def firstNombre(liste, x):
    lenL = len(liste)
    if lenL == 0:
        return 0
    elif x == liste[lenL // 2].x:
        return lenL//2
    elif liste[lenL // 2].x > x:
        return firstNombre(liste[:lenL // 2], x)
    else:
        return lenL // 2 + 1 + firstNombre(liste[lenL // 2 + 1:], x)

def miseEnRelation(pixelEns, heigth):
    yA = 0
    while(yA < heigth):
        xA = 0
        widthA = len(pixelEns[yA])
        while(xA < widthA):
            pA = pixelEns[yA][xA]
            yB = yA
            while(yB < heigth):
                if (yB == yA):
                    xB = xA + 1
                else:
                    xB = firstNombre(
                        pixelEns[yB], pA.x - int((r-(yA-yB)**2) ** (1 / 2)))
                widthB = len(pixelEns[yB])
                while(xB < widthB):
                    p = pA.relation(pixelEns[yB][xB], r)
                    if p == 1:
                        pA.union(pixelEns[yB][xB])
                        xB += 1
                    elif p == 3:
                        xB = widthB
                    else:
                        xB += 1
                yB += 1
                if (yA - yB) ** 2 > r:
                    yB = heigth
            xA += 1
        yA += 1


def nombreClasse(ensRoot, n):
    i = 0
    for element in ensRoot:
        if element.taille > n:
            i += 1
    return i


if __name__ == '__main__':
    r = int(sys.argv[2])
    n = int(sys.argv[3])
    im = Image.open(sys.argv[1])
    im = im.convert('1')
    width = im.size[0]
    heigth = im.size[1]
    data = list(im.getdata())
    pixelEns = [[Pixel(x, y)
                 for x in range(width) if data[x + y * width] == 0] for y in range(heigth)]
    heigth = len(pixelEns)
    ensRoot = {element for elements in pixelEns for element in elements}
    miseEnRelation(pixelEns, heigth)
    print(nombreClasse(ensRoot, n))
