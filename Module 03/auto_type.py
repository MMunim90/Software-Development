import pyautogui
from time import sleep
from random import *

sleep(5)

for i in range(0,5):
    # pyautogui.write('MMunim', interval=0.25)
    pyautogui.write(choice(['kemon acho bondu', 'valo achi', 'kalke ber hoba', 'na', 'keno?', 'college ache', 'koytay?', 'sokal 7 ta hoite 2 ta', 'kobe ber hote parba', 'jani na', 'oww']))
    pyautogui.press('enter')
