from PIL import Image
import croppTown
import NDVI
import Colors


def main():
    B3img = Image.open('B3.TIF')
    croppedB3 = croppTown.crop(B3img)
    B4img = Image.open('B4.TIF')
    croppedB4 = croppTown.crop(B4img)

    ndviArray = NDVI.getNdvi(croppedB3, croppedB4)
    colorizedImg = Colors.color_changer(ndviArray)
    colorizedImg.save("color.TIF")
    colorizedImg.show()


if __name__ == '__main__':
    main()
