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

def luminosity(pixelArr):
    im_matrix = loadImagetoArray(pixelArr)
    luminosity_Matrix = []
    for x in range(len(im_matrix)):
        tempMatrix = []
        for y in range(len(im_matrix[x])):
            R, G, B = im_matrix[x][y]
            lightness = (0.299*R + 0.587*G + 0.114*B)
            tempMatrix.append(lightness)
        luminosity_Matrix.append(tempMatrix)
    return luminosity_Matrix

def lightness(pixelArr):
    im_matrix = loadImagetoArray(pixelArr)
    lightness_Matrix = []
    for x in range(len(im_matrix)):
        tempMatrix = []
        for y in range(len(im_matrix[x])):
            lightness = (max(im_matrix[x][y]) + min(im_matrix[x][y])) / 2
            tempMatrix.append(lightness)
        lightness_Matrix.append(tempMatrix)
    return lightness_Matrix

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
COLOR_WEIGHT = 255 / (len(ASCII_MATRIX) - 1)
def brightnessToAscii(brightnessArr, invert=False):
    AsciiArray = []
    for i in range(len(brightnessArr)):
        tempArray = []
        for j in range(len(brightnessArr[i])):
            brightnessValue = brightnessArr[i][j]
            if invert:
                brightnessValue = 255 - brightnessValue
            tempArray.append(ASCII_MATRIX[round(brightnessValue / COLOR_WEIGHT)])
        AsciiArray.append(tempArray)
    return AsciiArray

def render(AsciiArray):
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            print(AsciiArray[x][y], end='')
            print(AsciiArray[x][y], end='')
            #print(AsciiArray[x][y], end='')

        print()

def imageFromCam():
    print("What would you like to name your image? ", end='')
    filename = input()
    cmd = [
        r'C:/Users/jek63/Downloads/CommandCam.exe',
        f'/filename {filename}.bmp'
    ]

    subprocess.run(' '.join(cmd), shell=True)
    return f"./{filename}.bmp"

print("Image to ASCII Art Program By: Jason King")
print()


print("What would you like to do?")
print("1. Print an image from your webcam.")
print("2. Print an image from a list")
print("> ", end='')

usrinput = int(input())
print()
match(usrinput):
    case 1:
        imageFile = imageFromCam()
    case 2:
        imagePaths = ["./japaneseCastle.jpg", "./mountain.jpg", "./Aqualung.jpg", "./blackWhiteSwirl.png"]
        print("What image do you want to print to the terminal?")
        print("Options: ", end='')

        for i in range(len(imagePaths)):
            print(f"{i}: {imagePaths[i]}  ", end='')
        print()
        print("> ", end='')
        imageFile = imagePaths[int(input())]

try:
    im = Image.open((imageFile))
    print("Successfully loaded image!")
    print(im.size)
except:
    print("Cannot Open File.", imageFile)
    quit()

print("Which transformation would you like to use for the image?")
print("0. Average Brightness    1. Luminosity    2. Lightness")
usrinput2 = int(input("> "))

match(usrinput2):
    case 0:
        bright_Matrix = avgBrightness(im)
        AsciiArray = brightnessToAscii(bright_Matrix)
        render(AsciiArray) 
    case 1:
        luminosity_Matrix = luminosity(im)
        AsciiArray = brightnessToAscii(luminosity_Matrix)
        render(AsciiArray) 
    case 2:
        lightness_Matrix = lightness(im)
        AsciiArray = brightnessToAscii(lightness_Matrix)
        render(AsciiArray) 

   