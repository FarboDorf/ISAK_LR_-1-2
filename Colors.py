import numpy as np
from PIL import Image


colors = [[4, 19, 61], [255, 255, 255], [196, 186, 165], [181, 150, 109], [164, 131, 77], [144, 114, 66],
          [125, 157, 44], [149, 182, 21], [118, 170, 4], [101, 162, 5], [82, 148, 5], [61, 134, 5], [28, 115, 5],
          [5, 94, 4], [4, 68, 5], [4, 56, 4], [5, 41, 4], [4, 18, 4]]


def color_changer(ndvi):
    ndvi_image = Image.new("RGB", (ndvi.shape[1], ndvi.shape[0]), color=(255, 255, 255))
    # rgb = np.empty(ndvi.shape)
    i = 0
    for row in ndvi:
        for j in range(len(row)):
            # also works but less accurate
            # cnt = -1
            # for k in range(18):
            #     if ndvi[i, j] < cnt:
            #         pixel = colors[k]
            #         break
            #     if k == 0:
            #         cnt += 1
            #         continue
            #     if k > 0:
            #         cnt += 0.033
            #     if k > 6:
            #         cnt += 0.05
            #     if k > 12:
            #         cnt += 0.1
            #         continue
            if(-1 <= ndvi[i, j] <= 0):
                pixel = colors[0]
            elif (0 < ndvi[i, j] <= 0.033):
                pixel = colors[1]
            elif (0.033 < ndvi[i, j] <= 0.066):
                pixel = colors[2]
            elif (0.066 < ndvi[i, j] <= 0.1):
                pixel = colors[3]
            elif (0.1 < ndvi[i, j] <= 0.133):
                pixel = colors[4]
            elif (0.133 < ndvi[i, j] <= 0.166):
                pixel = colors[5]
            elif (0.166 < ndvi[i, j] <= 0.2):
                pixel = colors[6]
            elif (0.2 < ndvi[i, j] <= 0.25):
                pixel = colors[7]
            elif (0.25 < ndvi[i, j] <= 0.3):
                pixel = colors[8]
            elif (0.3 < ndvi[i, j] <= 0.35):
                pixel = colors[9]
            elif (0.35 < ndvi[i, j] <= 0.4):
                pixel = colors[10]
            elif (0.4 < ndvi[i, j] <= 0.45):
                pixel = colors[11]
            elif (0.45 < ndvi[i, j] <= 0.5):
                pixel = colors[12]
            elif (0.5 < ndvi[i, j] <= 0.6):
                pixel = colors[13]
            elif (0.6 < ndvi[i, j] <= 0.7):
                pixel = colors[14]
            elif (0.7 < ndvi[i, j] <= 0.8):
                pixel = colors[15]
            elif (0.8 < ndvi[i, j] <= 0.9):
                pixel = colors[16]
            else:
                pixel = colors[17]
            ndvi_image.putpixel((j, i), (pixel[0], pixel[1], pixel[2]))
        i += 1
    return ndvi_image
