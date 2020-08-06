import pyautogui
from PIL import Image, ImageGrab 
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    for i in range(520, 540):
        for j in range(230, 260):
            if data[i, j] < 185 and data[i,j]>80:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
