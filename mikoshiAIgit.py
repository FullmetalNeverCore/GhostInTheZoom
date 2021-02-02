import pyautogui
import time
import keyboard
import random
import fileinput
import win32api, win32con
import aiogram 
import logging
import requests 
from termcolor import colored 
from colorama import init 
from pyautogui import *
import datetime
id = 
token = 

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
    print("Ver 2"+" "+"Telegram-Ed.")
    time.sleep(0.5)
    print("Created by NeverCore")
    time.sleep(0.5)
    print(colored("OPERATION DUMMY SYSTEM - MIKOSHI",'red'))
    time.sleep(2)
    print(colored("CONTROL SYSTEM TRANSFER - COMPLETE",'red'))
    time.sleep(2)
    print("Eternal System - Mikoshi is about to awake.")
    al1 = "Eternal System - Mikoshi is  awaken."
    sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
    sm = requests.get(sent)
    time.sleep(1)
    polling()

une = 513

def polling():
    les = open('les.txt', encoding='utf-8').read().split(',')
    lis = open('lis.txt', 'w', encoding='utf-8')
    wi = 1
    while wi:
                                wb = pyautogui.locateOnScreen('wbutton.png', grayscale=True, confidence=0.8)
                                if wb != None:
                                    print("Eternal System - Windows button found.")
                                    pyautogui.moveTo(wb)
                                    time.sleep(0.5)
                                    pyautogui.click(wb)
                                    time.sleep(0.5)
                                    pyautogui.typewrite('fire',interval=0.25)
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
                                                            if not les[0] == '-' or les[0] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 1."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[0].replace('\n','')
                                                        if now.hour == 9 and now.minute == 0 and now.second == 31:
                                                            print(les[1])
                                                            if not les[1] == '-' or les[1] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 2."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[1].replace('\n','')
                                                        if now.hour == 9 and now.minute == 50 and now.second == 31:
                                                            print([les[2]])
                                                            if not les[2] == '-' or les[2] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 3."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[2].replace('\n','')
                                                        if now.hour == 10 and now.minute == 40 and now.second == 31:
                                                            print(les[3])
                                                            if not les[3] == '-' or les[3] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 4."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[3].replace('\n','')
                                                        if now.hour == 11 and now.minute == 30 and now.second == 31:
                                                            print(les[4])
                                                            if not les[4] == '-' or les[4] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 5."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[4].replace('\n','')
                                                        if now.hour == 12 and now.minute == 20 and now.second == 31:
                                                            print(les[5])
                                                            if not les[5] == '-' or les[5] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 6."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[5].replace('\n','')
                                                        if now.hour == 13 and now.minute == 10 and now.second == 31:
                                                            print(les[6])
                                                            if not les[6] == '-' or les[6] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 7."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[6].replace('\n','')
                                                        if now.hour == 14 and now.minute == 0 and now.second == 31:
                                                            print(les[7])
                                                            if not les[7] == '-' or les[7] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 8."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[7].replace('\n','')
                                                        #test-label
                                                        if now.hour == 6 and now.minute == 39 and now.second == 31:
                                                            print("IT DID IT.")
                                                            print(les[1])
                                                            if les[4] != '-' or les[4] != '\n-':
                                                                timz = 0
                                                                lll = les[0].replace('\n','')
                                                                #polling()
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
                                                            if not les[0] == '-' or les[0] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 1."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[0].replace('\n','')
                                                        if now.hour == 9 and now.minute == 0 and now.second == 31:
                                                            print(les[1])
                                                            if not les[1] == '-' or les[1] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 2."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[1].replace('\n','')
                                                        if now.hour == 9 and now.minute == 50 and now.second == 31:
                                                            print([les[2]])
                                                            if not les[2] == '-' or les[2] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 3."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[2].replace('\n','')
                                                        if now.hour == 10 and now.minute == 40 and now.second == 31:
                                                            print(les[3])
                                                            if not les[3] == '-' or les[3] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 4."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[3].replace('\n','')
                                                        if now.hour == 11 and now.minute == 30 and now.second == 31:
                                                            print(les[4])
                                                            if not les[4] == '-' or les[4] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 5."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[4].replace('\n','')
                                                        if now.hour == 12 and now.minute == 20 and now.second == 31:
                                                            print(les[5])
                                                            if not les[5] == '-' or les[5] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 6."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[5].replace('\n','')
                                                        if now.hour == 13 and now.minute == 10 and now.second == 31:
                                                            print(les[6])
                                                            if not les[6] == '-' or les[6] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 7."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[6].replace('\n','')
                                                        if now.hour == 14 and now.minute == 0 and now.second == 31:
                                                            print(les[7])
                                                            if not les[7] == '-' or les[7] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 8."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[7].replace('\n','')
                                                        #test-label
                                                        if now.hour == 19 and now.minute == 47 and now.second == 31:
                                                            print("IT DID IT.")
                                                            print(les[1])
                                                            if not les[4] == '-' or les[4] == '\n-':
                                                                timz = 0
                                                                lll = les[5].replace('\n','')
                                                                #polling()
                                                        if now.hour == 18 and now.minute == 58 and now.second == 31:
                                                            print("IT DID IT.")
                                                            print(les[0])
                                                            if not les[0] == '-' or les[2] == '\n-':
                                                                timz = 0
                                                                lll = les[0].replace('\n','')
                                                                #polling()
                                                        if now.hour == 13 and now.minute == 31 and now.second == 31:
                                                            print("IT DID IT.")
                                                            print(les[0])
                                                            if not les[0] == '-' or les[0] == '\n-':
                                                                timz = 0
                                                                al1 = "Eternal System - Mikoshi is going on lesson 8."
                                                                sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
                                                                sm = requests.get(sent)
                                                                lll = les[0].replace('\n','')
                                                                #polling()
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
                                            pyautogui.typewrite('fire',interval=0.25)
                                            time.sleep(0.5)
                                    
                                else:
                                    print("Eternal System - searching for windows button.")
                                    time.sleep(0.5)



