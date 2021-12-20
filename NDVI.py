import numpy as np
np.seterr(divide='ignore', invalid='ignore')


def getNdvi(B3, B4):
    nir = np.array(B4)
    red = np.array(B3)
    numerator = nir - red
    denumerator = nir + red
    ndvi = numerator / denumerator
    # print(ndvi)
    return ndvi
