# import time
# from watchdog.observers import Observer
# from watchdog.events import PatternMatchingEventHandler
#
# if __name__ == "__main__":
#     patterns = ["*"]
#     ignore_patterns = None
#     ignore_directories = False
#     case_sensitive = True
#     my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
#
#
# def on_created(event):
#     print(f"hey, {event.src_path} has been created!")
#
#
# def on_deleted(event):
#     print(f"what the f**k! Someone deleted {event.src_path}!")
#
#
# def on_modified(event):
#     print(f"hey buddy, {event.src_path} has been modified")
#
#
# def on_moved(event):
#     print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
#
#
# my_event_handler.on_created = on_created
# my_event_handler.on_deleted = on_deleted
# my_event_handler.on_modified = on_modified
# my_event_handler.on_moved = on_moved
#
# # path = "C:/Users/swpin/Downloads"
# path = 'This PC/Galaxy Tab A (8.0", 2019)/Tablet/Kinesis/QTUG/Data'
# go_recursively = True
# my_observer = Observer()
# my_observer.schedule(my_event_handler, path, recursive=go_recursively)
#
# my_observer.start()
# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     my_observer.stop()
#     my_observer.join()
from PIL import Image
from ppadb.client import Client as AdbClient

import time
from ppadb.client import Client as AdbClient
# from Pillow import Image
from pytesseract import pytesseract

fallriskwords = '322 328'
fallrisknumber = '370 490'
previousfall = 0

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

if __name__ == '__main__':
    device, client = connect()
    while(1):

        screenshot = device.screencap()

        with open('c:/users/swpin/downloads/result.png', 'wb') as f:  # save the screenshot as result.png
            f.write(screenshot)
            print('Saved screenshot!')



        time.sleep(3)

def fallriskcrop():
    img = Image.open(r"C:/Users/swpin/Downloads/result.png")
    left = 0
    top = 50
    right = 510
    bottom = 292
    img_res = img.crop((left, top, right, bottom))
    img_res.show()