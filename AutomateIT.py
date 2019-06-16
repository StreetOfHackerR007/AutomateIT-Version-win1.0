import sys
import os
from time import sleep

try:
	from selenium import webdriver
except:
	print('[*] ERROR : Selenium Not Found...!\n[+] Install Selenium By Firing Following Command Without Quotes.\t>>> "pip install selenium"')
	sys.exit()

def banner():
    print('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    _         _                        _       ___ _
   / \  _   _| |_ ___  _ __ ___   __ _| |_ ___|_ _| |_
  / _ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \| || __|  _____    For
 / ___ \ |_| | || (_) | | | | | | (_| | ||  __/| || |_  |_____| WhatsApp
/_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___|___|\__|		By  R007

	Follow Us On IG - @STREET_OF_HACKER - R007
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
''')

def requirements():
        print('---'*25)
        print('\t\t\t >> REQUIREMENTS << ')
        print('---'*25)
        print('• Good Internet Connection')
        print('• Windows Operating System (Any Version Of Windows Is Supported)')
        print('• Latest Version Of Chrome Browser')
        print('---'*25)
        print('\n')

def send():
        print("\n")
        input("[-] Press Enter To Check Your User & Messge File Once And Make Sure It Is Perfect")
        sleep(1)
        os.system("notepad user.txt")
        sleep(1)
        os.system("notepad message.txt")
        
        try:
                user_file = open("user.txt","r")
                user = user_file.readlines()
                
                message_file = open("message.txt","r")
                message = message_file.read()
                SHIFT = '\ue008'
                msg = message.replace("\n",SHIFT+"\n"+SHIFT)
        except:
                print("[*] ERROR : Unexpected Error Found While Reading user.txt or message.txt file")

        input('[-] Press Any Button For Continue....')

        for name in user:
                try:
                        print("[+] Sending Message To : "+name)

                        #driver.find_element_by_css_selector("[title='Search or start new chat']").send_keys(name+"\n"+msg+"\n")
                        driver.find_element_by_css_selector("[title='Search or start new chat']").send_keys(name)
                        sleep(0.5)
                        driver.find_element_by_class_name("_3FeAD").send_keys(msg)
                        sleep(1)
                        driver.find_element_by_class_name("_3M-N-").click()
                        
                        
                        print("[-] Messge Sent To : "+name)
                        sleep(1)
                except:
                        print("[*] ERROR : Could Not Sent Message To : "+name)

        print(">>> ALL DONE <<<")

        user_file.close()
        message_file.close()

        send_more = input("[-] Want To Send More Message(Y/N) : ")
        
        if send_more == "y" or send_more == "Y" or send_more == "yes" or send_more == "Yes":
                send()
        else:
                print("[+] Logging Out Of Whatsapp...")
                driver.find_element_by_css_selector("[title='Menu']").click()
                driver.find_element_by_css_selector("[title='Log out']").click()
                print('\n\n'*20)
                print("[+] Press CTRL+C If Script Is Still Running....")
                sys.exit()

banner()
requirements()

print('[+] Wait While Loading Dependencies...!')
print('[+] Scan QR Code')

driver = webdriver.Chrome('../chromedriver.exe')
driver.maximize_window()
driver.get('https://web.whatsapp.com')

print('[+] Loading WhatsApp....\n')

try:
        send()
except:
        print("\n")
        banner()
        print("[+] Check Requirements...")
        sys.exit()
