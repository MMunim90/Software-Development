import pyautogui
from time import sleep

num = int(input())
n = 1

sleep(5)

for i in range(num):
    for j in range(n):
        pyautogui.write('#')
    pyautogui.press('enter')
    n += 1
    


# output:-

#
##
###
####
#####
