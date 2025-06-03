import subprocess
import os
from PIL import Image, ImageDraw, ImageFont

# Constant Variables
ASCII_MATRIX = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
COLOR_WEIGHT = 255 / (len(ASCII_MATRIX) - 1)

# MARK: RGB to Brightness
#---------------------------------------------------------------------------------------
# The 3 Brightness algorithms to convert the R G B values into a single brightness value

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
# MARK: 
# Brightness to ASCII Char

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

#----------------------------------------
# MARK: Rendering
# For rendering the ASCII Image to the terminal or To a Image

def renderToTerminal(imageObj, AsciiArray):
    for y in range(imageObj.size[1]):
        for x in range(imageObj.size[0]):
            print(AsciiArray[x][y], end='')
            # Uncomment these print statements below to unsquish your image that renders in the terminal.
            #print(AsciiArray[x][y], end='')
            #print(AsciiArray[x][y], end='')
        print()

def renderToImage(filename, ascii_array, image_size, invert):

    if invert == 1:
        textColor = (27, 27, 27)
        image_Color = (255, 255, 255)
    elif invert == 2:
        textColor = (255, 255, 255)
        image_Color = (27, 27, 27)
    else:
        textColor = (255, 255, 255)
        image_Color = (27, 27, 27)
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

# MARK: Opening Image

def openImage(imageFile):
    try:

        im = Image.open((imageFile))
        print("Successfully loaded image!")
        print("Image Size: ", im.size)
        print()
    except:
        print("Cannot Open File.", imageFile)
        quit()
    return im

# Loads the image into an array
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


# MARK: CommandCam
# This runs the CommandCam program

def imageFromCam():
    print("What would you like to name your image? ", end='')
    filename = input()
    cmd = [
        r'C:/Users/jek63/Downloads/CommandCam.exe',
        f'/filename {filename}.bmp'
    ]

    subprocess.run(' '.join(cmd), shell=True)
    return f"./{filename}.bmp"

# MARK: Menuing
# Terminal Menuing

def startmenu():
    print("Image to ASCII Art Program By: Jason King")
    print()


    print("What would you like to do?")
    print("1. Print an image from your webcam.")
    print("2. Print an image from a list")
    print("3. Print an image from your PC")
    print("0. Quit the program")
    print()
    print("> ", end='')

    usrinput = int(input())

# Error Checking
    if usrinput < 0 or usrinput > 3:
        while(usrinput < 0 or usrinput > 3):
            print("Invalid Response Please type a number 0 - 3")
            print()
            print("What would you like to do?")
            print("1: Print an image from your webcam.")
            print("2: Print an image from a list")
            print("3: Print an image from you PC")
            print("0: Quit the program")
            print()
            print("> ", end='')

            usrinput = int(input())
    print()
    return usrinput

def chooseImage(usrinput):
    match(usrinput):
        case 1:
            imageFile = imageFromCam()
            return imageFile
        case 2:
            imagePaths = ["japaneseCastle.jpg", "blackWhiteSwirl.png"]
            print("What image do you want to print to the terminal?")
            print("--Type--")

            for i in range(len(imagePaths)):
                print(f"{i + 1}: {imagePaths[i]}",)
            print("0: Quit")
            print()
            print("> ", end='')

            pathInput = int(input())

            if pathInput == 0:
                print("Good-Bye!")
                quit()
            else:
                pathInput -= 1
# Error Checking
            if pathInput < 0 or pathInput > len(imagePaths):
                while(pathInput < 0 or pathInput > len(imagePaths)):
                    print(f"Invalid Input Please Type a Number 0 - {len(imagePaths)}")
                    print()
                    imagePaths = ["japaneseCastle.jpg", "blackWhiteSwirl.png"]
                    print("What image do you want to print to the terminal?")
                    print("--Type--")

                    for i in range(len(imagePaths)):
                        print(f"{i + 1}: {imagePaths[i]}",)
                    print("0: Quit")
                    print()
                    print("> ", end='')

                    pathInput = int(input())

                    if pathInput == 0:
                        print("Good-Bye!")
                        quit()
                    else:
                        pathInput -= 1

            imageFile = os.path.abspath(os.path.join("./Images/", imagePaths[pathInput]))
            print("Loading Image...")
            return imageFile
        case 3:
            imageFile = None
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
                while(imageFile != None):
                    print("Error: Could Not find the Image.")

                    print("Would you like to try another file or Quit?")
                    print("Type: 1: Try Another File  2: Quit")
                    print()
                    opt = int(input())
                    match(opt):
                        case 2:
                            print("Good-Bye")
                            quit()
                        case 1:
                            filename = input("What is the name of the file you want to print: ")
                            print("Searching...")
                            for root, dirs, files in os.walk(r'c:\\'):
                                for name in files:
                                    if name == filename:
                                        print("Found it!")
                                        print(os.path.abspath(os.path.join(root, name)))
                                        imageFile = os.path.abspath(os.path.join(root, name))
                                        print("Loading Image...")
            return imageFile
        case 0:
            print("Good-Bye")
            quit()
    


