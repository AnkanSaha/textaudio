from gtts import gTTS as vansom
from playsound import playsound as play
import pyautogui as inputer
import time as delay
import sys

def convert(tl):
    if tl == 'bengali':
        language = ''
        language = 'bn'
    elif tl == 'english':
        language = 'en'
    elif tl == 'hindi':
        language = 'hi'
    elif tl == 'amharic':
        language = 'am'
    elif tl == 'arbic':
        language = 'ar'
    elif tl == 'basque':
        language = 'eu'
    elif tl == 'portuguese':
        language = 'pt-BR'
    elif tl == 'bulgarian':
        language = 'bg'
    elif tl == 'catalan':
        language = 'ca'
    elif tl == 'cherokee':
        language = 'chr'
    elif tl == 'croatian':
        language = 'hr'
    elif tl == 'czech':
        language = 'cs'
    elif tl == 'danish':
        language = 'da'
    elif tl == 'dutch':
        language = 'nl'
    elif tl == 'estonian':
        language = 'et'
    elif tl == 'filipino':
        language = 'fil'
    elif tl == 'finnish':
        language = 'fi'
    elif tl == 'french':
        language = 'fr'
    elif tl == 'german':
        language = 'de'
    elif tl == 'greek':
        language = 'el'
    elif tl == 'gujarati':
        language = 'gu'
    elif tl == 'hebrew':
        language = 'iw'
    elif tl == 'hungarian':
        language = 'hu'
    elif tl == 'icelandic':
        language = 'is'
    elif tl == 'indonesian':
        language = 'id'
    elif tl == 'italian':
        language = 'it'
    elif tl == 'japanese':
        language = 'ja'
    elif tl == 'kannada':
        language = 'kn'
    elif tl == 'korean':
        language = 'ko'
    elif tl == 'latvian':
        language = 'lv'
    elif tl == 'lithuanian':
        language = 'lt'
    elif tl == 'malay':
        language ='ms'
    elif tl == 'malayalam':
        language = 'ml'
    elif tl == 'marathi':
        language = 'mr'
    elif tl == 'norwegian':
        language = 'no'
    elif tl == 'polish':
        language = 'pl'
    elif tl == 'romanian':
        language = 'ro'
    elif tl == 'russian':
        language = 'ru'
    elif tl == 'serbian':
        language = 'sr'
    elif tl == 'chinese':
        language ='zh'
    elif tl == 'slovak':
        language = 'sk'
    elif tl == 'slovenian':
        language = 'sl'
    elif tl == 'spanish':
        language = 'es'
    elif tl == 'swahili':
        language = 'sw'
    elif tl == 'swedish':
        language = 'sv'
    elif tl == 'tamil':
        language = 'ta'
    elif tl == 'telugu':
        language = 'te'
    elif tl == 'thai':
        language = 'th'
    elif tl == 'turkish':
        language = 'tr'
    elif tl == 'urdu':
        language = 'ur'
    elif tl == 'ukrainian':
        language = 'uk'
    elif tl == 'vietnamese':
        language = 'vi'
    elif tl == 'welsh':
        language = 'cy'
    else :
        language = 'Invalid'
    return language