
# encoding:utf-8

import base64
import os
from time import sleep
from PIL import ImageGrab,Image

"""
Function: Read The Image From Clipboard and Return its Base64Encode
Author:WizzyAng

"""

def ClipboardImageToBase64():
    image = ImageGrab.grabclipboard()
    image.save("PhotoFromClipboard.bmp")
    with open("PhotoFromClipboard.bmp",'rb') as f:
        img = base64.b64encode(f.read())
    os.remove("PhotoFromClipboard.bmp")
    return img

def CheckIfIsImage():
    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image):
        return True
    else:
        return False

