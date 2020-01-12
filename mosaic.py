from scipy import ndimage 
from PIL import Image
import numpy


def partition(base, tile):

    im  = Image.open(base)
    px = im.load()

    pilTile = Image.fromarray(tile)
    baseW, baseH = base.size

    hTiles = 100
    wTiles = 100
    height = baseH // htiles
    width = baseW // wTiles

    curW, curH = [0, 0]

    for h in range(hTiles):
        curH = h * height
        for w in range(wTiles):
            curW = w * width
            rgb = avgRGB(curH, curW, height, width, base)
            mTile = colourize(tile, rgb)
            save2Base(base, colourize)

    return base

def avgRGB(curH, curW, height, width):
    rgb = [0,0,0]
    for h in range(height):
        for w in range(width):
            rgb[0] += px[h + curH, w + curW][0]
            rgb[1] += px[h + curH, w + curW][1]
            rgb[2] += px[h + curH, w + curW][2]
    rgb[0] = rgb[0] // (height * width)
    rgb[1] = rgb[1] // (height * width)
    rgb[2] = rgb[2] // (height * width)
    return rgb

def colourize(curH, curW

