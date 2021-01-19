from pynput.keyboard import Key, Controller
import time

kb = Controller()

def main():
    r = "y"
    while r == "y":
        setup()
        r = input("Do you want type something next [y/n]: ")
        if r == "y":
            spacemsg()
            print("Creating new session...")
            spacemsg()
        elif r == "n":
            spacemsg()
            print("Exiting...")
        else:
            spacemsg()
            print("You dont input any valid option any option")
            print("Exiting...")
            time.sleep(3)
        spacemsg()

def setup():
    spacemsg()
    print("=====[Zav.cz Hack by XglockManLP]=====")
    spacemsg()
    print("===============[Setup:]===============")
    text = input("Enter some text: ")
    delay = int(input("Enter start delay [Example: 3]: "))
    speedncv = int(input("Enter typing speed [Example: 250]: "))
    speed = delayconv(speedncv)
    print("==============[Reverse?]==============")
    rev = input("Do you want reverse text [y/n]: ")
    if rev=="y":
        text = reverse(text)
    else:
        print("The typer will continue without text reverse")
    print("===============[Modes:]===============")
    print("1) SingleTyper")
    print("2) MultiTyper")
    print("3) MultiTaskTyper")
    select = int(input("Select mode:"))
    if (select == 1):
        stpdonemsg()
        input("=======[Press any key to start]=======")
        singletype(text, delay, speed)
    elif (select == 2):
        print("==========[Additional Setup:]==========")
        count = int(input("Enter how many times want you type [Example: 3]: "))
        stpdonemsg()
        input("=======[Press any key to start]=======")
        multitype(text, delay, count, speed)
    elif (select == 3):
        print("==========[Additional Setup:]==========")
        textnd = input("Enter the second text: ")
        revnd = input("Do you want reverse text [y/n]: ")
        if revnd == "y":
            textnd = reverse(textnd)
        else:
            print("The typer will continue without text reverse")
        stpdonemsg()
        input("=======[Press any key to start]=======")
        multitasktype(text, textnd, delay, speed)
    else:
        print("You dont select any option")
        print("Exiting...")

def delayconv(delay):
    return delay / 1000

def typer(text, speed):
    split(text)
    for t in split(text):
        kb.type(t)
        time.sleep(speed)

def donemsg():
    print("================[Done]================")

def spacemsg():
    print("======================================")

def stpdonemsg():
    print("=============[Setup Done]=============")

def startdelay(delay):
    print("Waiting...")
    time.sleep(delay)
    print("Typing...")

def split(text):
    return [char for char in text]

def reverse(text):
    return text[::-1]

def singletype(text, delay, speed):
    startdelay(delay)
    typer(text, speed)
    donemsg()

def multitype(text, delay, count, speed):
    startdelay(delay)
    c = int(0)
    while c < count:
        typer(text, speed)
        c += 1
        kb.press(Key.enter)
    donemsg()

def multitasktype(text, textnd, delay, speed):
    startdelay(delay)
    typer(text, speed)
    kb.press(Key.enter)
    typer(textnd, speed)

main()