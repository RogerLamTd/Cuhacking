from scipy import ndimage 
from PIL import Image


def partition(base, partition, tiles):

    #PIL the base image
    im  = Image.open(base)
    pxB = im.load()
    baseW, baseH = im.size

    #convert partition image to PIL form
    pilTile = Image.fromarray(partition)

    wTile = baseW // tiles[0]
    hTile = baseH // tiles[1]

    # scale the partition
    pilTile = Image.resize(tuple(wTile, hTile))
    pxP = pilTile.load()

    curW, curH = [0, 0]

    #iterate through partitions
    for w in range(tiles[0]):
        curW = w * width
        for h in range(tiles[1]):
            curH = h * height
            colourize(pxB, pxP, curW, curH, width, height)

    return base

def colourize(pxB, pxP, curW, curH, width, height):
    #iterate through pixels in partition
    for w in range(width):
        for h in range(height):
            pxB[w + curW, h + curH] = tuple((i * pxP[0] // 255) for value in pxB[w + curW, h + curH])