def breaktheloop():
    crs = pyautogui.locateOnScreen('cross.png', grayscale=True, confidence=0.8)
    time.sleep(2)
    brkthelp = 1
    une = 0
    while brkthelp:
        if crs != None:
            print("Eternal System - Time is up,aborting previous process.")
            time.sleep(0.5)
            pyautogui.moveTo(crs)
            time.sleep(0.5)
            pyautogui.click(crs)
            time.sleep(0.5)
            python = sys.executable
            os.execl(python, python, * sys.argv)
        elif une == 66:
            time.sleep(0.5)
            print("Eternal System - Starting polling by force.")
            time.sleep(0.5)
            polling = 0
            polling()
        else:
            une += 1
            print("Eternal system - Time is up,but Mikoshi is unable to find the cross button.")
            time.sleep(1)




def start():
    t = 1 
    g = 0 
    une = 0
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
        elif une == 512:
            une += 1
            time.sleep(0.5)
            breaktheloop()
        else:
            une += 1 
            print(une)
            print("Eternel System - I can(not) see it.")
            time.sleep(0.5)
    while g:
        if une == 513:
            une = 0
        else:
            pass
        loc = pyautogui.locateOnScreen('mute.png', grayscale=True, confidence=0.8)
        if loc != None:
            pyautogui.moveTo(loc)
            print("Eternal system - I can see it.")
            time.sleep(0.5)
            pyautogui.click(loc)
            print("Eternal System - Entering the sleeping mode for 2260 seconds, Standby")
            time.sleep(2260)
            al1 = "Eternal System - Mikoshi is about to leave the lesson."
            sent = 'https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(id) + '&parse_mode=Markdown&text=' + str(al1)
            sm = requests.get(sent)            
            e = 1
            g = 0
        elif une == 66:
            une += 1
            print("Eternal System - Forcing entering into next loop.")
            time.sleep(0.5)
            print("Eternal System - Entering the sleeping mode for 2260 seconds, Standby")
            time.sleep(2260)
            e = 1
            g = 0 
        else:
            une += 1 
            print(une)
            print("Eternal System - I can(not) see it.")
            time.sleep(0.5) 
    while e:
                if une == 67:
                    une = 0
                else:
                    pass
                end = pyautogui.locateOnScreen('end.png', grayscale=True, confidence=0.8)
                if end != None:
                    print("Eternal System - The End is Nigh.")
                    pyautogui.moveTo(end)
                    time.sleep(0.5)
                    pyautogui.click(end)
                    g = 0
                    e = 0
                    python = sys.executable
                    os.execl(python, python, * sys.argv)
                elif une == 66:
                    g = 0 
                    print("Eternal System - Forcing entering into next loop.")
                    e = 0
                    python = sys.executable
                    os.execl(python, python, * sys.argv)
                else:
                    une += 1 
                    print(une)
                    pyautogui.move(20,-0,0.6)
                    time.sleep(0.5)
                     
logo()