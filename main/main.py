import os
import pathlib
import subprocess
import platform
import time
import random
import pyautogui
import requests
import inquirer

from config.config import SLEEP_BEFORE_START, SLEEP_BEFORE_STEP, WRITE_INTERVAL, FAST_PRESS_INTERVAL, bcolors, printColors
from modules.texts import texts, codesText
from modules.getRandom import getRandomAction, getRandomLacation, getRandomText, getRandomTrueOrFalse

def app() -> None:
    # print logo on start
    with open(os.path.join(os.path.dirname(__file__), 'config', 'intro.txt')) as f:
        intro = f.read()
        print(intro)
        f.close()

    # screenWidth, screenHeight = pyautogui.size()
    # print(screenWidth, screenHeight)
    isWindows = platform.system() == 'Windows'
    isMac = platform.system() == 'Darwin'
    isLinux = platform.system() == 'Linux'

    pathNow = pathlib.Path(__file__).parent.resolve()
    fileName = 'file.js'
    pathToFile = pathlib.Path().joinpath(pathNow, fileName)

    # Main mode quetion:
    startQuestions = [
        inquirer.List('mainMode', message='Choose a main mode?', choices=['spy', 'custom'], default='spy'),
    ]
    ans = inquirer.prompt(startQuestions)
    mainModeStr: str = ans['mainMode'] if ans != None else 'spy'

    isSpyMainMode = True if mainModeStr == 'spy' else False

    isPressDel = False
    isOpenEditor = False
    isWriteCode = False

    # TODO: switch this on <inquirer> lib, there is some cool features like true/false prompts and etc.
    if not isSpyMainMode:
        # Setup and user's inputs before start:
        # ask for use an Del button:
        print(bcolors.WARNING + 'Should I use the \'Del\' button?')
        askPressDel = input(' -> (y/n): ')
        isPressDel = True if askPressDel == 'y' or askPressDel == 'Y' else False
        print('Okey, I ll use it.' if isPressDel else 'Gotcha! Wont use it!')
        print(bcolors.ENDC + '')
        # ask for open an ediror or no:
        print(bcolors.WARNING + 'Should I open and editor?')
        askOpenEdito = input(' -> (y/n): ')
        isOpenEditor = True if askOpenEdito == 'y' or askOpenEdito == 'Y' else False
        print('Okey, I ll open an editor.' if isOpenEditor else 'Gotcha! Wont open!')
        print(bcolors.ENDC + '')
        # ask for should an app write the code or regular text:
        print(bcolors.WARNING + 'Should I write code or a regular text?')
        askWriteCode = input(' -> (<code> y/n <text>): ')
        isWriteCode = True if askWriteCode == 'y' or askWriteCode == 'Y' else False
        print('Okey, I ll write some code for you!' if isWriteCode else 'Well! I ll just write some text for you!')
        print(bcolors.ENDC + '')

    # Countdown:
    for i in range(SLEEP_BEFORE_START, 0, -1):
        print(i)
        time.sleep(1)

    # Open editor depends on os:
    if isOpenEditor and not isSpyMainMode:
        # Check a file exists
        fo = open(pathToFile, "w+")
        fo.close()

        if isMac:
            # open some text editor here or just use vim:
            # subprocess.call(["open", pathToFile, "-a", "webstorm"])
            # or:
            subprocess.run(['open', '.', '-a', 'terminal'])
            pyautogui.write('vim some.js')
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.press('i')
        elif isWindows:
            os.system(pathToFile)

    # Main loops:
    if isSpyMainMode:
        while True:
            time.sleep(SLEEP_BEFORE_STEP)

            pyautogui.press('enter')

            time.sleep(0.3)
            pyautogui.moveTo(getRandomLacation(), getRandomLacation(), duration=0.5)
    else:
        while True:
            time.sleep(SLEEP_BEFORE_STEP)

            pyautogui.press(getRandomAction())

            time.sleep(0.3)
            pyautogui.moveTo(getRandomLacation(), getRandomLacation(), duration=0.5)

            time.sleep(0.3)
            pyautogui.write(getRandomText(isWriteCode), interval=WRITE_INTERVAL)

            if getRandomTrueOrFalse() and isPressDel:
                pyautogui.press('backspace', presses=random.randint(4, 15), interval=FAST_PRESS_INTERVAL)

            pyautogui.press('enter')

    # NOTE: you also can make some http request here if you are sure you have internet connection:
    return
    r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    print(r.json())

if __name__ == "__main__":
    app()

