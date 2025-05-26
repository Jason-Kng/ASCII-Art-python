import subprocess
import os
import time
from PIL import Image, ImageDraw, ImageFont

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

def luminosity(imageObj):
    im_matrix = loadImagetoArray(imageObj)
    luminosity_Matrix = []
    for x in range(len(im_matrix)):
        tempMatrix = []
        for y in range(len(im_matrix[x])):
            R, G, B = im_matrix[x][y]
            lightness = (0.299*R + 0.587*G + 0.114*B)
            tempMatrix.append(lightness)
        luminosity_Matrix.append(tempMatrix)
    return luminosity_Matrix

def lightness(imageObj):
    im_matrix = loadImagetoArray(imageObj)
    lightness_Matrix = []
    for x in range(len(im_matrix)):
        tempMatrix = []
        for y in range(len(im_matrix[x])):
            lightness = (max(im_matrix[x][y]) + min(im_matrix[x][y])) / 2
            tempMatrix.append(lightness)
        lightness_Matrix.append(tempMatrix)
    return lightness_Matrix

def avgBrightness(imageObj):
    im_matrix = loadImagetoArray(imageObj)
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
            #print(AsciiArray[x][y], end='')
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

def ASCIIToImage(filename, ascii_array, image_size, invert):

    if invert == 1:
        textColor = (0, 0, 0)
        image_Color = (255, 255, 255)
    elif invert == 2:
        textColor = (255, 255, 255)
        image_Color = (0, 0, 0)
    else:
        textColor = (255, 255, 255)
        image_Color = (0, 0, 0)
    # create an image
    out = Image.new("RGB", image_size, image_Color)
    # get a font
    fnt = ImageFont.truetype("arial.ttf", 1, encoding="unic")
    # get a drawing context
    d = ImageDraw.Draw(out)
    # draw multiline text
    for y in range(image_size[1]):
        for x in range(image_size[0]):
            d.text((x, y), ascii_array[x][y], font=fnt, fill=textColor)
    out.save(filename)
    out.show()


print("Image to ASCII Art Program By: Jason King")
print()


print("What would you like to do?")
print("1. Print an image from your webcam.")
print("2. Print an image from a list")
print("3. Print an image from you PC")
print("0. Quit the program")
print("> ", end='')

imageFile = None
usrinput = int(input())
print()
match(usrinput):
    case 1:
        imageFile = imageFromCam()
    case 2:
        imagePaths = ["japaneseCastle.jpg", "mountain.jpg", "Aqualung.jpg", "blackWhiteSwirl.png"]
        print("What image do you want to print to the terminal?")
        print("Type: ", end='')

        for i in range(len(imagePaths)):
            print(f"{i}: {imagePaths[i]}  ", end='')
        print()
        print("> ", end='')
        imageFile = os.path.abspath(imagePaths[int(input())])
        print("Loading Image...")
    case 3:
        filename = input("What is the name of the file you want to print: ")
        print("Searching...")
        for root, dirs, files in os.walk(r'c:\\'):
            for name in files:
                if name == filename:
                    print("Found it!")
                    print(os.path.abspath(os.path.join(root, name)))
                    imageFile = os.path.abspath(os.path.join(root, name))
                    print("Loading Image...")
        if imageFile == None:
            print("Error: Could Not find the Image.")
            print("Good-Bye")
            quit()
    case 0:
        print("Good-Bye")
        quit()

try:
    
    im = Image.open((imageFile))
    print("Successfully loaded image!")
    print("Image Size: ", im.size)
except:
    print("Cannot Open File.", imageFile)
    quit()

print("Where would you like to print the image?")
print("Type: 0. Terminal    1. Image")
printLocation = int(input("> "))

print("Which transformation would you like to use for the image?")
print("Type: 0. Average Brightness    1. Luminosity    2. Lightness")
brightnessinput = int(input("> "))

print("Would you like to invert the brightness of the image?")
print("Type: 1. Yes 2. No")
invertInput = int(input("> "))

if invertInput == 1:
    invert = True
elif invertInput == 2:
    invert = False

match(brightnessinput):
    case 0:
        bright_Matrix = avgBrightness(im)
        AsciiArray = brightnessToAscii(bright_Matrix, invert)
        if printLocation == 0:
            render(AsciiArray)
        elif printLocation == 1:
            print("What would you like to name the file?")
            filename = input("> ")
            ASCIIToImage(filename, AsciiArray, im.size, invert)
        im.close()
    case 1:
        luminosity_Matrix = luminosity(im)
        AsciiArray = brightnessToAscii(luminosity_Matrix, invert)
        if printLocation == 0:
            render(AsciiArray)
        elif printLocation == 1:
            print("What would you like to name the file?")
            filename = input("> ")
            ASCIIToImage(filename, AsciiArray, im.size)
        im.close()
    case 2:
        lightness_Matrix = lightness(im)
        AsciiArray = brightnessToAscii(lightness_Matrix, invert)

        if printLocation == 0:
            render(AsciiArray)
        elif printLocation == 1:
            print("What would you like to name the file? (include file extension)")
            filename = input("> ")
            ASCIIToImage(filename, AsciiArray, im.size, invert)
        im.close() 

   