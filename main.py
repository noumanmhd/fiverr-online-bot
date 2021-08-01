import os
import random
import pyautogui
from time import sleep

WAIT = 4

SCREEN_X, SCREEN_Y = pyautogui.size()
IMG_PATH = os.path.join(os.getcwd(), 'img')
IMG_FILES = [os.path.join(IMG_PATH, f)
             for f in os.listdir(IMG_PATH) if os.path.isfile(os.path.join(IMG_PATH, f))]
IMG_FILES.sort()

def move_mouse():
    x = random.randint(0, SCREEN_X)
    y = random.randint(0, SCREEN_Y)
    pyautogui.moveTo(x, y, random.uniform(0.3, 1.5))
    sleep(WAIT/2)


def click_btn(btn):
    x, y = btn
    pyautogui.moveTo(x, y, .7, pyautogui.easeInQuad)
    pyautogui.click()


def get_btn(btn_img):
    return pyautogui.locateCenterOnScreen(btn_img, confidence=0.7)


def routine():
    for img_file in IMG_FILES:
        btn = get_btn(img_file)
        if btn != None:
            for _ in range(10):
                move_mouse()
            click_btn(btn)
            sleep(WAIT)


def main():
    while True:
        try:
            routine()
        except KeyboardInterrupt:
            exit(0)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
