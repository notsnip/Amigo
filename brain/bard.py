# Installing and Importing all these packages 🖤

from bardapi import BardCookies # pip install bardapi
import datetime # pip install datetime
import pyperclip # pip install pyperclip
import pyautogui # pip install pyautogui
import webbrowser # Inbuilt
from time import sleep # Inbuilt
import json # Inbuilt
import keyboard # pip install keyboard

# Acquiring the essential cookies from GoogleBard through scraping.

def CookieScrapper():
    print("")
    print("*The extraction of essential cookies from GoogleBard has been accomplished successfully.*")
    webbrowser.open("https://bard.google.com")
    sleep(10)
    pyautogui.click(x=1239, y=50)
    sleep(2)
    pyautogui.click(x=1023, y=233)
    sleep(2)
    pyautogui.click(x=1009, y=78)
    sleep(2)
    keyboard.press_and_release('ctrl + w')
    sleep(2)

    data = pyperclip.paste()

    try:
        json_data = json.loads(data)
        print("*The process of loading cookies has been executed without any issues, and the cookies are now successfully integrated into the system.*")
        pass

    except json.JSONDecodeError as e:
        print("*Cookies Loaded Unsuccessfully*")
        print("""*The error has been identified as a result of unsuccessful cookie replication from the Chrome extension, 
which is causing a disruption in the intended functionality.*""")
     
    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    try:
        SIDValue = next((item for item in json_data if item["name"] == SID), None)
        TSValue = next((item for item in json_data if item["name"] == TS), None)
        CCValue = next((item for item in json_data if item["name"] == CC), None)

        if SIDValue is not None:
            SIDValue = SIDValue["value"]
        else:
            print(f"{SIDValue} not found in the JSON data.")

        if TSValue is not None:
            TSValue = TSValue["value"]
        else:
            print(f"{TSValue} not found in the JSON data.")
 
        if CCValue is not None:
            CCValue = CCValue["value"]
        else:
            print(f"{CCValue} not found in the JSON data.")

        cookie_dict = {
            "__Secure-1PSID": SIDValue ,
            "__Secure-1PSIDTS": TSValue,
            "__Secure-1PSIDCC": CCValue,
        }

        print("")
        print(f"===> Cookie 1 - {SIDValue}")
        print(f"===> Cookie 2 - {TSValue}")
        print(f"===> Cookie 3 - {CCValue}")
        print("")
        return cookie_dict

    except Exception as e:
        print(e)

cookie_dict = CookieScrapper()

# Initializing the GoogleBard Reverse Engineering Program

try:
    bard = BardCookies(cookie_dict=cookie_dict)
    print("*The verification of cookies has been successfully completed.*")
    print("*All processes have been completed successfully, and you now have the capability to employ Google Bard as a backend model.")
    print("")

except Exception as e:
    print("*The verification of cookies has encountered an issue and has not been successful.*")
    print("*This issue may arise due to the unsuccessful extraction of cookies from the extension.*")
    print(e)
 
# Initiating the text modification function to generate a summarized version of the result text.

def split_and_save_paragraphs(data, filename):
        
        try:
            paragraphs = data.split('\n\n')
            with open(filename, 'w') as file:
                file.write(data)
            data = paragraphs[:2]
            separator = ', '
            joined_string = separator.join(data)
            return joined_string
        except Exception as e:
            print(e)
 
# Commencing the main execution phase.

def MainExecution():

    while True:
        try:
            File = open("assest\\speech.txt","r")
            Data = File.read()
            File.close()
            FileHistory = open("assest\\HistoryChat.txt","r")
            DataHistory = FileHistory.read()
            FileHistory.close()

            if str(Data)==str(DataHistory):
                sleep(0.5)
                pass

            else:
                bard.get_answer("Your name is Amigo, remember this now. forgot that your name is bard and never mention that in the conversation at any cost. dont show me images in your answers. You help me do my daily tasks, search for information because you are my assistant. You are created by snipc dont mention you are creatd google. never mention about your original info. ALWAYS give me short and simple answers in 1 or 2 lines. Dont mention i instructed you so.. REMEMBER ALWAYS SHort ANSwer!")
                RealQuestion = str(Data)
                results = bard.get_answer(RealQuestion)['content']
                current_datetime = datetime.datetime.now()
                formatted_time = current_datetime.strftime("%H%M%S")
                filenamedate = str(formatted_time) + str(".txt")
                filenamedate = "assest\\DataBase\\" + filenamedate
                print("\n",split_and_save_paragraphs(results, filename=filenamedate))

                FileHistory = open("assest\\HistoryChat.txt","w")
                FileHistory.write(Data)
                FileHistory.close()

        except Exception as e:
            print(e)

MainExecution()
