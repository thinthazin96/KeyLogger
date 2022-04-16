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

#Note: uncomment this block to create log.txt file if you are runnin for the first time.
#This function will store the user's keystroke in text file.
def write_file(keys):
    #Create and write in log.txt with write mode.
    with open('log.txt', 'w') as f:
        #Loop through each element in keys
        for key in keys:
            #store each element of keys in text file.
            f.write(f"{key}")

#This function will store the user's keystroke in text file.
# def write_file(keys):
#     #Create and write in log.txt with write mode.
#     with open("log.txt", "a") as f:
#         #Loop through each element in keys
#         for key in keys:
#             #store each element of keys in text file.
#             f.write(key)

#Call on_press and on_release function with loop
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()