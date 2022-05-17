from gtts import gTTS as vansom
from playsound import playsound as play
import pyautogui as inputer
import time as delay
import sys

# function for indexing Invalid language code 
def errorindexing(error):
    if error == 'Invalid':
        inputer.alert('You Typed a Invalid Language Name ,Please Enter right one')
        sys.exit()
    elif error != 'Invalid' :
        pass

# function for checking language blankness 
def languagecodeblankchecker(languagecode):
    if languagecode == '':
         inputer.alert("You Can't leave language name blank ,Please Enter right one")
         sys.exit()
    elif languagecode != '':
        pass

# function for text field blankness checking 
def textblankchecker(text):
    if text == '':
        inputer.alert("You Can't leave text field blank");
        sys.exit()
    elif text != '':
        pass

# function for audio filename checking 
def audiofilenameblankchecker(audiofilename):
    if audiofilename == '.mp3':
        inputer.alert("You Can't leave audio file name field blank");
        sys.exit()
    elif audiofilename != '':
        pass