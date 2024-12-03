import platform
import os
import pyautogui
import time


def func(name: str) -> None:
    cord = pyautogui.locateOnScreen(name, confidence=0.9)
    pyautogui.click(cord)


def emul() -> None:
    time.sleep(2)
    func('1.PNG')
    func('2.PNG')
    func('plus.PNG')
    func('7.PNG')
    func('equally.PNG')
    print('Выполнено')


def locate_image() -> None:
    plt = platform.system()

    if plt == "Windows":
        print("Windows")

        os.system('C:\Windows\System32\calc.exe')

        emul()

    elif plt == "Linux":
        print("Linux")

        pyautogui.press(['ALT', 'F2'])
        pyautogui.write('gnome-calculator')
        pyautogui.press('enter')

        emul()

    elif plt == "Darwin":
        print("MacOS")

        pyautogui.press(['Command', 'Spacebar'])
        pyautogui.write('calc')
        pyautogui.press('enter')

        emul()

    else:
        print("Unidentified system")


if __name__ == "__main__":
    locate_image()