def printingOptions():
    print("Where would you like to print the image?")
    print("--Type--\n1: Terminal\n2: Image\n0: Quit")
    print()
    printLocation = int(input("> "))

    if printLocation == 0:
        print("Good-Bye!")
        quit()

    if printLocation < 0 or printLocation > 2:
        while(printLocation < 0 or printLocation > 2):
            print("Where would you like to print the image?")
            print("--Type--\n1: Terminal\n2: Image\n0: Quit")
            print()
            printLocation = int(input("> "))

            if printLocation == 0:
                print("Good-Bye!")
                quit()

    print("Which transformation would you like to use for the image?")
    print("--Type--\n1: Average Brightness\n2: Luminosity\n3: Lightness\n0: Quit")
    print()
    brightnessInput = int(input("> "))

    if brightnessInput == 0:
        print("Good-Bye!")
        quit()

    if brightnessInput < 0 or brightnessInput > 3:
        while(brightnessInput < 0 or brightnessInput > 3):
            print("Which transformation would you like to use for the image?")
            print("--Type--\n1: Average Brightness\n2: Luminosity\n3: Lightness\n0: Quit")
            print()
            brightnessInput = int(input("> "))

            if brightnessInput == 0:
                print("Good-Bye!")
                quit()

    print("Would you like to invert the brightness of the image?")
    print("Type:\n1: Yes\n2: No\n0: Quit")
    print()
    invertInput = int(input("> "))

    if invertInput == 0:
        print("Good-Bye!")
        quit()

    if invertInput < 0 or invertInput > 2:
        while(invertInput < 0 or invertInput > 2):
            print("Would you like to invert the brightness of the image?")
            print("Type:\n1: Yes\n2: No\n0: Quit")
            print()
            invertInput = int(input("> "))

            if invertInput == 0:
                print("Good-Bye!")
                quit()

    return printLocation, brightnessInput, invertInput

def printingChoices(imageObj, printLocation, brightnessInput, invertInput):
    if invertInput == 1:
        invert = True
    elif invertInput == 2:
        invert = False

    match(brightnessInput):
        case 1:
            bright_Matrix = avgBrightness(imageObj)
            AsciiArray = brightnessToAscii(bright_Matrix, invert)
            if printLocation == 1:
                renderToTerminal(imageObj, AsciiArray)
            elif printLocation == 2:
                print("What would you like to name the file?")
                print()
                filename = input("> ")
                renderToImage(filename, AsciiArray, imageObj.size, invert)
            imageObj.close()
        case 2:
            luminosity_Matrix = luminosity(imageObj)
            AsciiArray = brightnessToAscii(luminosity_Matrix, invert)
            if printLocation == 1:
                renderToTerminal(imageObj, AsciiArray)
            elif printLocation == 2:
                print("What would you like to name the file?")
                print()
                filename = input("> ")
                renderToImage(filename, AsciiArray, imageObj.size, invert)
            imageObj.close()
        case 3:
            lightness_Matrix = lightness(imageObj)
            AsciiArray = brightnessToAscii(lightness_Matrix, invert)

            if printLocation == 1:
                renderToTerminal(imageObj, AsciiArray)
            elif printLocation == 2:
                print("What would you like to name the file? (include file extension)")
                print()
                filename = input("> ")
                renderToImage(filename, AsciiArray, imageObj.size, invert)
            imageObj.close() 

# MARK: Running the script
if __name__ == "__main__":
    usrInput = startmenu()
    imFile = chooseImage(usrInput)
    imObj = openImage(imFile)
    Choice = printingOptions()
    printingChoices(imObj, *Choice)
    quit()