import math
import subprocess
from PIL import Image

ASCII_MATRIX = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def loadImagetoArray(imageObj):
    width = imageObj.size[0]
    height = imageObj.size[1]
    pixel_matrix = []
    for x in range(width):
        newMatrix = []
        for y in range(height):
            newMatrix.append(imageObj.getpixel((x,y)))
        pixel_matrix.append(newMatrix)
    return pixel_matrix

def avgBrightness(pixelArr):
    im_matrix = loadImagetoArray(pixelArr)
    brightness_Matrix = []
    for x in range(len(im_matrix)):
        temp_Matrix = []
        for y in range(len(im_matrix[x])):
            r, g, b = im_matrix[x][y]
            brightness = (r + g + b) / 3
            temp_Matrix.append(brightness)
        brightness_Matrix.append(temp_Matrix)
    return brightness_Matrix

# 255 / 65 = 3.92..... -> 50 / 3.92... = 12.755... -> round up to 13
COLOR_WEIGHT = 255 / 65
def brightnessToAscii(brightnessArr):
    AsciiArray = []
    for i in range(len(brightnessArr)):
        tempArray = []
        for j in range(len(brightnessArr[i])):
            px = brightnessArr[i][j] / COLOR_WEIGHT
            #print(math.ceil(px))
            tempArray.append(ASCII_MATRIX[math.ceil(px) - 1])
        AsciiArray.append(tempArray)
    return AsciiArray

def render(AsciiArray):
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            print(AsciiArray[x][y], end='')
            print(AsciiArray[x][y], end='')
            #print(AsciiArray[x][y], end='')

        print()

print("What would you like to name your image? ", end='')
filename = input()
cmd = [
    r'C:/Users/jek63/Downloads/CommandCam.exe',
    f'/filename {filename}.bmp'
]

subprocess.run(' '.join(cmd), shell=True)

imagePath = f"./{filename}.bmp"

try:
    im = Image.open(imagePath)
    print("Successfully loaded image!")
    print(im.size)
except:
    print("Cannot Open File.", imagePath)
    quit()

pixel_Matrix = loadImagetoArray(im)
bright_Matrix = avgBrightness(im)
AsciiArray = brightnessToAscii(bright_Matrix)

render(AsciiArray)
print(im.size)     