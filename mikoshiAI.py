import pyautogui
import time
import keyboard
import random
import fileinput
import win32api, win32con
from termcolor import colored 
from colorama import init 
from pyautogui import *
import datetime

init()
#while 1:
    #if pyautogui.locateOnScreen('1.png') != None:
        #print("I can see it.")
        #time.sleep(0.5)
    #else:
        #print("I can(not) see it.")
        #time.sleep(0.5)
def logo():
    print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####@@@@@%##@@@##@@@@@#####@@@@@@@#####@@@&########@@@@@@@@@ (@@@@@@@@@@@         @@@@,    *@@@@@@.    /@@@@@@     .    /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  #@@  (@@@*  @@%  @@@@  ,@@   @@@*  @@#  @@@@@@  &@@@@@@@@@*   .@@@@@@@@@@@@@@@&  #@@@  .@@,  @@@@  ,@@.  @@@(  &@@  *@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  &@@  (@@@*  @@%  @@@@  /@@.  @@@*  @@%  @@@@@@  &@@@@@@@@ ...   &@@@@@@@@@@@@%  %@@@@  ,@@*  @@@@  /@@.  @@@(  @@@  /@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  &    #@@@*       @@@@  /@@.  @@@*      @@@@@@&  &@@@@@@/  ,.  ,  ,@@@@@@@@@@*  &@@@@@  ,@@*  @@@@  /@@.  @@@(  @@@  /@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  &@@  (@@@*  @@%  @@@@  /@@.  @@@@@@@@%  @@@@@@  &@@@@@             @@@@@@@@.  @@@@@@@  ,@@*  @@@@  /@@.  @@@(  @@@  /@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  &@@  (@@@*  @@%  @@@@  /@@.  @@@*  @@%  @@@@@@  @@@@/   ., * ..,.   /@@@@@   @@@@@@@@  ,@@*  @@@@  /@@.  @@@(  @@@  /@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/     .@@@@*  @@%  @@@@%      @@@@@      /@@@@@@  @@@     .* *.,,, ,    @@@         @@@(      *@@@@*      /@@@(  @@@  /@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
    """)
    time.sleep(0.5)
    print("Created by NeverCore")
    time.sleep(0.5)
    print(colored("OPERATION DUMMY SYSTEM - MIKOSHI",'red'))
    time.sleep(2)
    print(colored("CONTROL SYSTEM TRANSFER - COMPLETE",'red'))
    time.sleep(2)
    print("Eternal System - Mikoshi is about to awake.")
    time.sleep(1)
    start()
def start():
    t = 1 
    g = 0 
    lock = ['-','-','-','-','-','-','-']
    les = open('les.txt', encoding='utf-8').read().split(',')
    lis = open('lis.txt', 'w', encoding='utf-8')
    for i in range(len(les)):
        if les[i] == '-' or les[i] == '\n-':
            lis.write('-'+','+'\n')
        else:
            lis.write('+'+','+'\n')

    while t:
        loc1 = pyautogui.locateOnScreen('2.png', grayscale=True, confidence=0.8)
        lis.close()
        lis = open('lis.txt', 'w', encoding='utf-8')
        if loc1 != None:
            print("Eternal System - I can see it.")
            pyautogui.moveTo(loc1)
            time.sleep(0.5)
            pyautogui.click(loc1)
            t = 0
            print("Eternal System - Starting second loop..")
            time.sleep(0.5)
            g = 1
        else:
            print("Eternel System - I can(not) see it.")
            time.sleep(0.5)
    while g:
        loc = pyautogui.locateOnScreen('mute.png', grayscale=True, confidence=0.8)
        if loc != None:
            pyautogui.moveTo(loc)
            print("Eternal system - I can see it.")
            time.sleep(0.5)
            pyautogui.click(loc)
            print("Eternal System - Entering the sleeping mode for 2460 seconds, Standby")
            time.sleep(2460)
            e = 1
            while e:
                end = pyautogui.locateOnScreen('end.png', grayscale=True, confidence=0.8)
                if end != None:
                    print("Eternal System - The End is Nigh.")
                    pyautogui.moveTo(end)
                    time.sleep(0.5)
                    pyautogui.click(end)
                    g = 0
                    e = 0
                    wi = 1
                    while wi:
                                wb = pyautogui.locateOnScreen('wbutton.png', grayscale=True, confidence=0.8)
                                if wb != None:
                                    print("Eternal System - Windows button found.")
                                    pyautogui.moveTo(wb)
                                    time.sleep(0.5)
                                    pyautogui.click(wb)
                                    time.sleep(0.5)
                                    pyautogui.typewrite('firefox')
                                    print("Eternal System - Writing firefox.")
                                    time.sleep(0.5)
                                    wi = 0
                                    print("Eternal System - Starting Firefox.")
                                    time.sleep(0.5)
                                    fire = 1 
                                    while fire:
                                        firefox = pyautogui.locateOnScreen('firefox.png', grayscale=True, confidence=0.8)
                                        if firefox != None:
                                            print("Eternal System - Starting Firefox 2")
                                            pyautogui.moveTo(firefox)
                                            time.sleep(0.5)
                                            pyautogui.click(firefox)
                                            time.sleep(0.5)
                                            fire = 0 
                                            nn = 1 
                                            while nn:
                                                notnow = pyautogui.locateOnScreen('notnow.png', grayscale=True, confidence=0.8)
                                                if notnow != None:
                                                    print("Eternal System - NotNow is found")
                                                    pyautogui.moveTo(notnow)
                                                    time.sleep(0.5)
                                                    pyautogui.click(notnow)
                                                    time.sleep(0.5)
                                                    nn = 0
                                                    timz = 1
                                                    while timz:
                                                        now = datetime.datetime.now()
                                                        print(now.hour,now.minute,now.second)
                                                        if now.hour == 8 and now.minute == 10 and now.second == 31:
                                                            print(les[0])
                                                            if les[0] != '-' or les[0] != '\n-':
                                                                timz = 0
                                                                lll = les[0].replace('\n','')
                                                        if now.hour == 9 and now.minute == 0 and now.second == 31:
                                                            print(les[1])
                                                            if les[1] != '-' or les[1] != '\n-':
                                                                timz = 0
                                                                lll = les[1].replace('\n','')
                                                        if now.hour == 9 and now.minute == 50 and now.second == 31:
                                                            print([les[2]])
                                                            if les[2] != '-' or les[2] != '\n-':
                                                                timz = 0
                                                                lll = les[2].replace('\n','')
                                                        if now.hour == 10 and now.minute == 40 and now.second == 31:
                                                            print(les[3])
                                                            if les[3] != '-' or les[3] != '\n-':
                                                                timz = 0
                                                                lll = les[3].replace('\n','')
                                                        if now.hour == 11 and now.minute == 30 and now.second == 31:
                                                            print(les[4])
                                                            if les[4] != '-' or les[4] != '\n-':
                                                                timz = 0
                                                                lll = les[4].replace('\n','')
                                                        if now.hour == 12 and now.minute == 20 and now.second == 31:
                                                            print(les[5])
                                                            if les[5] != '-' or les[5] != '\n-':
                                                                timz = 0
                                                                lll = les[5].replace('\n','')
                                                        if now.hour == 13 and now.minute == 10 and now.second == 31:
                                                            print(les[6])
                                                            if les[6] != '-' or les[6] != '\n-':
                                                                timz = 0
                                                                lll = les[6].replace('\n','')
                                                        if now.hour == 14 and now.minute == 0 and now.second == 31:
                                                            print(les[7])
                                                            if les[7] != '-' or les[7] != '\n-':
                                                                timz = 0
                                                                lll = les[7].replace('\n','')
                                                        if now.hour == 21 and now.minute == 39 and now.second == 31:
                                                            print("IT DID IT.")
                                                            print(les[7])
                                                            if les[7] != '-' or les[7] != '\n-':
                                                                timz = 0
                                                                lll = les[7].replace('\n','')
                                                    print(lll)
                                                    sear = 1
                                                    while sear:
                                                        search = pyautogui.locateOnScreen('search.png', grayscale=True, confidence=0.8)
                                                        if search != None:
                                                            print("Eternal System - Found search bar")
                                                            pyautogui.moveTo(search)
                                                            time.sleep(0.5)
                                                            pyautogui.click()
                                                            time.sleep(0.5)
                                                            pyautogui.typewrite(lll)
                                                            time.sleep(0.5)
                                                            pyautogui.press('enter') 
                                                            sear = 0
                                                        else:
                                                            print("Eternal System - Searching for serach bar...")
                                                            time.sleep(0.5)
                                                    nn = 0 
                                                    t = 1
                                                    start()
                                                else:
                                                    print("Eternal System - NotNow is not found")
                                                    pyautogui.moveTo(notnow)
                                                    time.sleep(0.5)
                                                    pyautogui.click(notnow)
                                                    time.sleep(0.5)
                                                    timz = 1
                                                    while timz:
                                                        now = datetime.datetime.now()
                                                        print(now.hour,now.minute,now.second)
                                                        if now.hour == 8 and now.minute == 10 and now.second == 31:
                                                            print(les[0])
                                                            if les[0] != '-' or les[0] != '\n-':
                                                                timz = 0
                                                                lll = les[0].replace('\n','')
                                                        if now.hour == 9 and now.minute == 0 and now.second == 31:
                                                            print(les[1])
                                                            if les[1] != '-' or les[1] != '\n-':
                                                                timz = 0
                                                                lll = les[1].replace('\n','')
                                                        if now.hour == 9 and now.minute == 50 and now.second == 31:
                                                            print([les[2]])
                                                            if les[2] != '-' or les[2] != '\n-':
                                                                timz = 0
                                                                lll = les[2].replace('\n','')
                                                        if now.hour == 10 and now.minute == 40 and now.second == 31:
                                                            print(les[3])
                                                            if les[3] != '-' or les[3] != '\n-':
                                                                timz = 0
                                                                lll = les[3].replace('\n','')
                                                        if now.hour == 11 and now.minute == 30 and now.second == 31:
                                                            print(les[4])
                                                            if les[4] != '-' or les[4] != '\n-':
                                                                timz = 0
                                                                lll = les[4].replace('\n','')
                                                        if now.hour == 12 and now.minute == 20 and now.second == 31:
                                                            print(les[5])
                                                            if les[5] != '-' or les[5] != '\n-':
                                                                timz = 0
                                                                lll = les[5].replace('\n','')
                                                        if now.hour == 13 and now.minute == 32 and now.second == 31:
                                                            print(les[6])
                                                            if les[6] != '-' or les[6] != '\n-':
                                                                timz = 0
                                                                lll = les[6].replace('\n','')
                                                        if now.hour == 14 and now.minute == 0 and now.second == 31:
                                                            print(les[7])
                                                            if les[7] != '-' or les[7] != '\n-':
                                                                timz = 0
                                                                lll = les[7].replace('\n','')
                                                        if now.hour == 21 and now.minute == 39 and now.second == 31:
                                                            print("IT DID IT.")
                                                            print(les[7])
                                                            if les[7] != '-' or les[7] != '\n-':
                                                                timz = 0
                                                                lll = les[7].replace('\n','')
                                                    print(lll)
                                                    sear = 1
                                                    while sear:
                                                        search = pyautogui.locateOnScreen('search.png', grayscale=True, confidence=0.8)
                                                        if search != None:
                                                            print("Eternal System - Found search bar")
                                                            pyautogui.moveTo(search)
                                                            time.sleep(0.5)
                                                            pyautogui.click()
                                                            time.sleep(0.5)
                                                            pyautogui.typewrite(lll)
                                                            time.sleep(0.5)
                                                            pyautogui.press('enter') 
                                                            sear = 0
                                                        else:
                                                            print("Eternal System - Searching for serach bar...")
                                                            time.sleep(0.5)
                                                    nn = 0 
                                                    t = 1
                                                    start()
                                        else:
                                            print("Eternal System - searching firefox icon.")
                                            pyautogui.typewrite('firefox')
                                            time.sleep(0.5)
                                    
                                else:
                                    print("Eternal System - searching for windows button.")
                                    time.sleep(0.5)
                else:
                    print("Eternal System - Searching for the end button.")
                    pyautogui.move(20,-0,0.6)
                    time.sleep(0.5)
        else:
            print("I can(not) see it.")
            time.sleep(0.5) 

logo()