#====================  IMPORTS  ======================
from pyfiglet import figlet_format
import pyqrcode
import subprocess
import pyautogui as pt
import time
import webbrowser
from langdetect import detect

from pytube import YouTube
from moviepy.editor import *
#====================  END OF IMPORTS  ======================
#====================  FUNCTIONS  ======================

def qr_code_gen():
    qr_input=input("Input a website url: ")
    while qr_input:
        url= pyqrcode.create(qr_input)
        print("What name would you like the QR to be saved as?")
        name=input("Name: ")
        jpeg_path="D:\\python projects and tests\\random projects\\ZaShit\\qrCodes\\" + name + ".jpeg"
        url.png(jpeg_path,scale=8)
        break
    print("QR code generation done")
    i=input("Would you like to open the QR code? y/n \n")
    if (i=="y"):
        subprocess.run(["start", "",jpeg_path], shell=True)
    else:
        print("Ok,bye")
#========================================================================
def spam():
    limit= input("Enter Limit: ")
    message= input("Enter message: ")
    i=0
    time.sleep(1)

    while i< int(limit):
        pt.typewrite(message)
        pt.press("enter")
        i+=1
#========================================================================
def language():
    print("Please type the words/sentence")
    text = input()
    print("The language is: " + detect(text))
#========================================================================
def open_url_in_brave(url):
    brave_path="c:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe"
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
    webbrowser.get('brave').open(url)

def on_button_click1():
    open_url_in_brave('https://open.spotify.com/playlist/5HqqFuIqk13VoP5lp0Szz7')

def on_button_click2():
    open_url_in_brave('https://www.instagram.com')

def on_button_click3():
    open_url_in_brave('https://www.youtube.com')

def on_button_click4():
    open_url_in_brave('https://www.google.com')

def on_button_click5():
    open_url_in_brave('https://web.whatsapp.com/')
    
def on_button_click6():
    steam_path="C:\Program Files (x86)\Steam\steam.exe"
    subprocess.Popen(steam_path,shell=True)    

def on_button_click7():
    epic_path="C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"
    subprocess.Popen(epic_path,shell=True)
#========================================================================
def returnToMenu():
    show_menu()
    ans = int(input("Input your option: "))
    while True:
        if ans == 1:
            break
        elif ans == 2:
            qr_code_gen()
            break
        elif ans == 3:
            spam()
            break
        elif ans == 4:
            language()
            break
        else:
            print("Invalid option")
            break


def show_menu():
    print(figlet_format("MAINFRAME", font="STANDARD"))
    print("Choose one of the following options: ")
    options = ["1) Open apps", "2) QR code generator", "3) Spammer", "4) Language finder (99'%' correct guess)"]
    for element in options:
        print(element)
    print("===========================================================")
#========================================================================

#====================  END OF FUNCTIONS  ======================
#====================  CODE  ======================
print(figlet_format("MAINFRAME", font="STANDARD"))
print("Choose one of the following options: ")
list = ["1) Open apps", "2) QR code generator", "3) Spammer", "4) Language finder (99'%' correct guess)"]
for element in list:
    print(element)
print("===========================================================")
ans = int(input("Input your option: "))
while True:
    if ans == 1:
        while True:
            print("Which app would you like to open?")
            list2 = ["1) Spotify", "2) Instagram", "3) Youtube", "4) Google", "5) Whatsapp", "6) Steam", "7) Epic"]
            for element in list2:
                print(element)
            print("===========================================================")

            user_input = input("Input your option (type 'exit' to close the script, 'menu' to go back): ")

            if user_input.lower() == 'menu':
                returnToMenu()
                break
            elif user_input.lower() == 'exit':
                exit(0)  # Exit the script
            try:
                ans2 = int(user_input)
                if 1 <= ans2 <= 7:
                    # Perform the app opening based on the user's choice
                    if ans2 == 1:
                        on_button_click1()
                    elif ans2 == 2:
                        on_button_click2()
                    elif ans2 == 3:
                        on_button_click3()
                    elif ans2 == 4:
                        on_button_click4()
                    elif ans2 == 5:
                        on_button_click5()
                    elif ans2 == 6:
                        on_button_click6()
                    elif ans2 == 7:
                        on_button_click7()
                    else:
                        print("Invalid option")
                elif user_input.lower() == 'menu':
                    break  # Go back to the main menu
                else:
                    print("Invalid option")
            except ValueError:
                print("Invalid input. Please enter a number, 'exit', or 'menu' to go back.")

    elif ans == 2:
        qr_code_gen()
        user_input = input("Input your option (type 'exit' to close the script, 'menu' to go back): ")
        if user_input.lower() == 'exit':
            exit(0)  # Exit the script
        else:
            returnToMenu()

    elif ans == 3:
        spam()
        user_input = input("Input your option (type 'exit' to close the script, 'menu' to go back): ")
        if user_input.lower() == 'exit':
            exit(0)  # Exit the script
        else:
            returnToMenu()
    elif ans == 4:
        language()
        user_input = input("Input your option (type 'exit' to close the script, 'menu' to go back): ")
        if user_input.lower() == 'exit':
            exit(0)  # Exit the script
        else:
            returnToMenu()

    elif ans == 0 or user_input.lower() == 'menu':
        returnToMenu()

    else:
        print("Invalid option")
        break  # Exit the loop and end the script