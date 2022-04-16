import pynput

from pynput.keyboard import Key, Listener 

#This function will print the key that the user pressed.
def on_press(key):
    print(f"{key} pressed.")

#This function will get out of Loop
def on_release(key):
    #check if the user input is esc key.
    if key == Key.esc:
    #if yes, get out of the loop
        return False

#Call on_press and on_release function with loop
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()