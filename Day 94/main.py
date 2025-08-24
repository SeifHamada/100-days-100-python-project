import pyautogui
from PIL import ImageGrab
import time

print("Get ready... starting in 3 seconds")
time.sleep(3)


def is_obstacle(data):

    for x in range(250, 300):
        for y in range(380, 420):
            pixel = data.getpixel((x, y))
            if pixel[0] < 100 and pixel[1] < 100 and pixel[2] < 100:
                return True
    return False


while True:

    screen = ImageGrab.grab().convert("RGB")

    if is_obstacle(screen):
        pyautogui.press("space")
        time.sleep(0.1)
