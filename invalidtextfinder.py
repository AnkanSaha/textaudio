from gtts import gTTS as vansom
from playsound import playsound as play
import pyautogui as inputer
import time as delay
import sys


def errorindexing(error):
    if error == 'Invalid':
        inputer.alert('You Typed a Invalid Language Name ,Please Enter right one')
        sys.exit()
    elif error != 'Invalid' :
        pass