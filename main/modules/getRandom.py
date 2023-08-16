import random
from modules.texts import texts, codesText2 as codesText

def getRandomText(isCode = False):
    randText = random.randint(0, len(texts) - 1)
    randCode = random.randint(0, len(codesText) - 1)

    return texts[randText] if not isCode else codesText[randCode]

def getRandomLacation():
    locations = [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590]
    randLocation = random.randint(0, len(locations) - 1)

    return locations[randLocation]

def getRandomAction():
    actions = ['shift', 'enter', 'tab']
    randAction = random.randint(0, len(actions) - 1)

    return actions[randAction]

def getRandomTrueOrFalse():
    return random.randint(0, 10) > 5
