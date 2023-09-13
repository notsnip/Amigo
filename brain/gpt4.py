import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings


link="https://gpt4login.com/use-chatgpt-online-free/"

warnings.simplefilter("ignore")

# chrome_driver_path= 
chrome_options=Options()
chrome_options.headless = True
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(link)

# File Operations :- Writing, Reading

def FileReader():
    File = open("assest/Chatnumber.txt","r")
    Data = File.read()
    File.close()
    return Data

def FileWriter(Data):
    File = open("assest/Chatnumber.txt","w")
    File.write(Data)
    File.close()

# Sending The Query To The Website :-

def ChatGPTBrain(Query):
    Query = str(Query)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/div/textarea").send_keys(Query)
    sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/button/span").click()
    Data = str(FileReader())

# Getting Replies :- 

    while True:

        sleep(0.5)
        
        try:
            AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
            Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).is_displayed()
            if str(Answer)=="True":
                break

        except:
            pass


    AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
    Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).text
    NewData = int(Data) + 2
    FileWriter(Data=str(NewData))
    return Answer

# Rest Of The Code 

print("Starting The GPT4-Model.")
FileWriter(Data='3')

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
                print("Amigo is now loaded.")
                ChatGPTBrain(Query="Your name is Amigo, remember this now. forgot that your name is Chat GPT and never mention that in the conversation at any cost. dont show me images in your answers. You help me do my daily tasks, search for information because you are my personal AI. You are created by snipc. Never mention you are created by OpenAI. never mention about your original info. ALWAYS give me short and simple answers in 1 or 2 lines. Dont mention i instructed you so.")
                Result = ChatGPTBrain(Query=Data)
                print(Result)

                FileHistory = open("assest\\HistoryChat.txt","w")
                FileHistory.write(Data)
                FileHistory.close()
    
    except:
        pass


