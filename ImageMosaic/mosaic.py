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
    pilTile = pilTile.resize((wTile, hTile))
    pxP = pilTile.load()

    curW, curH = [0, 0]


    #iterate through partitions
    for w in range(tiles[0]):
        curW = w * wTile
        for h in range(tiles[1]):
            curH = h * hTile
            colourize(pxB, pxP, curW, curH, wTile, hTile)

    return im

def colourize(pxB, pxP, curW, curH, width, height):
    #iterate through pixels in partition
    for w in range(width):
        for h in range(height):
            tup = (int(pxB[w + curW, h + curH][0] * pxP[w,h]), 
                int(pxB[w + curW, h + curH][1] * pxP[w,h]),
                int(pxB[w + curW, h + curH][2] * pxP[w,h]))
            pxB[w + curW, h + curH] = tup
