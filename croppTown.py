import re


def getPicCoord(fileName):
    file = open(fileName)
    text = file.read()
    picCoord = {
        "UL": [float(re.search(r"(?<=CORNER_UL_LAT_PRODUCT = )\d*.\d*", text)[0]),
               float(re.search(r"(?<=CORNER_UL_LON_PRODUCT = )\d*.\d*", text)[0])],
        "UR": [float(re.search(r"(?<=CORNER_UR_LAT_PRODUCT = )\d*.\d*", text)[0]),
               float(re.search(r"(?<=CORNER_UR_LON_PRODUCT = )\d*.\d*", text)[0])],
        "LL": [float(re.search(r"(?<=CORNER_LL_LAT_PRODUCT = )\d*.\d*", text)[0]),
               float(re.search(r"(?<=CORNER_LL_LON_PRODUCT = )\d*.\d*", text)[0])],
        "LR": [float(re.search(r"(?<=CORNER_LR_LAT_PRODUCT = )\d*.\d*", text)[0]),
               float(re.search(r"(?<=CORNER_LR_LON_PRODUCT = )\d*.\d*", text)[0])],
    }
    file.close()
    return picCoord


def getThermalLines(fileName):
    file = open(fileName)
    text = file.read()
    THERMAL_LINES = float(re.search(r"(?<=THERMAL_LINES = )\d*.\d*", text)[0])
    THERMAL_SAMPLES = float(re.search(r"(?<=THERMAL_SAMPLES = )\d*.\d*", text)[0])
    file.close()
    return {"lines": THERMAL_LINES, "samples": THERMAL_SAMPLES}


def getCropCoord(image, thermal):
    pixels = image.load()
    for i in range(int(thermal["samples"])):
        for j in range(int(thermal["lines"])):
            r = pixels[j, i]
            if(r != 0):
                return j, i


def crop(image):
    MashadCoord = {
        "UL": [36.499729, 59.329481],
        "UR": [36.483207, 59.777099],
        "LL": [36.119715, 59.340393],
        "LR": [36.131859, 59.799147]

    }
    deltaCoordInPixel = {
        "UL": [],
        "UR": [],
        "LL": [],
        "LR": []
    }

    picCoord = getPicCoord("MTL.txt")
    thermal = getThermalLines("MTL.txt")
    print(thermal)

    # cropWidth, cropHeight = getCropCoord(image, thermal)
    # print(cropWidth, cropHeight)
    # cropped = image.crop((cropWidth, cropHeight, thermal["samples"], thermal["lines"]))
    # cropped.save("croppBlack.TIF")

    deltaWidth = thermal["samples"] / (picCoord["UR"][1] - picCoord["UL"][1])
    deltaHeight = thermal["lines"] / (picCoord["UL"][0] - picCoord["LL"][0])
    print(deltaWidth, deltaHeight)

    deltaCoordInPixel["UL"].append(abs(picCoord["UL"][0] - MashadCoord["UL"][0]) * deltaHeight)
    deltaCoordInPixel["UL"].append(abs(picCoord["UL"][1] - MashadCoord["UL"][1]) * deltaWidth)

    deltaCoordInPixel["LR"].append(abs(picCoord["UR"][0] - MashadCoord["LR"][0]) * deltaHeight)
    deltaCoordInPixel["LR"].append(abs(picCoord["LL"][1] - MashadCoord["LR"][1]) * deltaWidth)

    left = deltaCoordInPixel["UL"][1]
    upper = deltaCoordInPixel["UL"][0]
    right = deltaCoordInPixel["LR"][1]
    lower = deltaCoordInPixel["LR"][0]
    cropped = image.crop((left, upper, right, lower))
    cropped.save("cropped_" + image.filename)
    return cropped

