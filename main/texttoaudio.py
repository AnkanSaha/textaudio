    # import all modules
# 1. this for converting text to audio
from gtts import gTTS as vansom
# 2. this for playing converted audio ss
from playsound import playsound as play
# 3. this for maing input prompts 
import pyautogui as inputer
# 4. this for making self execution delay s
import time as delay
# 5. this for converting in language code  
from main.Logic.languageconverter import convert
# 6. this for validdating languages
from main.Logic.invalidtextfinder import errorindexing
# 7. this for text field blankness checker 
from main.Logic.invalidtextfinder import textblankchecker
# 8. this is for audio file blankness chacker 
from main.Logic.invalidtextfinder import audiofilenameblankchecker
# 9. this is for language code blankness checker 
from main.Logic.invalidtextfinder import languagecodeblankchecker

# main containing function 
def main():
    # take text input 
    text = inputer.prompt('Enter Your Text that you want to convert into sound')
    textblankchecker(text)
    delay.sleep(2)
    # take language input s
    templanguage = inputer.prompt('Enter Language Name in small case :: example ;- `english, hindi`')
    languagecodeblankchecker(templanguage)
    delay.sleep(2)
    # send language for validate in another file 
    language = convert(templanguage)
    # print validated result of language 
    print(language)
    # if found any error in language ,send for alert indexing s
    errorindexing(language)
    # take audio file name input ss
    audio = inputer.prompt('Enter audio file name to save `Without .mp3`')+'.mp3'
    audiofilenameblankchecker(audio)
    delay.sleep(2)
    # combinding all variables and making text to sound waves 
    sp = vansom(text=text, lang=language, slow=False)
    # saving converted text to sound wave file into this folder 
    sp.save(audio)
    # playing converted and saved audio file ss
    play(audio)