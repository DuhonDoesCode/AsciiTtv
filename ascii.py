import cv2
import math
import json
import sys
from colorama import Fore

class Ascii:
    def __init__(self, img: cv2.typing.MatLike, colors : str, res=int(json.dumps(json.loads(open("config.json", "r", encoding='utf-8').read())["resolution"]))):
        self.res = res
        self.img = img
        self.height, self.width, self.channels = self.img.shape
        self.colors = colors
        self.ascii = ""
        self.brightness = self.getBrightness()

    def getBrightness(self):
        avg = 0
        for h in range(math.floor(self.height/self.res)):
            for w in range(math.floor(self.width/self.res)):
                pixel = self.img[h, w]
                avg += int((int(pixel[0]) + int(pixel[1]) + int(pixel[2]))/3)
        return avg/(math.floor(self.height/self.res)*math.floor(self.width/self.res))


    def getClosestColor(self, pixel):
        r = pixel[2]
        g = pixel[1]
        b = pixel[0]
        rgb = [Fore.BLACK, Fore.RED, Fore.BLUE , Fore.MAGENTA, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.WHITE]
        index = 0
        if r > self.brightness/2:
            index += 1
        if b > self.brightness/2:
            index += 2
        if g > self.brightness/2:
            index += 4
        return rgb[index]
    
    def pixelClamp(self, x : int, y : int, colored=False):
        try:
            pixel = self.img[x, y]
        except:
            return self.colors[len(self.colors)]
        levels = len(self.colors)
        avg = (pixel[0] + pixel[1] + pixel[2])/3
        clamp = levels - round(avg/levels) - 1
        if colored:
            return self.getClosestColor(pixel) + self.colors[clamp]
        else:
            return self.colors[clamp]
    
    def imgToAscii(self, colored=False):
        ascii = ""
        for h in range(math.floor(self.height/self.res)):
            for w in range(math.floor(self.width/self.res)):
                symbol = self.pixelClamp(h*self.res - 1, w*self.res - 1, colored)
                ascii += symbol
            ascii += "\n"
        ascii.removesuffix("\n")
        return ascii
    
    def printAscii(self):
        split = self.ascii.split("\n")
        
        for i in split:
            sys.stdout.write(i + "\n")
            sys.stdout.flush()
            
    


    