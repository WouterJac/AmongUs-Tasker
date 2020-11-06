
import PIL
import pyautogui
from PIL import ImageGrab
from pytesseract import pytesseract
import numpy as nm
from python_imagesearch.imagesearch import *
import colorsys

impath = "C:\\Users\\jacob\\PycharmProjects\\Among USSR\\Images\\"


def imToString(xl, yt, xr, yb):
    # Path of tesseract executable
    pytesseract.tesseract_cmd = 'D:\\Program Files Harddrive\\Tesseract OCR\\tesseract.exe'

    # ImageGrab-To capture the screen image in a loop.
    # Bbox used to capture a specific area.
    cap = ImageGrab.grab(bbox=(xl, yt, xr, yb))

    # Converted the image to monochrome for it to be easily
    # read by the OCR and obtained the output String.
    tesstr = pytesseract.image_to_string(
        cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
        lang='eng',config='tessedit_char_whitelist 0123456789')
    tesstr = tesstr.replace('T', '7')
    tesstr = tesstr.replace('$', '5')
    tesstr = tesstr.replace('N', '1')
    tesstr = tesstr.replace('O', '0')
    tesstr = tesstr.replace('G', '6')
    tesstr = tesstr.replace('S', '5')
    tesstr = tesstr.replace('A', '4')
    tesstr = tesstr.replace('Z', '2')
    tesstr = tesstr.replace('Q', '9')
    return tesstr

    # print(pyautogui.pixel(pyautogui.position().x,pyautogui.position().y))
    # print(pyautogui.position().x, pyautogui.position().y)
    # print(clickIfRed(pyautogui.position().x, pyautogui.position().y)
    # print(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y))


def rocket():
    print('Rocket')
    print(pyautogui.position().x, pyautogui.position().y)


def lights():
    print('Lights')
    checkLight(613, 895)
    checkLight(785, 895)
    checkLight(955, 895)
    checkLight(1140, 895)
    checkLight(1308, 895)


def checkLight(x, y):
    if pyautogui.pixel(x, y)[1] == 77:
        pyautogui.click(x, y - 40)


def shields():
    # Shields
    print('Shields')
    clickIfRed(770, 370)
    clickIfRed(934, 370)
    clickIfRed(1170, 370)
    clickIfRed(770, 600)
    clickIfRed(940, 600)
    clickIfRed(1170, 600)
    clickIfRed(970, 770)
    # clickIfRed(pyautogui.position().x, pyautogui.position().y)


def clickIfRed(x, y):
    pix = pyautogui.pixel(x, y)
    red = pix[0]
    green = pix[1]
    blue = pix[2]
    pixHSV = colorsys.rgb_to_hsv(red / 255., green / 255., blue / 255.)
    pixHSV = tuple(255 * x for x in pixHSV)
    # if green + blue <210:
    #      pyautogui.click(x,y)
    #print(pixHSV)
    if (pixHSV[0] > 240 and pixHSV[0] < 250) or (pixHSV[0] > 0 and pixHSV[0] < 5):
        pyautogui.click(x, y)


def powerSlide():
    # PowerSlide
    print('Powerslide')
    printCursor()
    slidepos=(0,0)
    offset=96
    for i in range(8):
        # pyautogui.moveTo(591+(i*offset),788,1)
        testx = 591+(i*offset)
        if pixColor(testx,788)[0]>200:
            slidepos=(591+(i*offset),788)
            break
    pyautogui.moveTo(slidepos)
    pyautogui.dragTo(slidepos[0],slidepos[1]-150,0.3)


def powerClick():
    #Power Click
    pyautogui.click(961,543)


def sort():
    # Sort
    print('Sort')
    for i in range(3):
        s1 = imagesearch(impath + "\\Sort\\S" + str(i + 1) + "A.png")
        dest = imagesearch(impath + "Sort\\D" + str(i + 1) + ".png")
        if dest[0] != -1:
            print("dest position : ", dest[0], dest[1])
            pyautogui.moveTo(s1[0], s1[1])
            pyautogui.dragTo(dest[0], dest[1], 1)

        else:
            print("dest not found")

        s2 = imagesearch(impath + "Sort\\S" + str(i + 1) + "B.png")
        if dest[0] != -1:
            pyautogui.moveTo(s2[0], s2[1])
            pyautogui.dragTo(dest[0], dest[1], 1)
        if s1[0] != -1:
            print("s1 position : ", s1[0], s1[1])
        else:
            print("s1 not found")
        if s2[0] != -1:
            print("s2 position : ", s2[0], s2[1])
        else:
            print("s2 not found")


def idCode():
    # ID Code Flawed
    print('ID code')
    pyautogui.click(726, 913, 2, 0.4)
    IDcode = imToString(786, 698, 935, 784)[0:5]
    print(IDcode)
    baseX = 824
    baseY = 130
    for numchar in IDcode:
        digit = int(numchar)
        xoff = 0
        yoff = 0
        if digit == 0:
            xoff = 140
            yoff = 330
        else:
            xoff = ((digit - 1) % 3) * 140
            if digit > 3:
                yoff = 110
            if digit > 6:
                yoff = 220
        pyautogui.moveTo(baseX + xoff, baseY + yoff, 0.2)
        pyautogui.click()
        print('clicked ' + str(digit))
    pyautogui.moveTo(1050, 450, 0.2)
    pyautogui.click()


def thrash():
    # Thrash
    print('Thrash')
    pyautogui.moveTo(1279, 465)
    pyautogui.dragRel(0, 700, 2)


def wires():
    # Wires
    print('wires')
    printCursor()
    srcList = [(550, 270), (550, 460), (550, 640), (550, 830)]
    destList = [(1311, 270), (1311, 460), (1311, 640), (1311, 830)]
    for i in range(4):
        pyautogui.moveTo(srcList[i])
        destination = destList[wireFinder(srcList[i][0], srcList[i][1])]
        pyautogui.dragTo(destination[0], destination[1], 0.5)


def wireFinder(x, y):
    color = pixColor(x, y)
    destIndex = 0
    if color == (255, 0, 0):
        destIndex = 0  # Red
    elif color == (0, 0, 255):
        destIndex = 1  # Blue
    elif color == (255, 235, 4):
        destIndex = 2  # Yellow
    elif color == (255, 0, 255):
        destIndex = 3  # Pink
    return destIndex


def cardswipe():
    print('Cardswipe')
    pyautogui.click(726, 913, 2, 0.4)
    pyautogui.moveTo(522, 400)
    pyautogui.dragTo(1550, 400, 0.8)
    pyautogui.click(726, 913, 2, 0.4)
    print('Cardswipe done.')


def downUpload():
    pyautogui.click(950, 660)


def asteroids():
    print('Asteroids')

def temperature():
    print('Temperature')
    if(pixColor(1064,185)[2]>252):
        #Cold temp
        pyautogui.mouseDown(627, 616, 'left', 4)
    else:
        #Hot temp
        pyautogui.mouseDown(627,316,'left',4)


def sortSpecimen():
    print('Sort Specimen')
    printCursor()
    pyautogui.moveTo(500,450)
    pyautogui.dragTo(1070,407,1)
    pyautogui.moveTo(500,619)
    pyautogui.dragTo(860,583,1)
    pyautogui.moveTo(488,774)
    pyautogui.dragTo(1070,733,1)
    pyautogui.moveTo(483,297)
    pyautogui.dragTo(860,295,1)

def boardingPass():
    print('Boarding Pass')
    pyautogui.click(591,554,2,0.4)
    pyautogui.click(546,193,2,0.4)
    pyautogui.moveTo(591,554)
    pyautogui.dragTo(1400,554,1)


def downUpload2():
    pyautogui.click(950, 910)

def water():
    print('Water')
    pyautogui.mouseDown(890,150,'left',5)
    time.sleep(5)
    pyautogui.mouseUp()


def printCursor():
    # For development purposes
    pos = pyautogui.position()
    pixpos = pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)
    print(pos)
    print(pixpos)


def pixposColor():
    return pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)


def pixColor(x, y):
    return pyautogui.pixel(x, y)

path = "C:\\Users\\jacob\\PycharmProjects\\Among USSR\\Images\\TASKS\\"

print('Welcome. Current automated tasks:')
for task in os.listdir(path):
    print(task.split('.')[0])
print('\nNow looking for tasks...')

printCursor()

while(True):
    if imagesearch(path + "BoardingPass.png")[0] != -1:
        boardingPass()
    elif imagesearch(path + "Thrash.png")[0] != -1:
        thrash()
    elif imagesearch(path + "IDcode.png")[0] != -1:
        idCode()
    elif imagesearch(path + "Shields.png")[0] != -1:
        shields()
    elif imagesearch(path + "Shields2.png")[0] != -1:
        shields()
    elif imagesearch(path + "Slider.png")[0] != -1:
        powerSlide()
    elif imagesearch(path + "PowerClick.png")[0] != -1:
        powerClick()
    elif imagesearch(path + "Wires.png")[0] != -1:
        wires()
    elif imagesearch(path + "Sort.png")[0] != -1:
        sort()
    elif imagesearch(path + "Cardswipe.png")[0] != -1:
        cardswipe()
    elif imagesearch(path + "Download.png")[0] != -1:
        print('Download')
        downUpload()
    elif imagesearch(path + "Upload.png")[0] != -1:
        print('Upload')
        downUpload()
    elif imagesearch(path + "Upload2.png")[0] != -1:
        print('Upload2')
        downUpload2()
    elif imagesearch(path + "HotTemp.png")[0] != -1:
        temperature()
    elif imagesearch(path + "SortSpecimen.png")[0] != -1:
        sortSpecimen()
    elif imagesearch(path + "Water.png")[0] != -1:
        water()
    # elif imagesearch(path + "Rocket.png")[0] != -1:
    #     rocket()
    elif imagesearch(path + "Lights.png")[0] != -1:
        lights()

    time.sleep(0.5)



# if imagesearch(path + "Asteroids.png")[0] != -1:
#     asteroids()
